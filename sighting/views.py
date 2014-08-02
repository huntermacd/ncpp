from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user
from .models import Bird, Sighting
from .forms import SightingForm

# index of site maps to this view
# which will then call the 'bird_list.html' template
def bird_list(request):
	waterbirds_and_nearshore_birds = Bird.objects.filter(family="waterbirds_and_nearshore_birds")
	doves_woodpeckers_etc = Bird.objects.filter(family="doves_woodpeckers_etc")
	birds_of_prey = Bird.objects.filter(family="birds_of_prey")
	perching_birds = Bird.objects.filter(family="perching_birds")
	current_birder = get_user(request)
	sightings = None
	if not current_birder.is_anonymous():
		sightings = Sighting.objects.filter(birder=current_birder)
	ctx = {
		'waterbirds_and_nearshore_birds': waterbirds_and_nearshore_birds,
		'doves_woodpeckers_etc': doves_woodpeckers_etc,
		'birds_of_prey': birds_of_prey,
		'perching_birds': perching_birds,
		'sightings': sightings
	}
	return render(request, 'sighting/bird_list.html', ctx)

def bird_detail(request, bird_name):
	bird = get_object_or_404(Bird, slug=bird_name)
	current_birder = get_user(request)
	sighting = None
	ctx = {
		'bird': bird
	}
	if not current_birder.is_anonymous():
		sighting, created = Sighting.objects.get_or_create(birder=current_birder, bird=bird, defaults={'sighted': False})
		ctx['sighting'] = sighting
	if request.method == 'POST':
		form = SightingForm(request.POST, instance=sighting)
		if form.is_valid():
			form.save()
			return redirect('bird_list')
	else:
		form = SightingForm(instance=sighting)
	ctx['form'] = form
	return render(request, 'sighting/bird_detail.html', ctx)