import email

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from another python file import class
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from .forms import CreateUserForm
from .models import Category, Photo, Post


# Create your views here.
def user_is_superuser(user):
    return user.is_superuser


# Users login, reister, logout and Students Detail

# register part

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

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
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


# logout part

def logoutUser(request):
    logout(request)
    return redirect('login')


@user_passes_test(user_is_superuser)
def home(request):
    return render(request, 'Index.html', {'home': home})


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
def viewrequestform(request, pk):
    photo = Photo.objects.get(id=pk)
    Categories = Category.objects.get(id=pk)
    return render(request, 'Request.html', {'photo': photo, 'Categories': Categories})


@user_passes_test(user_is_superuser)
def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

            catagory = Category.objects.all()
            catagory.save()

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
            photo.save()
        return redirect('gallery')
    Catagories = Category.objects.all()

    context = {'categories': Catagories, 'PPhoto': Photo}
    return render(request, 'add.html', context)


# next


# book delete
class LDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('lmbook')
    template_name = 'confirm_delete.html'
    success_message = 'Data was deleted successfully'


class LManageBook(LoginRequiredMixin, ListView):
    model = User
    form_class = CreateUserForm
    template_name = 'manage_Student.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('-id')


class LEditView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = CreateUserForm
    template_name = 'edit_book.html'
    success_url = reverse_lazy('lmbook')
    success_message = 'Data was updated successfully'


#     borrow book


# book delete
class LDeleteViews(SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'confirm_delete_Book.html'
    success_url = reverse_lazy('lmstudent')
    success_message = 'Data was deleted successfully'


class LManageStudent(LoginRequiredMixin, ListView):
    model = Category
    from_class = Category
    template_name = 'manage_Book.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.order_by('-id')


class LEditViews(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = Category
    template_name = 'edit_student.html'
    success_url = reverse_lazy('lmstudent')
    success_message = 'Data was updated successfully'


# def Requeest(request):
#     return render(request, "request.html")


def accountp(request):
    form = User.objects.all()
    booked = User.objects.all()
    return render(request, 'accountpage.html', {'form': form, 'booked': booked})


# delete my account


class LDeletemeView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('accountpage')
    template_name = 'Delete_myaccount.html'
    success_message = 'Data was deleted successfully'


def Contact(request):
    form = User.objects.all()
    booked = Post.objects.all()
    catagory = Category.objects.all()
    return render(request, 'Contact.html', {'form': form, 'booked': booked, 'catagory': catagory})


def about(request):
    return render(request, "About.html")


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'Request.html')

    else:
        return render(request, 'Request.html')


def viewrequest(request):
    post = Post.objects.all()
    return render(request, 'Index.html', {"post": post})


def viewrequestmy(request):
    post = Post.objects.all()
    return render(request, 'accountpage.html', {"post": post})


class LManagerequestmy(LoginRequiredMixin, ListView):
    model = Post
    from_class = Post
    template_name = 'accountpage.html'
    context_object_name = 'students'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.order_by('-id')


class LManagerequest(LoginRequiredMixin, ListView):
    model = Post
    from_class = Post()
    template_name = 'Index.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-id')


# book delete
class LDeleterequest(SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('lmrequest')
    template_name = 'deleted.html'
    success_message = 'Data was deleted successfully'


def success(request):
    return render(request, "success.html")


def novels(request):
    return render(request, "novel.html")