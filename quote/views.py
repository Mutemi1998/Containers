from django.shortcuts import render
from django.http import HttpResponse

from quote.models import Contact, ContactUs


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def refrigerated_containers(request):
    return render(request, "refrigerated-containers.html")

def storage_containers(request):
    return render(request, "storage-containers.html")

def shipping_containers(request):
    return render(request, "shipping_containers.html")

def high_cube_containers(request):
    return render(request, "high-cube-containers.html")

def tunnel_containers(request):
    return render(request, "tunnel-containers.html")

def side_access_containers(request):
    return render(request, "side-access-containers.html")

def containers_for_sale(request):
    return render(request, "containers-for-sale.html")

def deliveries(request):
    return render(request, "deliveries.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactUs = ContactUs(name=name,email=email,phone=phone,address=address,subject=subject,message=message)
        contactUs.save()
        return render(request, "contact.html", {"message": "Your contact has been submitted successfully!"})
    else:
        return render(request, "contact.html")

def quotation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        type = request.POST.get('type')
        condition = request.POST.get('condition')
        message = request.POST.get('message')

        # Create a Contact object with the retrieved data
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            address=address,
            type=type,
            condition=condition,
            message=message
        )

        # Save the Contact object to the database
        contact.save()

        return render(request, "quotation.html", {"message": "Your quotation has been submitted successfully!"})
    else:
        return render(request, "quotation.html")

def modification(request):
    return render(request, "modification.html")

def technical_container_support(request):
    return render(request, "24-7-technical-container-support.html")

def container_commissioning(request):
    return render(request, "container-commissioning.html")

def container_site_surveys(request):
    return render(request, "container-site-surveys.html")

def container_painting(request):
    return render(request, "container-painting.html")

def container_dimensions(request):
    return render(request, "container-dimensions.html")