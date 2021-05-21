from django.conf.urls import url
from django.urls import path, include

from crm1 import urls
from . import views


urlpatterns = [

    # user login process path

    path('register/', views.registerPage, name="register"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # view access pages

    path('dashboard/', views.home, name="home"),
    path('account/', views.accountp, name="accountpage"),
    path('', views.dashboard, name="dashboard"),
    path('contact/', views.Contact, name="contact"),
    path('about/', views.about, name="about"),


    # books section

    path('gallery/', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"),
    path('request/<str:pk>/', views.viewrequestform, name="request"),
    path('add/', views.addPhoto, name="add"),

    # student delete
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('ldbookk/<int:pk>/', views.LDeleteView.as_view(), name='ldbookk'),
    path('lebook/<int:pk>/', views.LEditView.as_view(), name='lebook'),
    path('deleteAccount/', views.LDeletemeView.as_view(), name='accountpages'),

    #     view book
    path('lmstudent/<int:pk>/', views.LManageStudent.as_view(), name='lmstudent'),
    path('ldstudent/<int:pk>/', views.LDeleteViews.as_view(), name='ldstudent'),
    path('lestudent/<int:pk>/', views.LEditViews.as_view(), name='lestudent'),



    path('home/', views.viewrequest, name='home'),
    path('account/', views.viewrequestmy, name='account'),
    path('request/', views.createpost, name='lrequest'),
    path('home/', views.LManagerequest.as_view(), name='lmrequest'),
    path('ldrequest/<int:pk>/', views.LDeleterequest.as_view(), name='ldrequestb'),


    path('success/', views.success, name="success"),

    path('novel/', views.novels, name='novel')


]
