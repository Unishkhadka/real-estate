from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("properties/", property_list, name="properties"),
    path("property/<str:pk>/", property, name="property"),
    path("pricing/", pricing, name="pricing"),
    path("agents/", agents, name="agents"),
    path("agent/<str:pk>", agent, name="agent"),
    path("contact/", contact, name="contact"),
    path("payment-success/", payment_success, name="payment_success"),
    path("add-property/", add_property, name="add-property"),
    path("edit-profile/", edit_profile, name="edit-profile"),
    path("favourites/", favourites, name="favourites"),
]
