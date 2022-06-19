from django.contrib import admin
from django.urls import path, include
from shop import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('authentication.urls')),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
