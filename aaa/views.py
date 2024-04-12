from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Article.objects.all().order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles.html", context)

def article_detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article,}
    return render(request, "article_detail.html", context)

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data,
            }

    return render(request, "data_catch.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article.objects.create(title=title, content=content)# DB에 저장
    return redirect("article_detail", article.pk)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles")
    return redirect("article_detail", pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "edit.html", context)

def update(request, pk):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect("article_detail", article.pk)
    


