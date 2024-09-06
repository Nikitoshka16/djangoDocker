from django.shortcuts import render

# Create your views here.
def index(request):
    songs = [
        {'author': 'Coldplay', 'title': 'Let It Be', 'duration': '3:55'},
        {'author': 'Coldplay', 'title': 'Let It Be', 'duration': '5:28'},
        {'author': 'Beyoncé', 'title': 'Stronger', 'duration': '4:07'},
        {'author': 'Beyoncé', 'title': 'Stronger', 'duration': '3:47'},
        {'author': 'Eminem', 'title': 'Bohemian Rhapsody', 'duration': '3:45'},
        {'author': 'Coldplay', 'title': 'Fix You', 'duration': '4:07'},
        {'author': 'Beyoncé', 'title': 'Let It Be', 'duration': '4:07'},
        {'author': 'The Beatles', 'title': 'Believer', 'duration': '3:47'},
        {'author': 'Coldplay', 'title': 'Halo', 'duration': '5:30'},
        {'author': 'The Beatles', 'title': 'Believer', 'duration': '5:24'}
    ]
    return render(request, 'index.html', {'songs': songs})