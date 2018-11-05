from django.db import models
from django.contrib.auth.models import User

class ApiUserManager(models.Manager):
    """
        Manager for model ApiUser
    """
    def create_api_user(self, username, email, roll_no, password, **kwargs):
        """Method for creating ApiUser. returns API User"""
        user = User.objects.create_user(
            username,
            email,
            password,
            **kwargs)
        api_user = self.create(user=user, roll_no=roll_no)
        return api_user


class ApiUser(models.Model):
    """
    ApiUser extending django's User

    Attributes:
        user-- OneToOneField with Django User
        roll_no-- CharField (max_length 20)
    Ordering is done a/c to roll_no
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.roll_no} {self.user.username}'
   
    class Meta:
        ordering = ('roll_no',)
   
    objects = ApiUserManager()
