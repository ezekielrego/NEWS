from django.shortcuts import render
from .models import latestnews
from .models import activitiess
from django.views import View
from .models import weeklynews
from django.shortcuts import render, get_object_or_404

def index(request):
    # Retrieve the data from the database
    allnews = latestnews.objects.all()
    # Reversin the order of all columns
    allnews = allnews[::-1]
    # Pass the reversed data list to the template
    context = {'allnews': allnews}
    return render(request, 'index.html', context)

def about(request,):
   allnews = latestnews.objects.all() 
   allnews = {
      "allnews":allnews,
   }
   return render(request, "about.html",allnews)
def contact(request,):
   allnews = latestnews.objects.all() 
   allnews = {
      "allnews":allnews,
   }
   return render(request, "contact.html",allnews)

class NewsDetail(View):
    def get(self,request,pk):
        obj = get_object_or_404(latestnews, id=pk)
        thedetails = obj.newsdetails
        newsline = get_object_or_404(latestnews, id=pk)
        newsline = newsline.newsline
        return render(request,"newsdetail.html",locals())

class activitydet(View):
    def get(self,request,pk):
        obj = get_object_or_404(latestnews, id=pk)
        actdetails = obj.newsdetails
        newsline = get_object_or_404(latestnews, id=pk)
        newsline = newsline.activitydetails
        return render(request,"activities.html",locals())


def activity(request,):
   allact = activitiess.objects.all() 
   allact = {
       "allact":allact,
   }

   return render(request, "index.html",allact) 

def weekly(request):
   wnews = latestnews.objects.all() 
   wnews = {
       "wnews":wnews,
   }

   return render(request, "index.html",wnews)        



def latest(request):
    return render(request, 'latest_news.html',{})
# Create your views here.
