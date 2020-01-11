from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def homepage(request):
    jobs = Job.objects
    home_dict = {"jobs":jobs}
    return render(request, 'jobs/home.html', home_dict)
def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})