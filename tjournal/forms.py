from django import forms
from .models import Report
import datetime


CLOTHING_CHOICES = [
    ('Casual', 'Casual'),
    ('Professional', 'Professional')
]


class ReportForm(forms.Form):
    date = forms.DateField(
        label="Date: ",
        widget=forms.DateInput(attrs={'value': datetime.date.today()})
    )
    breakfast = forms.BooleanField(label="Did you eat breakfast? ", required=False)
    healthy = forms.BooleanField(label="Was it considered healthy? ", required=False)
    shower = forms.BooleanField(label="Did you shower? ", required=False)
    exercise = forms.BooleanField(label="Did you exercise? ", required=False)
    sleep = forms.IntegerField(label="How many hours did you sleep? ")
    clothes = forms.CharField(
        label="What clothes did you wear when trading? ",
        widget=forms.Select(choices=CLOTHING_CHOICES)
    )
    start = forms.TimeField(
        label="When did you begin trading? ",
        widget=forms.TimeInput(attrs={'value': datetime.time(9, 0, 0)})
    )
    rules = forms.BooleanField(label="Did you follow your trading rules? ", required=False)
    money = forms.DecimalField(
        label="How much money did you earn/lose? ",
        decimal_places=2,
        max_digits=1000,
        widget=forms.NumberInput(attrs={'placeholder': '0.00'})
    )
