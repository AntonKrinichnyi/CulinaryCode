from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from kitchen_managment.forms import (CookCreationForm,
                                     CookExperienceUpdateForm,
                                     CookUsernameSearchForm,
                                     DishForm,
                                     DishNameSearchForm,
                                     DishTypeNameSearchForm)
from .models import Dish, DishType, Cook


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
    context_object_name = "dishtype_list"
    template_name = "kitchen_managment/dishtype_list.html"
    paginate_by = 10
    queryset = DishType.objects.all()
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "",)
        context["search_form"] = DishTypeNameSearchForm(
            initial={"name": name})
        return context

    def get_queryset(self):
        form = DishTypeNameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"])


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = DishNameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"])


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    
    def toggle_assign_to_dish(request, pk):
        cook = Cook.objects.get(id=request.user.id)
        if (Dish.objects.get(id=pk) in cook.dishes.all()):
            cook.dishes.remove(pk)
        else:
            cook.dishes.add(pk)
        return HttpResponseRedirect(reverse_lazy("kitchen_managment:dish-detail", args=[pk]))

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
    queryset = Cook.objects.all()
    
    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookUsernameSearchForm(
            initial={"username": username}
        )
        return context
    
    def get_queryset(self):
        form = CookUsernameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                username__icontains=form.cleaned_data["username"]
            ) 


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dishtype")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen_managment/cook_create.html"
    success_url = reverse_lazy("kitchen_managment:cook-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    template_name = "kitchen_managment/cook_update.html"
    success_url = reverse_lazy("kitchen_managment:cook-list")
    form_class = CookExperienceUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_managment:cook-list")


class ToggleAssignToDishView(LoginRequiredMixin, generic.View):
    @staticmethod
    def get(request, pk):
        cook = Cook.objects.get(id=request.user.id)
        if (Dish.objects.get(id=pk) in cook.dishes.all()):
            cook.dishes.remove(pk)
        else:
            cook.dishes.add(pk)
        return HttpResponseRedirect(
            reverse_lazy("kitchen_managment:dish-detail",
                                                 args=[pk]))
