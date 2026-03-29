from django.urls import path
from .views import UserCSVUploadAPIView

urlpatterns = [
    path("upload/", UserCSVUploadAPIView.as_view(), name="user-csv-upload"),
]