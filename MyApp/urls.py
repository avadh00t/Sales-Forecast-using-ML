from django.urls import path

from .import views 

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('predict', views.predict,name='predict'),
    path('', views.landing,name='landing'),
    path('salepredict', views.predictsales, name='predictsales'),
]
