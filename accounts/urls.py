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
    # path('../delete/', views.StudentDelete, name='student_delete'),

    # student delete
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('ldbookk/<int:pk>/', views.LDeleteView.as_view(), name='ldbookk'),
    path('lebook/<int:pk>/', views.LEditView.as_view(), name='lebook'),

    #     borrow book
    #     path('book/<uuid:pk>/borrow/', views.borrow_book, name='borrow_book'),

    #     view book
    path('lmstudent/', views.LManageStudent.as_view(), name='lmstudent'),
    path('ldstudent/<int:pk>/', views.LDeleteViews.as_view(), name='ldstudent'),
    path('lestudent/<int:pk>/', views.LEditViews.as_view(), name='lestudent'),


    # request
    path('request/<int:pk>/', views.Resturant.as_view(), name='lrequest'),

]
