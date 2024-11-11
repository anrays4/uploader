from django.contrib import admin
from django.urls import path
from home.views import upload_page, download_page, download_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_page, name="download_page"),
    path('download/', download_page, name="upload_page"),
    path('download/<str:file_name>/', download_file, name='download_file')
]
