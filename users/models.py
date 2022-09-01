from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class Profile(models.Model):

    DEPARTMENT_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Electronics and Communications', 'Electronics and Communications'),
        ('Electrical and Electronics', 'Electrical and Electronics'),
        ('Information Technology', 'Information Technology'),
        ('Chemical', 'Chemical'),
        ('Mechanical', 'Mechanical'),
        ('Mechatronics', 'Mechatronics'),
        ('Civil', 'Civil'),
        ('Humanities and Science', 'Humanities and Science'),
        ('Management', 'Management'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    DEGREE_CHOICES = [
        ('Bachelor of Technology', 'Bachelor of Technology'),
        ('Bachelor of Engineering', 'Bachelor of Engineering'),
        ('Master of Technology', 'Master of Technology'),
        ('Master of Engineering', 'Master of Engineering'),
        ('Master of Business Administration', 'Master of Business Administration'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, blank=True, null=True)
    address = models.TextField()
    occupation = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=50, choices=DEGREE_CHOICES, blank=True, null=True)
    branch = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    year_of_passing = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.email} Profile'