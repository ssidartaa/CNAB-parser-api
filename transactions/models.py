from django.db import models

TRANSACTION_TYPE = {
    1: "Débito",
    2: "Boleto",
    3: "Financiamento",
    4: "Crédito",
    5: "Recebimento Empréstimo",
    6: "Vendas",
    7: "Recebimento TED",
    8: "Recebimento DOC",
    9: "Aluguel",
}


class Transaction(models.Model):
    type = models.CharField(max_length=22, choices=TRANSACTION_TYPE.items())
    date = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.PositiveIntegerField()
    credit_card = models.CharField(max_length=12)
    hour = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
