from django.urls import path
from .views import  profile_bb_add, profile_bb_detail, plug

app_name = 'main'

urlpatterns = [

    
    path('add/', profile_bb_add ,name='add_ads'),
    path('advert/', profile_bb_detail ,name='advert'),
    path('<int:id>/', plug ,name='plug'),

]