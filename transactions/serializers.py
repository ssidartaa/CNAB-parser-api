from rest_framework import serializers
from .models import Transaction
from django.core.validators import MaxLengthValidator


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("__all__",)
        extra_kwargs = {
            "date": {
                "validators": (MaxLengthValidator(8)),
            },
            "cpf": {
                "validators": (MaxLengthValidator(11)),
            },
            "hour": {
                "validators": (MaxLengthValidator(6)),
            },
        }

    def create(self, validated_data: dict) -> Transaction:
        value = validated_data.pop("value")
        validated_data["value"] = value / 100.00
        new_transaction = Transaction.objects.create(**validated_data)
        return new_transaction
