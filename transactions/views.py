from rest_framework import generics

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
