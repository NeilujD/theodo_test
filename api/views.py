from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Run
from .serializers import RunSerializer


class RunViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows runs to be created.
    """
    queryset = Run.objects.all().order_by('-start_date')
    serializer_class = RunSerializer

    def create(self, request):
        data = {
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'distance': request.data.get('distance'),
            'burnt_calories': request.data.get('burnt_calories'),
            'runner': str(request.user.id)
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # print(serializer.data)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        