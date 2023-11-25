import requests
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from .models import CoinDetail


def index(request):

    url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1'
    response=requests.get(url).json()
    for item in response:
        coin_name=item["name"]
        coin_symbol=item["symbol"]
        coin_current_price=item["current_price"]
        coin_market_cap=item["market_cap"]
        coin_market_cap_rank=item["market_cap_rank"]
        coin_high_24h=item["high_24h"]
        coin_low_24h=item["low_24h"]
        coin_ath=item["ath"]
        coin_ath_date=item["ath_date"]
        coin_atl=item["atl"]
        coin_atl_date=item["atl_date"]
        is_present=CoinDetail.objects.filter(name=coin_name)
        if is_present:
            coin=CoinDetail.objects.get(name=coin_name)
            coin.current_price=coin_current_price
            coin.market_cap=coin_market_cap
            coin.market_cap_rank=coin_market_cap_rank
            coin.high_24h=coin_high_24h
            coin.low_24h=coin_low_24h
            coin.ath=coin_ath
            coin.ath_date=coin_ath_date
            coin.atl=coin_atl
            coin.atl_date=coin_atl_date
            coin.save()
        else:
            coin_object=CoinDetail(name=coin_name, symbol=coin_symbol, current_price=coin_current_price,
                               market_cap=coin_market_cap, market_cap_rank=coin_market_cap_rank,
                               high_24h=coin_high_24h, low_24h=coin_low_24h, ath=coin_ath,
                               ath_date=coin_ath_date, atl=coin_atl, atl_date=coin_atl_date)
            coin_object.save()
    
    coin_details=CoinDetail.objects.all()
    

    return render(request, 'index.html', {"coin_details":coin_details})


def under_ath_range(request):
    all_coins=CoinDetail.objects.all()
    return render(request, 'ath.html', {"coin_details":all_coins})

def under_atl_range(request):
    all_coins=CoinDetail.objects.all()
    return render(request, 'atl.html', {"coin_details":all_coins})