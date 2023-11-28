from quote.models import Owner

def owner_processors(request):
    owner = Owner.objects.first()
    return {'owner': owner}