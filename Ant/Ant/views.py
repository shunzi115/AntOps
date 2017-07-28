from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return redirect('/navi/')

@csrf_exempt
def page_not_found(request):

    return render_to_response('not_found_page/404.html')