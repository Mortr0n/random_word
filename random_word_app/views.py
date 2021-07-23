from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1

    context = {
        'newWord': get_random_string(length=14),
    }
    return render(request, 'index.html', context)


def make_word(request):
    # request.session['newWord'] = {'word': request.POST[get_random_string(length=14)]}
    # print(get_random_string(length=14))
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')
