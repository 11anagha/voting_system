from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages

@login_required
def home(request):  
    elections = models.Election.objects.all()

    context = {
        "elections": elections
    }
    return render(request, "election/home.html", context)



@login_required
def candidates(request):
    user = request.user
    active_election = models.Election.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now()).first()

    if not active_election:
        messages.info(request, "Election is not active at this moment")
        return redirect("election_home")

    elif models.Vote.objects.filter(voter=user).exists():
        messages.info(request, "You already casted vote for this election")
        return redirect("election_home")
    else:
        candidates = models.Candidate.objects.all()

        context = {
            "candidates": candidates,
        }

    return render(request, "election/candidate.html", context)


@login_required
def vote(request, pk):
    candidate = models.Candidate.objects.get(id=pk)

    if request.method == "POST":
        voter = request.user
        candidate = models.Candidate.objects.get(id=pk)

        models.Vote.objects.create(voter=voter, election=candidate.election, candidate=candidate)
        messages.success(request, f"You voted for {candidate}")
        return redirect("election_home")

    context = {
        "candidate": candidate
    }
    
    return render(request, "election/vote.html", context)



