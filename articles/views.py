from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import ArticleForm
from .models import Article
# Create your views here.

def article_detail_view(request, slug=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", 
                  context=context)

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query)
    context = {
        "object_list": qs,
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm() 
        return redirect('article-detail', slug=article_object.slug)
        # context['created'] = True
    return render(request, "articles/create.html", 
                  context=context)