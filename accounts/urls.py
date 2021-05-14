from django.conf.urls import url
from django.urls import path

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
    path('Students/', views.Students, name="Students"),
    path('contact/', views.Contact, name="contact"),

    # books section

    path('gallery/', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"),
    path('add/', views.addPhoto, name="add"),

    # student delete
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('ldbookk/<int:pk>/', views.LDeleteView.as_view(), name='ldbookk'),
    path('lebook/<int:pk>/', views.LEditView.as_view(), name='lebook'),
    path('deleteAccount/<int:pk>/', views.LDeletemeView.as_view(), name='accountpages'),

    #     view book
    path('lmstudent/<int:pk>/', views.LManageStudent.as_view(), name='lmstudent'),
    path('ldstudent/<int:pk>/', views.LDeleteViews.as_view(), name='ldstudent'),
    path('lestudent/<int:pk>/', views.LEditViews.as_view(), name='lestudent'),

    # request
    path('request/', views.Requeest, name='lrequests'),
    path('request/', views.Request, name='lrequest'),
    path('rhome/<int:pk>/', views.RDeleteViews.as_view(), name='dashboards'),

]
