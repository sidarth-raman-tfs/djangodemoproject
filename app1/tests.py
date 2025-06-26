from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework import status

#tests if we can list the items
def test_list_itemones(api_client,db):
    resp = api_client.get(reverse('app1-list'))
    assert resp.status_code == status.HTTP_200_OK

#tests if we can create an item
def test_create_itemone(api_client,db):
    resp = api_client.post(reverse('app1-list'), {'name': 'Test', 'description': 'Desc'}, format='json')
    assert resp.status_code == status.HTTP_201_CREATED
