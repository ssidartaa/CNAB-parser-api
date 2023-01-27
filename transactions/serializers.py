from rest_framework import serializers
from .models import Transaction, TRANSACTION_TYPE

from datetime import datetime


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    date = serializers.CharField(max_length=8)
    hour = serializers.CharField(max_length=6)
    value = serializers.CharField(max_length=10)

    def create(self, validated_data: dict) -> Transaction:
        value = validated_data.pop("value")
        validated_data["value"] = int(value) / 100.00

        str_type = validated_data.pop("type")

        for key, value in TRANSACTION_TYPE.items():
            if key == str_type:
                validated_data["type"] = value

        str_date = validated_data.pop("date")

        str_hour = validated_data.pop("hour")

        formatted_datetime = f"{str_date[6:]}/{str_date[4:6]}/{str_date[:4]}-{str_hour[:2]}:{str_hour[2:4]}:{str_hour[4:]}"

        datetime_obj = datetime.strptime(formatted_datetime, "%d/%m/%Y-%H:%M:%S")

        date = datetime.date(datetime_obj)

        hour = datetime.time(datetime_obj)

        validated_data["date"] = date

        validated_data["hour"] = hour

        return Transaction.objects.create(**validated_data)
