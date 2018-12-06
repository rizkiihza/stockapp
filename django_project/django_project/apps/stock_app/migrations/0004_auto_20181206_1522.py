# Generated by Django 2.1.4 on 2018-12-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_auto_20181206_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalindicator',
            name='indicator_type',
            field=models.CharField(choices=[('macd', 'macd'), ('rsi', 'rsi'), ('stochastic', 'stochastic'), ('stochrsi', 'stochrsi')], default='macd', max_length=128),
        ),
        migrations.AlterField(
            model_name='technicalindicator',
            name='value',
            field=models.CharField(max_length=128),
        ),
    ]
