from django.shortcuts import render
from notice.models import Notice
from course.models import Course


def index(request):
    all_notice = Notice.objects.all()
    all_course = Course.objects.all()
    return render(request, "index.html", {"notices": all_notice, "courses": all_course})
