from django.urls import path
from . import views

urlpatterns = [
    path(path('<int:ticket_id>/', views.TicketList.as_view()),)
]