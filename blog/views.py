from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Post, Comment, Like
from .forms import CommentForm, FeedBackForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, resolve

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
        post = Post.objects.get(id=post_id)

        obj, created = Like.objects.get_or_create(post= post, user=request.user)
        if created:
            likeCount = post.like_set.all().count()
            return JsonResponse({"status": True, "likeCount": likeCount})
        else:
            obj.delete()
            likeCount = post.like_set.all().count()
            return JsonResponse({'status': False, "likeCount": likeCount})

def commentDelete(request):
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        delComment = Comment.objects.get(pk=int(comment_id)).delete()
        return JsonResponse({'message':"Comment Deleted Successfully!", "status": True})
    else:
        return JsonResponse({'message': "Cannot delete comment"+ str(delComment), "status": False})

@method_decorator(csrf_exempt, name='dispatch')
def commentUpdate(request, pk):

    if request.method == 'POST':
        request.POST._mutable = True
        comm = Comment.objects.get(pk=pk)
        request.POST['post'] = comm.post.id

        form = CommentForm(request.POST, instance=comm)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Comment Updated", 'post_id': comm.post.id})
        else:
            return JsonResponse({'error': form.errors, 'post_id': comm.post.id })
    else:
        comment = Comment.objects.get(pk=pk)
        initial = {'body': comment.body}
        form = CommentForm(initial=initial)
        comment_id = comment.pk
        context ={
            'comment_id': comment_id,
            'form': form
        }
        html = render_to_string('blog/update_comment.html', context)
        return HttpResponse(html)


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
        comments = Comment.objects.filter(post = post).order_by('-id')
        context = {
            'post': post,
            'comments': comments,
            'form': form
            
        }
        return render(request, self.template_name, context)



    def post(self, request,*args, **kwargs):
        request.POST._mutable = True

        post = Post.objects.get(pk=self.kwargs['pk'])
        request.POST['post'] = post.id
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            comment = Comment(author=request.user.username, body = form.cleaned_data['body'], post= post)
            comment.save()
            form = self.form_class()
        comments = Comment.objects.filter(post=post).order_by('-id')
        form = self.form_class()
        context = {
            "post": post, 
            "form": form,
            "comments": comments
        }
        return redirect('post-detail', pk=post.id)        # return render(request, self.template_name, context)
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


def profile_intro(request):
    links = settings.SOCIAL_LINKS


    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_mail('Thanks you for your feedback', 'We Will contact you shorly', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            form = FeedBackForm()
            return render(request, 'blog/selfprofile.html', {'form': form, 'links': links})
    form = FeedBackForm()

    return render(request, 'blog/selfprofile.html', {'form': form, 'links': links})