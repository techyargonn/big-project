from django.shortcuts import render
from .models import PostDoodle
from .forms import PostDoodleForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def home(request):
    return render(request, 'illustrations/index.html')

def artists(request):
    return render(request, 'illustrations/artists.html')

def contact(request):
    return render(request, 'illustrations/contact.html')

def illustrations(request):
    post_doodle = PostDoodle.objects.all()
    return render(request, 'illustrations/illustrations.html', {'post_doodle': post_doodle})

def create_doodle(request):
    if request.method == "POST":
        form = PostDoodleForm(request.POST, request.FILES)
        if form.is_valid():
            post_doodle = form.save(commit=False)
            post_doodle.user = request.user
            post_doodle.save()
            return redirect('illustrations')
    else:
        form = PostDoodleForm()
    return render(request, 'illustrations/create_doodle.html', {'form': form})


def delete_doodle(request, doodle_id):
    post_doodle = get_object_or_404(PostDoodle, pk=doodle_id, user = request.user)
    if request.method == "POST":
        post_doodle.delete()
        return redirect('illustrations')
    return render(request, 'illustrations/doodle_confirm_delete.html', {'post_doodle': post_doodle})


