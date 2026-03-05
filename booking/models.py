from django.db import models

class Slot(models.Model):
    slot_time = models.CharField(max_length=50)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.slot_time