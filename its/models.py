from django.db import models

# Create your models here.

class AuthToken(models.Model):
    token = models.CharField(max_length=1000)
    valid_till = models.DateTimeField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

