from django.shortcuts import render, get_object_or_404
from .models import Package
from .forms import PackageForm

def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)

def package_detail(request, package_id):
    """ A view to show individual package details """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'packages/package_detail.html', context)


def add_package(request):
    """ Add a package to the store """
    form = PackageForm()
    template = 'packages/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
