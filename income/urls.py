from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('home_page/',views.home_page,name='home_page'),
    # path('home_page/<int:page_id>/', views.home_page, name='home_page'),
    path('register', views.registration, name='registration'),

]