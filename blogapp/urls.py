from django.urls import path
import blogapp.views

urlpatterns = [
    path('', blogapp.views.home, name='home'),
    path('<int:blog_id>', blogapp.views.detail, name='detail'),
    path('new', blogapp.views.new, name='new'),
    path('create', blogapp.views.create, name='create'),
]