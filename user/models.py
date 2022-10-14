from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=17, primary_key=True)
    first_name = models.CharField(max_length=51)
    last_name = models.CharField(max_length = 51)
    email = models.CharField(max_length=51)
    phone = models.CharField(max_length=12)
    bdate = models.DateField()
    gender = models.CharField(max_length=6)
    address = models.TextField()
    class Meta:
        db_table = "\"USER\""