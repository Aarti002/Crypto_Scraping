from django.db import models


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    email = models.CharField(max_length=255,null=False)
    is_verified = models.BooleanField(max_length=10,default=False)
    daily_updates = models.BooleanField(max_length=10,default=False)
    objects = models.Manager()

class CoinDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True,null=False)
    symbol = models.CharField(max_length=50,null=False)
    current_price = models.DecimalField(max_digits=50, decimal_places=3, default=0.00,null=False)
    market_cap = models.BigIntegerField(null=False)
    market_cap_rank = models.IntegerField()
    high_24h = models.DecimalField(max_digits=50, decimal_places=3, default=0.00,null=False)
    low_24h = models.DecimalField(max_digits=50, decimal_places=3, default=0.00,null=False)
    ath = models.DecimalField(max_digits=50, decimal_places=3, default=0.00,null=False)
    ath_date = models.DateTimeField(null=False)
    atl = models.DecimalField(max_digits=50, decimal_places=3, default=0.00,null=False)
    atl_date = models.DateTimeField(null=False)
    objects = models.Manager()
