from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Release(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=200)
    version = models.CharField("Версия", max_length=200, blank=True, null=True)
    name = models.CharField("Исполнитель", max_length=200)
    cover = models.ImageField("Обложка", upload_to="covers/")
    cover_resized = ImageSpecField(source='cover',
                                   processors=[ResizeToFill(652, 652)],
                                   format='JPEG',
                                   options={'quality': 99})
    slug = models.SlugField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return "[%s] %s (%s) - %s" % (self.slug, self.name, self.version, self.title)

    def save(self, *args, **kwargs):
        slug_save(self)  # call slug_save, listed below
        super(Release, self).save(*args, **kwargs)


def slug_save(obj):
    """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    # Code by Jeremy S. on StackOverflow
    if not obj.slug:  # if there isn't a slug
        obj.slug = get_random_string(5, 'abcdefghijklmnopqrstuvwxyz0123456789')  # create one
        slug_is_wrong = True
        while slug_is_wrong:  # keep checking until we have a valid slug
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                slug_is_wrong = True
            naughty_words = [
                'promo',
                'admin',
                'exjaw',
            ]
            if obj.slug in naughty_words:
                slug_is_wrong = True
            if slug_is_wrong:
                # create another slug and check it again
                obj.slug = get_random_string(5, 'abcdefghijklmnopqrstuvwxyz0123456789')

    class Meta:
        verbose_name = "Релиз"
        verbose_name_plural = "Релизы"


class Platform(models.Model):
    title = models.CharField("Площадка", max_length=100)
    icon = models.ImageField("Иконка площадки", upload_to="platform/")

    SERVICE = "SER"
    SOCIAL = "SOC"
    PLATFORM_TYPE_CHOICES = [
        (SERVICE, "Сервис"),
        (SOCIAL, "Соц. сеть"),
    ]
    platform_type = models.CharField(
        max_length=3,
        choices=PLATFORM_TYPE_CHOICES,
        default=SERVICE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"


class Link(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    url = models.URLField(max_length=160)
    vision = models.BooleanField("Видимость", default=True)

    def __str__(self):
        return "%s - %s (%s)" % (self.platform.title, self.release.title, self.release.name)

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
