from django.contrib import admin
from django.urls import path
from .views import quiz, home, score
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('quiz', quiz, name='quiz'),
    path('score/', score, name='score'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
