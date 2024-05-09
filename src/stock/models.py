from django.db import models


class Slot(models.Model):
    company_name: str = models.CharField(max_length=20, null=False)
    stock_symbol: str = models.CharField(max_length=4, primary_key=True)
    industry: str = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.company_name


class Performance(models.Model):
    stock_symbol: str = models.ForeignKey(Slot, on_delete=models.CASCADE)
    trading_volume: float = models.FloatField(null=False, decimal_place=2)
