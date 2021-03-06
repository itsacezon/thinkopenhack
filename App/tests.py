from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
# Create your tests here.


class BarangayModelTest(APITestCase):
	fixtures = ["barangay_test.json", "program_test.json"]
	def setUp(self):
		self.client = APIClient()

	def testListsBarangay(self):
		response = self.client.get('/api/barangay')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def testListProgram(self):
		response = self.client.get('/api/program')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		response = self.client.get('/api/program?barangay=1')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def testCreateProgram(self):
		data = {
			'title': 'Free Circumcision',
			'barangay_id': 1,
			'tags': ['fitness','zumba', 'exercise'],
			'sessions': "[{\"id\": 1,\"description\": \"Get fit by attending our free zumba.\",\"address\": \"Covered Court\",\"date\": \"2016-03-15T07:45:06.091Z\",\"fee\": \"free\"}]"
		}
		response = self.client.post('/api/program/', data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def testCreateAttendee(self):
		data = {
			'health_program_id': 1,
			'session_id': 1,
			'user_id': 1
		}
		response = self.client.post('/api/attendee/', data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response = self.client.get('/api/program/1')
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)