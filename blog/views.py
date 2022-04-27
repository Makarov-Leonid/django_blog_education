from django.shortcuts import render

# Create your views here.


def posts_list(request):
    n = 'oleg'
    return render(request, 'blog/index.html', context={'name': n})
