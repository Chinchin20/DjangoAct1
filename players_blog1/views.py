from django.shortcuts import render

def home(request):
    return render(request, 'players_blog1/home.html')

def player(request):
    return render(request, 'players_blog1/player.html')

def team(request):
    return render(request, 'players_blog1/team.html')
