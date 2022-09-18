from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from characters.views import *
from django.urls import path, include


from the_a_team_galaxy import settings

urlpatterns = [
    path("", CharacterHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path("addpage/", AddPage.as_view(), name='add_page'),
    # path("addpage/", addpage, name='add_page'),
    # path("contact/", contact, name='contact'),
    path("contact/", ContactFormView.as_view(), name='contact'),
    path("login/", LoginUser.as_view(), name='login'),
    path("logout/", logout_user, name='logout'),
    path("register/", Register_User.as_view(), name='register'),
    # path("login/", login, name='login'),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name='post'),
    path("category/<slug:cat_slug>/", CharacterCategory.as_view(), name='category'),
    # path("post/<slug:post_slug>/", show_post, name='post'),
    # path("category/<slug:cat_slug>/", show_category, name='category'),
]

