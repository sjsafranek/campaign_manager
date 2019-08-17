from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from . import models


@login_required
def index(request):
    print(request.user)
    return HttpResponse("Hello, world. You're at the campaign manager index.")
