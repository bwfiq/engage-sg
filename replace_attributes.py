import os
import csv

# Define the mapping from variable names to their new labels
mapping = {
    "uid": "UID_UniqueRespondentID",
    "sample": "Sample_SampleType",
    "gender": "Gender_Gender",
    "age_2": "Age2_AgeGroups",
    "dwelling": "Dwelling_DwellingType",
    "industry": "Industry_CurrentIndustry",
    "social_involve_1": "SocialInvolve_SportsGroupParticipation",
    "social_involve_2": "SocialInvolve_ArtsCulturalGroupParticipation",
    "social_involve_3": "SocialInvolve_CommunityGroupParticipation",
    "social_involve_4": "SocialInvolve_WelfareSelfHelpGroupParticipation",
    "social_involve_5": "SocialInvolve_ReligiousGroupParticipation",
    "social_involve_6": "SocialInvolve_InterestHobbyGroupParticipation",
    "social_involve_7": "SocialInvolve_DiscussionGroupParticipation",
    "social_involve_8": "SocialInvolve_OtherParticipation",
    "social_involve_9": "SocialInvolve_NoneParticipation",
    "volunteerdonate_1": "VolunteerDonate_VolunteeredTime",
    "volunteerdonate_2": "VolunteerDonate_DonatedMoney",
    "volunteerdonate_3": "VolunteerDonate_DonatedGoodsServices",
    "volunteerdonate_4": "VolunteerDonate_VolunteeredForCommunityProjects",
    "volunteerdonate_5": "VolunteerDonate_DonatedBlood",
    "volunteerdonate_6": "VolunteerDonate_ResolvedCommunityIssues",
    "volunteerdonate_7": "VolunteerDonate_HelpedNeighbors",
    "volunteerdonate_8": "VolunteerDonate_OtherActivities",
    "volunteerdonate_9": "VolunteerDonate_NoneActivities",
    "volunteerdonate_freq": "VolunteerDonateFreq_FrequencyOfVolunteering",
    "volunteerdonate_metd": "VolunteerDonateMetd_MethodOfVolunteering",
    "snetwork_ethnicity": "SnetworkEthnicity_FriendsOfDifferentEthnicity",
    "snetwork_nationality": "SnetworkNationality_FriendsOfDifferentNationality",
    "snetwork_religion": "SnetworkReligion_FriendsOfDifferentReligion",
    "snetwork_income": "SnetworkIncome_FriendsOfDifferentIncome",
    "snetwork_education": "SnetworkEducation_FriendsOfDifferentEducation",
    "snetwork_sorientation": "SnetworkSorientation_FriendsOfDifferentOrientation",
    "close_sg_friends": "CloseSGFriends_HaveCloseSGanFriends",
    "sinteract_meal": "SinteractMeal_SharedAMealWithFriend",
    "sinteract_invitedfriend": "SinteractInvitedFriend_InvitedFriendToCelebration",
    "sinteract_beeninvited": "SinteractBeenInvited_BeenInvitedToCelebration",
    "sinteract_participated": "SinteractParticipated_ParticipatedInFestival",
    "support_immedfam": "SupportImmedfam_SupportFromImmediateFamily",
    "support_extfam": "SupportExtfam_SupportFromExtendedFamily",
    "support_worksch": "SupportWorksch_SupportFromWorkplaceSchool",
    "support_friends": "SupportFriends_SupportFromFriends",
    "os_exp_1": "OsExp_StudiedOverseas",
    "os_exp_2": "OsExp_WorkedOverseas",
    "os_exp_3": "OsExp_ExtendedStayOverseas",
    "os_exp_4": "OsExp_None",
    "time_os": "TimeOs_TimeSpentLivingOverseas",
    "study_os": "StudyOs_PlansToStudyOverseas",
    "work_os": "WorkOs_PlansToWorkOverseas",
    "travel_os": "TravelOs_PlansToTravelOverseas",
    "migrate_os": "MigrateOs_PlansToMigrateOverseas",
    "retire_os": "RetireOs_PlansToRetireOverseas",
    "outcome_connection": "OutcomeConnection_StrengthOfConnectionToSG",
    "outcome_future": "OutcomeFuture_StrengthOfDesireToShapeSGFuture",
    "pillarbeh_10": "Pillarbeh10_GettingAlongWithDiverseCultures",
    "pillarbeh_11": "Pillarbeh11_AvoidingRaciallySensitiveConversations",
    "pillarbeh_12": "Pillarbeh12_EasingRaciallySensitiveSituations",
    "pillarbeh_13": "Pillarbeh13_IncludingDifferentCulturesInLife",
    "pillarbeh_14": "Pillarbeh14_UnderstandingCulturalPractices",
    "pillarbeh_15": "Pillarbeh15_HavingGoodFriendsFromDifferentCultures",
    "pillarbeh_1": "Pillarbeh1_ConsiderateBehaviorInPublic",
    "pillarbeh_2": "Pillarbeh2_HelpingCloseFriendsFamily",
    "pillarbeh_3": "Pillarbeh3_HelpingWiderNetwork",
    "pillarbeh_4": "Pillarbeh4_RegularlyDonating",
    "pillarbeh_5": "Pillarbeh5_RegularlyVolunteering",
    "pillarbeh_6": "Pillarbeh6_OfferingHelpUnasked",
    "pillarbeh_7": "Pillarbeh7_ConstructiveFeedbackOnPolicies",
    "pillarbeh_8": "Pillarbeh8_LeadMobilityForCauses",
    "pillarbeh_9": "Pillarbeh9_ParticipatingInCommunityInitiatives",
    "pillarvals_12": "Pillarvals12_ActiveRoleInSociety",
    "pillarvals_13": "Pillarvals13_PotentialForPositiveChange",
    "pillarvals_14": "Pillarvals14_BelongingAndAcceptanceInSG",
    "pillarvals_21": "Pillarvals21_CommonGroundWithDifferentCultures",
    "pillarvals_22": "Pillarvals22_InteractingWithDifferentCulturesBenefitsMe",
    "pillarvals_23": "Pillarvals23_MeaningfulInteractionsWithCultures",
    "pillarvals_24": "Pillarvals24_MeaningfulInteractionsWithNationalities",
    "pillarvals_25": "Pillarvals25_RespectingCulturalDifferences",
    "pillarvals_26": "Pillarvals26_NoRaciallyInsensitiveRemarks",
    "pillarvals_29": "Pillarvals29_ConfidenceInSingaporeFuture",
    "pillarvals_30": "Pillarvals30_SupportInGoodAndBadTimes",
    "pillarvals_31": "Pillarvals31_OpportunitiesForPersonalAspirations",
    "pillarvals_32": "Pillarvals32_OpportunitiesToLiveByValues",
    "pillarvals_33": "Pillarvals33_CommittedToLongTermInSingapore",
    "pillarvals_1": "Pillarvals1_ConsistentWithValuesOfSociety",
    "pillarvals_2": "Pillarvals2_GuidedByDesireToDoRight",
    "pillarvals_3": "Pillarvals3_ActionsConsistentWithOthers",
    "pillarvals_4": "Pillarvals4_BeneficialActionsEvenIfCostly",
    "pillarvals_5": "Pillarvals5_ResponsibilityToContributeToSociety",
    "pillarvals_6": "Pillarvals6_HelpingOthersIncreasesWellBeing",
    "pillarvals_7": "Pillarvals7_HelpingRiskingOffense",
    "pillarvals_8": "Pillarvals8_KnowingHowToHelpPeopleInNeed",
    "pillarvals_9": "Pillarvals9_HavingASayInDecisions",
    "online_news": "OnlineNews_CheckNewsStayUpdated",
    "online_sm": "OnlineSM_CheckSocialMedia",
    "online_shop": "OnlineShop_ShoppingOnline",
    "online_areasinterest": "OnlineAreasInterest_InformationOnAreasOfInterest",
    "online_games": "OnlineGames_PlayingOnlineGames",
    "online_update": "OnlineUpdate_UpdateSelfInformation",
    "online_sharemedia": "OnlineSharemedia_ShareVideosPhotos",
    "online_watchmedia": "OnlineWatchmedia_WatchVideosMovies",
    "marital_stats": "MaritalStats_CurrentMaritalStatus",
    "hh_grandchildren": "HHMates_LiveWithGrandChildren",
    "hh_children": "HHChildren_LiveWithChildren",
    "children": "Children_HaveChildren",
    "age_youngestchild": "AgeYoungestChild_AgeOfYoungestChild",
    "hh_grandparents": "HHGrandparents_LiveWithGrandparents",
    "hh_parents": "HHParents_LiveWithParents",
    "hh_siblings": "HHSiblings_LiveWithSiblings",
    "hh_spouse": "HHSpouse_LiveWithSpouse",
    "hh_relatives": "HHRelatives_LiveWithOtherRelatives",
    "hh_helper": "HHHelper_LiveWithDomesticHelper",
    "hh_mates": "HHMates_LiveWithFriendsHousemates",
    "hh_employer_their_family": "HHMates_LiveWithEmployerFamily",
    "hh_other": "HHMates_LiveWithOther",
    "hh_none": "HHMates_NoneOfTheAboveStayAlone",
    "highest_ed": "HighestEd_HighestEducationLevel",
    "institution_deg": "InstitutionDeg_ConferringInstitutionForDegree",
    "occupation": "Occupation_CurrentOccupation",
    "mhi": "MHI_MonthlyHouseholdIncome",
    "mpi": "MPI_MonthlyPersonalIncome",
    "weight": "Weight_Weight"
}

# Function to replace attributes in a file
def replace_attributes_in_file(filename):
    if not os.path.isfile(filename):
        return

    with open(filename, 'r') as file:
        content = file.read()

    for var_name, new_value in mapping.items():
        content = content.replace(var_name, new_value)

    with open(filename, 'w') as file:
        file.write(content)

# Function to traverse directories and files
def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.txt'):  # Specify the file types to be changed
                file_path = os.path.join(root, file)
                replace_attributes_in_file(file_path)

# Specify the directory containing your codebase
directory_to_search = 'EngageSG/'  # Change this to your specific directory

# Run the replacement
traverse_directory(directory_to_search)

print("Attribute replacement completed_")