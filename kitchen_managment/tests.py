from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Dish, DishType

 
#Tests for admin panel
class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin.test",
            password="testpassword3232"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="testcook",
            password="passwordtest2323",
            license_number="TST12345",
        )

    def test_cook_has_years_of_experience(self) -> None:
        url = reverse("admin:kitchen_managment_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_has_years_of_expirience(self) -> None:
        url = reverse("admin:kitchen_managment_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)


#Test models
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


#Test views
URL = reverse("kitchen_managment:dish-list")
class PublickCarFormatTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self) -> None:
        res = self.client.get(URL)
        self.assertNotEqual(res.status_code, 200)
