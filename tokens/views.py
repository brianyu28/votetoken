import uuid

from django.shortcuts import render

from .models import Election, Voter, Token

def index(request):
    return render(request, "tokens/index.html")

def claim(request):

    # Validate email and one-time password
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    try:
        voter = Voter.objects.get(email=email, one_time_password=password)
    except Voter.DoesNotExist:
        return render(request, "tokens/index.html", {
            "error": "Invalid email address and/or one-time-password."
        })

    # Ensure each voter can only claim a single token
    if voter.claimed:
        return render(request, "tokens/index.html", {
            "error": "Token has already been claimed."
        })

    # Generate a new token for the user
    token = Token(token=uuid.uuid4().hex)
    token.save()

    # Record that voter has claimed a token
    voter.election.tokens.add(token)
    voter.claimed = True
    voter.save()

    # Display token
    return render(request, "tokens/claimed.html", {
        "token": token
    })
