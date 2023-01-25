from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("__all__",)

    def create(self, validated_data: dict) -> Transaction:
        value = validated_data.pop("value")
        validated_data["value"] = value / 100.00
        new_transaction = Transaction.objects.create(**validated_data)
        return new_transaction
