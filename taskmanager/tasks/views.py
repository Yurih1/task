from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def soft_delete(self, request, pk=None):
        """
        Class responsible for executing the 'soft delete' may not be the best way to do this, 
        a record of the user who performed this action and history would be a good improvement
        
        Args:
            request (_type_): api call
            pk (_type_, optional): Defaults to None.

        Returns:
            _type_: call response with the status of the execution performed

        """
        try:
            task = self.get_object()
            task.is_deleted = True
            task.save()
            return Response({'status': 'task deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
