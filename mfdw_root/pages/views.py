from django.shortcuts import render
from . models import Page
#from django.http import HttpResponse

# Create your views here.
#def index(request):
#    #return HttpResponse("<h1> Website Homepage </h1>")
#    return render(request, "pages/page.html")


def index(request, pagename):
    pagename = "/" + pagename # this is needed because Dj removes / from end of URLs, so need to add this to point to the root
    # load Page model
    pg = Page.objects.get(permalink=pagename)
    # topolate dictionary of items to pass to the template
    context = {
        "title" : pg.title,
        "content" : pg.bodytext,
        "last_updated" : pg.update_date,
        "page_list" : Page.objects.all(),
    }
    # assert False # enters the error page view
    return render(request, "pages/page.html", context)
