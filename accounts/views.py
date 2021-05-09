import itertools
from operator import not_

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from another python file import class
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView

from . import models
from .forms import CreateUserForm, BookForm, Student
from .models import Category, Photo


# Create your views here.
# def user_is_superuser(user):
#     return user.is_superuser

# Users login, reister, logout and Students Detail

# register part

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('register')

        context = {'form': form}
        return render(request, 'register.html', context)


# login part

def loginPage(request):
    if request.user.is_superuser:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if not request.user.is_superuser:
                login(request, user)
                return redirect('register')
            else:
                return redirect('register')
        else:
            messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


# logout part

def logoutUser(request):
    logout(request)
    return redirect('login')


# Students Details

def Students(request):
    Students = Student.objects.all()
    return render(request, 'manage_Student.html', {'Students': Students})


# @user_passes_test(user_is_superuser)
def home(request):
    return render(request, 'Index.html', {'home': home})


@login_required(login_url='login')
def dashboard(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def gallery(request):
    category = request.GET.get('category')
    if category is not None:
        photos = Photo.objects.filter(category__name=category)
    else:
        photos = Photo.objects.all()

    context = {'photos': photos}
    return render(request, 'gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    Categories = Category.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo, 'Categories': Categories})


@login_required(login_url='login')
def addPhoto(request):
    Catagories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': Catagories}
    return render(request, 'add.html', context)


# next


def searchpage(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Category.objects.all().filter(author=search)
        return render(request, 'searchpage.html', {'post': post})


# book search

@login_required
def usearch(request):
    query = request.GET['query']
    print(type(query))

    # data = query.split()
    data = query
    print(len(data))
    if (len(data) == 0):
        return redirect('dashboard')
    else:
        a = data

        # Searching for It
        qs5 = models.Category.objects.filter(name__iexact=a).distinct()
        qs6 = models.Category.objects.filter(name__exact=a).distinct()

        qs7 = models.Category.objects.all().filter(name__contains=a)
        qs8 = models.Category.objects.select_related().filter(id__contains=a).distinct()
        qs9 = models.Category.objects.filter(name__startswith=a).distinct()
        qs10 = models.Category.objects.filter(name__endswith=a).distinct()
        qs11 = models.Category.objects.filter(name__istartswith=a).distinct()
        qs12 = models.Category.objects.all().filter(name__icontains=a)
        qs13 = models.Category.objects.filter(name__iendswith=a).distinct()

        files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

        res = []
        for i in files:
            if i not in res:
                res.append(i)

        # word variable will be shown in html when user click on search button
        word = "Searched Result :"
        print("Result")

        print(res)
        files = res

        page = request.GET.get('page', 1)
        paginator = Paginator(files, 10)
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)

        if files:
            return render(request, 'result.html', {'files': files, 'word': word})
        return render(request, 'result.html', {'files': files, 'word': word})


@login_required
def lsearch(request):
    query = request.GET['query']
    print(type(query))

    # data = query.split()
    data = query
    print(len(data))
    if (len(data) == 0):
        return redirect('dashboard')
    else:
        a = data

        # Searching for It
        qs5 = models.Category.objects.filter(name__iexact=a).distinct()
        qs6 = models.Category.objects.filter(name__exact=a).distinct()

        qs7 = models.Category.objects.all().filter(name__contains=a)
        qs8 = models.Category.objects.select_related().filter(id__contains=a).distinct()
        qs9 = models.Category.objects.filter(name__startswith=a).distinct()
        qs10 = models.Category.objects.filter(name__endswith=a).distinct()
        qs11 = models.Category.objects.filter(name__istartswith=a).distinct()
        qs12 = models.Category.objects.all().filter(name__icontains=a)
        qs13 = models.Category.objects.filter(name__iendswith=a).distinct()

        files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

        res = []
        for i in files:
            if i not in res:
                res.append(i)

        # word variable will be shown in html when user click on search button
        word = "Searched Result :"
        print("Result")

        print(res)
        files = res

        page = request.GET.get('page', 1)
        paginator = Paginator(files, 10)
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)

        if files:
            return render(request, 'result.html', {'files': files, 'word': word})
        return render(request, 'result.html', {'files': files, 'word': word})


@login_required
def StudentDelete(request, pk):
    obj = get_object_or_404(Students, pk=pk)
    obj.delete()
    return redirect('index')


# def search(request):
#     if request.method == 'POST':
#         name = request.POST.getlist('search')
#         try:
#             status = Category.objects.filter(bookname__icontains=name)
#             # Add_prod class contains a column called 'bookname'
#         except Category.DoesNotExist:
#             status = None
#         return render(request, "searchpage.html", {"books": status})
#     else:
#         return render(request, "searchpage.html", {})


# book delete
class LDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('lmbook')
    success_message = 'Data was deleted successfully'


class LManageBook(LoginRequiredMixin, ListView):
    model = User
    template_name = 'manage_Student.html'
    context_object_name = 'books'
    paginate_by = 6

    def get_queryset(self):
        return User.objects.order_by('-id')




# class LEditView(LoginRequiredMixin, UpdateView):
#     model = User
#     form_class = BookForm
#     template_name = 'edit_book.html'
#     success_url = reverse_lazy('lmbook')
#     success_message = 'Data was updated successfully'


class LEditView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = BookForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('lmbook')
    success_message = 'Data was updated successfully'
