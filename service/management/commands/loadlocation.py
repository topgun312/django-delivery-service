from django.core.management.base import BaseCommand
import pandas as pd
from service.models import Location


def copy_from_csv_to_db() -> None:
  """
  Функция для импорта данных из файла uszips.csv в базу данных.
  """
  df = pd.read_csv('uszips.csv', sep=',')
  row_iter = df.iterrows()
  data = [
    Location(
      zip_num=int(row['zip']),
      lat=float(row['lat']),
      lng=float(row['lng']),
      city=row['city'],
      state_name=row['state_name']
    )
    for index, row in row_iter
  ]

  Location.objects.bulk_create(objs=data)


class Command(BaseCommand):
  help = 'Выгрузка данных из файла uszips.csv в БД'

  def handle(self, *args, **options):
    try:
      if Location.objects.all().count() == 0:
        copy_from_csv_to_db()
        print(f'Загрузка файла uszips.csv в БД успешно завершена!')
      else:
        print('Данные в таблице Location уже существуют!')
    except Exception as ex:
      print(f'Ошибка загрузки данных: {ex}')
