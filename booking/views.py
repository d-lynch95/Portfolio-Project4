from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'form.html')

def appointment(request):
    if request.method== "POST" :
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        
        return render(request, 'appointment.html', {
            'your_name': your_name,
 			'your_phone': your_phone,
 			'your_email': your_email,
 			'your_address': your_address,
 			'your_schedule': your_schedule,
 			'your_date': your_date,
 			'your_message': your_message
 			}) 
    
    else:
        return render(request, 'home.html', {})