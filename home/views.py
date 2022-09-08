from django.db.models import Q
from django.shortcuts import render
from .models import CarDetail, Cars, CarBrand
from django.views.generic import DetailView, ListView

# Create your views here.


def home_page(request):
    context = {}
    return render(request, "home.html", context)


class CarDetailListView(ListView):
    model = CarDetail
    template_name = "details/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["car_brands"] = CarBrand.objects.filter(~Q(brand_name="Any"))

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_dict = {}
        for field in ("search", "brand"):
            value = self.request.GET.get(field, None)
            if value:
                if field == "brand":
                    filter_dict[field] = CarBrand.objects.get(brand_name=value)
                else:
                    filter_dict[field] = value
        if filter_dict:
            queryset = queryset.filter(**filter_dict).all()
        return queryset


class CarDetailDetailView(DetailView):
    model = CarDetail
    template_name = "details/one-detail.html"


class CarListView(ListView):
    model = Cars
    template_name = "cars/car-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["car_brands"] = CarBrand.objects.filter(~Q(brand_name="Any"))
        context["year_range"] = range(1990, 2023)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_dict = {}
        for field in ("search", "brand", "year"):
            value = self.request.GET.get(field, None)
            if value:
                if field == "brand":
                    brand_value = CarBrand.objects.filter(
                        brand_name=value
                    ).first()
                    if brand_value:
                        filter_dict[field] = brand_value
                else:
                    filter_dict[field] = value
        if filter_dict:
            mod_queryset = queryset.filter(**filter_dict)
            if mod_queryset.exists():
                return mod_queryset
            else:
                return {}
        return queryset


class CarDetailView(DetailView):
    model = Cars
    template_name = "cars/car-detail.html"
