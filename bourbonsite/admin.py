from django.contrib import admin
from .models import Bourbon, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('RatingID', 'Pub_Date', 'User_Name', 'Rating')
    list_filter = ['Pub_Date', 'User_Name']


class BourbonAdmin(admin.ModelAdmin):
    model = Bourbon
    list_display = ('BourbonID', 'Bourbon', 'Location')
    list_filter = ['Location']


admin.site.register(Bourbon, BourbonAdmin)
admin.site.register(Review, ReviewAdmin)