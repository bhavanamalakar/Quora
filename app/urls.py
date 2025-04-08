from django.urls import path
from . import views  # Importing views from the current app

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page displaying all questions
    path('register/', views.register_view, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('post/', views.post_question, name='post_question'),  # Form to post a new question
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),  # Question detail with answers
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),  # Like or unlike an answer
    path('my-activity/', views.my_activity, name='my_activity'),  # View user's questions, answers, and likes
]
