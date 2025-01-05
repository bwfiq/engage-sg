from django.db import models

class SurveyResponse(models.Model):
    UID_UniqueRespondentID = models.CharField(max_length=50, primary_key=True)  # Unique respondent ID
    Sample_SampleType = models.CharField(max_length=100)                # Sample type
    Gender_Gender = models.CharField(max_length=100)                 # Gender
    Age2_AgeGroups = models.CharField(max_length=50)                  # Age groups
    Dwelling_DwellingType = models.CharField(max_length=50)               # Dwelling type
    Industry_CurrentIndustry = models.CharField(max_length=100)              # Current Industry_CurrentIndustry
    
    # Social involvement fields
    SocialInvolve_SportsGroupParticipation = models.CharField(max_length=100)  # Sports related groups
    SocialInvolve_ArtsCulturalGroupParticipation = models.CharField(max_length=100)  # Arts and Cultural groups
    SocialInvolve_CommunityGroupParticipation = models.CharField(max_length=100)  # Community groups
    SocialInvolve_WelfareSelfHelpGroupParticipation = models.CharField(max_length=100)  # Welfare & Self-Help groups
    SocialInvolve_ReligiousGroupParticipation = models.CharField(max_length=100)  # Religious groups
    SocialInvolve_InterestHobbyGroupParticipation = models.CharField(max_length=100)  # Interest & Hobby groups
    SocialInvolve_DiscussionGroupParticipation = models.CharField(max_length=100)  # Discussion groups
    SocialInvolve_OtherParticipation = models.CharField(max_length=100)  # Other
    SocialInvolve_NoneParticipation = models.CharField(max_length=100)  # None of the above

    # Volunteer and donation fields
    VolunteerDonate_VolunteeredTime = models.CharField(max_length=100)  # Volunteered time
    VolunteerDonate_DonatedMoney = models.CharField(max_length=100)  # Donated money
    VolunteerDonate_DonatedGoodsServices = models.CharField(max_length=100)  # Donated goods/services
    VolunteerDonate_VolunteeredForCommunityProjects = models.CharField(max_length=100)  # Volunteered time for projects
    VolunteerDonate_DonatedBlood = models.CharField(max_length=100)  # Donated blood
    VolunteerDonate_ResolvedCommunityIssues = models.CharField(max_length=100)  # Worked with citizens
    VolunteerDonate_HelpedNeighbors = models.CharField(max_length=100)  # Helped neighbors
    VolunteerDonate_OtherActivities = models.CharField(max_length=100)  # Other
    VolunteerDonate_NoneActivities = models.CharField(max_length=100)  # None of the above
    VolunteerDonateFreq_FrequencyOfVolunteering = models.CharField(max_length=50)  # Frequency of volunteering/donating
    VolunteerDonateMetd_MethodOfVolunteering = models.CharField(max_length=50)  # Method of volunteering/donating

    # Social networks fields
    SnetworkEthnicity_FriendsOfDifferentEthnicity = models.CharField(max_length=100)    # Close friends of different ethnicity
    SnetworkNationality_FriendsOfDifferentNationality = models.CharField(max_length=100)   # Close friends of different nationality
    SnetworkReligion_FriendsOfDifferentReligion = models.CharField(max_length=100)      # Close friends of different religion
    SnetworkIncome_FriendsOfDifferentIncome = models.CharField(max_length=100)        # Close friends of different income
    SnetworkEducation_FriendsOfDifferentEducation = models.CharField(max_length=100)     # Close friends of different education
    SnetworkSorientation_FriendsOfDifferentOrientation = models.CharField(max_length=100)   # Close friends of different sexual orientation
    CloseSGFriends_HaveCloseSGanFriends = models.CharField(max_length=100)       # Have close Singaporean friends

    # Social interaction fields
    SinteractMeal_SharedAMealWithFriend = models.CharField(max_length=100)         # Shared a meal with different ethnicity
    SinteractInvitedFriend_InvitedFriendToCelebration = models.CharField(max_length=100) # Invited friend of different ethnicity
    SinteractBeenInvited_BeenInvitedToCelebration = models.CharField(max_length=100)   # Been invited to celebration
    SinteractParticipated_ParticipatedInFestival = models.CharField(max_length=100)   # Participated in celebration

    # Support fields
    SupportImmedfam_SupportFromImmediateFamily = models.CharField(max_length=100)       # Support from immediate family
    SupportExtfam_SupportFromExtendedFamily = models.CharField(max_length=100)          # Support from extended family
    SupportWorksch_SupportFromWorkplaceSchool = models.CharField(max_length=100)         # Support from workplace/school
    SupportFriends_SupportFromFriends = models.CharField(max_length=100)         # Support from friends

    # Overseas experience fields
    OsExp_StudiedOverseas = models.CharField(max_length=100)                # Studied overseas
    OsExp_WorkedOverseas = models.CharField(max_length=100)                # Worked overseas
    OsExp_ExtendedStayOverseas = models.CharField(max_length=100)                # Stayed overseas for non-work reasons
    OsExp_None = models.CharField(max_length=100)                # None of the above
    TimeOs_TimeSpentLivingOverseas = models.CharField(max_length=50)                 # Time spent living overseas
    StudyOs_PlansToStudyOverseas = models.CharField(max_length=100)                # Plans to study overseas
    WorkOs_PlansToWorkOverseas = models.CharField(max_length=100)                 # Plans to work overseas
    TravelOs_PlansToTravelOverseas = models.CharField(max_length=100)               # Plans to travel overseas
    MigrateOs_PlansToMigrateOverseas = models.CharField(max_length=100)              # Plans to migrate overseas
    RetireOs_PlansToRetireOverseas = models.CharField(max_length=100)               # Plans to retire overseas

    # Outcome connection fields
    OutcomeConnection_StrengthOfConnectionToSG = models.CharField(max_length=100)      # Strength of connection to Singapore
    OutcomeFuture_StrengthOfDesireToShapeSGFuture = models.CharField(max_length=100)          # Desire to shape Singapore’s future

    # Behavioral characteristics fields
    Pillarbeh1_ConsiderateBehaviorInPublic = models.CharField(max_length=100)             # Considerate behavior in public settings
    Pillarbeh2_HelpingCloseFriendsFamily = models.CharField(max_length=100)             # Helping close friends and family
    Pillarbeh3_HelpingWiderNetwork = models.CharField(max_length=100)             # Helping wider networks
    Pillarbeh4_RegularlyDonating = models.CharField(max_length=100)             # Regularly donating to causes
    Pillarbeh5_RegularlyVolunteering = models.CharField(max_length=100)             # Regularly volunteering for causes
    Pillarbeh6_OfferingHelpUnasked = models.CharField(max_length=100)             # Offering help without being asked
    Pillarbeh7_ConstructiveFeedbackOnPolicies = models.CharField(max_length=100)             # Giving constructive feedback
    Pillarbeh8_LeadMobilityForCauses = models.CharField(max_length=100)             # Leading or mobilizing for causes
    Pillarbeh9_ParticipatingInCommunityInitiatives = models.CharField(max_length=100)             # Participating in community initiatives
    Pillarbeh10_GettingAlongWithDiverseCultures = models.CharField(max_length=100)            # Getting along with people from different cultures
    Pillarbeh11_AvoidingRaciallySensitiveConversations = models.CharField(max_length=100)            # Avoiding racially-sensitive situations
    Pillarbeh12_EasingRaciallySensitiveSituations = models.CharField(max_length=100)            # Easing racially-sensitive situations
    Pillarbeh13_IncludingDifferentCulturesInLife = models.CharField(max_length=100)            # Including people from different cultures
    Pillarbeh14_UnderstandingCulturalPractices = models.CharField(max_length=100)            # Understanding different cultures
    Pillarbeh15_HavingGoodFriendsFromDifferentCultures = models.CharField(max_length=100)            # Good friends from different cultures

    # Value-based characteristics fields
    Pillarvals1_ConsistentWithValuesOfSociety = models.CharField(max_length=100)            # Acting consistently with societal values
    Pillarvals2_GuidedByDesireToDoRight = models.CharField(max_length=100)            # Desire to do the right thing
    Pillarvals3_ActionsConsistentWithOthers = models.CharField(max_length=100)            # Actions consistent with society
    Pillarvals4_BeneficialActionsEvenIfCostly = models.CharField(max_length=100)            # Willingness to benefit others
    Pillarvals5_ResponsibilityToContributeToSociety = models.CharField(max_length=100)            # Responsibility to contribute to society
    Pillarvals6_HelpingOthersIncreasesWellBeing = models.CharField(max_length=100)            # Helping others for well-being
    Pillarvals7_HelpingRiskingOffense = models.CharField(max_length=100)            # Helping others without offending
    Pillarvals8_KnowingHowToHelpPeopleInNeed = models.CharField(max_length=100)            # Knowing how to help people in need
    Pillarvals9_HavingASayInDecisions = models.CharField(max_length=100)            # Desire to participate in decision-making
    Pillarvals12_ActiveRoleInSociety = models.CharField(max_length=100)           # Encouraged to play an active role in society
    Pillarvals13_PotentialForPositiveChange = models.CharField(max_length=100)           # Ability to create positive change
    Pillarvals14_BelongingAndAcceptanceInSG = models.CharField(max_length=100)           # Feeling of belonging in Singapore
    Pillarvals21_CommonGroundWithDifferentCultures = models.CharField(max_length=100)           # Commonalities with diverse cultures
    Pillarvals22_InteractingWithDifferentCulturesBenefitsMe = models.CharField(max_length=100)           # Benefit of interacting with diverse cultures
    Pillarvals23_MeaningfulInteractionsWithCultures = models.CharField(max_length=100)           # Opportunities for meaningful interactions with diverse cultures
    Pillarvals24_MeaningfulInteractionsWithNationalities = models.CharField(max_length=100)           # Opportunities for meaningful interactions with diverse nationalities
    Pillarvals25_RespectingCulturalDifferences = models.CharField(max_length=100)           # Respect for cultural differences
    Pillarvals26_NoRaciallyInsensitiveRemarks = models.CharField(max_length=100)           # Wrong to make culturally insensitive remarks
    Pillarvals29_ConfidenceInSingaporeFuture = models.CharField(max_length=100)           # Confidence in Singapore's future
    Pillarvals30_SupportInGoodAndBadTimes = models.CharField(max_length=100)           # Willing to support Singapore in tough times
    Pillarvals31_OpportunitiesForPersonalAspirations = models.CharField(max_length=100)           # Opportunities to achieve aspirations
    Pillarvals32_OpportunitiesToLiveByValues = models.CharField(max_length=100)           # Opportunities to live by personal values
    Pillarvals33_CommittedToLongTermInSingapore = models.CharField(max_length=100)           # Commitment to staying in Singapore long-term

    # Online behavior fields
    OnlineNews_CheckNewsStayUpdated = models.CharField(max_length=100)            # Check news/current affairs
    OnlineSM_CheckSocialMedia = models.CharField(max_length=100)              # Use social media platforms
    OnlineShop_ShoppingOnline = models.CharField(max_length=100)            # Shopping behavior
    OnlineAreasInterest_InformationOnAreasOfInterest = models.CharField(max_length=100)   # Searching for information of interest
    OnlineGames_PlayingOnlineGames = models.CharField(max_length=100)           # Online gaming behavior
    OnlineUpdate_UpdateSelfInformation = models.CharField(max_length=100)          # Updating self-information online
    OnlineSharemedia_ShareVideosPhotos = models.CharField(max_length=100)      # Sharing media online
    OnlineWatchmedia_WatchVideosMovies = models.CharField(max_length=100)      # Watching videos/movies online

    # Household demographics fields
    MaritalStats_CurrentMaritalStatus = models.CharField(max_length=100)          # Current marital status
    Children_HaveChildren = models.CharField(max_length=100)               # Have Children_HaveChildren
    AgeYoungestChild_AgeOfYoungestChild = models.CharField(max_length=100)      # Age of youngest child
    HHGrandparents_LiveWithGrandparents = models.CharField(max_length=100)        # Live with grandparents
    HHParents_LiveWithParents = models.CharField(max_length=100)             # Live with parents
    HHSiblings_LiveWithSiblings = models.CharField(max_length=100)            # Live with siblings
    HHSpouse_LiveWithSpouse = models.CharField(max_length=100)              # Live with spouse
    HHChildren_LiveWithChildren = models.CharField(max_length=100)            # Live with Children_HaveChildren
    HHRelatives_LiveWithOtherRelatives = models.CharField(max_length=100)           # Live with other relatives
    HHHelper_LiveWithDomesticHelper = models.CharField(max_length=100)              # Live with domestic helper
    HHMates_LiveWithFriendsHousemates = models.CharField(max_length=100)               # Live with friends/housemates
    HHMates_LiveWithEmployerFamily = models.CharField(max_length=100) # Live with employer's family
    HHMates_LiveWithGrandChildren = models.CharField(max_length=100)       # Live with grandChildren_HaveChildren
    HHMates_LiveWithOther = models.CharField(max_length=100)               # Live with other arrangements
    HHMates_NoneOfTheAboveStayAlone = models.CharField(max_length=100)                # Stay alone

    # Education and Occupation_CurrentOccupation fields
    HighestEd_HighestEducationLevel = models.CharField(max_length=100)            # Highest attained education level
    InstitutionDeg_ConferringInstitutionForDegree = models.CharField(max_length=100)       # Conferring institution for degree/post-grad
    Occupation_CurrentOccupation = models.CharField(max_length=100)            # Current Occupation_CurrentOccupation
    
    # Economic fields
    MHI_MonthlyHouseholdIncome = models.CharField(max_length=50)                    # Monthly household income
    MPI_MonthlyPersonalIncome = models.CharField(max_length=50)                    # Monthly personal income
    Weight_Weight = models.FloatField()                             # Weight (can also consider using PositiveIntegerField if Weight_Weight is always a positive integer)

    # Define a string representation for the model
    def __str__(self):
        return f"{self.UID_UniqueRespondentID} - {self.Gender_Gender} - {self.Age2_AgeGroups}"