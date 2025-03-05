from django.urls import path,include
from .views import SignupView,LoginView,LogoutView,ToDoAPIView



urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', ToDoAPIView.as_view(), name='todo-list-create'),   
    path('todos/<int:pk>/', ToDoAPIView.as_view(), name='todo-detail'),
]
