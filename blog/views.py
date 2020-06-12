from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment, Like
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page


cache_page(300)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id=int(post_id))
        m = Like(post=likedpost)
        m.save()
        likeCount = likedpost.like_set.all().count()
        return JsonResponse({"message": "Success", "likeCount": likeCount})
    else:
        return JsonResponse({"message":"Unsuccess"})


def commentDelete(request):
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        delComment = Comment.objects.get(pk=int(comment_id)).delete()
        return JsonResponse({'message':"Comment Deleted Successfully!", "status": True})
    else:
        return JsonResponse({'message': "Cannot delete comment"+ str(delComment), "status": False})

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def get(self, request, *args, **kwargs):
        
        post = Post.objects.get(pk=self.kwargs['pk'])
        form = self.form_class()
        comments = Comment.objects.filter(post = post)
        context = {
            'post': post,
            'comments': comments,
            'form': form
        }
        return render(request, self.template_name, context)



    def post(self, request,*args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = Comment(author=request.user.username, body = form.cleaned_data['body'], post= post)
            comment.save()
            form = self.form_class()
        comments = Comment.objects.filter(post=post)
        context = {
            "post": post, 
            "form": form,
            "comments": comments
        }
        return render(request, self.template_name, context)
class PostCreateView(LoginRequiredMixin,  CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

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


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})