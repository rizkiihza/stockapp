from django.contrib import admin
from django.apps import apps

# Register your models here.
Company = apps.get_model("stock_app", "Company")
TechnicalIndicator = apps.get_model("stock_app", "TechnicalIndicator")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = (
        "code",
        "date_created"
        )
    list_display = (
        "code",
        "date_created"
        )
    readonly_fields = (
        "date_created",
        )

@admin.register(TechnicalIndicator)
class TechnicalIndicatorAdmin(admin.ModelAdmin):
    fields = (
        "company",
        "indicator_type",
        "value",
        "date_created")
    list_display = (
        "company",
        "indicator_type",
        "value",
        "date_created")
    readonly_fields = (
        "date_created",
    )
