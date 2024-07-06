from django.db import models

class PrivacyRisk(models.Model):
    RISK_LEVEL_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    risk_level = models.CharField(max_length=6, choices=RISK_LEVEL_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RegulatoryFramework(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    effective_date = models.DateField()
    compliance_requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    framework = models.ForeignKey(RegulatoryFramework, on_delete=models.CASCADE)
    privacy_risk = models.ForeignKey(PrivacyRisk, on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    evaluator_name = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return f"Evaluation of {self.framework} for {self.privacy_risk}"
