from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Track

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


