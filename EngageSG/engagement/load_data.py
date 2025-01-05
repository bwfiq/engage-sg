import os
import sys
import csv

# Need this to run the script not as a module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EngageSG.settings")

import django
django.setup()

from engagement.models import SurveyResponse

def load_data_from_csv():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'SocialValuesSurveydata.csv') # Hardcode relative path so script can be run from anywhere

    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Create a new SurveyResponse object from row data
            survey_response = SurveyResponse(
                UID_UniqueRespondentID=row['UID_UniqueRespondentID'],  # Unique respondent ID
                Sample_SampleType=row['Sample_SampleType'],  # Sample type
                Gender_Gender=row['Gender_Gender'],  # Gender
                Age2_AgeGroups=row['Age2_AgeGroups'],  # Age groups
                Dwelling_DwellingType=row['Dwelling_DwellingType'],  # Dwelling type
                Industry_CurrentIndustry=row['Industry_CurrentIndustry'],  # Current Industry_CurrentIndustry
                
                # Social involvement fields
                SocialInvolve_SportsGroupParticipation=row['SocialInvolve_SportsGroupParticipation'],  # Sports related groups
                SocialInvolve_ArtsCulturalGroupParticipation=row['SocialInvolve_ArtsCulturalGroupParticipation'],  # Arts and Cultural groups
                SocialInvolve_CommunityGroupParticipation=row['SocialInvolve_CommunityGroupParticipation'],  # Community groups
                SocialInvolve_WelfareSelfHelpGroupParticipation=row['SocialInvolve_WelfareSelfHelpGroupParticipation'],  # Welfare & Self-Help groups
                SocialInvolve_ReligiousGroupParticipation=row['SocialInvolve_ReligiousGroupParticipation'],  # Religious groups
                SocialInvolve_InterestHobbyGroupParticipation=row['SocialInvolve_InterestHobbyGroupParticipation'],  # Interest & Hobby groups
                SocialInvolve_DiscussionGroupParticipation=row['SocialInvolve_DiscussionGroupParticipation'],  # Discussion groups
                SocialInvolve_OtherParticipation=row['SocialInvolve_OtherParticipation'],  # Other
                SocialInvolve_NoneParticipation=row['SocialInvolve_NoneParticipation'],  # None of the above

                # Volunteer and donation fields
                VolunteerDonate_VolunteeredTime=row['VolunteerDonate_VolunteeredTime'],  # Volunteered time
                VolunteerDonate_DonatedMoney=row['VolunteerDonate_DonatedMoney'],  # Donated money
                VolunteerDonate_DonatedGoodsServices=row['VolunteerDonate_DonatedGoodsServices'],  # Donated goods/services
                VolunteerDonate_VolunteeredForCommunityProjects=row['VolunteerDonate_VolunteeredForCommunityProjects'],  # Volunteered time for projects
                VolunteerDonate_DonatedBlood=row['VolunteerDonate_DonatedBlood'],  # Donated blood
                VolunteerDonate_ResolvedCommunityIssues=row['VolunteerDonate_ResolvedCommunityIssues'],  # Worked with fellow citizens
                VolunteerDonate_HelpedNeighbors=row['VolunteerDonate_HelpedNeighbors'],  # Helped a neighbor
                VolunteerDonate_OtherActivities=row['VolunteerDonate_OtherActivities'],  # Other
                VolunteerDonate_NoneActivities=row['VolunteerDonate_NoneActivities'],  # None of the above
                VolunteerDonateFreq_FrequencyOfVolunteering=row['VolunteerDonateFreq_FrequencyOfVolunteering'],  # Frequency of volunteering/donating
                VolunteerDonateMetd_MethodOfVolunteering=row['VolunteerDonateMetd_MethodOfVolunteering'],  # Method of volunteering/donating

                # Social networks fields
                SnetworkEthnicity_FriendsOfDifferentEthnicity=row['SnetworkEthnicity_FriendsOfDifferentEthnicity'],  # Close friends of different ethnicity
                SnetworkNationality_FriendsOfDifferentNationality=row['SnetworkNationality_FriendsOfDifferentNationality'],  # Close friends of different nationality
                SnetworkReligion_FriendsOfDifferentReligion=row['SnetworkReligion_FriendsOfDifferentReligion'],  # Close friends of different religion
                SnetworkIncome_FriendsOfDifferentIncome=row['SnetworkIncome_FriendsOfDifferentIncome'],  # Close friends of different income
                SnetworkEducation_FriendsOfDifferentEducation=row['SnetworkEducation_FriendsOfDifferentEducation'],  # Close friends of different education
                SnetworkSorientation_FriendsOfDifferentOrientation=row['SnetworkSorientation_FriendsOfDifferentOrientation'],  # Close friends of different sexual orientation
                CloseSGFriends_HaveCloseSGanFriends=row['CloseSGFriends_HaveCloseSGanFriends'],  # Have close Singaporean friends

                # Social interaction fields
                SinteractMeal_SharedAMealWithFriend=row['SinteractMeal_SharedAMealWithFriend'],  # Shared a meal with a friend of different ethnicity/nationality
                SinteractInvitedFriend_InvitedFriendToCelebration=row['SinteractInvitedFriend_InvitedFriendToCelebration'],  # Invited a friend to a celebration
                SinteractBeenInvited_BeenInvitedToCelebration=row['SinteractBeenInvited_BeenInvitedToCelebration'],  # Been invited by a friend
                SinteractParticipated_ParticipatedInFestival=row['SinteractParticipated_ParticipatedInFestival'],  # Participated in a celebration

                # Support fields
                SupportImmedfam_SupportFromImmediateFamily=row['SupportImmedfam_SupportFromImmediateFamily'],  # Support from immediate family
                SupportExtfam_SupportFromExtendedFamily=row['SupportExtfam_SupportFromExtendedFamily'],  # Support from extended family
                SupportWorksch_SupportFromWorkplaceSchool=row['SupportWorksch_SupportFromWorkplaceSchool'],  # Support from workplace/school
                SupportFriends_SupportFromFriends=row['SupportFriends_SupportFromFriends'],  # Support from friends

                # Overseas experience fields
                OsExp_StudiedOverseas=row['OsExp_StudiedOverseas'],  # Studied overseas
                OsExp_WorkedOverseas=row['OsExp_WorkedOverseas'],  # Worked overseas
                OsExp_ExtendedStayOverseas=row['OsExp_ExtendedStayOverseas'],  # Stayed overseas for non-work reasons
                OsExp_None=row['OsExp_None'],  # None of the above
                TimeOs_TimeSpentLivingOverseas=row['TimeOs_TimeSpentLivingOverseas'],  # Time spent living overseas
                StudyOs_PlansToStudyOverseas=row['StudyOs_PlansToStudyOverseas'],  # Plans to study overseas
                WorkOs_PlansToWorkOverseas=row['WorkOs_PlansToWorkOverseas'],  # Plans to work overseas
                TravelOs_PlansToTravelOverseas=row['TravelOs_PlansToTravelOverseas'],  # Plans to travel overseas
                MigrateOs_PlansToMigrateOverseas=row['MigrateOs_PlansToMigrateOverseas'],  # Plans to migrate overseas
                RetireOs_PlansToRetireOverseas=row['RetireOs_PlansToRetireOverseas'],  # Plans to retire overseas

                # Outcome connection fields
                OutcomeConnection_StrengthOfConnectionToSG=row['OutcomeConnection_StrengthOfConnectionToSG'],  # Strength of connection to Singapore
                OutcomeFuture_StrengthOfDesireToShapeSGFuture=row['OutcomeFuture_StrengthOfDesireToShapeSGFuture'],  # Desire to shape Singapore’s future

                # Behavioral characteristics fields
                Pillarbeh1_ConsiderateBehaviorInPublic=row['Pillarbeh1_ConsiderateBehaviorInPublic'],  # Considerate behavior in public settings
                Pillarbeh2_HelpingCloseFriendsFamily=row['Pillarbeh2_HelpingCloseFriendsFamily'],  # Helping close friends and family
                Pillarbeh3_HelpingWiderNetwork=row['Pillarbeh3_HelpingWiderNetwork'],  # Helping wider networks
                Pillarbeh4_RegularlyDonating=row['Pillarbeh4_RegularlyDonating'],  # Regularly donating to causes
                Pillarbeh5_RegularlyVolunteering=row['Pillarbeh5_RegularlyVolunteering'],  # Regularly volunteering for causes
                Pillarbeh6_OfferingHelpUnasked=row['Pillarbeh6_OfferingHelpUnasked'],  # Offering help without being asked
                Pillarbeh7_ConstructiveFeedbackOnPolicies=row['Pillarbeh7_ConstructiveFeedbackOnPolicies'],  # Giving constructive feedback
                Pillarbeh8_LeadMobilityForCauses=row['Pillarbeh8_LeadMobilityForCauses'],  # Leading or mobilizing for causes
                Pillarbeh9_ParticipatingInCommunityInitiatives=row['Pillarbeh9_ParticipatingInCommunityInitiatives'],  # Participating in community initiatives
                Pillarbeh10_GettingAlongWithDiverseCultures=row['Pillarbeh10_GettingAlongWithDiverseCultures'],  # Getting along with diverse cultures
                Pillarbeh11_AvoidingRaciallySensitiveConversations=row['Pillarbeh11_AvoidingRaciallySensitiveConversations'],  # Avoiding racially-sensitive situations
                Pillarbeh12_EasingRaciallySensitiveSituations=row['Pillarbeh12_EasingRaciallySensitiveSituations'],  # Easing racially-sensitive situations
                Pillarbeh13_IncludingDifferentCulturesInLife=row['Pillarbeh13_IncludingDifferentCulturesInLife'],  # Including people from different cultures
                Pillarbeh14_UnderstandingCulturalPractices=row['Pillarbeh14_UnderstandingCulturalPractices'],  # Understanding different cultures
                Pillarbeh15_HavingGoodFriendsFromDifferentCultures=row['Pillarbeh15_HavingGoodFriendsFromDifferentCultures'],  # Good friends from different cultures

                # Value-based characteristics fields
                Pillarvals1_ConsistentWithValuesOfSociety=row['Pillarvals1_ConsistentWithValuesOfSociety'],  # Acting in line with societal values
                Pillarvals2_GuidedByDesireToDoRight=row['Pillarvals2_GuidedByDesireToDoRight'],  # Desire to do the right thing
                Pillarvals3_ActionsConsistentWithOthers=row['Pillarvals3_ActionsConsistentWithOthers'],  # Consistency with societal actions
                Pillarvals4_BeneficialActionsEvenIfCostly=row['Pillarvals4_BeneficialActionsEvenIfCostly'],  # Willingness to benefit others
                Pillarvals5_ResponsibilityToContributeToSociety=row['Pillarvals5_ResponsibilityToContributeToSociety'],  # Responsibility to contribute to society
                Pillarvals6_HelpingOthersIncreasesWellBeing=row['Pillarvals6_HelpingOthersIncreasesWellBeing'],  # Helping others for personal well-being
                Pillarvals7_HelpingRiskingOffense=row['Pillarvals7_HelpingRiskingOffense'],  # Helping others even if it risks offense
                Pillarvals8_KnowingHowToHelpPeopleInNeed=row['Pillarvals8_KnowingHowToHelpPeopleInNeed'],  # Knowing how to help people in need
                Pillarvals9_HavingASayInDecisions=row['Pillarvals9_HavingASayInDecisions'],  # Desire to participate in decision-making
                Pillarvals12_ActiveRoleInSociety=row['Pillarvals12_ActiveRoleInSociety'],  # Encouragement to play an active role
                Pillarvals13_PotentialForPositiveChange=row['Pillarvals13_PotentialForPositiveChange'],  # Confidence in creating positive change
                Pillarvals14_BelongingAndAcceptanceInSG=row['Pillarvals14_BelongingAndAcceptanceInSG'],  # Feeling of belonging in Singapore
                Pillarvals21_CommonGroundWithDifferentCultures=row['Pillarvals21_CommonGroundWithDifferentCultures'],  # Commonalities with diverse cultures
                Pillarvals22_InteractingWithDifferentCulturesBenefitsMe=row['Pillarvals22_InteractingWithDifferentCulturesBenefitsMe'],  # Benefits of interacting with diverse cultures
                Pillarvals23_MeaningfulInteractionsWithCultures=row['Pillarvals23_MeaningfulInteractionsWithCultures'],  # Opportunities for meaningful interactions
                Pillarvals24_MeaningfulInteractionsWithNationalities=row['Pillarvals24_MeaningfulInteractionsWithNationalities'],  # Respect for cultural differences
                Pillarvals25_RespectingCulturalDifferences=row['Pillarvals25_RespectingCulturalDifferences'],  # Concerns about racial insensitivity
                Pillarvals26_NoRaciallyInsensitiveRemarks=row['Pillarvals26_NoRaciallyInsensitiveRemarks'],  # Confidence in Singapore's future
                Pillarvals29_ConfidenceInSingaporeFuture=row['Pillarvals29_ConfidenceInSingaporeFuture'],  # Willing to support Singapore
                Pillarvals30_SupportInGoodAndBadTimes=row['Pillarvals30_SupportInGoodAndBadTimes'],  # Opportunities to achieve aspirations
                Pillarvals31_OpportunitiesForPersonalAspirations=row['Pillarvals31_OpportunitiesForPersonalAspirations'],  # Commitment to staying in Singapore

                # Online behavior fields
                OnlineNews_CheckNewsStayUpdated=row['OnlineNews_CheckNewsStayUpdated'],  # Check news/current affairs
                OnlineSM_CheckSocialMedia=row['OnlineSM_CheckSocialMedia'],  # Use social media platforms
                OnlineShop_ShoppingOnline=row['OnlineShop_ShoppingOnline'],  # Shopping behavior
                OnlineAreasInterest_InformationOnAreasOfInterest=row['OnlineAreasInterest_InformationOnAreasOfInterest'],  # Searching for information of interest
                OnlineGames_PlayingOnlineGames=row['OnlineGames_PlayingOnlineGames'],  # Online gaming behavior
                OnlineUpdate_UpdateSelfInformation=row['OnlineUpdate_UpdateSelfInformation'],  # Updating self-information online
                OnlineSharemedia_ShareVideosPhotos=row['OnlineSharemedia_ShareVideosPhotos'],  # Sharing media online
                OnlineWatchmedia_WatchVideosMovies=row['OnlineWatchmedia_WatchVideosMovies'],  # Watching videos/movies online

                # Household demographics fields
                MaritalStats_CurrentMaritalStatus=row['MaritalStats_CurrentMaritalStatus'],  # Current marital status
                Children_HaveChildren=row['Children_HaveChildren'],  # Have Children_HaveChildren
                AgeYoungestChild_AgeOfYoungestChild=row['AgeYoungestChild_AgeOfYoungestChild'],  # Age of youngest child
                HHGrandparents_LiveWithGrandparents=row['HHGrandparents_LiveWithGrandparents'],  # Live with grandparents
                HHParents_LiveWithParents=row['HHParents_LiveWithParents'],  # Live with parents
                HHSiblings_LiveWithSiblings=row['HHSiblings_LiveWithSiblings'],  # Live with siblings
                HHSpouse_LiveWithSpouse=row['HHSpouse_LiveWithSpouse'],  # Live with spouse
                HHChildren_LiveWithChildren=row['HHChildren_LiveWithChildren'],  # Live with Children_HaveChildren
                HHRelatives_LiveWithOtherRelatives=row['HHRelatives_LiveWithOtherRelatives'],  # Live with other relatives
                HHHelper_LiveWithDomesticHelper=row['HHHelper_LiveWithDomesticHelper'],  # Live with domestic helper
                HHMates_LiveWithFriendsHousemates=row['HHMates_LiveWithFriendsHousemates'],  # Live with friends/housemates
                HHMates_LiveWithEmployerFamily=row['HHMates_LiveWithEmployerFamily'],  # Live with employer's family
                HHMates_LiveWithGrandChildren=row['HHMates_LiveWithGrandChildren'],  # Live with grandChildren_HaveChildren
                HHMates_LiveWithOther=row['HHMates_LiveWithOther'],  # Live with other arrangements
                HHMates_NoneOfTheAboveStayAlone=row['HHMates_NoneOfTheAboveStayAlone'],  # Stay alone

                # Education and Occupation_CurrentOccupation fields
                HighestEd_HighestEducationLevel=row['HighestEd_HighestEducationLevel'],  # Highest attained education level
                InstitutionDeg_ConferringInstitutionForDegree=row['InstitutionDeg_ConferringInstitutionForDegree'],  # Conferring institution for degree/post-grad
                Occupation_CurrentOccupation=row['Occupation_CurrentOccupation'],  # Current Occupation_CurrentOccupation
                
                # Economic fields
                MHI_MonthlyHouseholdIncome=row['MHI_MonthlyHouseholdIncome'],  # Monthly household income
                MPI_MonthlyPersonalIncome=row['MPI_MonthlyPersonalIncome'],  # Monthly personal income
                Weight_Weight=row['Weight_Weight'],  # Weight
            )
            try:
                survey_response.save()
                #print(f"Inserted response for UID_UniqueRespondentID: {survey_response.UID_UniqueRespondentID}")
            except Exception as e:
                print(f"Error inserting response for UID_UniqueRespondentID {row['UID_UniqueRespondentID']}: {str(e)}")

if __name__ == '__main__':
    load_data_from_csv()