from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Post.objects.filter().order_by('id')
        return queryset
    fields =['text','picture']
    list_display = ['id','created_at','modified_at','archived_at']
admin.site.register(Post,PostAdmin)