from django.shortcuts import render

def home(request):
    return render(request, 'players_blog2/home.html')

def player(request):
    return render(request, 'players_blog2/player.html')

def team(request):
    return render(request, 'players_blog2/team.html')