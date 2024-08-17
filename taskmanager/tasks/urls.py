from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<uuid:pk>/soft-delete/', TaskViewSet.as_view({'post': 'soft_delete'}), name='task-soft-delete'),

]