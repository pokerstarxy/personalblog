from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
from models import BlogPost,Movie
from django.shortcuts import render_to_response,redirect,get_object_or_404
from math import ceil
from collections import defaultdict
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.
# home,blogpost,archive,about,talks,rss
exclude_posts = ("about", "projects", "talks")

@cache_page(60)
def home(request,page=''):
    args={}
    args['blogposts'] = BlogPost.objects.exclude(title__in=exclude_posts)
    max_page = ceil(len(args['blogposts']) / 3)
    if page and int(page) < 2:  # /0, /1 -> /
        return redirect("/")
    else:
        page = int(page) if (page and int(page) > 0) else 1
        args['page'] = page

        args['prev_page'] = page+1 if page <= max_page else None


        args['newer_page'] = page - 1 if page >= 1 else None
        # as template slice filter, syntax: list|slice:"start:end"
        args['sl'] = str(3 * (page - 1)) + ':' + str(3 * (page - 1) + 3)
        #import datetime
        #args['date_now']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render(request, 'css3two_blog/index.html', args)


@cache_page(60*5)
def blogpost(request, slug, post_id):
    args = {'blogpost': get_object_or_404(BlogPost, pk=post_id)}
    return render(request, 'css3two_blog/blogpost.html', args)

@cache_page(60)
def archive(request):
    args = dict()
    blogposts = BlogPost.objects.exclude(title__in=exclude_posts)

    def get_sorted_posts(category):
        posts_by_year = defaultdict(list)
        posts_of_a_category = blogposts.filter(category=category)  # already sorted by pub_date
        for post in posts_of_a_category:
            year = post.pub_date.year
            posts_by_year[year].append(post)  # {'2013':post_list, '2014':post_list}
        posts_by_year = sorted(posts_by_year.items(), reverse=True)  # [('2014',post_list), ('2013',post_list)]
        return posts_by_year

    args['data'] = [
        ('programming', get_sorted_posts(category="programming")),
        ('nt', get_sorted_posts(category="nt")),
        ('nc', get_sorted_posts(category="nc")),  # no category
    ]

    return render(request, 'css3two_blog/archive.html', args)

@cache_page(60*5)
def about(request):
    the_about_post = get_object_or_404(BlogPost, title="about")
    args = {"about": the_about_post}
    return render(request, 'css3two_blog/about.html', args)


def article(request, freshness):
    """ redirect to article accroding to freshness, latest->oldest:freshness=1->N """
    if freshness.isdigit():
        try:
            article_url = BlogPost.objects.all()[int(freshness) - 1].get_absolute_url()
            return redirect(article_url)
        except IndexError:
            raise Http404
        except AssertionError:  # freshness=0
            raise Http404
    else:
        return redirect('/')


def movies(request,page=1):

    try:
        page=int(page)

    except Exception:
        return redirect('/movies')
    else:
        if page < 1:
            return redirect('/movies')
        else:
            args= defaultdict(list)
            mv_list=Movie.objects.order_by('-id')
            slpage=Paginator(mv_list,100)
            args['data']=slpage.page(page)
            args['older_page']=page+1 if page< slpage.num_pages else 0
            args['ne_page']=page-1 if page> 1 else 0
            args['pre_page']=page
            return render_to_response('css3two_blog/movie.html',args)


def webchat(request):
    # use markdown to show talks, could be changed if need better formatting
    html = "<meta http-equiv=\"refresh\" content=\"3;url= \
           /\">Under Development. Will return to homepage."
    return HttpResponse(html)


def contact(request):

    return render_to_response('contact_form/contact_form.html')


def mailme(request):
    mail_cont=request.GET["body"]
    mail_name=request.GET["name"]
    mail_email=request.GET["email"]
    recipients=['pokerstar_xy@sina.com']
    recipients.append(mail_email)
    send_mail(mail_name, mail_cont, 'pokerstar_xy@sina.com', recipients)
    return redirect('/')


