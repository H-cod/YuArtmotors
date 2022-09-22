from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import CarDetail, Cars, CarBrand
from django.db.models import Q


# Create your views here.


def home_page(request):
    context = {}
    return render(request, "home/home.html", context)


class CarDetailListView(ListView):
    paginate_by = 12
    model = CarDetail
    template_name = "details/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["car_brands"] = CarBrand.objects.filter(~Q(brand_name="Any"))

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_list = []
        for field in ("search", "brand"):
            value = self.request.GET.get(field, None)
            if value:
                if field == "brand":
                   filter_list.append(Q(brand=CarBrand.objects.get(
                       brand_name=value).pk))
                else:
                    filter_list.append(Q(detail_name__icontains=value))
        if filter_list:
            queryset = queryset.filter(*filter_list)
        return queryset


class CarDetailDetailView(DetailView):
    model = CarDetail
    template_name = "details/one-detail.html"


class CarListView(ListView):
    paginate_by = 12
    model = Cars
    template_name = "cars/cars.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["car_brands"] = CarBrand.objects.filter(~Q(brand_name="Any"))
        context["year_range"] = range(1990, 2023)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_list = []
        for field in ("search", "brand", "year_from", "year_to"):
            value = self.request.GET.get(field, None)
            if value:
                if field == "brand":
                    brand = CarBrand.objects.filter(
                            brand_name=value).first()
                    if brand:
                        filter_list.append(Q(brand=brand.pk))
                elif field == 'search':
                    filter_list.append(Q(
                        name__icontains=value
                    ))
                elif field == 'year_from':
                    filter_list.append(Q(
                        year__gte=value
                    ))
                elif field == 'year_to':
                    filter_list.append(Q(
                        year__lte=value))

        if filter_list:
            queryset = queryset.filter(*filter_list)
            if queryset.exists():
                return queryset
            else:
                return {}
        return queryset


class CarDetailView(DetailView):
    model = Cars
    template_name = "cars/car-detail.html"
