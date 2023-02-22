from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Note
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView


menu = [{'title': "Про сайт", 'url_name': 'home'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Категорії", 'url_name': 'notes'},
        {'title': "Category", 'url_name': 'cats'}]

# Create your views here.
class NotesHome(ListView):
    model = Note  # Модель список екземплярів якої будемо подавати
    template_name = 'notes/index.html'  # Адреса шаблону, куди подавати
    context_object_name = 'notes_list'  # Ім'я з яким викликається в шаблоні index.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Передаємо вже сформований контекст
        context['menu'] = menu
        context['title'] = 'Головна сторінка'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Note.objects.all()


# def get_notes_list(request):
#     context = {'notes_list': Note.objects.all()}
#     return render(request, 'notes/index.html', context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'notes/addpage.html'
    success_url = reverse_lazy('home')  # Маршрут, куди ми перейдемо після додавання статті
    # Функція reverse_lazy - будує маршрут коли він буде потрібен, а не наперед
    # Це запобігає помилці, коли маршрут намагається побудуватися, коли django
    # Ще його не побудував

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додавання статті'
        context['menu'] = menu
        return context


class AddCat(CreateView):
    form_class = AddCatForm
    template_name = 'notes/addcat.html'
    success_url = reverse_lazy('home')  # Маршрут, куди ми перейдемо після додавання статті
    # Функція reverse_lazy - будує маршрут коли він буде потрібен, а не наперед
    # Це запобігає помилці, коли маршрут намагається побудуватися, коли django
    # Ще його не побудував

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додавання категорії'
        context['menu'] = menu
        return context

class NotesListView(ListView):

    template_name = 'notes/index.html'

    def get_queryset(self):
        notes_category = self.request.GET.get('category', None)
        if notes_category:
            self.queryset = Note.objects.filter(category=notes_category)
        else:
            self.queryset = Note.objects.all()
        return self.queryset


def show_post(request, post_id):
    post = get_object_or_404(Note, id=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.category_id,
    }

    return render(request, 'notes/post.html', context=context)


def edit_note(request, post_id):
    my_note = get_object_or_404(Note, pk=post_id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=my_note)
        if form.is_valid():
            form.save()
            return redirect('post', post_id=my_note.pk)
    else:
        form = UpdateForm(instance=my_note)
    return render(request, 'notes/editpage.html', {'form': form})


def delete_note(request, post_id):
    print(f'In delete_topic: {post_id}')
    topic = Note.objects.filter(id=post_id)
    topic.delete()
    return render(request, 'notes/del.html')


class SearchListView(ListView):
    model = Note
    template_name = 'notes/search.html'

    def get_queryset(self):
        if notes_title := self.request.GET.get('title', None):
            self.queryset = Note.objects.filter(title=notes_title)
        else:
            self.queryset = [Note.objects.count()]
        return self.queryset
