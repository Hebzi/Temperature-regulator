from django.urls import path
from . import views as tr_views

app_name = 'temp_regulator'
urlpatterns = [
    path('', tr_views.home, name='home'),
    path('modes/', tr_views.modes, name='modes'),
    path('modes/party-mode/', tr_views.party_mode, name='party-mode'),
    path('modes/vacation-mode/', tr_views.vacation_mode, name='vacation-mode'),
    path('modes/conditioning-mode/', tr_views.conditioning_mode, name='conditioning-mode'),
    path('heating-plan/', tr_views.heating_plan, name='heating-plan'),
]
