from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelform_factory, forms, modelformset_factory, inlineformset_factory
from .models import Usecase, Scenario
from .forms import UsecaseForm, ScenarioForm, StepForm, ScenarioInlineFormSet


# Create your views here.
def home(request):
    context = {}
    list = something
    context = {"usecases":list}
    return render(request,template_name='requirements/usecase-list',context=context)

def manage_Scenarios(request, usecase_id):
    usecase = Usecase.objects.get(pk=usecase_id)
    if request.method == "POST":
        formset = ScenarioInlineFormSet(request.POST, request.FILES, instance=usecase)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return redirect('scenario-create', usecase.pk)
    else:
        formset = ScenarioInlineFormSet(instance=usecase)
    return render(request, 'requirements/scenarios.html', {'formset': formset})


def create_usecase(request):
    context = {}
    form = UsecaseForm()
    scenario_formset = ScenarioInlineFormSet()
    # steps_formset =

    if request.method == 'POST':
        form = UsecaseForm(request.POST)
        scenario_formset = ScenarioInlineFormSet(request.POST, instance=form.instance)
        if form.is_valid() and scenario_formset.is_valid():
            f = form.save()
            instances = scenario_formset.save(commit=False)
            for instance in instances:
                instance.usecase = f
                instance.save()
            new_form = UsecaseForm()
            context = {"usecase_form": form,}
            messages.success(request, f'Use Case Saved!')
            return redirect('usecase-create')


    context = {
    'usecase_form':  form,
    "scenario_formset": scenario_formset,
    }
    return render(request,'requirements/usecase.html',context)


class UsecaseListView():
    pass
