from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PcIndex.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('add/', views.PcAdd.as_view(), name='pcadd'),
    path('post/<slug:pc_slug>/', views.PcAbout.as_view(), name='pcabout'),
    path('type/<slug:pctype_slug>/', views.ShowPcType.as_view(), name='pctype'),
    path('login/', views.login, name='login'),
]
