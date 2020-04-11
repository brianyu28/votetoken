import uuid

from django.shortcuts import render

from .models import Election, Voter, Token

def index(request):
    return render(request, "tokens/index.html")

def claim(request):
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    try:
        voter = Voter.objects.get(email=email, one_time_password=password)
    except Voter.DoesNotExist:
        return render(request, "tokens/index.html", {
            "error": "Invalid email address and/or one-time-password."
        })

    if voter.claimed:
        return render(request, "tokens/index.html", {
            "error": "Token has already been claimed."
        })

    token = Token(token=uuid.uuid4().hex)
    token.save()

    voter.election.tokens.add(token)
    voter.claimed = True
    voter.save()

    return render(request, "tokens/claimed.html", {
        "token": token
    })
