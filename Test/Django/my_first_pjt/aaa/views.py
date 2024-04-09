from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def users(request):
    return render(request, "users.html")

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
