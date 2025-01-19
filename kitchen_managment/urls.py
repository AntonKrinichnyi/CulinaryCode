from django.urls import path
from .views import (
    index,
    CookCreateView,
    CookDetailView,
    CookExperienceUpdateView,
    CookListView,
    CookDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index",),
    path("dishtype/", DishTypeListView.as_view(), name="dishtype-list",),
    path(
        "dishtype/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create",),
    path(
        "dishtype/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",),
    path(
        "dishtype/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete"),
    path("dish/", DishListView.as_view(), "dish-list",),
    path("dish/<int:pk>/", DishDetailView.as_view(), "dish-detail",),
    path("dish/create/", DishCreateView.as_view(), "dish-create",),
    path("dish/<int:pk>/update", DishUpdateView.as_view(), "dish-update",),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), "dish-delete",),
    path(
        "dish/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    path("cook/", CookListView.as_view(), "cook-list",),
    path("cook/<int:pk>/", CookDetailView.as_view(), "cook-detail"),
    path("cook/create/", CookCreateView.as_view(), "cook-create",),
    path(
        "cook/<int:pk>/update",
        CookExperienceUpdateView.as_view(),
        "cook-update",),
    path("cook/<int:pk>/delete", CookDeleteView.as_view(), "cook-delete"),
]