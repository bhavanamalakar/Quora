from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link question to the user who posted it
    title = models.CharField(max_length=255)   # Question title
    body = models.TextField(blank=True)      # Optional detailed description
    created_at = models.DateTimeField(auto_now_add=True)   # Set timestamp when question is created

    def __str__(self):
        return self.title         # Display question title in admin or shell


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User who posted the answer
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')    # Link to the related question
    body = models.TextField()               # Answer content
    created_at = models.DateTimeField(auto_now_add=True)      # Timestamp of answer creation
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)    # Users who liked this answer

    def total_likes(self):
        return self.likes.count()      # Returns the number of likes on this answer

    def __str__(self):
        return f"Answer to {self.question.title}"   # Display format for admin or shell

