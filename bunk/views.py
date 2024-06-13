from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Bunk, User
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bunk/index.html'
    context_object_name = 'latest_bunk_list'
    def get_queryset(self):
        return Bunk.objects.all()

class DetailView(generic.DetailView):
    model = User
    template_name = 'bunk/user.html'
    # context_object_name = 'user_bunks'
    # def get_queryset(self):
    #     return User.bunk_set.all()

def addbunkmate(request, from_user_id, to_user_id):
    from_user = get_object_or_404(User, pk=from_user_id)
    try:
        # to_user = User.objects.get(pk=request.POST['to_user_id'])
        to_user = User.objects.get(pk=to_user_id)
    except (KeyError, User.DoesNotExist):
        # Redisplay the form.
        return render(request, 'bunk/user.html', {
            'error_message': "Invalid/nonexistent username.",
            'user': from_user
        })
    else:
        new_bunk = Bunk.create(from_user, to_user, timezone.now())
        new_bunk.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bunk:user', args=(from_user_id, )))

