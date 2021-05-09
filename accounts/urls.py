from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    # user login process path

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # view access pages

    path('', views.home, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('Students/', views.Students, name="Students"),

    # books section

    path('gallery/', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"),

    path('add/', views.addPhoto, name="add"),

    path('search/', views.usearch, name='usearch'),
    path('lsearch/', views.lsearch, name='lsearch'),

    #     student delete
    path('../delete/', views.StudentDelete, name='student_delete'),

    # student delete
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('ldbookk/', views.LDeleteView.as_view(), name='ldbookk'),
    path('lebook/', views.LEditView.as_view(), name='lebook'),

]
