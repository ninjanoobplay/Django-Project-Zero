from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agenda/', views.agenda, name='ver_agenda'),
    path('agenda/submit_delete', views.submit_delete, name='delete_agenda'),
    
]
