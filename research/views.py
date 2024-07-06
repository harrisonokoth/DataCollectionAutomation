from django.shortcuts import render, redirect
from .forms import PrivacyRiskForm, RegulatoryFrameworkForm, EvaluationForm

def home(request):
    return render(request, 'research/home.html')

def privacy_assessment(request):
    if request.method == 'POST':
        form = PrivacyRiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PrivacyRiskForm()
    return render(request, 'research/privacy_assessment.html', {'form': form})

def regulatory_evaluation(request):
    if request.method == 'POST':
        form = RegulatoryFrameworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegulatoryFrameworkForm()
    return render(request, 'research/regulatory_evaluation.html', {'form': form})

def evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EvaluationForm()
    return render(request, 'research/evaluation.html', {'form': form})
