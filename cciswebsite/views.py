import markdown
from django.shortcuts import render
from notice.models import Notice
from course.models import Course


def index(request):
    all_notice = Notice.objects.all()
    all_course = Course.objects.all()
    return render(request, "index.html", {"notices": all_notice, "courses": all_course})


def blog_content(request,id):
    a_course = Course.objects.get(id=id)
    a_course.content = markdown.markdown(a_course.content.replace("\r\n", ' \n'), extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return render(request, 'coursecontent.html', {"courses": a_course})


def notice_content(request,id):
    a_notice = Notice.objects.get(id=id)
    return render(request, 'noticecontent.html', {"notice":a_notice})