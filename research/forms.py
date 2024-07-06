from django import forms
from .models import PrivacyRisk, RegulatoryFramework, Evaluation

class PrivacyRiskForm(forms.ModelForm):
    class Meta:
        model = PrivacyRisk
        fields = ['name', 'description', 'risk_level']

class RegulatoryFrameworkForm(forms.ModelForm):
    class Meta:
        model = RegulatoryFramework
        fields = ['name', 'description', 'effective_date', 'compliance_requirements']

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['framework', 'privacy_risk', 'evaluation_date', 'evaluator_name', 'comments']
