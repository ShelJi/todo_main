from django.urls import path, reverse_lazy

from .views import IndexView, SignupView, LoginViewZ

from django.contrib.auth.views import LogoutView

app_name = "todoweb"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginViewZ.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("todoweb:login")), name="logout"),
]
