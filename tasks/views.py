# # from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import permissions
# from .models import *
# from .serializers import *

# # RetrieveUpdateDestroyAPIView: Used for read-write-delete endpoints to represent a single model instance.
# # ListCreateAPIView: Used for read-write endpoints to represent a collection of model instances.

# #retrieve List
# class TodoListView(ListCreateAPIView):

#     serializer_class = TaskSerializer
#     permission_classes = (permissions.IsAuthenticated, ) #permissions for accessing

#     #override the perform_create method according to our needs
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
#     #retrieve the querySet list
#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)
    

# #get particular task
# class TaskView(RetrieveUpdateDestroyAPIView):

#     serializer_class = TaskSerializer
#     permission_classes = (permissions.IsAuthenticated, ) #permissions for accessing
#     lookup_field = 'id' #unique identifier       #tasks/<identifer>

#     #retrieve the querySet list
#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)
    

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)