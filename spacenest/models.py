from django.db import models
from django.utils.translation import gettext_lazy as _
import shortuuid
from users.models import CustomUser as User


from django.db import models
from django.utils.translation import gettext_lazy as _
import shortuuid
from users.models import CustomUser as User

class Property(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    name = models.CharField(_("Property Name"), max_length=200)
    location = models.CharField(_("Location"), max_length=200)
    province = models.CharField(_("Province"), max_length=200)
    listing_type = models.CharField(_("Listing Type"), max_length=20)
    description = models.TextField(_("Description"))
    price = models.PositiveIntegerField(_("Price"))
    property_image = models.ImageField(_("Property Image"),
        upload_to="property/",
        default="property/default.jpg",
        null=True,
        blank=True,)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    parking = models.PositiveIntegerField(_("Parking Space"), default=0)
    bathroom = models.PositiveIntegerField(_("Bathroom"), default=0)
    bedroom = models.PositiveIntegerField(_("Bedroom"), default=0)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self) -> str:
        return self.name

class Favourite(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
