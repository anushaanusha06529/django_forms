from django import forms



class ContactForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=(['male','MALE'],['female','FEMALE']))
    gender=forms.ChoiceField(choices=(['male','MALE'],['female','FEMALE']),widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=(['python','python'],['django','django']))
    course=forms.MultipleChoiceField(choices=(['python','python'],['django','django']),widget=forms.CheckboxSelectMultiple)