from django.db import models

# Create your models here.
"""
TODO:

- title
- description
- deadline date
- created time
- updated time
- is done
"""

class Todo(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True) # unlimited length
    deadline = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'To-Do'
        verbose_name_plural = 'To-Dos'
        # ordering = ('-id')