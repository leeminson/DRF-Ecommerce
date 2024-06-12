from django.db import models
from django.contrib.auth.models import AbstractUser
class FullName(models.Model):
  first_name=models.CharField(max_length=25)
  last_name=models.CharField(max_length=25)
class User(AbstractUser):
   username = None
   last_login = None
   is_staff = None
   is_superuser = None
   first_name = None
   last_name = None
   email=None
   full_name=models.ForeignKey(FullName,on_delete=models.CASCADE)
   emails = models.EmailField(max_length=100, unique=True)
   mobile = models.CharField(max_length=12)
   password = models.CharField(max_length=255)
   confirm_password= models.CharField(max_length=255)
   USERNAME_FIELD = 'emails'
   def __str__(self):
      return '%s %s %s %s %s %s' % (self.
                  email, self.mobile, self.password)
class Address(models.Model):
   house_num=models.CharField(max_length=25)
   street=models.CharField(max_length=100)
   district=models.CharField(max_length=100)
   city=models.CharField(max_length=100)
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses')