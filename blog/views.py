from django.views import generic
from django.urls import reverse_lazy
# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse

from .models import post
from .forms import PostForm



class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

# def post_list_view(request):
#     posts_list = post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

# def post_detail_view(request, pk):
#     Post = get_object_or_404(post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': Post})


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})

# def post_update_view(request, pk):
#     Post = get_object_or_404(post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=Post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={'form': form})

# def post_delete_view(request, pk):
#     Post = get_object_or_404(post, pk=pk)
#     if request.method == 'POST':
#         Post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'Post': Post})


