from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    # Page from the theme
    return render(request, 'dashboard_index.html')
