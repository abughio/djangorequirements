from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelform_factory
from requirements.models import Usecase

# Create your views here.
def create_usecase(request):
    if request.method == 'POST':
        form = request.POST.get("usecaseform")
        if form.form_valid():
            form.save()
            messages.success(request, f'Your comment is posted!')
            return redirect('post-comments')
    else:
            context = {
            'usecaseform':  modelform_factory(Usecase, fields = ("description","trigger","preConditions","postConditions")),
            }
    return render(request,'requirements/usecase.html',context)
