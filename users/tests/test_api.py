import io
from django.urls import reverse
from rest_framework.test import APITestCase

class UserCSVUploadAPITest(APITestCase):
    def create_csv_file(self, content: str):
        file = io.BytesIO(content.encode("utf-8"))
        file.name = "test.csv"
        return file

    def test_upload_valid_csv(self):
        url = reverse("user-csv-upload")

        csv_content = """
            name,email,age
            John,john@gmail.com,25
        """

        file = self.create_csv_file(csv_content)

        response = self.client.post(url, {"file": file}, format="multipart")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["success_count"], 1)

    def test_upload_no_file(self):
        url = reverse("user-csv-upload")

        response = self.client.post(url, {}, format="multipart")

        self.assertEqual(response.status_code, 400)