from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import ApplicantForm

def show_form(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html', { 'form': form })
    else:
        form = ApplicantForm()

    return render(request, 'applicant.html', { 'form': form })

def process_form(request):
    if request.method == 'POST':
        form = ApplicantForm(request)
        if form.is_valid():
            return HttpResponseRedirect('/result')
    else:
        return HttpResponseRedirect('/result')

def get_javascript(request):
    return render(request, "javascript.html")
