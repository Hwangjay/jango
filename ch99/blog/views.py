from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
# from models import Post
from blog.models import Post

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2    #한 페이지에 보이는 글 개수 설정

class PostDV(DetailView):
    model = Post
    #template_name = 'post_detail.html'

class PostAV(ArchiveIndexView):
    model = Post
    # template_name = 'post_archive.html'
    date_field = 'modify_dt' # 기준 날짜, 날짜별로 정리


class PostYAV(YearArchiveView):
    model = Post
    # template_name = 'post_archive_year.html'
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    # template_name = 'post_archive_month.html'
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    # template_name = 'post_archive_day.html'
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    # template_name = 'post_archive_day.html'
    date_field = 'modify_dt'