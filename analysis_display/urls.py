from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<str:Unique_Squirrel_ID>', views.sightings_id, name='sightings_id'),
    path('sightings_add/', views.sightings_add, name='sightings_add'),
    path('sightings_stats/', views.sightings_stats, name='sightings_stats'),
    path('main_index/', views.main_index, name='main_index'),
    path('upload_f0', views.main_upload_file_views),
    path('download_f', views.main_download_file_views),
    path('upload_t', views.sightings_add_upload_text),
    path('update_t', views.sightings_update_upload_text),
]
