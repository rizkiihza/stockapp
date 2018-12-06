from django.urls import path

from django_project.api.views.stock_app import (
    CompanyTechnicalAPIView,
    TechnicalIndicatorAPIView
)

urlpatterns = [
    path('technical/<str:stock_code>/',
            CompanyTechnicalAPIView.as_view(),
            name='company-technical'),

    path('technical/<str:stock_code>/<str:indicator_type>/',
            TechnicalIndicatorAPIView.as_view(),
            name="technical-indicator")
]