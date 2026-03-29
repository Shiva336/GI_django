import io
from django.test import TestCase
from users.services import process_csv
from users.models import User


class ProcessCSVTest(TestCase):

    def create_csv_file(self, content: str):
        return io.BytesIO(content.encode("utf-8"))

    def test_valid_csv(self):
        csv_content = """
            name,email,age
            John,john@gmail.com,25
            Jane,jane@gmail.com,30
        """
        file = self.create_csv_file(csv_content)
        file.name = "test.csv"

        result = process_csv(file)

        self.assertEqual(result["success_count"], 2)
        self.assertEqual(result["failure_count"], 0)
        self.assertEqual(User.objects.count(), 2)

    def test_invalid_rows(self):
        csv_content = """
            name,email,age
            ,invalid-email,200
        """
        file = self.create_csv_file(csv_content)
        file.name = "test.csv"

        result = process_csv(file)

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        self.assertEqual(User.objects.count(), 0)

    def test_duplicate_email(self):
        User.objects.create(name="Existing", email="test@gmail.com", age=25)

        csv_content = """
            name,email,age
            New,test@gmail.com,30
        """
        file = self.create_csv_file(csv_content)
        file.name = "test.csv"

        result = process_csv(file)

        self.assertEqual(result["success_count"], 0)
        self.assertEqual(result["failure_count"], 1)
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_file_type(self):
        file = self.create_csv_file("data")
        file.name = "test.txt"

        with self.assertRaises(ValueError):
            process_csv(file)