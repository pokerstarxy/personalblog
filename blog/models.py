#coding=utf8
from __future__ import unicode_literals

from django.db import models
# from django.utils import timezone
# for slug, get_absolute_url
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from datetime import datetime

# delete md_file before delete/change model
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.base import ContentFile
from unidecode import unidecode
from taggit.managers import TaggableManager
import markdown,os,sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# Create your models here.

upload_dir = 'content/BlogPost/%s/%s'


class BlogPost(models.Model):

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural='博客'

    def get_html_name(self,filename):
        if self.pub_date:
            year = self.pub_date.year
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, filename)
        return upload_to

    def get_upload_md_name(self,filename):
        if self.pub_date:
            year = self.pub_date.year   # always store in pub_year folder
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, self.title + '.md')
        return upload_to
    CATEGORY_CHOICES={
        ('programming', 'Programming'),
        ('nt', 'Note'),
        ('nc', 'No Category'),
    }
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    md_file = models.FileField(upload_to=get_upload_md_name,blank=True)
    pub_date = models.DateTimeField( auto_now_add=True)
    last_edit_date = models.DateTimeField( auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    html_file = models.FileField(upload_to=get_html_name)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    @property
    def filename(self):
        if self.md_file:
            return os.path.basename(self.title)
        else:
            return 'no_md_file'

    def savec(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        if not self.body and self.md_file:
            self.body = self.md_file.read()
        html = markdown.markdown(self.body)
        self.html_file.save(self.title + '.html',
                            ContentFile(html.encode('utf-8')), save=True)
        #self.md_file.delete(save=True)
        super(BlogPost,self).save(*args, **kwargs)

    def display_html(self):
        with open(self.html_file.path) as f:
            return f.read()

    def get_absolute_url(self):
        return reverse('blogpost',kwargs={'slug': self.slug, 'post_id': self.id})


@receiver(pre_delete, sender=BlogPost)
def blogpost_delete(instance,**kwargs):
    if instance.md_file:
        instance.md_file.delete(save=True)
    if instance.html_file:
        instance.html_file.delete(save=True)


class BlogPostImage(models.Model):
    def get_upload_img_name(self, filename):
        upload_to = upload_dir % ('images', filename)  # filename involves extension
        return upload_to

    blogpost = models.ForeignKey(BlogPost, related_name='images')
    image = models.ImageField(upload_to=get_upload_img_name)


class Movie(models.Model):
    num = models.CharField(max_length=20,unique=True)
    date = models.TextField(max_length=20,blank=True)
    name = models.TextField(max_length=100)
    country = models.TextField(max_length=20,blank=True)
    language = models.TextField(max_length=50,blank=True)
    star = models.TextField(max_length=200,blank=True)
    detail = models.TextField(blank=True)
    xl_url = models.TextField(max_length=150,blank=True)
    bd_url = models.TextField(max_length=50,blank=True)
    bd_pwd = models.CharField(max_length=5,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='电影'
        ordering = ['pub_date']
    def __unicode__(self):
        return self.name





