from django.shortcuts import render
from news.models import News, SliderHomepage, ServiceHomepage

def homepage(request):
    news = News.objects.all()
    sliders = SliderHomepage.objects.all()
    service = ServiceHomepage.objects.all()
    context = {
        'news':news,
        'sliders':sliders,
        'service':service,
    }
    return render(request, 'index.html', context)

def mkassaPage(request):
    return render(request, 'mkassa.html')
