from django.urls import path, reverse_lazy

from .views import IndexView, SignupView, LoginViewZ, ShowTaskView, DetailTaskView, UpdateTaskView

from django.contrib.auth.views import LogoutView

app_name = "todoweb"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('view/', ShowTaskView.as_view(), name="showTask"),
    path('detail/<int:pk>/', DetailTaskView.as_view(), name="detail"),
    
    path('update/<int:pk>/', UpdateTaskView.as_view(), name="update"),
    # path('delete/<int:pk>/', Delete                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   TaskView.as_view(), name="delete"),
    
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginViewZ.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("todoweb:login")), name="logout"),
]
