from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen_managment.models import Dish, DishType



class DishTypeModelTest(TestCase):
    def test_str_method(self) -> None:
        dishtype = DishType.objects.create(
            name="testdihtype",
        )
        self.assertEqual(str(dishtype), "testdihtype")


class DishModelTest(TestCase):
    def test_str_method(self) -> None:
        dishtype = DishType.objects.create(
            name="testdihtype",
        )
        dish = Dish.objects.create(
            name="testdish",
            dishtype=dishtype,
            price=10.00,
        )
        self.assertEqual(str(dish), "testdish 10.00")


class CookModelTest(TestCase):
    def test_str_method(self) -> None:
        user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword4545",
            first_name="testfirstname",
            last_name="testlastname",
            years_of_experience=2
        )
        self.assertEqual(str(user), "testuser(testfirstname testlastname)")
