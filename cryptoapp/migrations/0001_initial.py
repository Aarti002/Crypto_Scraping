# Generated by Django 3.2.5 on 2023-11-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=10)),
                ('current_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('market_cap', models.BigIntegerField()),
                ('market_cap_rank', models.IntegerField()),
                ('high_24h', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('low_24h', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('ath', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('ath_date', models.DateTimeField()),
                ('atl', models.DecimalField(decimal_places=3, default=0.0, max_digits=50)),
                ('atl_date', models.DateTimeField()),
            ],
        ),
    ]
