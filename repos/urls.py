from django.urls import path
from . import views

app_name = 'repos'
urlpatterns = [
    path('organization', views.organization_repos, name='organization'),
    path('stars', views.stars_repos, name='stars'),
]