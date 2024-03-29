import uuid
from django.db import models
from django.utils import timezone

from Account.models import DuberUser, DuberDriver
from Duber import settings
from Duber.settings import RideStatus, VehicleType


# Create your models here.
# model for rides
def half_hour_from_now():
    return timezone.now() + timezone.timedelta(minutes=30)


class Ride(models.Model):
    ride_id = models.UUIDField(max_length=10, default=uuid.uuid4, editable=False, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username', blank=False,
                              null=False, related_name='owner')
    driver = models.ForeignKey(DuberDriver, on_delete=models.CASCADE, to_field='duber_user', blank=True,
                               null=True, related_name='driver')
    sharer = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='sharer')

    dst_addr = models.CharField(max_length=100)
    owner_desired_arrival_time = models.DateTimeField(blank=False, null=False, default=half_hour_from_now())

    num_passengers_owner_party = models.PositiveIntegerField()
    num_passengers_sharer_party = models.PositiveIntegerField(default=0)
    is_shareable = models.BooleanField(default=False)
    owner_desired_vehicle_type = models.IntegerField(choices=VehicleType, blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)

    status = models.IntegerField(choices=RideStatus, default=RideStatus.OPEN)
    time_created = models.DateTimeField(auto_now_add=True)
    time_uptate = models.DateTimeField(auto_now=True)
    time_complete = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'ride'
        verbose_name_plural = 'rides'

    def __str__(self):
        return "{}-owner:{}-driver:{}-dst:{}".format(self.ride_id, self.owner, self.driver, self.dst_addr)


class SharerRide(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, to_field='ride_id', blank=False, null=False)
    sharer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username', blank=False,
                               null=False)
    num_passengers_sharer_party = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'sharer ride info'
        verbose_name_plural = 'sharer rides'

    def __str__(self):
        return "{}-{}-{}".format(self.ride.ride_id, self.sharer_id, self.num_passengers_sharer_party)
