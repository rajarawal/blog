from blog.models import Post
from django import template

register = template.Library()
#or define custom name also : @register.simple_tag(name = 'some_name')
@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post123.html')
def show_latest_post(count = 3):
    latest_post = Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}

from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count = 3):
    return Post.objects.annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]
