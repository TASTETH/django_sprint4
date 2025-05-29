from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import get_object_or_404
from .models import Post, Category
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserUpdateForm


User = get_user_model()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'image', 'category']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        qs = Post.objects.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)[:5]


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_queryset(self):
        qs = Post.objects.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)


class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(
            Category,
            slug=category_slug,
            is_published=True
        )
        qs = self.category.posts.select_related(
            'category', 'location', 'author'
        ).all()
        return filter_published_posts(qs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def filter_published_posts(queryset):
    return queryset.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )


class ProfileDetailView(DetailView):
    model = User
    template_name = 'blog/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts = user.post_set.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        ).select_related('category', 'location', 'author')
        context['page_obj'] = posts
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'blog/user.html'
    success_url = reverse_lazy('blog:profile')

    def get_object(self, queryset=None):
        return self.request.user
