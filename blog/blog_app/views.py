from django.shortcuts import render
from .models import FormModel
from django.contrib.auth.decorators import login_required


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)

@login_required
def userIndex(request):
    form_list = FormModel.objects.filter(user=request.user)
    context = {'form_list': form_list}
    return render(request, 'blog_app/index.html', context)