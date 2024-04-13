from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

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

@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) #데이터 바인딩된 폼
        if form.is_valid():
        #데이터를 저장
            article = form.save() 
        # 다른곳으로 리다이렉트
            return redirect("article_detail", article.pk)
    else:
            form = ArticleForm()
    context = {"form": form}    
    return render(request, "create.html", context)
    

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles")
    return redirect("article_detail", pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "form" : form,
        "article": article,
    }
    return render(request, "update.html", context)
    


