from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def add_question(request):
    return HttpResponse("Add new review")


def show_id(request, question_id):
    return HttpResponse("You choose id: " + str(question_id))


def show_by_year(request, year):
    return HttpResponse("Valid year id: " + str(year))
