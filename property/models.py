from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, null=True)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    new_building = models.BooleanField('Новостройка', null=True, blank=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='complaints')
    text = models.TextField('Текст жалобы')

class Owner(models.Model):
    flats = models.ManyToManyField(Flat, related_name='owners')
    
    def __str__(self):
        owner = self.flats.all().first()
        return f'{owner.owner}, {owner.owners_phonenumber} ({owner.owners_pure_phone}р.)'

    def owner(self):
        return self.flats.all().first().owner

    def owners_phonenumber(self):
        return self.flats.all().first().owners_phonenumber

    def owners_pure_phone(self):
        return self.flats.all().first().owners_pure_phone
