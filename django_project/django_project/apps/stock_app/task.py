from django.apps import apps
from django.utils.timezone import datetime

from django_project.apps.stock_app import constants
from django_project.clients.alpha_vantage.technical_indicator import TechIndicatorClient

Company = apps.get_model("stock_app", "Company")
TechnicalIndicator = apps.get_model("stock_app", "TechnicalIndicator")


def create_technical_indicator(company, indicator_type):

    technical_indicator_client = TechIndicatorClient(constants.INDONESIAN_INDEX)

    # indicator type checking
    if indicator_type == constants.INDICATOR_RSI:
        score = technical_indicator_client.get_rsi(company.code)
    elif indicator_type == constants.INDICATOR_MACD:
        score = technical_indicator_client.get_macd(company.code)
    elif indicator_type == constants.INDICATOR_STOCHASTIC:
        score = technical_indicator_client.get_stoch(company.code)
    elif indicator_type == constants.INDICATOR_STOCHASTIC_RSI:
        score = technical_indicator_client.get_stochrsi(company.code)

    # pick the last score only
    last_score = technical_indicator_client.get_last_value(score)

    technical_indicator = TechnicalIndicator.objects.create(company=company,
                                                indicator_type=indicator_type, value=last_score)
    return technical_indicator

def get_or_create_technical_indicator_today(company, indicator_type):
    technical_indicator = TechnicalIndicator.objects.filter(
        company=company,
        indicator_type=indicator_type,
        date_created=datetime.today()
    ).first()

    if technical_indicator is None:
        technical_indicator = create_technical_indicator(company, indicator_type)

    return technical_indicator