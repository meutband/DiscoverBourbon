from django.contrib import admin
from .models import Bourbon, Cluster1


class Cluster1Admin(admin.ModelAdmin):
    model = Cluster1
    list_display = ['name', 'get_members']


admin.site.register(Bourbon)
admin.site.register(Cluster1, Cluster1Admin)