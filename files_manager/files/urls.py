from django.urls import path
from .views import File_Upload, File_Detail

urlpatterns = [
    path('upload/',File_Upload.as_view(),name='upload_file'),
    path('get/<str:filename>',File_Detail.as_view(),name='get_file'),
    path('delete/<str:filename>',File_Detail.as_view(),name='delete_file'),
]
