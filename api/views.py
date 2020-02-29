
import json
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from dateutil import parser


from .models import Run
from .serializers import RunSerializer


class RunViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows runs to be created.
    """
    queryset = Run.objects.all().order_by('-start_date')
    serializer_class = RunSerializer

    def create(self, request):
        # Use the authenticated user to link the run
        data = {
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'distance': request.data.get('distance'),
            'burnt_calories': request.data.get('burnt_calories'),
            'runner': str(request.user.id)
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(runner=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StatisticsView(APIView):
    """
        API endpoint that permit to return basic statistics about user runs
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        # Check if required parameters are set
        if not start_date or not end_date:
            return Response({'error': 'missing_params'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = parser.parse(start_date)
            end_date = parser.parse(end_date)
        except:
            return Response({'error': 'bad_dates_format'}, status=status.HTTP_400_BAD_REQUEST)

        # Filter the runs by the authenticated user and given start and end dates
        runs = Run.objects.filter(start_date__gte=start_date, end_date__lte=end_date, runner__id=request.user.id)
        
        # Calculate the values
        avg_distance = 0 if len(runs) == 0 else sum(run.distance for run in runs) / len(runs)
        avg_calories = 0 if len(runs) == 0 else sum(run.burnt_calories for run in runs) / len(runs)
        
        return Response({'success': True, 'average_distance': avg_distance, 'average_burnt_calories': avg_calories}, status=status.HTTP_200_OK)
        