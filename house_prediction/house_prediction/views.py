from django.shortcuts import render
from . import ml_predict


def home(request):
    return render(request,'index.html')



def result(request):
    if request.method == 'POST':
        # Get all input fields from POST
        area = float(request.POST.get("area", 0))
        bedrooms = int(request.POST.get("bedrooms", 0))
        bathrooms = int(request.POST.get("bathrooms", 0))
        stories = int(request.POST.get("stories", 0))
        mainroad = int(request.POST.get("mainroad", 0))
        guestroom = int(request.POST.get("guestroom", 0))
        basement = int(request.POST.get("basement", 0))
        hotwaterheating = int(request.POST.get("hotwaterheating", 0))
        airconditioning = int(request.POST.get("airconditioning", 0))
        parking = int(request.POST.get("parking", 0))
        prefarea = int(request.POST.get("prefarea", 0))
        furnishingstatus = int(request.POST.get("furnishingstatus", 0))

        # Call your ML runner
        prediction = ml_predict.prediction_model(
            area, bedrooms, bathrooms, stories, mainroad, guestroom,
            basement, hotwaterheating, airconditioning, parking,
            prefarea, furnishingstatus
        )

        return render(request, 'result.html', {'prediction': prediction})

    # If someone accesses /result via GET, redirect to home
    return render(request, 'index.html')
