from django.contrib import admin

# Register your models here.
from .models import Departamento, Ciudad

admin.site.register(Departamento)
admin.site.register(Ciudad)
