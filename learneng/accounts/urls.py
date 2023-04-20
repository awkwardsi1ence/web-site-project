from django.urls import path
from . import views

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('visitors_info/', views.visitors_info, name='visitors_info'),
]
