from django.contrib import admin
# Bookmark 디렉터리의 models.py에서 Bookmark 클래스 가져와서 사용
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','url')
