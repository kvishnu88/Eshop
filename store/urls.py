from django.urls import path
from store.views import Login, Signup
from store import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view())
]
