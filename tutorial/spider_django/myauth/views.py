from django.shortcuts import render_to_response
from django.template import RequestContext
from sina import callback


def index(request, template_name="index.html"):
    if 'code' in request.GET:
        callback(request)
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
