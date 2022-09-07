from pipes import Template
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from .models import Ads
from .form import AdsForm 
# Create your views here.

@login_required
def profile(request):
    bbs = Ads.objects.filter(author=request.user.pk)
    context = {'bbs': bbs}
    return render(request, 'profile/main_profile.html', context)

@login_required
def profile_bb_detail(request):
    bb = Ads.objects.filter(author=request.user.pk)

    context = {'bb': bb}
    return render(request, 'profile/user_ads.html', context)



@login_required
def profile_bb_add(request):
    if request.method == 'POST':
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            bb = form.save()

            return render(request, 'profile/main_profile.html', {'bb':bb})
    else:
        form = AdsForm(initial={'author': request.user.pk})
        
    context = {'form': form, }
    return render(request, 'main/ads.html', context)



# class Plug(TemplateView):
#     template_name = 'plug/plug.html'
    
#     def get(self, request, *args, **kwarg):
#         self.plug = get_object_or_404(Ads, id = id )
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['plug_one'] = self.plug
        
#         return context

def plug(request, id):
    plug = get_object_or_404(Ads, id = id )
    is_user = request.user

    context = {'plug_one': plug, 'is_user': is_user }
    return render(request, 'plug/plug.html', context)