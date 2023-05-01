from django.contrib import admin
from .models import DjangoQuizQuestion, PythonQuizQuestion, HtmlQuizQuestion, CssQuizQuestion, JavascriptQuizQuestion

# Register your models here.

class DjangoQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'option_1', 'option_2', 'option_3', 'option_4')

class PythonQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'option_1', 'option_2', 'option_3', 'option_4')

class HtmlQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'option_1', 'option_2', 'option_3', 'option_4')

class CssQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'option_1', 'option_2', 'option_3', 'option_4')

class JavascriptQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'option_1', 'option_2', 'option_3', 'option_4')

admin.site.register(DjangoQuizQuestion, DjangoQuizAdmin)
admin.site.register(PythonQuizQuestion, PythonQuizAdmin)
admin.site.register(HtmlQuizQuestion, HtmlQuizAdmin)
admin.site.register(CssQuizQuestion, CssQuizAdmin)
admin.site.register(JavascriptQuizQuestion, JavascriptQuizAdmin)
