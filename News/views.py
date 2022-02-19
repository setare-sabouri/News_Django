
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required



def Detail(request,slug):
        # return HttpResponse(slug)
    new = models.News.objects.get(slug=slug)
    args={'new':new}
    return render(request, 'NewsDetails.html',args)


def showList(request):
    newsObjs=models.News.objects.all().order_by('date')
    args={'newsObjs':newsObjs}
    return render(request ,'news.html',args)

@login_required(login_url = "/accounts/login")
def create_news(request):
    if request.method=='POST':
        form=forms.Create_News(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False) #data base no commit yet
            instance.author = request.user
            instance.save()
            return redirect('News:list')
    else:
        form=forms.Create_News()
    
    args={'form':form}
    return render(request ,'create_news.html',args)


def contact_us(request):
    return render(request ,'contact.html')