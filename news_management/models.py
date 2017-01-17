from django.db import models
from userprofile.models import Staff
from django.utils import timezone


class Post(models.Model):
    """
    abstract model, including every items be shown in new website
    """
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)
    last_modify_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Staff,
        related_name='created_posts',
        on_delete=models.SET_NULL,
        null=True
    )
    editor = models.ForeignKey(
        Staff,
        related_name='edit_posts',
        on_delete=models.SET_NULL,
        null=True
    )

    view_number = models.IntegerField(default=0)
    like_number = models.IntegerField(default=0)
    tags = models.ManyToManyField(
        'Tag',
        related_name='tagged_posts'
    )

    def __str__(self):
        return self.title


class Article(Post):
    """
    abstract article model
    """
    class Meta:
        abstract = True

    photographer = models.ForeignKey(
        Staff,
        related_name='photograph_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    content = models.TextField()


class UncheckedArticle(Article):
    """
    create new item when staff in college cast a new manuscript
    """
    author = models.ForeignKey(
        Staff,
        related_name='created_unchecked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    editor = models.ForeignKey(
        Staff,
        related_name='edit_unchecked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    photographer = models.ForeignKey(
        Staff,
        related_name='photograph_unchecked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='tagged_unchecked_articles'
    )


class CheckedArticle(Article):
    """
    news articles displayed on the site
    """
    check_time = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        Staff,
        related_name='created_checked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    editor = models.ForeignKey(
        Staff,
        related_name='edit_checked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    photographer = models.ForeignKey(
        Staff,
        related_name='photograph_checked_articles',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='tagged_checked_articles'
    )


# class Album(Post):
#     """
#     UNDER CONSTRUCTION
#     consists of pictures, abstract
#     """
#
#
# class Photo(models.Model):
#     photographer = models.ForeignKey(
#         Staff,
#         related_name='photograph_photos',
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     photo_path = models.URLField()
#     description = models.TextField()
#     title = models.CharField(max_length=50)
#     album = models.ForeignKey(  # the album to which this photo belongs
#         Album,
#         related_name='photos',
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.title
#
#
# class Video(Post):
#     """
#     UNDER CONSTRUCTION
#     a video as a post
#     """
#     video_path = models.URLField()
#     description = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=50)
    is_main_tag = models.BooleanField  # whether as a navigation item

    def __str__(self):
        return self.name




























