#coding=utf8
from django.contrib import admin
# Register your models here.
from .models import BlogPost, BlogPostImage,Movie
from django.forms import TextInput, Textarea
from django import forms
from django.core.files.base import ContentFile
from django.conf import  settings
import os


class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage
    extra = 3

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('num',)



class BlogPostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        widgets = {
            'body': Textarea(attrs={'rows': 30, 'cols': 100}),
            'title': TextInput(attrs={'size': 40}),
        }
        exclude = ('html_file',)


class BlogPostAdmin(admin.ModelAdmin):

    form = BlogPostAdminForm
    inlines = [BlogPostImageInline, ]

    # @staticmethod
    # def delete_old_md_file():
    #     # delete old md files, this method is unused now
    #     md_file_list = []
    #     for blogpost in BlogPost.objects.all():
    #         if blogpost.md_file:
    #             md_file_list.append(blogpost.filename)
    #
    #     with open('md_file_list.txt', 'wt') as f:
    #         f.write(str(md_file_list))
    #
    #     for root, subdirs, files in os.walk(os.path.join(settings.MEDIA_ROOT, 'content/BlogPost')):
    #         for file in files:
    #             if file not in md_file_list:
    #                 os.remove(os.path.join(root, file))

    def save_model(self, request, obj, form, change):
        if obj:
            filename = obj.filename
            if not obj.body:   # body有内容的时候才会更新md_file
                if filename != 'no_md_file':
                    obj.body = obj.md_file.read()
            obj.md_file.delete(save=True)
            obj.html_file.delete(save=True)
            obj.md_file.save(filename+'.md', ContentFile(obj.body.encode('utf8')), save=True)
            obj.savec()


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Movie)