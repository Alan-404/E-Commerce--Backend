from django.db import models
from user.models import User
# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length = 17, primary_key=True)
    password = models.TextField()
    role = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "account"