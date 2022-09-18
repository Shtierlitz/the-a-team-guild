from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from .utils import *
from .forms import *
from .models import *
from characters.utils import DataMixin




class CharacterHome(DataMixin, ListView):
    paginate_by = 10
    model = Character
    template_name = 'characters/index.html'
    context_object_name = "posts"   # изменение названия переменной для шаблона
    # extra_context = {'title': "Главная страница"} # название вкладки. (только статические)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Character.objects.filter(is_published=True).select_related('cat')
        # select_related нужен чтобы не дублировались sql запросы


class ShowPost(DataMixin, DetailView):
    model = Character
    template_name = 'characters/post.html'
    slug_url_kwarg = 'post_slug'           # изменение название переменной для urls.py (по умолчанию slug)
    # pk_url_kwarg = 'post_pk'     # тоже, но для id (по умолчанию pk)
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = context['post']
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class CharacterCategory(DataMixin, ListView):
    model = Character
    template_name = 'characters/index.html'
    context_object_name = 'posts'
    allow_empty = False # 404 если нету записей

    def get_queryset(self):
        return Character.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Фракция - ' + str(context['posts'][0].cat)
        # context['menu'] = menu
        # context['cat_selected'] = context['posts'][0].cat_id
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Фракция - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    contact_list = Character.objects.all()
    paginator = Paginator(contact_list, 3)  # класс пагинатора для функции

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "characters/about.html", {'page_obj': page_obj, 'menu': menu, 'title': "О сайте"})
# def about(request):
#     return render(request, 'characters/about.html', {"menu": menu, 'title': "О сайте"})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'characters/addpage.html'
    success_url = reverse_lazy('home')          # формирует маршрут на случай если не сделана get_absolute_url()
    login_url = reverse_lazy('login')             # переадресация на страницу регистрации
    raise_exception = True                  # страница на случай невтаоризации

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление персонажа')
        return dict(list(context.items()) + list(c_def.items()))

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'characters/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['content'])
        return redirect('home')


def send_message(name, email, content):
    text = get_template("characters/message.html")
    html = get_template("characters/message.html")
    context = {
        'name': name,
        'email': email,
        'content': content
    }
    subject = "Сообщение от пользователя"
    from_email = "example@gmail.com"
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['rollbar1990@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

class Register_User(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'characters/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_falid(self, form):
        """При успешной регистрации пользователь автоматически авторизируется
         и перенаправляется на главную страницу"""
        user = form.save()  # сохраняем форму в БД
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'characters/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     """Возвращает на главную страницу если валидация прошла успешно (иначе ошибка)
    #     альтернатива ему LOGIN_REDIRECT_URL = '/' в settings.py"""
    #     return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')



# def categories(request, catid):
#     return HttpResponse(f"<h1>categories {catid}</h1>")
#
# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)
#
#     return HttpResponse(f"<h1>archive {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def serverError(request):
    return HttpResponseServerError("<h1>Ошибка сервера</h1>")

# def index(request):
#     posts = Character.objects.all()
#
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': "Главная страница",
#         'cat_selected': 0,
#     }
#     return render(request, 'characters/index.html', context=context)

# def show_category(request, cat_slug):
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = Character.objects.filter(cat_id=cat[0].id)
#
#
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': "Отображене по рубрикам",
#         'cat_selected': cat[0].id,
#
#     }
#
#     return render(request, 'characters/index.html', context=context)

# def show_post(request, post_slug):
#     post = get_object_or_404(Character, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'characters/post.html', context=context)


# def addpage(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'form': form,
#         'menu': menu,
#         'title': 'Добавление персонажа'
#     }
#     return render(request, 'characters/addpage.html', context=context)

# def login(request):
#     return HttpResponse("Авторизация")

# def contact(request):
#     return HttpResponse("Обратная связь")