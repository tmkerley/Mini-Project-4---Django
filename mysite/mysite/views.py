from django.http import HttpResponse
from django.views import generic
import datetime

class HomeView(generic.DetailView):
    template_name = 'polls/index.html'

    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)