from django.contrib import admin
from .models import Movies,Movies2,Registration

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','durations','date','rating']
    list_display_links  =['name',]
    
class Movie2Admin(admin.ModelAdmin):
    list_display = ['name','durations','date','rating']
    list_display_links  = ['name',]
    
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']
    
admin.site.register(Movies,MovieAdmin)
admin.site.register(Movies2,Movie2Admin)
admin.site.register(Registration,RegistrationAdmin)


