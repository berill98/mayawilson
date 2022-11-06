from django.shortcuts import render

# Create your views here.
def add_to_basket(request, package_id):
    """ Add a package to the basket """

    quantity = int(1),
    date = request.POST.get('photodate')
    basket = request.session.get('basket', {})

    basket[package_id] = quantity 
    request.session['basket'] = basket  
    print(basket)
    return render(request, 'checkout/checkout.html')