from django.db import models
from django.utils.translation import gettext_lazy as _
import shortuuid
from django.utils import timezone
from users.models import CustomUser as User
from django_ckeditor_5.fields import CKEditor5Field


class Property(models.Model):
    PROVINCE_CHOICES = [
        ("koshi", _("Koshi Province")),
        ("madhesh", _("Madhesh Province")),
        ("bagmati", _("Bagmati Province")),
        ("gandaki", _("Gandaki Province")),
        ("lumbini", _("Lumbini Province")),
        ("karnali", _("Karnali Province")),
        ("sudurpashchim", _("Sudurpashchim Province")),
    ]

    LISTING_TYPE_CHOICES = [
        ("sell", _("Sell")),
        ("rent", _("Rent")),
    ]

    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    name = models.CharField(_("Property Name"), max_length=200)
    location = models.CharField(_("Location"), max_length=200)
    province = models.CharField(_("Province"), max_length=200, choices=PROVINCE_CHOICES)
    listing_type = models.CharField(
        _("Listing Type"), max_length=20, choices=LISTING_TYPE_CHOICES
    )
    description = CKEditor5Field("Text", config_name="extends")
    price = models.PositiveIntegerField(_("Price"))
    property_image = models.ImageField(
        _("Property Image"),
        upload_to="property/",
        default="property/default.jpg",
        null=True,
        blank=True,
    )
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


class Membership(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        


class UserMembership(models.Model):
    INITIATED = "initiated"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    PAYMENT_STATUS_CHOICES = [
        (INITIATED, "Initiated"),
        (PROCESSING, "Processing"),
        (COMPLETED, "Completed"),
        (FAILED, "Failed"),
    ]
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS_CHOICES, default=INITIATED
    )

    def __str__(self):
        return f"{self.user.full_name}'s {self.membership.name} Membership"

    class Meta:
        unique_together = ("user", "membership")

class Payment(models.Model):
    id = models.CharField(
        _("ID"), primary_key=True, max_length=22, default=shortuuid.uuid, editable=False
    )
    pidx = models.CharField(max_length=50, unique=True)
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    txn_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.user_membership.user.full_name}"