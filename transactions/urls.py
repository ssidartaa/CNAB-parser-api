from django.urls import path
from . import views

urlpatterns = [
    path("transaction/", views.TransactionView.as_view()),
    path("transaction/<int:pk>/", views.TransactionDetailView.as_view()),
]
