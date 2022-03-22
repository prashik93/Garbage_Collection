from django.contrib import admin
from .models import Flat,Manager,Analytics

# Register your models here.
class FlatAdmin(admin.ModelAdmin):
    list_display = ['flat','name','block','status','score']

admin.site.register(Flat,FlatAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['flat','name','bloc','segregated']

admin.site.register(Manager,ManagerAdmin)


class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ['flat','name','bloc','violations']

admin.site.register(Analytics,AnalyticsAdmin)