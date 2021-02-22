from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!</h1>")
def meme(request):
    return HttpResponse("<img src='https://sun9-73.userapi.com/impg/xfCeRe1sNazEK_eo5Jl6dPA9LQBZH_Uh0-mEdQ/zV-Gv48r7mw.jpg?size=600x457&quality=96&proxy=1&sign=d00ac6affba31ae3975c11b6c982d758&type=album'>")