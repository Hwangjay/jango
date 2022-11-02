from django.urls import path, re_path
# from blog.views import PostLV, PostDV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name = 'index'),
    # /blog/
    path('post/', views.PostLV.as_view(), name = 'post_list'),
    # /blog/post/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name = 'post_detail'), #파이썬 정규 표현식
    # /blog/post/'뚫리지 않는 방패'…양자 시대 준비하는 이통3사(종합)/
    path('archive/', views.PostAV.as_view(), name = 'post_archive'),
    # /blog/archive/
    path('archive/<int:year>/', views.PostYAV.as_view(), name = 'post_year_archive'),
    # /blog/archive/2021/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name = 'post_month_archive'),
    # /blog/archive/2021/jul/
    path('archive/<int:year>/<str:month>/<int:day>', views.PostDAV.as_view(), name = 'post_day_archive'),
    # /blog/archive/2021/jul/05/
    path('archive/today/', views.PostTAV.as_view(), name = 'post_today_archive'),
    # /blog/archive/today/
]