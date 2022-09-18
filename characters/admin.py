from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')# 'get_html_photo',
    list_display_links = ('id', 'title')
    search_fields = ('title', 'about')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    # отображает поля для редактирвания в админке
    fields = ('title', 'about', 'photo', "get_html_photo", 'slug', 'is_published',
              'abil1', 'skil1', 'photo_skill_1', 'get_html_photo_1',
              'abil2', 'skil2', 'photo_skill_2', 'get_html_photo_2',
              'abil3', 'skil3', 'photo_skill_3', 'get_html_photo_3',
                'abil4', 'skil4', 'photo_skill_4', 'get_html_photo_4',
              'abil5', 'skil5', 'photo_skill_5', 'get_html_photo_5',
                 'abil6', 'skil6', 'photo_skill_6', 'get_html_photo_6',
              'abil7', 'skil7', 'photo_skill_7', 'get_html_photo_7',
                'abil8', 'skil8', 'photo_skill_8', 'get_html_photo_8',
              'abil9', 'skil9', 'photo_skill_9', 'get_html_photo_9',
                'abil10', 'skil10', 'photo_skill_10', 'get_html_photo_10',
              'abil11', 'skil11', 'photo_skill_11', 'get_html_photo_11',
              'cat', 'time_create', 'time_update')

    # отображает нередактируемые поля
    readonly_fields = ('time_create', 'time_update', 'get_html_photo', 'get_html_photo_1',
                       'get_html_photo_2', 'get_html_photo_3', 'get_html_photo_4',
                       'get_html_photo_5', 'get_html_photo_6', 'get_html_photo_7',
                       'get_html_photo_8', 'get_html_photo_9', 'get_html_photo_10',
                       'get_html_photo_11')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


    def get_html_photo_1(self, object):
        if object.photo_skill_1:
            return mark_safe(f"<img src='{object.photo_skill_1.url}' width=50>")

    get_html_photo_1.short_description = "Основная"

    def get_html_photo_2(self, object):
        if object.photo_skill_2:
            return mark_safe(f"<img src='{object.photo_skill_2.url}' width=50>")

    get_html_photo_2.short_description = "Особая"

    def get_html_photo_3(self, object):
        if object.photo_skill_3:
            return mark_safe(f"<img src='{object.photo_skill_3.url}' width=50>")

    get_html_photo_3.short_description = "Особая"

    def get_html_photo_4(self, object):
        if object.photo_skill_4:
            return mark_safe(f"<img src='{object.photo_skill_4.url}' width=50>")

    get_html_photo_4.short_description = "Особая"

    def get_html_photo_5(self, object):
        if object.photo_skill_5:
            return mark_safe(f"<img src='{object.photo_skill_5.url}' width=50>")

    get_html_photo_5.short_description = "Лидерская"

    def get_html_photo_6(self, object):
        if object.photo_skill_6:
            return mark_safe(f"<img src='{object.photo_skill_6.url}' width=50>")

    get_html_photo_6.short_description = "Уник."

    def get_html_photo_7(self, object):
        if object.photo_skill_7:
            return mark_safe(f"<img src='{object.photo_skill_7.url}' width=50>")

    get_html_photo_7.short_description = "Уник."

    def get_html_photo_8(self, object):
        if object.photo_skill_8:
            return mark_safe(f"<img src='{object.photo_skill_8.url}' width=50>")

    get_html_photo_8.short_description = "Уник."

    def get_html_photo_9(self, object):
        if object.photo_skill_9:
            return mark_safe(f"<img src='{object.photo_skill_9.url}' width=50>")

    get_html_photo_9.short_description = "Уник."

    def get_html_photo_10(self, object):
        if object.photo_skill_10:
            return mark_safe(f"<img src='{object.photo_skill_10.url}' width=50>")

    get_html_photo_10.short_description = "Уник."

    def get_html_photo_11(self, object):
        if object.photo_skill_11:
            return mark_safe(f"<img src='{object.photo_skill_11.url}' width=50>")

    if get_html_photo_11:
        get_html_photo_11.short_description = "Абсолютная."


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name",)}       # Заполняет слаги автоматически на основе поля name


admin.site.register(Character, CharacterAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Админ-панель The A Team Galaxy"
admin.site.site_header = "Админ-панель The A Team Galaxy"
