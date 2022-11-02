from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark       #표
    #template name = 'bookmark[모델명] list.html'
    #context object name = 'object list'

class BookmarkDV(DetailView):
    model = Bookmark
