from django.urls import path
from apps.resources import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('resources/<int:id>', views.DetailResourceView.as_view(), name='resources-detail'),
    path('resources/all', views.AllResourcesView.as_view(), name='all-resources'),
    path('resources/post', views.resource_post, name='resource-post'),
]
