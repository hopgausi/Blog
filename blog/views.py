from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.text import slugify
from django.views import generic
from .models import Article
from .forms import ArticleForm

class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self): 
        articles = Article.objects.filter(publish=True)[:5]
        return articles


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'title'
        return context
    

@login_required
def create_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            #get logged in user
            post_author =  request.user
            #slugify post title
            post_title = slugify(form.cleaned_data.get('title'))
            # save the post without commiting to db
            post = form.save(commit=False)

            # assign to post Article model
            post.slug = post_title
            post.author = post_author
            # save the post
            post.save()
            messages.success(request, 'Your Post Has been created!')
            return redirect('blog:home')

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    template_name = 'blog/create_post.html'
    return render(request, template_name, context)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
           return True
        else:
            return False
    
     

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Article
    success_url = '/'
    template_name = 'blog/delete_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
           return True
        else:
            return False