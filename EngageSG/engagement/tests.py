from django.test import TestCase
from .models import SurveyResponse
from .load_data import load_data_from_csv

class LoadDataTests(TestCase):

    def setUp(self):
        SurveyResponse.objects.all().delete()

    def test_loading_data_from_csv(self):
        print("\nTesting functionality: Load data from CSV")
        load_data_from_csv()
        expected_entry_count = 3076

        actual_count = SurveyResponse.objects.count()
        
        print(f"Expected entry count: {expected_entry_count}, Actual entry count: {actual_count}")
        self.assertEqual(actual_count, expected_entry_count, "The number of loaded entries does not match the expected count.\n")
        print("Success: Survey response data loaded from CSV successfully.")