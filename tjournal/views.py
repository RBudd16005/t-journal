from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Report
from .forms import ReportForm


def index(request, *args, **kwargs):
    return render(request, "index.html", {})


def report(request, *args, **kwargs):
    form = ReportForm()
    return render(request, "report.html", {'form': form})


def confirmation(request, *args, **kwargs):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            Report.objects.create(**form.cleaned_data)
            return render(request, "confirmation.html", {})
        else:
            return render(request, "failure.html", {'form': form})


def data(request, *args, **kwargs):
    reports = Report.objects.all()
    reports_json = serializers.serialize('json', reports)
    return HttpResponse(reports_json, content_type='application/json')


def review(request, *args, **kwargs):
    return render(request, "review.html", {})
