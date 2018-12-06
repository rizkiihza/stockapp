from rest_framework import serializers
from django.apps import apps
from django.utils.timezone import datetime

from django_project.apps.stock_app.task import get_or_create_technical_indicator_today
from django_project.apps.stock_app import constants

Company = apps.get_model("stock_app", "Company")
TechnicalIndicators = apps.get_model("stock_app", "TechnicalIndicator")

class TechnicalIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalIndicators

        fields = (
            'company',
            'indicator_type',
            'value',
        )

        read_only_fields = (
            'company',
            'indicator_type',
            'value',
        )

class CompanyTechnicalSerializer(serializers.Serializer):

    stock_code = serializers.CharField(max_length=128, required=True)

    def create(self, validated_data):

        stock_code = validated_data.get('stock_code')

        technical_indicators = []

        for indicator_type in constants.INDICATOR_TYPES:
            company, _ = Company.objects.get_or_create(code=stock_code)
            technical_indicator = get_or_create_technical_indicator_today(company, indicator_type)
            technical_indicators.append(technical_indicator)

        return TechnicalIndicatorSerializer(technical_indicators, many=True).data


