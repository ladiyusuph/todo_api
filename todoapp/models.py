from django.db import models
from django.contrib.auth.models import User

# class TodoOwner(models.Manager):
#     def get_queryset(self, request):
#         return super(request).get_queryset().filter(owner=request.user)
    

class TodoList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    task = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='task_owner', on_delete=models.CASCADE)
    # objects = models.Manager()
    # owner_objects = TodoOwner()
    