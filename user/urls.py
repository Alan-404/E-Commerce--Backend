from django.urls import path
from user import views
urlpatterns = [
    path("media", views.user_media)
]