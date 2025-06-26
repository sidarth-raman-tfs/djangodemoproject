from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework import status
# Create your tests here.
def test_list_movies(api_client,db):
    resp = api_client.get(reverse('app2-list'))
    assert resp.status_code==status.HTTP_200_OK


def test_create_movie(api_client,db):
    resp = api_client.post(reverse('app2-list'),{'title':'A movie', 'description':'test description'},format = 'json')
    assert resp.status_code == status.HTTP_201_CREATED

