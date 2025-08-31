from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache response for 15 minutes
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({
        "data": properties
    })
