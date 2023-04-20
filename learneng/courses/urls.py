from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CoursesDetailView.as_view(), name='courses_detail'),
    path('page<int:pk>/', views.TopicsDetailView.as_view(), name='topic_details'),
    path('create_topics', views.create_topics, name='create_topics')
]
