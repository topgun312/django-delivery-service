import random
from typing import Any, List, Dict

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from geopy import distance


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def unique_number() -> int:
  """
  Функция для создания уникального номера машины.
  """
  numb = str(random.randint(1000, 9999)) + random.choice(LETTERS)
  return numb


def location_random() -> Any:
  """
  Функция для создания случайной локации при создании машины.
  """
  all_loc = Location.objects.all()
  random_loc_id = random.randint(1, all_loc[len(all_loc) -1].id)
  return all_loc[random_loc_id]


class Cargo(models.Model):
  """
  Модель для грузов.
  """
  pick_up = models.ForeignKey("Location", on_delete=models.PROTECT, null=False, blank=False, related_name='pick_up_loc')
  delivery = models.ForeignKey("Location", on_delete=models.PROTECT, null=False, blank=False, related_name='delivery_loc')
  weight = models.IntegerField(null=False, blank=False, validators=[
    MinValueValidator(1, message='Минимальный вес груза 1 кг.'),
    MaxValueValidator(1000, message='Максимальный вес груза 1000 кг.')], verbose_name='Вес груза')
  description = models.CharField(max_length=255, null=False, blank=False, verbose_name='Описание')

  objects = models.Manager()

  def __str__(self):
    return f'Груз {self.pk}'

  class Meta:
    verbose_name = 'Груз'
    verbose_name_plural = 'Грузы'

  @property
  def get_count_cars(self) -> int:
    """
    Метод для получения количества ближайших машин до груза ( =< 450 миль).
    """
    cargo_coords = self.pick_up.lat, self.pick_up.lng
    car_count = 0
    cars = Car.objects.all()
    for car in cars:
      car_coords = car.current_location.lat, car.current_location.lng
      distance_of_cargo = distance.distance(cargo_coords, car_coords).miles
      if distance_of_cargo <= 450:
        car_count += 1
    return car_count

  @property
  def get_cars_info(self) -> List[Dict[str, float]]:
    """
    Метод для получения списка номеров всех машин с расстоянием до выбранного груза.
    """
    cargo_coords = self.pick_up.lat, self.pick_up.lng
    cars_info = []
    cars = Car.objects.all()
    for car in cars:
      car_info = {}
      car_coords = car.current_location.lat, car.current_location.lng
      distance_of_cargo = distance.distance(cargo_coords, car_coords).miles
      car_info['number'] = car.number
      car_info['distance'] = round(distance_of_cargo, 1)
      cars_info.append(car_info)
    return cars_info

  def get_absolute_url(self):
    return reverse('cargo_detail', kwargs={'pk': self.pk})


class Car(models.Model):
  """
  Модель для машин.
  """
  number = models.CharField(max_length=5, null=False, blank=False, unique=True, default=unique_number)
  current_location = models.ForeignKey('Location', on_delete=models.PROTECT, default=location_random, null=False, blank=False, related_name='cur_loc')
  load_capacity = models.IntegerField(null=False, blank=False, validators=[
    MinValueValidator(1, message='Минимальный вес груза 1 кг.'),
    MaxValueValidator(1000, message='Максимальный вес груза 1000 кг.')])

  objects = models.Manager()

  def __str__(self):
    return str(self.number)

  class Meta:
    verbose_name = 'Машина'
    verbose_name_plural = 'Машины'

  def get_absolute_url(self):
    return reverse('car_detail', kwargs={'pk': self.pk})


class Location(models.Model):
  """
  Модель для локаций.
  """
  city = models.CharField(max_length=255, null=False, blank=False)
  state_name = models.CharField(max_length=255, null=False, blank=False)
  zip_num = models.IntegerField(unique=True, null=False, blank=False, db_index=True)
  lat = models.FloatField(null=False, blank=False)
  lng = models.FloatField(null=False, blank=False)

  objects = models.Manager()

  def __str__(self):
    return str(self.zip_num)

  class Meta:
    verbose_name = 'Локация'
    verbose_name_plural = 'Локации'