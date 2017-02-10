# -*- coding: utf-8 -*-
import stripe
from django.shortcuts import render, redirect
# from mysite.settings.local import stripe_keys
from django.conf import settings


def index(request):

    STRIPE_API_KEY = settings.STRIPE_KEYS['publishable_key']
    stripe.api_key = settings.STRIPE_KEYS['secret_key']

    return render(request, 'onetimestripe/index.html', {'key': STRIPE_API_KEY,
                                                        'host': settings.HOST_NAME,
                                                        'price': '3500',
                                                        'description': 'Abonnement d\'un mois à la plate-forme'})


def charge(request):

    if request.method != 'POST':
        return redirect('/')

    # Process update status object
    # object_id = request.form['object_id']
    # object = Object.query.get(object_id_id)

    try:
        token = request.POST['stripeToken']
        amount = 500 # 5 USD

        stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Django Charge',
            source = token
        )

    except stripe.CardError, e:
        return redirect('/')

    return render(request, 'onetimestripe/charge.html', {'amount': amount})