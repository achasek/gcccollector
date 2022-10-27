from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('critters/', views.critters_index, name="index"),
    path('critters/<int:critter_id>/', views.critters_detail, name='detail'),
    path('critters/create/', views.CritterCreate.as_view(), name="critters_create"),
    path('critters/<int:pk>/update/', views.CritterUpdate.as_view(), name='critters_update'),
    path('critters/<int:pk>/delete/', views.CritterDelete.as_view(), name='critters_delete'),
]

