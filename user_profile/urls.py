from django.urls import path
from .views import Basic_v, Logining, Profile_v, PassChange, RegisterUserView, ChangeUserInfoView, logoutuser


app_name = 'user_profile'

urlpatterns = [

    path('', Basic_v.as_view(),name='main'),
    path('logout/', logoutuser ,name='logout'),
    path('login/', Logining.as_view(),name='login'),

    
    path('profile/', Profile_v.as_view(),name='profile'),
    path('ads/', Profile_v.as_view(),name='ads'),
    path('editprofile/', ChangeUserInfoView.as_view(),name='edit'),
    path('change_password/', PassChange.as_view(),name='change_password'),
    path('register/', RegisterUserView.as_view(),name='register'),


]