from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('bookmark/', include)'bookmark.urls')),
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]