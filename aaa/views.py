from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def hello(request):
    name = "우영"
    tags = ["#활발한", "#많이힘듬"]
    game = {
        "today": "구스구스덕",
        "yesterday": "롤",
        "tomorrow": "GTA5",
    }

    context ={
        "name": name,
        "tags": tags,
        "game": game,

    }
    return render(request, "hello.html", context)

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data,
            }

    return render(request, "data_catch.html", context)

