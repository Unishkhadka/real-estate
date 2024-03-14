from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    # properties = Property.objects.values_list(
    #     "id",
    #     "name",
    #     "listing_type",
    #     "price",
    #     "property_image",
    #     "parking",
    #     "bathroom",
    #     "bedroom"
    # )[:3]
    properties = Property.objects.all()[:3]
    context = {"properties": properties}
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


@login_required(login_url="login")
def pricing(request):
    return render(request, "spacenest/pricing.html")


def agents(request):
    agent_list = User.objects.filter(is_agent=True)
    context = {"agents": agent_list}
    return render(request, "spacenest/agents.html", context)


@login_required(login_url="login")
def add_property(request):
    if request.method == "POST":
        name = request.POST["name"]
        location = request.POST["location"]
        province = request.POST["province"]
        listing_type = request.POST["listing_type"]
        price = request.POST["price"]
        image = request.FILES["image"]
        description = request.POST["description"]
        parking = request.POST["parking"]
        bathroom = request.POST["bathroom"]
        bedroom = request.POST["bedroom"]
        Property.objects.create(
            name=name,
            location=location,
            province=province,
            listing_type=listing_type,
            description=description,
            price=price,
            property_image=image,
            parking=parking,
            owner=request.user,
            bathroom=bathroom,
            bedroom=bedroom,
        )
        return redirect("property")
    return render(request, "spacenest/add_property.html")


def edit_profile(request):
    return render(request, "spacenest/edit_profile.html")


def favourites(request):
    return render(request, "spacenest/favourites.html")


def contact(request):
    return render(request, "spacenest/contact.html")
