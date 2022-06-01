from django.contrib import admin
from django.urls import path,include

from School_Management.settings import MEDIA_ROOT
from .views import root
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('facilities/', include('facilities.urls')),
    path('post/', include('post.urls')),
    path('settings/', include('settings.urls')),
    path('about/', include('about.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Moinul Admin"
admin.site.site_title = "Moinul Admin Portal"
admin.site.index_title = "Welcome to Moinul Researcher Portal"