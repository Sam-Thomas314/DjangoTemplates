from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.
def popular_course_list(request):
    context = {}
    if request.method == "GET":
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        #using the object model mange to read all course list
        # order by most popular and grab the top ten and add to course_list

        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)
def enroll(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, pk=course_id)
        #Try to read the cour object
        #if not found raise the 404 exception
        course.total_enrollment +=1
        course.save()
        return HttpResponseRedirect(reverse(viewname = 'onlinecourse:popular_course_list'))

