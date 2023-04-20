from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('knowledge_base', views.knowledge_base, name='knowledge_base'),
    path('test', views.test, name='test'),
    path('beginner', views.beginner, name='beginner'),
    path('elementary', views.elementary, name='elementary'),
    path('pre_intermediate', views.pre_intermediate, name='pre_intermediate'),
    path('intermediate', views.intermediate, name='intermediate'),
    path('upper_intermediate', views.upper_intermediate, name='upper_intermediate'),
    path('advanced', views.advanced, name='advanced'),
    path('add_review', views.add_review, name='add_review')
]
