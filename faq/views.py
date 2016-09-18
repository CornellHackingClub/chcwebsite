from django.contrib.auth.models import User
from django.shortcuts import render
from .models import FAQ
from django.db.models import Q

# Just using function based views for now because they're easy
def faq_home(request):
    user = request.user

    if request.method == 'POST' and request.user.is_authenticated:
        question = request.POST['query']
        FAQ.objects.create(title=question, user=str(user))

    queryset = FAQ.objects.all()

    error = None

    print user

    if str(user) != 'admin':
        queryset = queryset.filter(Q(user__exact=str(user)) | Q(user__exact='admin'))

    context = {
        "questions": queryset,
        "username": user,
        "error": error
    }
    response = render(request, "faq.html", context)
    response['X-XSS-Protection'] = 0
    return response
