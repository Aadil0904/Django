from django.shortcuts import render

# Create your views here.
def register_view(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'users/register.html')