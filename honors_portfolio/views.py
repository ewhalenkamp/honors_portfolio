from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

def home(request):
    return render(request, 'honors_portfolio/home.html')

def eol(request, course_id):
    templatename = 'eol-'+str(course_id)
    return render(request,'honors_portfolio/'+templatename+'.html')

def hc(request):
    return render(request,'honors_portfolio/hc.html')

def pr(request):
    return render(request,'honors_portfolio/pr.html')

def lg(request):
    return render(request,'honors_portfolio/lg.html')