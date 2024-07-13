from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField(default=0)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField(default=0)
    publication_date = models.DateField()
    number_of_pages = models.SmallIntegerField(default=0)
    language = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)


class Member(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    membership_date = models.DateField()
    membership_type = models.CharField(max_length=100)


class Loan(models.Model):
    member_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()
    due_date = models.DateTimeField()


class Fine(models.Model):
    loan_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(null=True, blank=True)


class Reservation(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    status = models.CharField(max_length=100)
