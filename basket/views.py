from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_to_basket(request, package_id):
    """ Add a package to the basket """

    date = request.POST.get('photodate')

    request.session['basket'] = {f'{package_id}': date}
    messages.success(request, 'Successfully added to the basket!')
    return redirect(reverse('checkout'))
