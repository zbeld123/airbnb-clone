from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "in_finished",
    )

    list_filter = ("status",)

    pass
