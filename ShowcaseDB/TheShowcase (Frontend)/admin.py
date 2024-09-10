from django.contrib import admin
from .models import City,Country,State, Employee, User

# admin.site.register(User)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Employee)
# Register your models here.
