#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 20:41:30 2022

@author: jpartyka
"""

import os
import sys
import random

from scipy.stats import truncnorm
from censusname import Censusname

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)



team_list = ["New York", "Miami", "Atlanta", "Washington", "Buffalo","Philadelphia",
             "Chicago","Detroit","Green Bay","Pittsburgh","New Orleans","Cincinnati",
             "Minnesota","Dallas","Kansas City","St. Louis","Denver","Houston",
             "San Francisco","Seattle","Oakland","San Diego","Arizona","Las Vegas"]

position_to_player_attribute_list_dict = {"qb":['arm_strength_rating','arm_accuracy_rating','intelligence_rating','speed_rating','elusiveness_rating','stamina_rating',],
                              "rb":['speed_rating','elusiveness_rating','strength_rating','ball_protection_rating','catching_rating','stamina_rating'],
                              "fb":['speed_rating','elusiveness_rating','strength_rating','ball_protection_rating','catching_rating','stamina_rating'],
                              "wr": ['catching_rating','route_rating','jumping_rating','speed_rating','ball_protection_rating','stamina_rating','penalty_avoidance_rating'],
                              "te":['catching_rating','route_rating','speed_rating','ball_protection_rating','strength_rating','stamina_rating','block_power_rating','block_agility_rating'],
                              "k":['leg_rating','accuracy_rating','adjustment_rating','onside_kick_rating','directionality_rating'],
                              "p":['leg_rating','directionality_rating','hangtime_rating','precision_rating','consistency_rating','surehands_rating'],
                              "ol":['block_power_rating','block_agility_rating','penalty_avoidance_rating','fumble_recovery_rating'],
                              "dl":['block_power','block_agility','speed_rating','pass_knockdown_rating','penalty_avoidance_rating','tackle_rating','fumble_inducment_rating','fumble_recovery_rating'],
                              "lb":['speed_rating','route_rating','pass_defense_rating','interception_rating','fumble_inducment_rating','tackle_rating','penalty_avoidance_rating'],
                              "cb":['speed_rating','route_rating','pass_defense_rating','interception_rating','fumble_inducment_rating','tackle_rating','penalty_avoidance_rating'],
                              "sf":['speed_rating','route_rating','pass_defense_rating','interception_rating','fumble_inducment_rating','tackle_rating','penalty_avoidance_rating'],
                              "sto":['speed_rating','elusiveness_rating','strength_rating','ball_protection_rating'],
                              'std':['speed_rating','agility_rating','tackle_rating','fumble_inducment_rating']}

player_position_list = list(position_to_player_attribute_list_dict.keys())

fbs_school_list = ['Abilene Christian University', 'Appalachian State University', 'Arizona State University', 'Arkansas State University', 'Auburn University', 'Ball State University', 'Baylor University', 'Boise State University', 'Boston College', 'Bowling Green State University', 'Brigham Young University', 'California State University – Fresno', 'Central Michigan University', 'Clemson University', 'Coastal Carolina University', 'Colorado State University', 'Duke University', 'East Carolina University', 'Eastern Michigan University', 'Florida Atlantic University', 'Florida International University', 'Florida State University', 'Georgia Southern University', 'Georgia State University', 'Georgia Tech', 'Indiana University', 'Iowa State University', 'Kansas State University', 'Kent State University', 'Liberty University', 'Louisiana State University (LSU)', 'Louisiana Tech University', 'Marshall University', 'Miami University', 'Michigan State University', 'Middle Tennessee State University', 'Mississippi State University', 'New Mexico State University', 'North Carolina State University', 'Northern Illinois University', 'Northwestern University', 'Ohio State University', 'Ohio University', 'Oklahoma State University', 'Old Dominion University', 'Oregon State University', 'Penn State', 'Purdue University', 'Rice University', 'Rutgers University', 'San Diego State University', 'San Jose State University', 'Southern Methodist University – SMU', 'Stanford University', 'SUNY University at Buffalo', 'Syracuse University', 'Temple University', 'Texas A&M University', 'Texas Christian University', 'Texas State University', 'Texas Tech University', 'Troy University', 'Tulane University', 'United States Air Force Academy', 'United States Military Academy', 'United States Naval Academy', 'University of Akron', 'University of Alabama', 'University of Alabama – Birmingham', 'University of Arizona', 'University of Arkansas', 'University of California – Berkeley', 'University of California – Los Angeles – UCLA', 'University of Central Florida', 'University of Cincinnati', 'University of Colorado – Boulder', 'University of Connecticut', 'University of Florida', 'University of Georgia', 'University of Hawaii at Manoa', 'University of Houston', 'University of Illinois', 'University of Iowa', 'University of Kansas', 'University of Kentucky', 'University of Louisiana', 'University of Louisiana – Monroe', 'University of Louisville', 'University of Maryland', 'University of Massachusetts – Amherst', 'University of Memphis', 'University of Miami', 'University of Michigan', 'University of Minnesota', 'University of Mississippi', 'University of Missouri', 'University of Nebraska', 'University of Nevada – Las Vegas', 'University of Nevada – Reno', 'University of New Mexico', 'University of North Carolina at Chapel Hill', 'University of North Carolina at Charlotte', 'University of North Texas', 'University of Notre Dame', 'University of Oklahoma', 'University of Oregon', 'University of Pittsburgh', 'University of South Alabama', 'University of South Carolina', 'University of South Florida', 'University of Southern California', 'University of Southern Mississippi', 'University of Tennessee', 'University of Texas – Austin', 'University of Texas – El Paso', 'University of Texas – San Antonio', 'University of Toledo', 'University of Tulsa', 'University of Utah', 'University of Virginia', 'University of Washington', 'University of Wisconsin', 'University of Wyoming', 'Utah State University', 'Vanderbilt University', 'Virginia Tech', 'Wake Forest University', 'Washington State University', 'West Virginia University', 'Western Kentucky University', 'Western Michigan University']
fcs_school_list = ['Alabama A&M University', 'Alabama State University', 'Alcorn State University', 'Austin Peay State University', 'Bethune-Cookman University', 'Brown University', 'Bryant University', 'Bucknell University', 'Butler University', 'California Polytechnic State University – San Luis Obispo', 'California State University – Sacramento', 'Campbell University', 'Central Connecticut State University', 'Charleston Southern University', 'Colgate University', 'College of the Holy Cross', 'Columbia University', 'Cornell University', 'Dartmouth College', 'Davidson College', 'Delaware State University', 'Dixie State University', 'Drake University', 'Duquesne University', 'East Tennessee State University', 'Eastern Illinois University', 'Eastern Kentucky University', 'Eastern Washington University', 'Elon University', 'Florida A&M University', 'Fordham University', 'Furman University', 'Gardner-Webb University', 'Georgetown University', 'Grambling State University', 'Hampton University', 'Harvard University', 'Houston Baptist University', 'Howard University', 'Idaho State University', 'Illinois State University', 'Indiana State University', 'Jackson State University', 'Jacksonville State University', 'James Madison University', 'Kennesaw State University', 'Lafayette College', 'Lamar University', 'Lehigh University', 'Long Island University', 'Marist College', 'McNeese State University', 'Mercer University', 'Merrimack College', 'Mississippi Valley State University', 'Missouri State University', 'Monmouth University', 'Montana State University', 'Morehead State University', 'Morgan State University', 'Murray State University', 'Nicholls State University', 'Norfolk State University', 'North Carolina A&T State University', 'North Carolina Central University', 'North Dakota State University', 'Northern Arizona University', 'Northwestern State University of Louisiana', 'Portland State University', 'Prairie View A & M University', 'Presbyterian College', 'Princeton University', 'Robert Morris University – Pennsylvania', 'Sacred Heart University', 'Saint Francis University', 'Sam Houston State University', 'Samford University', 'South Carolina State University', 'South Dakota State University', 'Southeast Missouri State University', 'Southeastern Louisiana University', 'Southern Illinois University Carbondale', 'Southern University & A&M College', 'Southern Utah University', 'Stephen F Austin State University', 'Stetson University', 'SUNY Stony Brook University', 'SUNY University at Albany', 'Tarleton State University', 'Tennessee State University', 'Tennessee Technological University', 'Texas Southern University', 'The Citadel', 'Towson University', 'University of Arkansas at Pine Bluff', 'University of California – Davis', 'University of Central Arkansas', 'University of Dayton', 'University of Delaware', 'University of Idaho', 'University of Maine', 'University of Montana', 'University of New Hampshire', 'University of North Alabama', 'University of North Dakota', 'University of Northern Colorado', 'University of Northern Iowa', 'University of Pennsylvania – Penn', 'University of Rhode Island', 'University of Richmond', 'University of San Diego', 'University of South Dakota', 'University of St. Thomas – Minnesota', 'University of Tennessee – Chattanooga', 'University of Tennessee – Martin', 'University of the Incarnate Word', 'Valparaiso University', 'Villanova University', 'Virginia Military Institute – VMI', 'Wagner College', 'Weber State University', 'Western Carolina University', 'Western Illinois University', 'William & Mary', 'Wofford College', 'Yale University', 'Youngstown State University']
d2_school_list = ['Adams State University', 'Albany State University', 'Alderson Broaddus University', 'Allen University', 'American International College', 'Anderson University – South Carolina', 'Angelo State University', 'Arkansas Tech University', 'Ashland University', 'Assumption University', 'Augustana University – South Dakota', 'Barton College', 'Bemidji State University', 'Benedict College', 'Bentley University', 'Black Hills State University', 'Bloomsburg University of Pennsylvania', 'Bluefield State College', 'Bowie State University', 'California University of Pennsylvania', 'Carson-Newman University', 'Catawba College', 'Central State University', 'Central Washington University', 'Chadron State College', 'Chowan University', 'Clarion University of Pennsylvania', 'Clark Atlanta University', 'Colorado Mesa University', 'Colorado School of Mines', 'Colorado State University – Pueblo', 'Concord University', 'Concordia University, St. Paul – Minnesota', 'Davenport University', 'Delta State University', 'East Central University', 'East Stroudsburg University of Pennsylvania', 'Eastern New Mexico University', 'Edinboro University', 'Edward Waters University', 'Elizabeth City State University', 'Emporia State University', 'Erskine College', 'Fairmont State University', 'Fayetteville State University', 'Ferris State University', 'Fort Hays State University', 'Fort Lewis College', 'Fort Valley State University', 'Franklin Pierce University', 'Frostburg State University', 'Gannon University', 'Glenville State College', 'Grand Valley State University', 'Harding University', 'Henderson State University', 'Hillsdale College', 'Indiana University of Pennsylvania', 'Johnson C. Smith University', 'Kentucky State University', 'Kentucky Wesleyan College', 'Kutztown University of Pennsylvania', 'Lake Erie College', 'Lane College', 'Lenoir-Rhyne University', 'Limestone University', 'Lincoln University – Missouri', 'Lincoln University Pennsylvania', 'Lindenwood University', 'Livingstone College', 'Lock Haven University', 'Mars Hill University', 'McKendree University', 'Mercyhurst University', 'Michigan Technological University', 'Midwestern State University', 'Miles College', 'Millersville University of Pennsylvania', 'Minnesota State University – Mankato', 'Minnesota State University – Moorhead', 'Minot State University', 'Mississippi College', 'Missouri Southern State University', 'Missouri University of Science & Technology', 'Missouri Western State University', 'Morehouse College', 'New Mexico Highlands University', 'Newberry College', 'North Greenville University', 'Northeastern State University', 'Northern Michigan University', 'Northern State University', 'Northwest Missouri State University', 'Northwestern Oklahoma State University', 'Northwood University – Michigan', 'Notre Dame College', 'Ohio Dominican University', 'Oklahoma Baptist University', 'Ouachita Baptist University', 'Pace University', 'Pittsburg State University', 'Post University', 'Quincy University', 'Saginaw Valley State University', 'Saint Anselm College', "Saint Augustine's University", 'Savannah State University', 'Seton Hill University', 'Shaw University', 'Shepherd University', 'Shippensburg University of Pennsylvania', 'Shorter University', 'Slippery Rock University', 'South Dakota Mines', 'Southeastern Oklahoma State University', 'Southern Arkansas University', 'Southern Connecticut State University', 'Southern Nazarene University', 'Southwest Baptist University', 'Southwest Minnesota State University', 'Southwestern Oklahoma State University', 'Stonehill College', 'Texas A&M University – Commerce', 'Texas A&M University – Kingsville', "The University of Virginia's College at Wise", 'Tiffin University', 'Truman State University', 'Tusculum University', 'Tuskegee University', 'University of Arkansas at Monticello', 'University of Central Missouri', 'University of Central Oklahoma', 'University of Charleston', 'University of Findlay', 'University of Indianapolis', 'University of Mary', 'University of Minnesota – Duluth', 'University of Nebraska at Kearney', 'University of New Haven', 'University of North Carolina at Pembroke', 'University of Sioux Falls', 'University of Texas – Permian Basin', 'University of West Alabama', 'University of West Florida', 'University of West Georgia', 'Upper Iowa University', 'Valdosta State University', 'Virginia State University', 'Virginia Union University', 'Walsh University', 'Washburn University', 'Wayne State College', 'Wayne State University', 'West Chester University of Pennsylvania', 'West Liberty University', 'West Texas A&M University', 'West Virginia State University', 'West Virginia Wesleyan College', 'Western Colorado University', 'Western New Mexico University', 'Western Oregon University', 'Wheeling University', 'William Jewell College', 'Wingate University', 'Winona State University', 'Winston-Salem State University']
d3_school_list = ['Adrian College', 'Albion College', 'Albright College', 'Alfred University', 'Allegheny College', 'Alma College', 'Alvernia University', 'Amherst College', 'Anderson University – Indiana', 'Anna Maria College', 'Augsburg University', 'Augustana College – Illinois', 'Aurora University', 'Austin College', 'Averett University', 'Baldwin Wallace University', 'Bates College', 'Belhaven University', 'Beloit College', 'Benedictine University', 'Berry College', 'Bethany College – West Virginia', 'Bethel University – Minnesota', 'Birmingham-Southern College', 'Bluffton University', 'Bowdoin College', 'Brevard College', 'Bridgewater College', 'Bridgewater State University', 'Buena Vista University', 'California Lutheran University', 'Capital University', 'Carleton College', 'Carnegie Mellon University', 'Carroll University', 'Carthage College', 'Case Western Reserve University', 'Castleton University', 'Catholic University of America', 'Central College', 'Centre College', 'Chapman University', 'Christopher Newport University', 'Claremont-Mudd-Scripps Colleges', 'Coe College', 'Colby College', 'College of Wooster', 'Concordia College – Minnesota', 'Concordia University – Chicago', 'Concordia University Wisconsin', 'Cornell College', 'Crown College', 'Curry College', 'Dean College', 'Defiance College', 'Delaware Valley University', 'Denison University', 'DePauw University', 'Dickinson College', 'East Texas Baptist University', 'Elmhurst University', 'Endicott College', 'Eureka College', 'Fairleigh Dickinson University – College at Florham', 'Ferrum College', 'Finlandia University', 'Fitchburg State University', 'Framingham State University', 'Franklin & Marshall College', 'Franklin College', 'Gallaudet University', 'Geneva College', 'George Fox University', 'Gettysburg College', 'Greensboro College', 'Greenville University', 'Grinnell College', 'Grove City College', 'Guilford College', 'Gustavus Adolphus College', 'Hamilton College', 'Hamline University', 'Hampden-Sydney College', 'Hanover College', 'Hardin-Simmons University', 'Hartwick College', 'Heidelberg University', 'Hendrix College', 'Hilbert College', 'Hiram College', 'Hobart & William Smith College', 'Hope College', 'Howard Payne University', 'Huntingdon College', 'Husson University', 'Illinois College', 'Illinois Wesleyan University', 'Ithaca College', 'John Carroll University', 'Johns Hopkins University', 'Juniata College', 'Kalamazoo College', 'Kean University', 'Kenyon College', 'Keystone College', "King's College – Pennsylvania", 'Knox College', 'LaGrange College', 'Lake Forest College', 'Lakeland University', 'Lawrence University', 'Lebanon Valley College', 'Lewis & Clark College', 'Linfield University', 'Loras College', 'Luther College', 'Lycoming College', 'Macalester College', 'Manchester University', 'Marietta College', 'Martin Luther College', 'Maryville College', 'Massachusetts Institute of Technology – MIT', 'McDaniel College', 'McMurry University', 'Methodist University', 'Middlebury College', 'Millikin University', 'Millsaps College', 'Misericordia University', 'Monmouth College', 'Montclair State University', 'Moravian University', 'Mount St. Joseph University', 'Muhlenberg College', 'Muskingum University', 'Nebraska Wesleyan University', 'Nichols College', 'North Carolina Wesleyan College', 'North Central College', 'North Park University', 'Norwich University', 'Oberlin College', 'Ohio Northern University', 'Ohio Wesleyan University', 'Olivet College', 'Otterbein University', 'Pacific Lutheran University', 'Pacific University', 'Plymouth State University', 'Pomona-Pitzer Colleges', 'Randolph-Macon College', 'Rensselaer Polytechnic Institute – RPI', 'Rhodes College', 'Ripon College', 'Rockford University', 'Rose-Hulman Institute of Technology', 'Rowan University', "Saint John's University – Minnesota", 'Saint Vincent College – Pennsylvania', 'Salisbury University', 'Salve Regina University', 'Sewanee – The University of the South', 'Shenandoah University', 'Simpson College', 'Southern Virginia University', 'Southwestern University', 'Springfield College', 'St. John Fisher College', 'St. Lawrence University', 'St. Norbert College', 'St. Olaf College', 'Stevenson University', 'Sul Ross State University', 'SUNY Buffalo State College', 'SUNY College at Brockport', 'SUNY Cortland', 'SUNY Maritime College', 'SUNY Morrisville', 'Susquehanna University', 'Texas Lutheran University', 'The College of New Jersey', 'The College of St. Scholastica', 'Thiel College', 'Trine University', 'Trinity College – Connecticut', 'Trinity University – Texas', 'Tufts University', 'Union College – New York', 'United States Coast Guard Academy', 'United States Merchant Marine Academy', 'University of Chicago', 'University of Dubuque', 'University of La Verne', 'University of Mary Hardin-Baylor', 'University of Massachusetts – Dartmouth', 'University of Minnesota – Morris', 'University of Mount Union', 'University of New England', 'University of Northwestern – St. Paul', 'University of Puget Sound', 'University of Redlands', 'University of Rochester', 'University of Wisconsin – Eau Claire', 'University of Wisconsin – La Crosse', 'University of Wisconsin – Oshkosh', 'University of Wisconsin – Platteville', 'University of Wisconsin – River Falls', 'University of Wisconsin – Stevens Point', 'University of Wisconsin – Stout', 'University of Wisconsin – Whitewater', 'Ursinus College', 'Utica College', 'Wabash College', 'Wartburg College', 'Washington & Jefferson College', 'Washington & Lee University', 'Washington University in St. Louis', 'Waynesburg University', 'Wesleyan University', 'Western Connecticut State University', 'Western New England University', 'Westfield State University', 'Westminster College – Missouri', 'Westminster College – Pennsylvania', 'Wheaton College – Illinois', 'Whittier College', 'Whitworth University', 'Widener University', 'Wilkes University', 'Willamette University', 'William Paterson University of New Jersey', 'Williams College', 'Wilmington College', 'Wittenberg University', 'Worcester Polytechnic Institute', 'Worcester State University']


#player ability normal distribution for most players and abilities
player_ability_norm_dist_obj = get_truncated_normal(mean=80, sd=6.7, low=50, upp=100)

#distributions used for fb speed, elusiveness and strength
fb_speed_elusiveness_norm_dist_obj = get_truncated_normal(mean=65, sd=6.7, low=50, upp=85)
fb_strength_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

#distributions used for te - speed is slower, strength and block power are higher than average
te_speed_norm_dist_obj = get_truncated_normal(mean=65, sd=6.7, low=50, upp=85)
te_strength_bpwr_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

#distribution used for wr - speed is higher than normal
wr_speed_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

#distribution used for sf - speed is higher than normal
sf_speed_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

#distribution used for lb - tackle_rating is higher than normal
lb_tackle_norm_dist_obj = get_truncated_normal(mean=85, sd=6.7, low=70, upp=100)

#age normal distribution for punters and kickers
pk_age_norm_dist_obj = get_truncated_normal(mean=35, sd=6.7, low=19, upp=50)

#age normal distribution for running backs
rb_age_norm_dist_obj = get_truncated_normal(mean=27, sd=6.7, low=19, upp=40)

#age normal distribution for all other player positions
otherpos_age_norm_dist_obj = get_truncated_normal(mean=30, sd=6.7, low=19, upp=46)

#height dists
six_feet_tall_inches_norm_dist_obj = get_truncated_normal(mean=3, sd=3, low=0, upp=11)
five_feet_tall_inches_norm_dist_obj = get_truncated_normal(mean=10, sd=3, low=5, upp=11)

C = Censusname()

player_name_to_info_dict_dict = {}
player_position_to_name_list_dict = {}

player_name_to_combined_attr_score_dict = {}

team_to_player_list_dict = {}

#create list of player positions that will represent the number of players to create for each team (55)
roster_position_count_list = []
roster_position_count_qb_list = ["qb"] * 2
roster_position_count_rb_list = ["rb"] * 2
roster_position_count_te_list = ["te"] * 2
roster_position_count_fb_list = ["fb"] * 1
roster_position_count_wr_list = ["wr"] * 3
roster_position_count_ol_list = ["ol"] * 8
roster_position_count_k_list = ["k"] * 1
roster_position_count_p_list = ["p"] * 1
roster_position_count_dl_list = ["dl"] * 8
roster_position_count_lb_list = ["lb"] * 3
roster_position_count_cb_list = ["cb"] * 3
roster_position_count_sf_list = ["sf"] * 3

roster_position_count_list = roster_position_count_qb_list + roster_position_count_rb_list + roster_position_count_te_list + roster_position_count_fb_list + \
                             roster_position_count_wr_list + roster_position_count_ol_list + roster_position_count_k_list + roster_position_count_p_list + \
                             roster_position_count_dl_list + roster_position_count_lb_list + roster_position_count_cb_list + roster_position_count_sf_list

for this_team in team_list:
    
    team_to_player_list_dict[this_team] = []
    
    for player_position in roster_position_count_list:
        
        player_name_uniqueness_verified = False
        
        #age is dependent on the player_position
        player_age = -1
        
        if player_position in ['p','k']:
            player_age = round(float(pk_age_norm_dist_obj.rvs()))
        elif player_position == 'rb':
            player_age = round(float(rb_age_norm_dist_obj.rvs()))
        else:
            player_age = round(float(otherpos_age_norm_dist_obj.rvs()))
        
        #height in inches is determined via a normal dist
        
        height_feet = -1
        height_inches = -1

        height_feet_random_value = random.randint(0,9)
        
        if height_feet_random_value <= 7:
            height_feet = 6
            height_inches = round(float(six_feet_tall_inches_norm_dist_obj.rvs()))
        else:
            height_feet = 5
            height_inches = round(float(five_feet_tall_inches_norm_dist_obj.rvs()))
        
        #weight in lbs is position dependent - ols and dls have one dist, everyone else has another
        #it is also height dependent - the taller the player, the more the player is likely to weigh
        
        mean_lb_weight = -1
        low_lb_weight = -1
        high_lb_weight = -1
        mean_nlb_weight = -1
        low_nlb_weight = -1
        high_nlb_weight = -1
        
        if height_feet == 5 and height_inches <= 8:
            mean_lb_weight = 225
            low_lb_weight = 200
            high_lb_weight = 250
            mean_nlb_weight = 160
            low_nlb_weight = 140
            high_nlb_weight = 180
        elif height_feet == 5 and height_inches > 8:
            mean_lb_weight = 265
            low_lb_weight = 235
            high_lb_weight = 285
            mean_nlb_weight = 190
            low_nlb_weight = 170
            high_nlb_weight = 210
        elif height_feet == 6 and height_inches <= 6:
            mean_lb_weight = 300
            low_lb_weight = 275
            high_lb_weight = 325
            mean_nlb_weight = 220
            low_nlb_weight = 190
            high_nlb_weight = 250
        elif height_feet == 6 and height_inches > 6:
            mean_lb_weight = 340
            low_lb_weight = 315
            high_lb_weight = 365
            mean_nlb_weight = 275
            low_nlb_weight = 250
            high_nlb_weight = 300
        
        linebacker_weight_norm_dist_obj = get_truncated_normal(mean=mean_lb_weight, sd=20, low=low_lb_weight, upp=high_lb_weight)
        non_linebacker_weight_norm_dist_obj = get_truncated_normal(mean=mean_nlb_weight, sd=25, low=low_nlb_weight, upp=high_nlb_weight)
        
        weight_lbs = -1
        
        if player_position in ['dl','ol']:
            weight_lbs = round(linebacker_weight_norm_dist_obj.rvs())
        else:
            weight_lbs = round(non_linebacker_weight_norm_dist_obj.rvs())
        
        while player_name_uniqueness_verified == False:
        
            gender_value = random.randint(0, 1)

            if gender_value == 0:
                given_gender = "male"
            else:
                given_gender = "female"

            #let's say that 1 out of every 50 players uses a middle initial
            using_middle_initial_value = random.randint(0, 49)

            if using_middle_initial_value == 25:
                middle_initial_letter_idx = random.randint(0, 25)
                middle_initial = chr(ord('A') + middle_initial_letter_idx) + ". "
            else:
                middle_initial = "" 

            player_name = C.generate(nameformat='{given} ' + middle_initial + '{surname}', given=given_gender)
        
            if player_name not in list(player_name_to_info_dict_dict.keys()):
                player_name_uniqueness_verified = True
        
        #alma mater
        school_random_value = random.randint(0, 99)
        fbs_random_value = random.randint(0, len(fbs_school_list) - 1)
        fcs_random_value = random.randint(0, len(fcs_school_list) - 1)
        d2_random_value = random.randint(0, len(d2_school_list) - 1)
        d3_random_value = random.randint(0, len(d3_school_list) - 1)
        
        school_name = ""
        school_value = -1
        
        if school_value <= 74:
            school_name = fbs_school_list[fbs_random_value]
        elif school_value > 74 and school_value <= 92:
            school_name = fcs_school_list[fcs_random_value]
        elif school_value > 92 and school_value < 99:
            school_name = d2_school_list[d2_random_value]
        else:
            school_name = d3_school_list[d3_random_value]
   

        this_player_attribute_list = position_to_player_attribute_list_dict[player_position]
        this_player_attribute_value_dict = {}
        
        player_name_to_combined_attr_score_dict[player_name] = -1
        
        for this_attribute in this_player_attribute_list:
            
            #check for customized distributions
            if player_position == "fb" and this_attribute in ['speed_rating','elusiveness_rating']:
                this_player_attribute_value_dict[this_attribute] = round(float(fb_speed_elusiveness_norm_dist_obj.rvs()), 2)
            elif player_position == "fb" and this_attribute == 'strength_rating':
                this_player_attribute_value_dict[this_attribute] = round(float(fb_strength_norm_dist_obj.rvs()), 2)
            elif player_position == "te" and this_attribute == 'speed_rating':
                this_player_attribute_value_dict[this_attribute] = round(float(te_speed_norm_dist_obj.rvs()), 2)
            elif player_position == "te" and this_attribute in ['strength_rating', 'block_power_rating']:
                this_player_attribute_value_dict[this_attribute] = round(float(te_strength_bpwr_dist_obj.rvs()), 2)
            elif player_position == "wr" and this_attribute == "speed_rating":
                this_player_attribute_value_dict[this_attribute] = round(float(wr_speed_norm_dist_obj.rvs()), 2)
            elif player_position == "sf" and this_attribute == "speed_rating":
                this_player_attribute_value_dict[this_attribute] = round(float(sf_speed_norm_dist_obj.rvs()), 2)
            elif player_position == "sf" and this_attribute == "tackle_rating":
                this_player_attribute_value_dict[this_attribute] = round(float(lb_tackle_norm_dist_obj.rvs()), 2)
            else:
                this_player_attribute_value_dict[this_attribute] = round(float(player_ability_norm_dist_obj.rvs()), 2)
        
            player_name_to_combined_attr_score_dict[player_name] += this_player_attribute_value_dict[this_attribute]
        
        player_name_to_combined_attr_score_dict[player_name] = player_name_to_combined_attr_score_dict[player_name] / len(this_player_attribute_list)
        
        player_name_to_info_dict_dict[player_name] = {}
        player_name_to_info_dict_dict[player_name]["player_name"] = player_name
        player_name_to_info_dict_dict[player_name]["age"] = player_age
        player_name_to_info_dict_dict[player_name]["position"] = player_position
        player_name_to_info_dict_dict[player_name]["height"] = str(height_feet) + "'" + str(height_inches)
        player_name_to_info_dict_dict[player_name]["weight"] = str(weight_lbs) + " pounds"
        player_name_to_info_dict_dict[player_name]["school"] = school_name
        player_name_to_info_dict_dict[player_name]["attributes"] = this_player_attribute_value_dict
        player_name_to_info_dict_dict[player_name]["team"] = this_team
        
        if player_position not in player_position_to_name_list_dict:
            player_position_to_name_list_dict[player_position] = []
        
        player_position_to_name_list_dict[player_position].append(player_name)
        
        team_to_player_list_dict[this_team].append(player_name)
        

best_player_name = max(player_name_to_combined_attr_score_dict, key=player_name_to_combined_attr_score_dict.get)

print("The best player in the league is: " + best_player_name)
print("***************")
print(player_name_to_info_dict_dict[best_player_name])
        
    #print("------------------------------------")

#print(len(player_name_to_info_dict_dict.keys()))

#print(team_to_player_list_dict)

#ny_player_names_list = team_to_player_list_dict["New York"]
#print(ny_player_names_list)

#for this_player_name in ny_player_names_list:
#    this_player_info_list = player_name_to_info_dict_dict[this_player_name]
#    print(this_player_info_list)
#    print('------------------------')

#qb_list = player_position_to_name_list_dict["qb"]

#for this_qb_name in qb_list:
#    print(player_name_to_info_dict_dict[this_qb_name])

