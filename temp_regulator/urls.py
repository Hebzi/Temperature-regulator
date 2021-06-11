from django.urls import path
from . import views as tr_views

app_name = 'temp_regulator'
urlpatterns = [
    path('', tr_views.home, name='home'),
    path('modes/', tr_views.modes, name='modes'),
    path('heating-plan/', tr_views.heating_plan, name='heating-plan'),
]
