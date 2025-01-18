from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from kitchen_managment.forms import CookCreationForm, CookExperienceUpdateForm, DishForm
from .models import Dish, DishType, Cook


@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dish = Dish.objects.count()
    num_dishtype = DishType.objects.count()
    
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    
    context = {
        "num_cooks": num_cooks,
        "num_dish": num_dish,
        "num_dishtype": num_dishtype,
        "num_visits": num_visits + 1,
    }
    
    return render(request, "kitchen_managment/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishtype-list"
    template_name = "kitchen_managment/dishtype_list.html"
    paginate_by = 10


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_managment:dishtype-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_managment:dishtype-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen_managment:dishtype-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.all().select_related("dishtype")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    
    def post(self, request, *args, **kwargs):
        dish = self.get_object()
        if request.user in dish.cooks.all():
            dish.cooks.remove(request.user)
        else:
            dish.cooks.add(request.user)
        return redirect(reverse(
            "kitchen_managment:dish-detail",
            kwargs={"pk": dish.pk}
        ))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.object
        user = self.request.user
        context["is_cook"] = dish.cooks.filter(id=user.id).exists()
        return context


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen_managment:dish-list")
    form_class = DishForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    success_url = reverse_lazy("kitchen_managment:dish-list")
    form_class = DishForm


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_managment:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 10


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dish__dishtype")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen_managment:cook-list")
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("kitchen_managment:cook-list")
    form_class = CookExperienceUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_managment:cook-list")
