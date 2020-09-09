from django.shortcuts import render,get_object_or_404
from .models import  Post
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from taggit.models import Tag
def post_list_view(request ,tag_slug = None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag , slug = tag_slug)
        post_list = post_list.filter(tags__in =[tag])
    pagintaor = Paginator(post_list , 2)
    page_number = request.GET.get('page')
    try:
        post_list = pagintaor.page(page_number)
    except PageNotAnInteger:
        post_list = pagintaor.page(1)
    except EmptyPage:
        post_list = pagintaor.page(pagintaor.num_pages)
    return render(request ,'blog/post_list.html',{'post_list':post_list ,'tag':tag})

from .forms import CommentForm

def post_detail_view(request , year , month , day , post):
    post = get_object_or_404(Post , slug = post , status = 'published' , publish__year = year , publish__month = month , publish__day = day)
    comments = post.comments.filter(active = True)
    comment_submit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_submit = True
    else:
        form = CommentForm()
    return render(request , 'blog/post_detail.html',{'post':post , 'form':form , 'comment_submit':comment_submit ,'comments':comments})


#class based views

# from django.views.generic import ListView
#
# class PostListView(ListView):
#     model = Post
#     paginate_by = 2

from django.core.mail import send_mail
from .forms import SendMailForm

def send_mail_view(request,id):
    post = get_object_or_404(Post , id = id , status = 'published')
    sent = False
    if request.method == 'POST':
        form  = SendMailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{}({}) Recommends to read '.format(cd['name'],cd['email'])
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = 'Read Post at : \n {} \n\n {}\'s Comments : \n{}'.format(post_url,cd['name'],cd['comment'])
            send_mail(subject,message,'durga@gmail.com',[cd['to']])
            sent = True
    else:
        form = SendMailForm()
    return render(request , 'blog/sharebymail.html', {'form':form ,'post':post,'sent':sent})
