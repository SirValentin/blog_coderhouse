from django.urls import path
from users.views import login_request, register, logout_request, view_profile

urlpatterns = [
    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_request, name="logout"),
    path('profile/', view_profile, name="profile"),
]