from django.shortcuts import render
from .models import Post, Category
from django.db.models import Count

# Create your views here.


def home(request):
    posts = Post.objects.all()

    categories = list(Post.objects.all().order_by('categories').values(
        'categories'
    ).annotate(count=Count('categories')))
    categories = {c['categories']: c['count'] for c in categories}
    # print(categories)
    all_category = list(Category.objects.all())
    all_category = {c.id: c.name for c in all_category}

    # create dictionary for category name and its post count
    cat_post = dict(zip(all_category.values(), categories.values()))

    # cat = {i.name: categories[i.id - 1]['count'] for i in all_category}
    # print(cat)
    return render(request, 'blog/home.html', {'posts': posts, 'categories': cat_post})


def iot_groups(request):
    return render(request, 'blog/iot_groups.html')


def ai_groups(request):
    return render(request, 'blog/ai_groups.html')


def energy_groups(request):
    return render(request, 'blog/energy_groups.html')


def robotics_groups(request):
    return render(request, 'blog/robotics_groups.html')


def lab_journal(request):
    return render(request, 'blog/lab_journal.html')


def lab_conf_talk(request):
    return render(request, 'blog/lab_conf-talk.html')


def events(request):
    return render(request, 'blog/events.html')


def future_member(request):
    return render(request, 'blog/future_member.html')


def about(request):
    return render(request, 'blog/about.html')


def post(request, slug):
    post = Post.objects.get(slug=slug)
    print(post)
    return render(request, 'blog/post.html', {'post': post})


def category(request, category_name):
    category = Category.objects.get(name=category_name)
    print(category.id)
    posts = Post.objects.filter(categories=category.id)
    print(posts)
    return render(request, 'blog/category.html', {
        'category_name': category_name,
        'posts': posts
    })
