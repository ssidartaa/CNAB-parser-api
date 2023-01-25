from django.urls import path
from . import view

urlpatterns = [
    path("transaction/", view.TransactionView),
    path("transaction/<int:pk>/", view.TransactionDetailView),
]
