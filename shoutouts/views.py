from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from shoutouts.forms import ShoutoutForm
from shoutouts.models import Shoutout, Like
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


class Shoutouts(View):
    def get(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
        return render(request, "shoutouts.html", {"form": form, "shoutouts": shoutouts})

    def post(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            content = form.cleaned_data["content"]
            create_new_shoutout = Shoutout.objects.create(
                recipient=recipient,
                content=content,
                datetime=timezone.now(),
                user=request.user,
            )
            return redirect("shoutouts:home")
        elif not form.is_valid():
            return render(
                request, "shoutouts.html", {
                    "form": form, "shoutouts": shoutouts}
            )


class ViewStudentShoutouts(View):
    def get(self, request, recipient_id):
        recipient = User.objects.get(id=recipient_id)
        return render(
            request,
            "individual-shoutouts.html",
            {"recipient": recipient},
        )


class LikeUpVote(View):
    def post(self, request, shoutout_id):
        shoutout = get_object_or_404(Shoutout, pk=shoutout_id)
        shoutout.like_set.get_or_create(user=request.user)
        return redirect(request.POST.get("next", "shoutouts:home"))
