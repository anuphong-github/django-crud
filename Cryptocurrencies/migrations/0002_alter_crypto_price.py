# Generated by Django 3.2 on 2021-04-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cryptocurrencies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
