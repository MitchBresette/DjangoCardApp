from django.shortcuts import render, redirect, get_object_or_404
from .forms import CardForm
from .models import Card
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# add card functon to add a new card to card list
@login_required
def add_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect("card_list")
    else:
        form = CardForm()
    return render(request, "cards/add_card.html", {"form": form})


# edit card function to update existing card on card list
@login_required
def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, user = request.user)

    if request.method == "POST":
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect("card_list")
    else:
        form = CardForm(instance=card)

    return render(request, "cards/edit_card.html", {"form": form, "card": card})


# delete function to remove one card from card list
@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, user=request.user)

    if request.method == "POST":
        card.delete()
        return redirect("card_list")

    return render(request, "cards/delete_card.html", {"card": card})


# displays the users card list
@login_required
def card_list(request):
    query = request.GET.get("q", "")
    cards = Card.objects.filter(user=request.user)
    # card objects is created via django: this error can be ignored.

    # filter for cards
    if query:
        cards = cards.filter(
            Q(name__icontains=query) |
            Q(type__icontains=query) |
            Q(rarity__icontains=query)
        )


    return render(request, "cards/card_list.html", {"cards": cards, "query": query})


# register new user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("card_list")

    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


