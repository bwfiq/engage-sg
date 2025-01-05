from django.test import TestCase
from .models import SurveyResponse
from .load_data import load_data_from_csv
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SurveyResponseTests(APITestCase):
    def setUp(self):
        SurveyResponse.objects.all().delete()
        self.Sample_SampleType_response = SurveyResponse.objects.create(
            UID_UniqueRespondentID="123456",
            Sample_SampleType="Resident (Citizen/PR)",
            Gender_Gender="Female",
            Age2_AgeGroups="25-34 years old",
            Dwelling_DwellingType="HDB 3 room",
            Industry_CurrentIndustry="Wholesale and Retail Trade",
            SocialInvolve_SportsGroupParticipation="Yes",
            SocialInvolve_ArtsCulturalGroupParticipation="No",
            SocialInvolve_CommunityGroupParticipation="Yes",
            SocialInvolve_WelfareSelfHelpGroupParticipation="No",
            SocialInvolve_ReligiousGroupParticipation="No",
            SocialInvolve_InterestHobbyGroupParticipation="Yes",
            SocialInvolve_DiscussionGroupParticipation="No",
            SocialInvolve_OtherParticipation="Yes",
            SocialInvolve_NoneParticipation="No",
            VolunteerDonate_VolunteeredTime="Yes",
            VolunteerDonate_DonatedMoney="No",
            VolunteerDonate_DonatedGoodsServices="Yes",
            VolunteerDonate_VolunteeredForCommunityProjects="Yes",
            VolunteerDonate_DonatedBlood="No",
            VolunteerDonate_ResolvedCommunityIssues="Yes",
            VolunteerDonate_HelpedNeighbors="No",
            VolunteerDonate_OtherActivities="Yes",
            VolunteerDonate_NoneActivities="No",
            VolunteerDonateFreq_FrequencyOfVolunteering="Weekly",
            VolunteerDonateMetd_MethodOfVolunteering="Online",
            SnetworkEthnicity_FriendsOfDifferentEthnicity="Yes",
            SnetworkNationality_FriendsOfDifferentNationality="No",
            SnetworkReligion_FriendsOfDifferentReligion="Yes",
            SnetworkIncome_FriendsOfDifferentIncome="No",
            SnetworkEducation_FriendsOfDifferentEducation="Yes",
            SnetworkSorientation_FriendsOfDifferentOrientation="No",
            CloseSGFriends_HaveCloseSGanFriends="Yes",
            SinteractMeal_SharedAMealWithFriend="No",
            SinteractInvitedFriend_InvitedFriendToCelebration="Yes",
            SinteractBeenInvited_BeenInvitedToCelebration="Yes",
            SinteractParticipated_ParticipatedInFestival="No",
            SupportImmedfam_SupportFromImmediateFamily="Yes",
            SupportExtfam_SupportFromExtendedFamily="No",
            SupportWorksch_SupportFromWorkplaceSchool="Yes",
            SupportFriends_SupportFromFriends="No",
            OsExp_StudiedOverseas="No",
            OsExp_WorkedOverseas="Yes",
            OsExp_ExtendedStayOverseas="No",
            OsExp_None="None",
            TimeOs_TimeSpentLivingOverseas="1 year",
            StudyOs_PlansToStudyOverseas="No",
            WorkOs_PlansToWorkOverseas="Yes",
            TravelOs_PlansToTravelOverseas="No",
            MigrateOs_PlansToMigrateOverseas="No",
            RetireOs_PlansToRetireOverseas="Yes",
            OutcomeConnection_StrengthOfConnectionToSG="Strong",
            OutcomeFuture_StrengthOfDesireToShapeSGFuture="Very strong",
            Pillarbeh1_ConsiderateBehaviorInPublic="Yes",
            Pillarbeh2_HelpingCloseFriendsFamily="No",
            Pillarbeh3_HelpingWiderNetwork="Yes",
            Pillarbeh4_RegularlyDonating="No",
            Pillarbeh5_RegularlyVolunteering="Yes",
            Pillarbeh6_OfferingHelpUnasked="No",
            Pillarbeh7_ConstructiveFeedbackOnPolicies="Yes",
            Pillarbeh8_LeadMobilityForCauses="No",
            Pillarbeh9_ParticipatingInCommunityInitiatives="Yes",
            Pillarbeh10_GettingAlongWithDiverseCultures="No",
            Pillarbeh11_AvoidingRaciallySensitiveConversations="Yes",
            Pillarbeh12_EasingRaciallySensitiveSituations="No",
            Pillarbeh13_IncludingDifferentCulturesInLife="Yes",
            Pillarbeh14_UnderstandingCulturalPractices="No",
            Pillarbeh15_HavingGoodFriendsFromDifferentCultures="Yes",
            Pillarvals1_ConsistentWithValuesOfSociety="Yes",
            Pillarvals2_GuidedByDesireToDoRight="Strongly agree",
            Pillarvals3_ActionsConsistentWithOthers="Agree",
            Pillarvals4_BeneficialActionsEvenIfCostly="Disagree",
            Pillarvals5_ResponsibilityToContributeToSociety="Agree",
            Pillarvals6_HelpingOthersIncreasesWellBeing="Yes",
            Pillarvals7_HelpingRiskingOffense="No",
            Pillarvals8_KnowingHowToHelpPeopleInNeed="Yes",
            Pillarvals9_HavingASayInDecisions="Strongly agree",
            Pillarvals12_ActiveRoleInSociety="Yes",
            Pillarvals13_PotentialForPositiveChange="No",
            Pillarvals14_BelongingAndAcceptanceInSG="Yes",
            Pillarvals21_CommonGroundWithDifferentCultures="Agree",
            Pillarvals22_InteractingWithDifferentCulturesBenefitsMe="Strongly agree",
            Pillarvals23_MeaningfulInteractionsWithCultures="Disagree",
            Pillarvals24_MeaningfulInteractionsWithNationalities="Agree",
            Pillarvals25_RespectingCulturalDifferences="Agree",
            Pillarvals26_NoRaciallyInsensitiveRemarks="No",
            Pillarvals29_ConfidenceInSingaporeFuture="Yes",
            Pillarvals30_SupportInGoodAndBadTimes="Strongly agree",
            Pillarvals31_OpportunitiesForPersonalAspirations="Agree",
            Pillarvals32_OpportunitiesToLiveByValues="Disagree",
            Pillarvals33_CommittedToLongTermInSingapore="Yes",
            OnlineNews_CheckNewsStayUpdated="Yes",
            OnlineSM_CheckSocialMedia="No",
            OnlineShop_ShoppingOnline="Yes",
            OnlineAreasInterest_InformationOnAreasOfInterest="No",
            OnlineGames_PlayingOnlineGames="Yes",
            OnlineUpdate_UpdateSelfInformation="No",
            OnlineSharemedia_ShareVideosPhotos="Yes",
            OnlineWatchmedia_WatchVideosMovies="No",
            MaritalStats_CurrentMaritalStatus="Married",
            Children_HaveChildren="Yes",
            AgeYoungestChild_AgeOfYoungestChild="6",
            HHGrandparents_LiveWithGrandparents="No",
            HHParents_LiveWithParents="Yes",
            HHSiblings_LiveWithSiblings="No",
            HHSpouse_LiveWithSpouse="Yes",
            HHChildren_LiveWithChildren="No",
            HHRelatives_LiveWithOtherRelatives="Yes",
            HHHelper_LiveWithDomesticHelper="No",
            HHMates_LiveWithFriendsHousemates="No",
            HHMates_LiveWithEmployerFamily="No",
            HHMates_LiveWithGrandChildren="No",
            HHMates_LiveWithOther="No",
            HHMates_NoneOfTheAboveStayAlone="No",
            HighestEd_HighestEducationLevel="Bachelor's",
            InstitutionDeg_ConferringInstitutionForDegree="Example University",
            Occupation_CurrentOccupation="Engineer",
            MHI_MonthlyHouseholdIncome="S4,001-S5,000",
            MPI_MonthlyPersonalIncome="S2,001-S3,000",
            Weight_Weight=70.5
    )
    
    def test_create_survey_response(self):
        print("\nTesting functionality: Create Survey Response at endpoint: /api/surveyresponses/")

        url = reverse('surveyresponse-list')
        data = {
            "UID_UniqueRespondentID": "123457",
            "Sample_SampleType": "Resident (Citizen/PR)",
            "Gender_Gender": "Male",
            "Age2_AgeGroups": "35-44 years old",
            "Dwelling_DwellingType": "Private Apartment",
            "Industry_CurrentIndustry": "Information Technology",
            "SocialInvolve_SportsGroupParticipation": "Yes",
            "SocialInvolve_ArtsCulturalGroupParticipation": "No",
            "SocialInvolve_CommunityGroupParticipation": "No",
            "SocialInvolve_WelfareSelfHelpGroupParticipation": "Yes",
            "SocialInvolve_ReligiousGroupParticipation": "Yes",
            "SocialInvolve_InterestHobbyGroupParticipation": "No",
            "SocialInvolve_DiscussionGroupParticipation": "Yes",
            "SocialInvolve_OtherParticipation": "No",
            "SocialInvolve_NoneParticipation": "No",
            "VolunteerDonate_VolunteeredTime": "Yes",
            "VolunteerDonate_DonatedMoney": "No",
            "VolunteerDonate_DonatedGoodsServices": "No",
            "VolunteerDonate_VolunteeredForCommunityProjects": "Yes",
            "VolunteerDonate_DonatedBlood": "No",
            "VolunteerDonate_ResolvedCommunityIssues": "No",
            "VolunteerDonate_HelpedNeighbors": "Yes",
            "VolunteerDonate_OtherActivities": "No",
            "VolunteerDonate_NoneActivities": "No",
            "VolunteerDonateFreq_FrequencyOfVolunteering": "Monthly",
            "VolunteerDonateMetd_MethodOfVolunteering": "In-person",
            "SnetworkEthnicity_FriendsOfDifferentEthnicity": "Yes",
            "SnetworkNationality_FriendsOfDifferentNationality": "No",
            "SnetworkReligion_FriendsOfDifferentReligion": "No",
            "SnetworkIncome_FriendsOfDifferentIncome": "Yes",
            "SnetworkEducation_FriendsOfDifferentEducation": "Yes",
            "SnetworkSorientation_FriendsOfDifferentOrientation": "No",
            "CloseSGFriends_HaveCloseSGanFriends": "Yes",
            "SinteractMeal_SharedAMealWithFriend": "Yes",
            "SinteractInvitedFriend_InvitedFriendToCelebration": "No",
            "SinteractBeenInvited_BeenInvitedToCelebration": "Yes",
            "SinteractParticipated_ParticipatedInFestival": "No",
            "SupportImmedfam_SupportFromImmediateFamily": "Yes",
            "SupportExtfam_SupportFromExtendedFamily": "No",
            "SupportWorksch_SupportFromWorkplaceSchool": "Yes",
            "SupportFriends_SupportFromFriends": "No",
            "OsExp_StudiedOverseas": "Yes",
            "OsExp_WorkedOverseas": "Yes",
            "OsExp_ExtendedStayOverseas": "No",
            "OsExp_None": "None",
            "TimeOs_TimeSpentLivingOverseas": "2 years",
            "StudyOs_PlansToStudyOverseas": "No",
            "WorkOs_PlansToWorkOverseas": "Yes",
            "TravelOs_PlansToTravelOverseas": "Yes",
            "MigrateOs_PlansToMigrateOverseas": "No",
            "RetireOs_PlansToRetireOverseas": "Yes",
            "OutcomeConnection_StrengthOfConnectionToSG": "Moderate",
            "OutcomeFuture_StrengthOfDesireToShapeSGFuture": "Strong",
            "Pillarbeh1_ConsiderateBehaviorInPublic": "Yes",
            "Pillarbeh2_HelpingCloseFriendsFamily": "Yes",
            "Pillarbeh3_HelpingWiderNetwork": "No",
            "Pillarbeh4_RegularlyDonating": "No",
            "Pillarbeh5_RegularlyVolunteering": "Yes",
            "Pillarbeh6_OfferingHelpUnasked": "Yes",
            "Pillarbeh7_ConstructiveFeedbackOnPolicies": "No",
            "Pillarbeh8_LeadMobilityForCauses": "Yes",
            "Pillarbeh9_ParticipatingInCommunityInitiatives": "No",
            "Pillarbeh10_GettingAlongWithDiverseCultures": "Yes",
            "Pillarbeh11_AvoidingRaciallySensitiveConversations": "No",
            "Pillarbeh12_EasingRaciallySensitiveSituations": "Yes",
            "Pillarbeh13_IncludingDifferentCulturesInLife": "No",
            "Pillarbeh14_UnderstandingCulturalPractices": "Yes",
            "Pillarbeh15_HavingGoodFriendsFromDifferentCultures": "No",
            "Pillarvals1_ConsistentWithValuesOfSociety": "Yes",
            "Pillarvals2_GuidedByDesireToDoRight": "Agree",
            "Pillarvals3_ActionsConsistentWithOthers": "Disagree",
            "Pillarvals4_BeneficialActionsEvenIfCostly": "Yes",
            "Pillarvals5_ResponsibilityToContributeToSociety": "No",
            "Pillarvals6_HelpingOthersIncreasesWellBeing": "Yes",
            "Pillarvals7_HelpingRiskingOffense": "No",
            "Pillarvals8_KnowingHowToHelpPeopleInNeed": "Yes",
            "Pillarvals9_HavingASayInDecisions": "Yes",
            "Pillarvals12_ActiveRoleInSociety": "No",
            "Pillarvals13_PotentialForPositiveChange": "Yes",
            "Pillarvals14_BelongingAndAcceptanceInSG": "No",
            "Pillarvals21_CommonGroundWithDifferentCultures": "Agree",
            "Pillarvals22_InteractingWithDifferentCulturesBenefitsMe": "Disagree",
            "Pillarvals23_MeaningfulInteractionsWithCultures": "Yes",
            "Pillarvals24_MeaningfulInteractionsWithNationalities": "No",
            "Pillarvals25_RespectingCulturalDifferences": "Yes",
            "Pillarvals26_NoRaciallyInsensitiveRemarks": "No",
            "Pillarvals29_ConfidenceInSingaporeFuture": "Yes",
            "Pillarvals30_SupportInGoodAndBadTimes": "Agree",
            "Pillarvals31_OpportunitiesForPersonalAspirations": "Strongly agree",
            "Pillarvals32_OpportunitiesToLiveByValues": "No",
            "Pillarvals33_CommittedToLongTermInSingapore": "Yes",
            "OnlineNews_CheckNewsStayUpdated": "Yes",
            "OnlineSM_CheckSocialMedia": "No",
            "OnlineShop_ShoppingOnline": "Yes",
            "OnlineAreasInterest_InformationOnAreasOfInterest": "No",
            "OnlineGames_PlayingOnlineGames": "Yes",
            "OnlineUpdate_UpdateSelfInformation": "No",
            "OnlineSharemedia_ShareVideosPhotos": "Yes",
            "OnlineWatchmedia_WatchVideosMovies": "No",
            "MaritalStats_CurrentMaritalStatus": "Single",
            "Children_HaveChildren": "No",
            "AgeYoungestChild_AgeOfYoungestChild": "N/A",
            "HHGrandparents_LiveWithGrandparents": "No",
            "HHParents_LiveWithParents": "Yes",
            "HHSiblings_LiveWithSiblings": "No",
            "HHSpouse_LiveWithSpouse": "No",
            "HHChildren_LiveWithChildren": "No",
            "HHRelatives_LiveWithOtherRelatives": "Yes",
            "HHHelper_LiveWithDomesticHelper": "No",
            "HHMates_LiveWithFriendsHousemates": "No",
            "HHMates_LiveWithEmployerFamily": "No",
            "HHMates_LiveWithGrandChildren": "No",
            "HHMates_LiveWithOther": "No",
            "HHMates_NoneOfTheAboveStayAlone": "Yes",
            "HighestEd_HighestEducationLevel": "Master's",
            "InstitutionDeg_ConferringInstitutionForDegree": "Another University",
            "Occupation_CurrentOccupation": "Manager",
            "MHI_MonthlyHouseholdIncome": "S6,001-S7,000",
            "MPI_MonthlyPersonalIncome": "S3,001-S4,000",
            "Weight_Weight": 75.0
        }
        response = self.client.post(url, data, format='json')

        # Print the response content for debugging
        #print("Response status:", response.status_code)
        #print("Response data:", response.data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Success: Created a new survey response.")
        
    def test_list_survey_responses(self):
        print("\nTesting functionality: List Survey Responses at endpoint: /api/surveyresponses/")
        url = reverse('surveyresponse-list')
        response = self.client.get(url)
        
        print("Response status:", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print("Success: Fetched survey responses.")

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
        
class SocialInvolvementByEducationTests(TestCase):
    def setUp(self):
        SurveyResponse.objects.all().delete()
        load_data_from_csv()

    def test_social_involvement_by_education(self):
        print("\nTesting functionality: Social Involvement by Education at endpoint: /api/social-involvement/education/")
        url = reverse('social-involvement-by-education')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict), "Response data should be a dictionary.")
        self.assertGreater(len(response.data), 0, "The response data should contain statistics for at least one education level.")

        print("Success: Validated social involvement statistics by education response.")