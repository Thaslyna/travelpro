from django.shortcuts import render


from tvelapp.models import Destination


# Create your views here.


def home(request):
    obj = Destination.objects.all()
    return render(request, "index.html", {'results': obj})
