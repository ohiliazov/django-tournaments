from datetime import datetime

from django.shortcuts import render

from tournaments.models import Tournament


def index(request):
    tournaments = Tournament.objects.all()
    now = datetime.now()
    return render(
        request,
        "tournaments/index.html",
        {"now": now.isoformat(), "tournaments": tournaments},
    )
