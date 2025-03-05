from django.urls import path,include
from .views import SignupView,LoginView,LogoutView,ToDoAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/', ToDoAPIView.as_view(), name='todo-list-create'),   
    path('todos/<int:pk>/', ToDoAPIView.as_view(), name='todo-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login k liye
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
