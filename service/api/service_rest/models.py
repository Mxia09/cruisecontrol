from django.db import models

class Technician(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    employee_id = models.PositiveIntegerField(unique=True)

class Appointment(models.Model):
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=150)
    vin = models.CharField(max_length=150, unique=True)
    customer = models.CharField(max_length=150)
    technician = models.ForeignKey(Technician, related_name="appointment", on_delete=models.CASCADE)
