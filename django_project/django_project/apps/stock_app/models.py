from django.db import models
from django_project.apps.stock_app.constants import *

# Create your models here.
class Company(models.Model):
    code = models.CharField(primary_key=True, unique=True, max_length=128)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.code)

class TechnicalIndicator(models.Model):
    INDICATORS = (
        (INDICATOR_MACD, "macd"),
        (INDICATOR_RSI, "rsi"),
        (INDICATOR_STOCHASTIC, "stochastic"),
        (INDICATOR_STOCHASTIC_RSI, "stochrsi")
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="indicators")
    indicator_type = models.CharField(max_length=128, choices=INDICATORS, default=INDICATOR_MACD)
    value = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s | %s | %s" % (self.company, self.indicator_type, self.value)
