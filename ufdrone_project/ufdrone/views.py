from django.shortcuts import render, redirect
from .forms import DroneSightingForm
from .models import DroneSighting


def home(request):
    
    total_sightings = DroneSighting.objects.count()
    states_covered = DroneSighting.objects.values('state').distinct().count()
    recent_sightings = DroneSighting.objects.filter(date_reported__gte='2024-12-01').count()

    return render(request, 'ufdrone/home.html', {
        'total_sightings': total_sightings,
        'states_covered': states_covered,
        'recent_sightings': recent_sightings,
    })

# View for submitting a new drone sighting
def submit_sighting(request):
    if request.method == 'POST':
        form = DroneSightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sighting_success')  # Redirect to success page after submission
    else:
        form = DroneSightingForm()
    return render(request, 'ufdrone/submit_sighting.html', {'form': form})

# View to display a success message after submission
def sighting_success(request):
    return render(request, 'ufdrone/sighting_success.html')

# View to list all submitted drone sightings
def list_sightings(request):
    sightings = DroneSighting.objects.all().order_by('-date_reported')  # Get all sightings, sorted by newest first
    return render(request, 'ufdrone/list_sightings.html', {'sightings': sightings})
