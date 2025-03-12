from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def contact(request):
    ECFO=ContactForm()
    d={'ECFO':ECFO}
    if request.method=='POST':
        FDO=ContactForm(request.POST)
        if FDO.is_valid():
            return HttpResponse(str(FDO.cleaned_data))
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_Topic.html',d)