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
                uid=row['uid'],  # Unique respondent ID
                sample=row['sample'],  # Sample type
                gender=row['gender'],  # Gender
                age_2=row['age_2'],  # Age groups
                dwelling=row['dwelling'],  # Dwelling type
                industry=row['industry'],  # Current industry
                
                # Social involvement fields
                social_involve_1=row['social_involve_1'],  # Sports related groups
                social_involve_2=row['social_involve_2'],  # Arts and Cultural groups
                social_involve_3=row['social_involve_3'],  # Community groups
                social_involve_4=row['social_involve_4'],  # Welfare & Self-Help groups
                social_involve_5=row['social_involve_5'],  # Religious groups
                social_involve_6=row['social_involve_6'],  # Interest & Hobby groups
                social_involve_7=row['social_involve_7'],  # Discussion groups
                social_involve_8=row['social_involve_8'],  # Other
                social_involve_9=row['social_involve_9'],  # None of the above

                # Volunteer and donation fields
                volunteerdonate_1=row['volunteerdonate_1'],  # Volunteered time
                volunteerdonate_2=row['volunteerdonate_2'],  # Donated money
                volunteerdonate_3=row['volunteerdonate_3'],  # Donated goods/services
                volunteerdonate_4=row['volunteerdonate_4'],  # Volunteered time for projects
                volunteerdonate_5=row['volunteerdonate_5'],  # Donated blood
                volunteerdonate_6=row['volunteerdonate_6'],  # Worked with fellow citizens
                volunteerdonate_7=row['volunteerdonate_7'],  # Helped a neighbor
                volunteerdonate_8=row['volunteerdonate_8'],  # Other
                volunteerdonate_9=row['volunteerdonate_9'],  # None of the above
                volunteerdonate_freq=row['volunteerdonate_freq'],  # Frequency of volunteering/donating
                volunteerdonate_metd=row['volunteerdonate_metd'],  # Method of volunteering/donating

                # Social networks fields
                snetwork_ethnicity=row['snetwork_ethnicity'],  # Close friends of different ethnicity
                snetwork_nationality=row['snetwork_nationality'],  # Close friends of different nationality
                snetwork_religion=row['snetwork_religion'],  # Close friends of different religion
                snetwork_income=row['snetwork_income'],  # Close friends of different income
                snetwork_education=row['snetwork_education'],  # Close friends of different education
                snetwork_sorientation=row['snetwork_sorientation'],  # Close friends of different sexual orientation
                close_sg_friends=row['close_sg_friends'],  # Have close Singaporean friends

                # Social interaction fields
                sinteract_meal=row['sinteract_meal'],  # Shared a meal with a friend of different ethnicity/nationality
                sinteract_invitedfriend=row['sinteract_invitedfriend'],  # Invited a friend to a celebration
                sinteract_beeninvited=row['sinteract_beeninvited'],  # Been invited by a friend
                sinteract_participated=row['sinteract_participated'],  # Participated in a celebration

                # Support fields
                support_immedfam=row['support_immedfam'],  # Support from immediate family
                support_extfam=row['support_extfam'],  # Support from extended family
                support_worksch=row['support_worksch'],  # Support from workplace/school
                support_friends=row['support_friends'],  # Support from friends

                # Overseas experience fields
                os_exp_1=row['os_exp_1'],  # Studied overseas
                os_exp_2=row['os_exp_2'],  # Worked overseas
                os_exp_3=row['os_exp_3'],  # Stayed overseas for non-work reasons
                os_exp_4=row['os_exp_4'],  # None of the above
                time_os=row['time_os'],  # Time spent living overseas
                study_os=row['study_os'],  # Plans to study overseas
                work_os=row['work_os'],  # Plans to work overseas
                travel_os=row['travel_os'],  # Plans to travel overseas
                migrate_os=row['migrate_os'],  # Plans to migrate overseas
                retire_os=row['retire_os'],  # Plans to retire overseas

                # Outcome connection fields
                outcome_connection=row['outcome_connection'],  # Strength of connection to Singapore
                outcome_future=row['outcome_future'],  # Desire to shape Singapore’s future

                # Behavioral characteristics fields
                pillarbeh_1=row['pillarbeh_1'],  # Considerate behavior in public settings
                pillarbeh_2=row['pillarbeh_2'],  # Helping close friends and family
                pillarbeh_3=row['pillarbeh_3'],  # Helping wider networks
                pillarbeh_4=row['pillarbeh_4'],  # Regularly donating to causes
                pillarbeh_5=row['pillarbeh_5'],  # Regularly volunteering for causes
                pillarbeh_6=row['pillarbeh_6'],  # Offering help without being asked
                pillarbeh_7=row['pillarbeh_7'],  # Giving constructive feedback
                pillarbeh_8=row['pillarbeh_8'],  # Leading or mobilizing for causes
                pillarbeh_9=row['pillarbeh_9'],  # Participating in community initiatives
                pillarbeh_10=row['pillarbeh_10'],  # Getting along with diverse cultures
                pillarbeh_11=row['pillarbeh_11'],  # Avoiding racially-sensitive situations
                pillarbeh_12=row['pillarbeh_12'],  # Easing racially-sensitive situations
                pillarbeh_13=row['pillarbeh_13'],  # Including people from different cultures
                pillarbeh_14=row['pillarbeh_14'],  # Understanding different cultures
                pillarbeh_15=row['pillarbeh_15'],  # Good friends from different cultures

                # Value-based characteristics fields
                pillarvals_1=row['pillarvals_1'],  # Acting in line with societal values
                pillarvals_2=row['pillarvals_2'],  # Desire to do the right thing
                pillarvals_3=row['pillarvals_3'],  # Consistency with societal actions
                pillarvals_4=row['pillarvals_4'],  # Willingness to benefit others
                pillarvals_5=row['pillarvals_5'],  # Responsibility to contribute to society
                pillarvals_6=row['pillarvals_6'],  # Helping others for personal well-being
                pillarvals_7=row['pillarvals_7'],  # Helping others even if it risks offense
                pillarvals_8=row['pillarvals_8'],  # Knowing how to help people in need
                pillarvals_9=row['pillarvals_9'],  # Desire to participate in decision-making
                pillarvals_12=row['pillarvals_12'],  # Encouragement to play an active role
                pillarvals_13=row['pillarvals_13'],  # Confidence in creating positive change
                pillarvals_14=row['pillarvals_14'],  # Feeling of belonging in Singapore
                pillarvals_21=row['pillarvals_21'],  # Commonalities with diverse cultures
                pillarvals_22=row['pillarvals_22'],  # Benefits of interacting with diverse cultures
                pillarvals_23=row['pillarvals_23'],  # Opportunities for meaningful interactions
                pillarvals_24=row['pillarvals_24'],  # Respect for cultural differences
                pillarvals_25=row['pillarvals_25'],  # Concerns about racial insensitivity
                pillarvals_26=row['pillarvals_26'],  # Confidence in Singapore's future
                pillarvals_29=row['pillarvals_29'],  # Willing to support Singapore
                pillarvals_30=row['pillarvals_30'],  # Opportunities to achieve aspirations
                pillarvals_31=row['pillarvals_31'],  # Commitment to staying in Singapore

                # Online behavior fields
                online_news=row['online_news'],  # Check news/current affairs
                online_sm=row['online_sm'],  # Use social media platforms
                online_shop=row['online_shop'],  # Shopping behavior
                online_areasinterest=row['online_areasinterest'],  # Searching for information of interest
                online_games=row['online_games'],  # Online gaming behavior
                online_update=row['online_update'],  # Updating self-information online
                online_sharemedia=row['online_sharemedia'],  # Sharing media online
                online_watchmedia=row['online_watchmedia'],  # Watching videos/movies online

                # Household demographics fields
                marital_stats=row['marital_stats'],  # Current marital status
                children=row['children'],  # Have children
                age_youngestchild=row['age_youngestchild'],  # Age of youngest child
                hh_grandparents=row['hh_grandparents'],  # Live with grandparents
                hh_parents=row['hh_parents'],  # Live with parents
                hh_siblings=row['hh_siblings'],  # Live with siblings
                hh_spouse=row['hh_spouse'],  # Live with spouse
                hh_children=row['hh_children'],  # Live with children
                hh_relatives=row['hh_relatives'],  # Live with other relatives
                hh_helper=row['hh_helper'],  # Live with domestic helper
                hh_mates=row['hh_mates'],  # Live with friends/housemates
                hh_employer_their_family=row['hh_employer_their_family'],  # Live with employer's family
                hh_grandchildren=row['hh_grandchildren'],  # Live with grandchildren
                hh_other=row['hh_other'],  # Live with other arrangements
                hh_none=row['hh_none'],  # Stay alone

                # Education and occupation fields
                highest_ed=row['highest_ed'],  # Highest attained education level
                institution_deg=row['institution_deg'],  # Conferring institution for degree/post-grad
                occupation=row['occupation'],  # Current occupation
                
                # Economic fields
                mhi=row['mhi'],  # Monthly household income
                mpi=row['mpi'],  # Monthly personal income
                weight=row['weight'],  # Weight
            )
            try:
                survey_response.save()
                #print(f"Inserted response for uid: {survey_response.uid}")
            except Exception as e:
                print(f"Error inserting response for uid {row['uid']}: {str(e)}")

if __name__ == '__main__':
    load_data_from_csv()