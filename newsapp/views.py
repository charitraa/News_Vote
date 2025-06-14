from django.shortcuts import render, get_object_or_404
from .models import NewsCard

def news_card(request, card_id):
    card = get_object_or_404(NewsCard, id=card_id)
    return render(request, "news_card.html", {"card": card})

def vote(request, card_id, action):
    card = get_object_or_404(NewsCard, id=card_id)
    if action == "upvote":
        card.votes += 1
    elif action == "downvote":
        card.votes -= 1
    card.save()
    return render(request, "partials/vote_count.html", {"votes": card.votes})
