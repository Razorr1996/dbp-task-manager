from http import HTTPStatus
from typing import Type, Container

from django.db import models
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase

from main.models import Tag, Task, User


class TestAdmin(APITestCase):
    client: APIClient
    admin: User

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.admin = User.objects.create_superuser(
            "test_login", email=None, password=None
        )
        cls.client = APIClient()
        cls.client.force_login(cls.admin)

    @classmethod
    def assert_form(
        cls,
        model: Type[models.Model],
        key: int,
        check_actions: Container = (),
        follow: bool = True,  # For CSRF-tokens
    ) -> None:
        app_label = model._meta.app_label
        model_name = model._meta.model_name

        actions = {"changelist": [], "add": [], "change": (key,)}

        if check_actions:
            actions = {key: val for key, val in actions.items() if key in check_actions}

        for action, args in actions.items():
            url = reverse(f"admin:{app_label}_{model_name}_{action}", args=args)
            response = cls.client.get(url, follow=follow)
            assert response.status_code == HTTPStatus.OK, response.content

    def test_user(self):
        self.assert_form(User, self.admin.id)

    def test_tag(self):
        tag = Tag.objects.create()
        self.assert_form(Tag, tag.id)

    def test_task(self):
        task = Task.objects.create()
        self.assert_form(Task, task.id)
