from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True) 
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='residents')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='residents')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='residents')

    USERNAME_FIELD = 'email'  # Define the unique identifier for the user
    REQUIRED_FIELDS = []  # Required fields for creating a superuser

    objects = UserManager()

    def __str__(self):
        return f"{self.user_id} : {self.address_line1} : {self.city}, {self.state}"

class Employee(User):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name}"
