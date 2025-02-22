from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


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
