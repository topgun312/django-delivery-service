from service.models import Car
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
  help = 'Добавляем по умолчанию 20 машин в БД'

  def handle(self, *args, **options):
    try:
      if Car.objects.all().count() == 0:
        for _ in range(1, 21):
          Car.objects.create(load_capacity=random.randint(1, 1000))
        print(f'Машины в БД добавлены!')
      else:
        print('Машины в таблице Car уже существуют!')
    except Exception as ex:
      print(f'Ошибка создания данных {ex}')