from django.shortcuts import render
from django.db.models import Q
from .models import *


def index(request):
    # properties = Property.objects.values_list(
    #     "id",
    #     "name",
    #     "listing_type",
    #     "price",
    #     "property_image",
    #     "parking",
    #     "bathroom",
    #     "bedroom",
    # )[:3]
    properties = Property.objects.all()[:3]
    context = {'properties':properties}
    return render(request, "spacenest/index.html", context)


def property(request):
    properties = Property.objects.values_list(
        "id",
        "name",
        "listing_type",
        "price",
        "property_image",
        "parking",
        "bathroom",
        "bedroom",
    )

    if request.method == "GET":
        location = request.GET.get("location")
        min_price = request.GET.get("min-price")
        max_price = request.GET.get("max-price")
        listing_type = request.GET.get("listing-type")
        province = request.GET.get("province")

        filters = Q()

        if location:
            filters &= Q(location__icontains=location)
        if min_price:
            filters &= Q(price__gte=min_price)
        if max_price:
            filters &= Q(price__lte=max_price)
        if listing_type and listing_type != "all":
            filters &= Q(listing_type=listing_type)
        if province and province != "all":
            filters &= Q(province=province)

        properties = Property.objects.filter(filters)

    context = {"properties": properties}
    return render(request, "spacenest/properties.html", context)
