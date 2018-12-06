from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps

from django_project.apps.stock_app.task import get_or_create_technical_indicator_today
from django_project.api.serializers.stock_app import (
    CompanyTechnicalSerializer,
    TechnicalIndicatorSerializer,
)

TechnicalIndicator = apps.get_model("stock_app", "TechnicalIndicator")
Company = apps.get_model("stock_app", "Company")

class CompanyTechnicalAPIView(APIView):

    def get(self, request, stock_code=None):
        c_ser = CompanyTechnicalSerializer(data={"stock_code" : stock_code})

        if c_ser.is_valid():
            try:
                res = c_ser.save()
                if res:
                    return Response(res)
                else:
                    return Response({"error message" : "no data"}, status.HTTP_406_NOT_ACCEPTABLE)
            except Exception as e:
                error_message = str(e)
                return Response({"error message ": error_message}, status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"error message ": "data not valid"}, status.HTTP_406_NOT_ACCEPTABLE)

class TechnicalIndicatorAPIView(APIView):

    def get(self, request, stock_code=None, indicator_type=None):
        company, _ = Company.objects.get_or_create(code=stock_code)
        technical_indicator = get_or_create_technical_indicator_today(company, indicator_type)

        res = TechnicalIndicatorSerializer(technical_indicator).data
        return Response(res)