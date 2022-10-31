from django.urls import path

from . import views

# class based views
urlpatterns = [
    path('home', views.HomeView.as_view(), name="home"),
    path('authorized', views.AuthorizedView.as_view())
]

# urlpatterns = [
#     path('home', views.home),
#     path('authorized', views.authorized)
# ]