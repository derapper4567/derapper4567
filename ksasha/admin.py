from django.contrib import admin
from. models import ksasha



class ksashaAdmin(admin.ModelAdmin):
    list_display = ('name','payment','reg_no','email')
# Register your models here.
admin.site.register(ksasha, ksashaAdmin)
