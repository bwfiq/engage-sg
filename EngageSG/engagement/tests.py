from django.test import TestCase
from .models import SurveyResponse
from .load_data import load_data_from_csv
from django.urls import reverse
from rest_framework import status

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
    
class SocialInvolvementStatisticsTests(TestCase):
    def setUp(self):
        SurveyResponse.objects.all().delete()
        load_data_from_csv()

    def test_social_involvement_statistics(self):
        print("\nTesting functionality: Social Involvement Statistics at endpoint: /api/social-involvement/")
        url = reverse('social-involvement-statistics')
        response = self.client.get(url)
        
        expected_age_groups = ['16-19 years old', '20-24 years old', '25-34 years old', '35-44 years old', 
                               '45-54 years old', '55-64 years old', '65-75 years old']
        for age_group in expected_age_groups:
            self.assertIn(age_group, response.data, f"{age_group} not found in response data.")
            print(f"Checked for age group: {age_group} - Found: {age_group in response.data}")
        
        print("Success: All expected age groups were found in the response data.")
        
class VolunteerDonationHabitsTests(TestCase):
    def setUp(self):
        SurveyResponse.objects.all().delete()
        load_data_from_csv()

    def test_volunteer_habits(self):
        print("\nTesting functionality: Volunteer Habits at endpoint: /api/volunteer-habits/")
        url = reverse('volunteer-habits')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list), "Response data should be a list")
        
        contains_female = any(entry['Gender_Gender'] == 'Female' for entry in response.data)
        self.assertTrue(contains_female, "'Female' not found in the response data")
        
        print("Success: Validated volunteer habits response.")