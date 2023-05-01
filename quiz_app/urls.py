from django.contrib import admin
from django.urls import path
from .views import quiz, home, score

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('quiz', quiz, name='quiz'),
    path('score/', score, name='score'),
]