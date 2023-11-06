from django.contrib import admin
from .models import Place#enable adnmin console to work with datat in db, look, edit, modify, add data

# Register your models here.
admin.site.register(Place)