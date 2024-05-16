from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)


class Schedule(models.Model):
    """
    Represents the daily work hours for an employee
    """
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=128)
    contact_mobile = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=128)
    duration = models.SmallIntegerField(help_text="Represents the duration in minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time_expected = models.DateTimeField()
    end_time = models.DateTimeField()
    price_expected = models.DecimalField(max_digits=10, decimal_places=2)
    price_actual = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    price_final = models.DecimalField(max_digits=10, decimal_places=2)
    canceled = models.BooleanField()
    cancellation_reason = models.TextField()


class ServiceProvided(models.Model):
    """
    The service_provided table is a list of all the services the client received during their appointment.
    This information is used to calculate the overall price and to keep a history of services provided to the customer.
    """
    id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ServiceBooked(models.Model):
    """
    The service_booked table stores a list of the services each client requested,
    plus the service price at that time.
    This information could be used to avoid asking the client what they want (again) when they arrive at the salon.
    """
    id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
