from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View

# Create your views here.
class InfoView(TemplateView):
    template_name = 'carClimate/info.html'

class QuestionView(TemplateView):
    template_name = 'carClimate/questions.html'