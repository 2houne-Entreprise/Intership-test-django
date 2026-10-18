from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from projects.models import Project




class ProjectAuthenticationTests(TestCase):
    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse("projets:list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('projets:list')}",
        )




User = get_user_model()


class ProjectCreationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )
        self.client.login(
            username="testuser",
            password="TestPassword123!",
        )

    def test_project_is_created_successfully(self):
        response = self.client.post(
            reverse("projets:create"),
            {
                "name": "Projet de test",
                "description": "Description du projet",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Project.objects.filter(
                name="Projet de test",
                user=self.user,
            ).exists()
        )