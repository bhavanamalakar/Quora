from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth.decorators import login_required


def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login after successful registration
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  # Authenticate user
        if user:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home on successful login
    return render(request, 'login.html')


def logout_view(request):
    logout(request)  # Log out the current user
    return redirect('login')


@login_required  # Requires user to be logged in to access
def home_view(request):
    questions = Question.objects.all().order_by('-created_at')  # Show newest questions first
    return render(request, 'home.html', {'questions': questions})


@login_required
def post_question(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user  # Associate question with logged-in user
            question.save()
            return redirect('home')
    return render(request, 'post_question.html', {'form': form})


@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # Fetch question or show 404
    answers = question.answers.all()  # Get all answers related to the question
    answer_form = AnswerForm()
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user = request.user  # Associate answer with user
            answer.question = question  # Link answer to the question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': answer_form})


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)  # Remove like if already liked
    else:
        answer.likes.add(request.user)  # Add like if not already liked
    return redirect('question_detail', question_id=answer.question.id)


@login_required
def my_activity(request):
    user = request.user
    questions_posted = Question.objects.filter(user=user).order_by('-created_at')  # User's posted questions
    answers_posted = Answer.objects.filter(user=user).order_by('-created_at')  # User's posted answers
    answers_liked = Answer.objects.filter(likes=user).order_by('-created_at')  # Answers liked by user

    return render(request, 'my_activity.html', {
        'questions_posted': questions_posted,
        'answers_posted': answers_posted,
        'answers_liked': answers_liked,
    })
