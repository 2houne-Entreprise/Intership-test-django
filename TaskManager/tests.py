from django.test import TestCase
from TaskManager.forms import TaskForm


class TaskFormValidationTests(TestCase):
    def test_empty_title_is_invalid(self):
        form = TaskForm(data={
            "title": "",
            "status": "pending",
            "deadline": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertEqual(
            form.errors["title"][0],
            "Le titre de la tâche est obligatoire.",
        )