from django.shortcuts import render
from .models import DjangoQuizQuestion, PythonQuizQuestion, HtmlQuizQuestion, CssQuizQuestion, JavascriptQuizQuestion

def quiz(request):
    if request.method == 'POST':
        selected_option = request.POST.get('options') 
        request.session['selected_option'] = selected_option
        questions = None
        if selected_option == 'Django':
            questions = DjangoQuizQuestion.objects.all()
            total_questions = DjangoQuizQuestion.objects.count()
        elif selected_option == 'Python':
            questions = PythonQuizQuestion.objects.all()
            total_questions = PythonQuizQuestion.objects.count()
        elif selected_option == 'HTML':
            questions = HtmlQuizQuestion.objects.all()
            total_questions = HtmlQuizQuestion.objects.count()
        elif selected_option == 'CSS':
            questions = CssQuizQuestion.objects.all()
            total_questions = CssQuizQuestion.objects.count()
        elif selected_option == 'JavaScript':
            questions = JavascriptQuizQuestion.objects.all()
            total_questions = JavascriptQuizQuestion.objects.count()

        else:
            return render(request, 'home.html')

        # Save questions and total_questions in the session to use in score object
        request.session['questions'] = list(questions.values())
        request.session['total_questions'] = total_questions

        context = {'questions': questions, 
                   'selected_option': selected_option, 
                   'total_questions': total_questions}
        return render(request, 'quiz.html', context)
   


def home(request):
    return render(request, 'home.html')

def score(request):
    selected_option = request.session.get('selected_option')
    # Retrieve questions and total_questions from the session
    questions = request.session.get('questions')
    total_questions = request.session.get('total_questions')
    if request.method == 'POST':        
        score = 0
        results = []
        for question in questions:
            selected_answer = request.POST.get(f'question_{question["id"]}')
            if selected_answer == question['answer']:
                score += 1
                results.append((question, selected_answer, True))
            else:
                results.append((question, selected_answer, False))
        percentage = int((score/total_questions)*100)
        context = {'score': score, 
                   'results': results,
                   'questions': questions,
                   'total_questions': total_questions,
                   'percentage': percentage,
                   'selected_option': selected_option} 
        return render(request,'score.html', context)
    else:
        return render(request, 'home.html', {'questions': questions})