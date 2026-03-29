from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    
    email = models.EmailField(unique=True, db_index=True) 
    
    age = models.PositiveIntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email