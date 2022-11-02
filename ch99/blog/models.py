from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', max_length=50, unique=True, allow_unicode=True, help_text='one word for title alies.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    # 내부 클래스
    # 필드 속성 외 필요 데이터(파라미터) 사용 목적
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'       # 디폴트 값 : 앱명_모델클래스명
        ordering = ('-modify_dt',)    # 정렬 (날짜순)

    def __str__(self):
        return self.title

    # 메소드가 정의된 객체를 지칭하는 url 반환
    # 제목에서 중요 단어를 뽑아서 만든 슬러그를 주소창에서 사용할 url로 지정
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_dt를 기준으로 최신 포스트 반환
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    # modify_dt를 기준으로 예전 포스트 반환
    def get_next(self):
        return self.get_next_by_modify_dt()