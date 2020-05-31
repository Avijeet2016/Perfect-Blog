from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, CategoryForm, PostForm 
from .models import Post, Category


def post_list(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    search = request.GET.get('s')
    if search:
        post_list = post_list.filter (
            Q(title__icontains=search) | 
            Q(content__icontains=search)
        )
    paginator = Paginator(post_list, 5)  # 5 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    context = {'post_list': post_list, 'page': page}
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug)
    new_comment = None
    if post.exists():
        post = post.first()
        comments = post.comments.filter(active=True)
        related = Post.objects.filter(category=post.category).exclude(slug=slug)[:6]
    else:
        return HttpResponse('<h3>Page not found</h3>')
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': post, 
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'related': related,
        }
    return render(request, 'blog/post_detail.html', context)


def blog_post_list(request):
    posts = Post.objects.order_by('-created_on')
    context = {'posts': posts, }
    return render(request, 'admin/blog_post_list.html', context)


def blog_post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post, }
    return render(request, 'admin/blog_post_detail.html', context)


def create_blog_post(request):
    if request.user.is_authenticated:
        post_form = PostForm(request.POST or None)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.save()
            messages.success(request, 'New Post is created successfully!')
            return redirect('blog:blog-post-list')
        context = {'post_form': post_form, }
        return render(request, 'admin/create_blog_post.html', context)
    else:
        return redirect('blog:blog-post-list')


def update_blog_post(request, id):
    if request.user.is_authenticated:
        post_obj = get_object_or_404(Post, id=id)
        post_form = PostForm(request.POST or None, instance=post_obj)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.save()
            messages.success(request, 'Post is updated successfully!')
            return redirect('blog:blog-post-list')
        context = {'post_form': post_form, }
        return render(request, 'admin/update_blog_post.html', context)
    else:
        return redirect('blog:blog-post-list')


def delete_blog_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=id)
        post.delete()
        messages.warning(request, 'Post is deleted!!')
        return redirect('blog:blog-post-list')
    else:
        return redirect('blog:blog-post-list')


def catwise_post(request, cat_name):
    cat_obj = Category.objects.get(name=cat_name)
    post_list = Post.objects.filter(category=cat_obj)
    context = {'post_list': post_list, }
    return render(request, 'blog/catwise_post.html', context)


def create_category(request):
    if request.user.is_authenticated:
        cat_form = CategoryForm(request.POST or None)
        if cat_form.is_valid():
            instance = cat_form.save(commit=False)
            instance.save()
            messages.success(request, 'Category is created successfully!')
            return redirect('blog:category-list')
        context = {'cat_form': cat_form, }
        return render(request, 'admin/create_category.html', context)
    else:
        return redirect('blog:category-list')


def category_list(request):
    categories = Category.objects.order_by('-id')
    context = {'categories': categories, }
    return render(request, 'admin/category_list.html', context)


def update_category(request, id):
    if request.user.is_authenticated:
        cat_obj = get_object_or_404(Category, id=id)
        cat_form = CategoryForm(request.POST or None, instance=cat_obj)
        if cat_form.is_valid():
            instance = cat_form.save(commit=False)
            instance.save()
            messages.success(request, 'Category is updated successfully!')
            return redirect('blog:category-list')
        context = {'cat_form': cat_form, }
        return render(request, 'admin/update_category.html', context)
    else:
        return redirect('blog:category-list')


def delete_category(request, id):
    if request.user.is_authenticated:
        cat_obj = get_object_or_404(Category, id=id)
        cat_obj.delete()
        messages.warning(request, 'Category is deleted!!')
        return redirect('blog:category-list')
    else:
        return redirect('blog:category-list')

