from django.urls import path
from . import views 

app_name = 'carsapp'

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("sign-up/", views.sign_up, name="signup")
]