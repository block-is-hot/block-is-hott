from django.test import TestCase

# Create your tests here.


class BasicAPIViewTests(TestCase):
    """Class for testing views."""

    def test_crime_correct(self):
        """Test."""
        response = self.client.get('/api/v1/crime/')
        self.assertEqual(response.status_code, 200)

    def test_entertainment_correct(self):
        """Test."""
        response = self.client.get('/api/v1/entertainment/')
        self.assertEqual(response.status_code, 200)

    def test_events_correct(self):
        """Test."""
        response = self.client.get('/api/v1/events/')
        self.assertEqual(response.status_code, 200)

    def test_art_correct(self):
        """Test."""
        response = self.client.get('/api/v1/art/')
        self.assertEqual(response.status_code, 200)

    def test_dirtiness_correct(self):
        """Test."""
        response = self.client.get('/api/v1/dirtiness/')
        self.assertEqual(response.status_code, 200)

    def test_login_correct(self):
        """Test."""
        response = self.client.get('/api/v1/login/')
        self.assertEqual(response.status_code, 405)

    def test_user_correct(self):
        """Test."""
        response = self.client.get('/api/v1/user/')
        self.assertEqual(response.status_code, 200)
