from . import models
from django.template import loader
from django.http import HttpResponse


def index(request):
    videos_week = models.Video.objects.order_by('-publish_date')[:7]
    print(videos_week)
    template = loader.get_template('videoofday/index.html')
    print(template)
    context = {
        'videos': videos_week,
    }
    return HttpResponse(template.render(context, request))


def live(request):
    videos_week = models.Video.objects.order_by('-publish_date')[:7]
    print(videos_week)
    template = loader.get_template('videoofday/live.html')
    print(template)
    context = {
        'videos': videos_week,
    }
    return HttpResponse(template.render(context, request))


def store(request):
    videos_week = models.Video.objects.order_by('-publish_date')[:7]
    print(videos_week)
    template = loader.get_template('videoofday/store.html')
    print(template)
    context = {
        'videos': videos_week,
    }
    return HttpResponse(template.render(context, request))
