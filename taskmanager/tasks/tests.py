from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User


class TaskTests(APITestCase):
    """
    Class responsible for handling tests related to tasks
    
    #TODO Improve test coverage, today we only tested one case.
    Args:
        APITestCase (_type_): _description_
    """
    def setUp(self):
        """
        This friend of ours is responsible for creating our object for testing, 
        always use it when necessary
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': '2024-12-31',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
