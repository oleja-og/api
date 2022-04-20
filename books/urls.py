from django.urls import path
from .views import BookListViev


urlpatterns = [
    path('', BookListViev.as_view(), name="home"),
]