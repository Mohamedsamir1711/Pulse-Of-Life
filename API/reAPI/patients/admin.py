from django.contrib import admin
from .models import Stable
from .models import Ftable

# Register your models here.

admin.site.register(Stable)
admin.site.register(Ftable)
