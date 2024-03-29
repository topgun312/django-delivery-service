from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from service.forms import CargoForm, CarForm
from service.models import Location, Cargo, Car


class CargoCreateView(CreateView):
  """
  Представление для создания груза.
  """
  template_name = 'service/create_cargo.html'
  form_class = CargoForm
  model = Cargo
  success_url = reverse_lazy('cargo_list')

  def form_valid(self, form):
    pick_up_zip = form.cleaned_data['pick_up_zip']
    delivery_zip = form.cleaned_data['delivery_zip']
    fields = form.save(commit=False)
    fields.pick_up = Location.objects.filter(zip_num=pick_up_zip).first()
    fields.delivery = Location.objects.filter(zip_num=delivery_zip).first()
    fields.save()
    return super().form_valid(form)


class CargoListView(ListView):
  """
  Представление для отображения списка грузов.
  """
  template_name = 'service/cargo_list.html'
  context_object_name = 'cargo'
  model = Cargo
  ordering = ['id']



class CargoDetailViews(DetailView):
  """
  Представление для просмотра детальной страницы груза.
  """
  template_name = 'service/cargo_detail.html'
  context_object_name = 'cargo'

  def get_object(self, queryset=None):
    return get_object_or_404(Cargo.objects, pk=self.kwargs[self.pk_url_kwarg])


class CargoUpdateView(UpdateView):
  """
  Представление для редактирования информации груза.
  """
  model = Cargo
  template_name = 'service/cargo_update.html'
  fields = ['weight', 'description']
  success_url = reverse_lazy('cargo_list')


class CargoDeleteView(DeleteView):
  """
  Представление для удаления груза.
  """
  model = Cargo
  template_name = 'service/cargo_delete.html'
  context_object_name = 'cargo'
  success_url = reverse_lazy('cargo_list')


class CarCreateView(CreateView):
  """
  Представление для создания машины.
  """
  template_name = 'service/create_car.html'
  form_class = CarForm
  model = Car
  success_url = reverse_lazy('car_list')

  def form_valid(self, form):
    current_location_zip = form.cleaned_data['current_location_zip']
    fields = form.save(commit=False)
    fields.current_location = Location.objects.filter(zip_num=current_location_zip).first()
    fields.save()
    return super().form_valid(form)

class CarDetailView(DetailView):
  """
  Представление для просмотра детальной страницы машины.
  """
  template_name = 'service/car_detail.html'
  context_object_name = 'car'

  def get_object(self, queryset=None):
    return get_object_or_404(Car.objects, pk=self.kwargs[self.pk_url_kwarg])


class CarListView(ListView):
  """
  Представление для просмотра списка машин.
  """
  template_name = 'service/car_list.html'
  context_object_name = 'cars'
  model = Car
  ordering = ['id']


class CarUpdateView(UpdateView):
  """
  Представление для редактирования информации о машине.
  """
  model = Car
  form_class = CarForm
  template_name = 'service/car_update.html'
  success_url = reverse_lazy('car_list')

  def form_valid(self, form):
    current_location_zip = form.cleaned_data['current_location_zip']
    fields = form.save(commit=False)
    fields.current_location = Location.objects.filter(zip_num=current_location_zip).first()
    fields.save()
    return super().form_valid(form)

class CarDeleteView(DeleteView):
  """
  Представление для удаления груза.
  """
  model = Car
  template_name = 'service/car_delete.html'
  context_object_name = 'car'
  success_url = reverse_lazy('car_list')




