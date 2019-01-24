from .models import Usecase, Scenario, Step
from django.forms import ModelForm, modelformset_factory, inlineformset_factory

class UsecaseForm(ModelForm):
    class Meta:
        model = Usecase
        fields = ['name','description','trigger','preConditions','postConditions','trigger','businessRules','requirements','includes','extends']

class ScenarioForm(ModelForm):
    def is_valid(self,usecase):
        self.fields['usecase'] = usecase
        super(ScenarioForm, self).is_valid()

    class Meta:
        model = Scenario
        fields = ['entryPoint','type','desc']

class StepForm(ModelForm):
    
    def is_valid(self,scenario):
        self.fields['scenario'] = scenario
        super(StepForm, self).is_valid()

    class Meta:
        model = Step
        fields = ['stepNo','desc','uses','state']

SecnarioFormset = modelformset_factory(
    Scenario,
    fields = ('type', 'desc'),
    extra=1

)
ScenarioInlineFormSet = inlineformset_factory(
    Usecase,
    Scenario,
    fields=('type','desc'),
    extra=1
)