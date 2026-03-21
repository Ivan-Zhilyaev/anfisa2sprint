from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.proposal_create, name='create'),
    path('accepted/', views.accepted, name='accepted'),
    path('<int:pk>/edit/', views.proposal_create, name='edit'),
    path('<int:pk>/delete/', views.delete_proposal, name='delete'),
]
