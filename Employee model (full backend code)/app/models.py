from django.db import models
import datetime
import uuid


## TODO: CHANGE THIS TO SIONE'S USER MODEL ##
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField() #Email field necessary or not?
    user_type = models.CharField(max_length=15)
    date_joined = models.DateField(default=datetime.date.today)
    last_login = models.DateField(default=datetime.date.today)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_phone = models.CharField(max_length=20, default='', blank=True, null=True)
    location_id = models.IntegerField(default=0, blank=True, null=True)
    user_birthdate = models.DateField(default=datetime.date.today)
    bio = models.CharField(default='', max_length=250, blank=True)
    linkedin = models.CharField(default='', max_length=20, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(User):
    employee_id = models.UUIDField(default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=50, default='N/A')
    job_title = models.CharField(max_length=50, default='N/A')

    class Meta(User.Meta):
        pass

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.job_title}'