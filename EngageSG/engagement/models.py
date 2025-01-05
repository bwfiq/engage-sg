from django.db import models

class SurveyResponse(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)  # Unique respondent ID
    sample = models.CharField(max_length=100)                # Sample type
    gender = models.CharField(max_length=100)                 # Gender
    age_2 = models.CharField(max_length=50)                  # Age groups
    dwelling = models.CharField(max_length=50)               # Dwelling type
    industry = models.CharField(max_length=100)              # Current industry
    
    # Social involvement fields
    social_involve_1 = models.CharField(max_length=100)  # Sports related groups
    social_involve_2 = models.CharField(max_length=100)  # Arts and Cultural groups
    social_involve_3 = models.CharField(max_length=100)  # Community groups
    social_involve_4 = models.CharField(max_length=100)  # Welfare & Self-Help groups
    social_involve_5 = models.CharField(max_length=100)  # Religious groups
    social_involve_6 = models.CharField(max_length=100)  # Interest & Hobby groups
    social_involve_7 = models.CharField(max_length=100)  # Discussion groups
    social_involve_8 = models.CharField(max_length=100)  # Other
    social_involve_9 = models.CharField(max_length=100)  # None of the above

    # Volunteer and donation fields
    volunteerdonate_1 = models.CharField(max_length=100)  # Volunteered time
    volunteerdonate_2 = models.CharField(max_length=100)  # Donated money
    volunteerdonate_3 = models.CharField(max_length=100)  # Donated goods/services
    volunteerdonate_4 = models.CharField(max_length=100)  # Volunteered time for projects
    volunteerdonate_5 = models.CharField(max_length=100)  # Donated blood
    volunteerdonate_6 = models.CharField(max_length=100)  # Worked with citizens
    volunteerdonate_7 = models.CharField(max_length=100)  # Helped neighbors
    volunteerdonate_8 = models.CharField(max_length=100)  # Other
    volunteerdonate_9 = models.CharField(max_length=100)  # None of the above
    volunteerdonate_freq = models.CharField(max_length=50)  # Frequency of volunteering/donating
    volunteerdonate_metd = models.CharField(max_length=50)  # Method of volunteering/donating

    # Social networks fields
    snetwork_ethnicity = models.CharField(max_length=100)    # Close friends of different ethnicity
    snetwork_nationality = models.CharField(max_length=100)   # Close friends of different nationality
    snetwork_religion = models.CharField(max_length=100)      # Close friends of different religion
    snetwork_income = models.CharField(max_length=100)        # Close friends of different income
    snetwork_education = models.CharField(max_length=100)     # Close friends of different education
    snetwork_sorientation = models.CharField(max_length=100)   # Close friends of different sexual orientation
    close_sg_friends = models.CharField(max_length=100)       # Have close Singaporean friends

    # Social interaction fields
    sinteract_meal = models.CharField(max_length=100)         # Shared a meal with different ethnicity
    sinteract_invitedfriend = models.CharField(max_length=100) # Invited friend of different ethnicity
    sinteract_beeninvited = models.CharField(max_length=100)   # Been invited to celebration
    sinteract_participated = models.CharField(max_length=100)   # Participated in celebration

    # Support fields
    support_immedfam = models.CharField(max_length=100)       # Support from immediate family
    support_extfam = models.CharField(max_length=100)          # Support from extended family
    support_worksch = models.CharField(max_length=100)         # Support from workplace/school
    support_friends = models.CharField(max_length=100)         # Support from friends

    # Overseas experience fields
    os_exp_1 = models.CharField(max_length=100)                # Studied overseas
    os_exp_2 = models.CharField(max_length=100)                # Worked overseas
    os_exp_3 = models.CharField(max_length=100)                # Stayed overseas for non-work reasons
    os_exp_4 = models.CharField(max_length=100)                # None of the above
    time_os = models.CharField(max_length=50)                 # Time spent living overseas
    study_os = models.CharField(max_length=100)                # Plans to study overseas
    work_os = models.CharField(max_length=100)                 # Plans to work overseas
    travel_os = models.CharField(max_length=100)               # Plans to travel overseas
    migrate_os = models.CharField(max_length=100)              # Plans to migrate overseas
    retire_os = models.CharField(max_length=100)               # Plans to retire overseas

    # Outcome connection fields
    outcome_connection = models.CharField(max_length=100)      # Strength of connection to Singapore
    outcome_future = models.CharField(max_length=100)          # Desire to shape Singapore’s future

    # Behavioral characteristics fields
    pillarbeh_1 = models.CharField(max_length=100)             # Considerate behavior in public settings
    pillarbeh_2 = models.CharField(max_length=100)             # Helping close friends and family
    pillarbeh_3 = models.CharField(max_length=100)             # Helping wider networks
    pillarbeh_4 = models.CharField(max_length=100)             # Regularly donating to causes
    pillarbeh_5 = models.CharField(max_length=100)             # Regularly volunteering for causes
    pillarbeh_6 = models.CharField(max_length=100)             # Offering help without being asked
    pillarbeh_7 = models.CharField(max_length=100)             # Giving constructive feedback
    pillarbeh_8 = models.CharField(max_length=100)             # Leading or mobilizing for causes
    pillarbeh_9 = models.CharField(max_length=100)             # Participating in community initiatives
    pillarbeh_10 = models.CharField(max_length=100)            # Getting along with people from different cultures
    pillarbeh_11 = models.CharField(max_length=100)            # Avoiding racially-sensitive situations
    pillarbeh_12 = models.CharField(max_length=100)            # Easing racially-sensitive situations
    pillarbeh_13 = models.CharField(max_length=100)            # Including people from different cultures
    pillarbeh_14 = models.CharField(max_length=100)            # Understanding different cultures
    pillarbeh_15 = models.CharField(max_length=100)            # Good friends from different cultures

    # Value-based characteristics fields
    pillarvals_1 = models.CharField(max_length=100)            # Acting consistently with societal values
    pillarvals_2 = models.CharField(max_length=100)            # Desire to do the right thing
    pillarvals_3 = models.CharField(max_length=100)            # Actions consistent with society
    pillarvals_4 = models.CharField(max_length=100)            # Willingness to benefit others
    pillarvals_5 = models.CharField(max_length=100)            # Responsibility to contribute to society
    pillarvals_6 = models.CharField(max_length=100)            # Helping others for well-being
    pillarvals_7 = models.CharField(max_length=100)            # Helping others without offending
    pillarvals_8 = models.CharField(max_length=100)            # Knowing how to help people in need
    pillarvals_9 = models.CharField(max_length=100)            # Desire to participate in decision-making
    pillarvals_12 = models.CharField(max_length=100)           # Encouraged to play an active role in society
    pillarvals_13 = models.CharField(max_length=100)           # Ability to create positive change
    pillarvals_14 = models.CharField(max_length=100)           # Feeling of belonging in Singapore
    pillarvals_21 = models.CharField(max_length=100)           # Commonalities with diverse cultures
    pillarvals_22 = models.CharField(max_length=100)           # Benefit of interacting with diverse cultures
    pillarvals_23 = models.CharField(max_length=100)           # Opportunities for meaningful interactions with diverse cultures
    pillarvals_24 = models.CharField(max_length=100)           # Opportunities for meaningful interactions with diverse nationalities
    pillarvals_25 = models.CharField(max_length=100)           # Respect for cultural differences
    pillarvals_26 = models.CharField(max_length=100)           # Wrong to make culturally insensitive remarks
    pillarvals_29 = models.CharField(max_length=100)           # Confidence in Singapore's future
    pillarvals_30 = models.CharField(max_length=100)           # Willing to support Singapore in tough times
    pillarvals_31 = models.CharField(max_length=100)           # Opportunities to achieve aspirations
    pillarvals_32 = models.CharField(max_length=100)           # Opportunities to live by personal values
    pillarvals_33 = models.CharField(max_length=100)           # Commitment to staying in Singapore long-term

    # Online behavior fields
    online_news = models.CharField(max_length=100)            # Check news/current affairs
    online_sm = models.CharField(max_length=100)              # Use social media platforms
    online_shop = models.CharField(max_length=100)            # Shopping behavior
    online_areasinterest = models.CharField(max_length=100)   # Searching for information of interest
    online_games = models.CharField(max_length=100)           # Online gaming behavior
    online_update = models.CharField(max_length=100)          # Updating self-information online
    online_sharemedia = models.CharField(max_length=100)      # Sharing media online
    online_watchmedia = models.CharField(max_length=100)      # Watching videos/movies online

    # Household demographics fields
    marital_stats = models.CharField(max_length=100)          # Current marital status
    children = models.CharField(max_length=100)               # Have children
    age_youngestchild = models.CharField(max_length=100)      # Age of youngest child
    hh_grandparents = models.CharField(max_length=100)        # Live with grandparents
    hh_parents = models.CharField(max_length=100)             # Live with parents
    hh_siblings = models.CharField(max_length=100)            # Live with siblings
    hh_spouse = models.CharField(max_length=100)              # Live with spouse
    hh_children = models.CharField(max_length=100)            # Live with children
    hh_relatives = models.CharField(max_length=100)           # Live with other relatives
    hh_helper = models.CharField(max_length=100)              # Live with domestic helper
    hh_mates = models.CharField(max_length=100)               # Live with friends/housemates
    hh_employer_their_family = models.CharField(max_length=100) # Live with employer's family
    hh_grandchildren = models.CharField(max_length=100)       # Live with grandchildren
    hh_other = models.CharField(max_length=100)               # Live with other arrangements
    hh_none = models.CharField(max_length=100)                # Stay alone

    # Education and occupation fields
    highest_ed = models.CharField(max_length=100)            # Highest attained education level
    institution_deg = models.CharField(max_length=100)       # Conferring institution for degree/post-grad
    occupation = models.CharField(max_length=100)            # Current occupation
    
    # Economic fields
    mhi = models.CharField(max_length=50)                    # Monthly household income
    mpi = models.CharField(max_length=50)                    # Monthly personal income
    weight = models.FloatField()                             # Weight (can also consider using PositiveIntegerField if weight is always a positive integer)

    # Define a string representation for the model
    def __str__(self):
        return f"{self.uid} - {self.gender} - {self.age_2}"