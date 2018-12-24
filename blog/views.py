from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from . import models
from django.contrib.auth.models import User
from comments.views import CommentCreateView


def home(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post,id=pk)
        form = CommentCreateView(request.POST)
        if form.form_valid(post):
            form.save()
            messages.success(request, f'Your comment is posted!')
            return redirect('post-comments', pk)
    else:
            context = {
            'post': get_object_or_404(Post,id=pk),
            'form': CommentCreateView()
            }
    return render(request,'blog/post_detail.comments.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'# <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'summary', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'summary', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def selfConciousnessView(request,pk):
    context = {}
    if request.method == 'POST':
        questionnaire = get_object_or_404(models.Questionnaire,id=pk)
        for items in questionnaire.items.all():

            print(items.text)
        return redirect('questionnaire', pk)
    else:
            survey = get_object_or_404(models.Questionnaire,id=pk)

            context = {
            'survey': survey,
            'range':range(0,4),
            }
    return render(request,'blog/questionnaire.html',context)