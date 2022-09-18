from django.db import models
from django.urls import reverse


class Character(models.Model):
    title = models.CharField(max_length=255, verbose_name="Имя персонажа")
    about = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to='photos/characters', verbose_name="Фото")

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    skil1 = models.TextField(blank=True, verbose_name="Текст")
    skil2 = models.TextField(blank=True, verbose_name="Текст")
    skil3 = models.TextField(blank=True, verbose_name="Текст")
    skil4 = models.TextField(blank=True, verbose_name="Текст")
    skil5 = models.TextField(blank=True, verbose_name="Текст")
    skil6 = models.TextField(blank=True, verbose_name="Текст")
    skil7 = models.TextField(blank=True, verbose_name="Текст")
    skil8 = models.TextField(blank=True, verbose_name="Текст")
    skil9 = models.TextField(blank=True, verbose_name="Текст")
    skil10 = models.TextField(blank=True, verbose_name="Текст")
    skil11 = models.TextField(blank=True, verbose_name="Текст")

    abil1 = models.CharField(max_length=50, null=True, verbose_name="Основная", blank=True)
    abil2 = models.CharField(max_length=50, null=True, verbose_name="Особая", blank=True)
    abil3 = models.CharField(max_length=50, null=True, verbose_name="Особая", blank=True)
    abil4 = models.CharField(max_length=50, null=True, verbose_name="Особая", blank=True)
    abil5 = models.CharField(max_length=50, null=True, verbose_name="Лидерская", blank=True)
    abil6 = models.CharField(max_length=50, null=True, verbose_name="Уник.", blank=True)
    abil7 = models.CharField(max_length=50, null=True, verbose_name="Уник.", blank=True)
    abil8 = models.CharField(max_length=50, null=True, verbose_name="Уник.", blank=True)
    abil9 = models.CharField(max_length=50, null=True, verbose_name="Уник.", blank=True)
    abil10 = models.CharField(max_length=50, null=True, verbose_name="Уник.", blank=True)
    abil11 = models.CharField(max_length=50, null=True, verbose_name="Абсолютная", blank=True)

    photo_skill_1 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Основная", null=True, blank=True)
    photo_skill_2 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Особая", null=True, blank=True)
    photo_skill_3 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Особая", null=True, blank=True)
    photo_skill_4 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Особая", null=True, blank=True)
    photo_skill_5 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Лидерская", null=True, blank=True)
    photo_skill_6 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Уник.", null=True, blank=True)
    photo_skill_7 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Уник.", null=True, blank=True)
    photo_skill_8 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Уник.", null=True, blank=True)
    photo_skill_9 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Уник.", null=True, blank=True)
    photo_skill_10 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Уник.", null=True, blank=True)
    photo_skill_11 = models.ImageField(upload_to='photos/characters/skils', verbose_name="Абсолютная", null=True, blank=True)

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Фракция")
#
    def __str__(self):      # Возвращает title вместо pk при обращении
        return self.title
#
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Персонажи ЗВ"
        verbose_name_plural = "Персонажи ЗВ"
        ordering = ['title', 'time_create']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Фракция")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Фракция"
        verbose_name_plural = "Фракции"
        ordering = ['name']
