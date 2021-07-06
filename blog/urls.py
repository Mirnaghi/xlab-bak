from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('iot-groups', views.iot_groups, name='blog-iot_groups'),
    path('ai-groups', views.ai_groups, name='blog-ai_groups'),
    path('energy-groups', views.energy_groups, name='blog-energy_groups'),
    path('robotics-groups', views.robotics_groups, name='blog-robotics_groups'),
    path('lab-journal', views.lab_journal, name='blog-lab-journal'),
    path('lab-conf-talk', views.lab_conf_talk, name='blog-lab-conf-talk'),
    path('future-member/', views.future_member, name='blog-future-member'),
    path('events/', views.events, name='blog-events'),
    path('about/', views.about, name='about'),
    path('<str:slug>/', views.post, name='post'),
    path('categories/<str:category_name>/', views.category, name='category')
]
