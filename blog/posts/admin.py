from django.contrib import admin
from .models import Post, Review
# Register your models here.

class PostModel(admin.ModelAdmin):

    list_display = ('title', 'rating', 'publishd_at', 'category')
    list_filter = ('category', 'rating')



class ReviewModel(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'created_at')
    list_filter = ('post',)

admin.site.register(Post)
admin.site.register(Review, ReviewModel)