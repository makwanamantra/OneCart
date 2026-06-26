from django.urls import path
from . import views as v
urlpatterns= [
    path('login/',v.login_a,name='login'),
    path('logout/',v.logout_a,name='logout'),
    path('signup/',v.signup,name='signup'),
]