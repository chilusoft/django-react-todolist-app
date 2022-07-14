from django.db import models



class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title