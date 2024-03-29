from django import forms
from service.models import Cargo, Car


class CargoForm(forms.ModelForm):
  """
  Форма для создания груза.
  """
  pick_up_zip = forms.IntegerField(required=True, label='Почтовый индекс отправителя')
  delivery_zip = forms.IntegerField(required=True, label='Почтовый индекс получателя')

  class Meta:
    model = Cargo
    fields = ['weight', 'description', 'pick_up_zip', 'delivery_zip']
    # labels = {
    #   'weight': 'Вес груза',
    #   'description': 'Описание'
    # }

class CarForm(forms.ModelForm):
  """
  Форма для создания и редактирования машины.
  """
  current_location_zip = forms.IntegerField(required=True, label='Текущая локация')

  class Meta:
    model = Car
    fields = ['number', 'load_capacity', 'current_location_zip']
    labels = {
      'load_capacity': 'Грузоподъемность',
      'current_location_zip': 'Индекс текущей локации',
      'number': 'Номер машины'
    }


