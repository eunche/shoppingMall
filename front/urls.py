from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('bottom/',views.bottom, name='bottom'),
    path('cap/',views.cap, name='cap'),
    path('outer/',views.outer, name='outer'),
    path('shoe/',views.shoe, name='shoe'),
    path('top/',views.top, name='top'),
    path('search/', views.search, name='search'),
]