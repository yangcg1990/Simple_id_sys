from django.contrib import admin
from .models import Provinces, Cities, Areas, Id_number

# Register your models here.
admin.site.register(Provinces)
admin.site.register(Cities)
admin.site.register(Areas)
admin.site.register(Id_number)