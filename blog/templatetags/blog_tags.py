from atexit import register
from unicodedata import category
from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts=Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-postcategories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dic = {}
    for name in categories:
        cat_dic[name] = posts.filter(category=name).count()
    return {'categories':cat_dic}