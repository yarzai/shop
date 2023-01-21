from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def welcome(request):

    # return HttpResponse("<h1>Hi</h1>")
    val = "Hi"
    print(dir(request))
    print(request.user)

    return render(request, 'products/welcome.html', {"result": val, "test": 12})


def test():
    print("done")
