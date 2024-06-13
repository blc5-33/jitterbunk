from django.urls import path

from . import views

app_name = 'bunk'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/<int:pk>/', views.DetailView.as_view(), name='user'),
    path('user/<int:from_user_id>/addbunkmate/<int:to_user_id>', views.addbunkmate, name='addbunkmate'),
]