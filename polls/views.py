from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


# Create your views here.

# the 'name' value as called by then {%url%} template tag
def index(request):
    # return HttpResponse("Hello world, You are at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # return HttpResponse("You are looking at question: %s." % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are looking at the votes of question %s" % question_id)
