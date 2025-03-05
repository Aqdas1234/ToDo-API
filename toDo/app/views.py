from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import ToDo
from .serializers import ToDoSerializer,UserSerializer,LoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class SignupView(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)
    
class ToDoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = ToDoSerializer
    def get(self, request, pk=None):
        if pk:
            # Retrieve a single to-do item
            todo = get_object_or_404(ToDo, pk=pk, user=request.user)
            serializer = ToDoSerializer(todo)
        else:
            # List all to-do items for the authenticated user
            todos = ToDo.objects.filter(user=request.user)
            serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new to-do item
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing to-do item
        todo = get_object_or_404(ToDo, pk=pk, user=request.user)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a to-do item
        todo = get_object_or_404(ToDo, pk=pk, user=request.user)
        todo.delete()
        return Response({"message": "To-Do deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

