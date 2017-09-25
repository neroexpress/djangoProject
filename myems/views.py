from django.shortcuts import render
from .rosterbots import Roster


def index(request):
    return render(request, 'myems/index.html',{})

def about(request):
    return render(request, 'myems/about.html',{})

def contact(request):
    return render(request,'myems/contact.html',{})

def table(request):
    return render(request, 'myems/table.html',
                  {'players': Roster.get_player_list(Roster()),
                   'score_sum':sum([sum(player.sl) for player in
                                    Roster.get_player_list(Roster())])})