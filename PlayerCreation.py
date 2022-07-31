# coding: utf-8

from scipy.stats import truncnorm
import random
import names
import copy

from jpartyfb.models import *
from AssortedEnums import PlayingStatus

class PlayerCreation():

    def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
        return truncnorm(
            (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

    position_to_player_attribute_list_dict = {
        "qb": ['arm_strength_rating', 'arm_accuracy_rating', 'intelligence_rating', 'speed_rating',
               'elusiveness_rating', 'stamina_rating'],
        "rb": ['speed_rating', 'elusiveness_rating', 'strength_rating', 'ball_protection_rating', 'catching_rating',
               'stamina_rating'],
        "fb": ['speed_rating', 'elusiveness_rating', 'strength_rating', 'ball_protection_rating', 'catching_rating',
               'stamina_rating'],
        "wr": ['catching_rating', 'route_rating', 'jumping_rating', 'speed_rating', 'ball_protection_rating',
               'stamina_rating', 'penalty_avoidance_rating'],
        "te": ['catching_rating', 'route_rating', 'speed_rating', 'ball_protection_rating', 'strength_rating',
               'stamina_rating', 'block_power_rating', 'block_agility_rating'],
        "k": ['leg_rating', 'accuracy_rating', 'adjustment_rating', 'onside_kick_rating', 'directionality_rating'],
        "p": ['leg_rating', 'directionality_rating', 'hangtime_rating', 'precision_rating', 'consistency_rating',
              'surehands_rating'],
        "ol": ['block_power_rating', 'block_agility_rating', 'penalty_avoidance_rating', 'fumble_recovery_rating'],
        "dl": ['block_power_rating', 'block_agility_rating', 'speed_rating', 'pass_knockdown_rating', 'penalty_avoidance_rating',
               'tackle_rating', 'fumble_inducement_rating', 'fumble_recovery_rating'],
        "lb": ['speed_rating', 'route_rating', 'pass_defense_rating', 'interception_rating', 'fumble_inducement_rating',
               'tackle_rating', 'penalty_avoidance_rating'],
        "cb": ['speed_rating', 'route_rating', 'pass_defense_rating', 'interception_rating', 'fumble_inducement_rating',
               'tackle_rating', 'penalty_avoidance_rating'],
        "sf": ['speed_rating', 'route_rating', 'pass_defense_rating', 'interception_rating', 'fumble_inducement_rating',
               'tackle_rating', 'penalty_avoidance_rating'],
        "sto": ['speed_rating', 'elusiveness_rating', 'strength_rating', 'ball_protection_rating'],
        'std': ['speed_rating', 'agility_rating', 'tackle_rating', 'fumble_inducement_rating']}

    player_position_list = list(position_to_player_attribute_list_dict.keys())

    # football numbers
    qb_k_p_number_bounds_list = [1, 19]
    wr_te_number_bounds_list = [80, 89]
    ol_dl_number_bounds_list = [60, 79]
    rb_fb_cb_sf_number_bounds_list = [20, 49]
    lb_number_bounds_list = [90, 99]
    sto_std_number_bounds_list = [50, 59]

    position_to_number_bounds_list_dict = {"qb": qb_k_p_number_bounds_list, "rb": rb_fb_cb_sf_number_bounds_list,
                                           "fb": rb_fb_cb_sf_number_bounds_list,
                                           "wr": wr_te_number_bounds_list, "te": wr_te_number_bounds_list,
                                           "k": qb_k_p_number_bounds_list, "p": qb_k_p_number_bounds_list,
                                           "ol": ol_dl_number_bounds_list, "dl": ol_dl_number_bounds_list,
                                           "lb": lb_number_bounds_list, "cb": rb_fb_cb_sf_number_bounds_list,
                                           "sf": rb_fb_cb_sf_number_bounds_list, "sto": sto_std_number_bounds_list,
                                           "std": sto_std_number_bounds_list}

    #alma mater
    fbs_school_list = ['Abilene Christian University', 'Appalachian State University', 'Arizona State University',
                       'Arkansas State University', 'Auburn University', 'Ball State University', 'Baylor University',
                       'Boise State University', 'Boston College', 'Bowling Green State University',
                       'Brigham Young University', 'California State University at Fresno',
                       'Central Michigan University', 'Clemson University', 'Coastal Carolina University',
                       'Colorado State University', 'Duke University', 'East Carolina University',
                       'Eastern Michigan University', 'Florida Atlantic University', 'Florida International University',
                       'Florida State University', 'Georgia Southern University', 'Georgia State University',
                       'Georgia Tech', 'Indiana University', 'Iowa State University', 'Kansas State University',
                       'Kent State University', 'Liberty University', 'Louisiana State University (LSU)',
                       'Louisiana Tech University', 'Marshall University', 'Miami University',
                       'Michigan State University', 'Middle Tennessee State University', 'Mississippi State University',
                       'New Mexico State University', 'North Carolina State University', 'Northern Illinois University',
                       'Northwestern University', 'Ohio State University', 'Ohio University',
                       'Oklahoma State University', 'Old Dominion University', 'Oregon State University', 'Penn State',
                       'Purdue University', 'Rice University', 'Rutgers University', 'San Diego State University',
                       'San Jose State University', 'Southern Methodist University', 'Stanford University',
                       'SUNY University at Buffalo', 'Syracuse University', 'Temple University', 'Texas A&M University',
                       'Texas Christian University', 'Texas State University', 'Texas Tech University',
                       'Troy University', 'Tulane University', 'United States Air Force Academy',
                       'United States Military Academy', 'United States Naval Academy', 'University of Akron',
                       'University of Alabama', 'University of Alabama at Birmingham', 'University of Arizona',
                       'University of Arkansas', 'University of California at Berkeley',
                       'University of California at Los Angeles', 'University of Central Florida',
                       'University of Cincinnati', 'University of Colorado', 'University of Connecticut',
                       'University of Florida', 'University of Georgia', 'University of Hawaii at Manoa',
                       'University of Houston', 'University of Illinois', 'University of Iowa', 'University of Kansas',
                       'University of Kentucky', 'University of Louisiana', 'University of Louisiana at Monroe',
                       'University of Louisville', 'University of Maryland', 'University of Massachusetts at Amherst',
                       'University of Memphis', 'University of Miami', 'University of Michigan',
                       'University of Minnesota', 'University of Mississippi', 'University of Missouri',
                       'University of Nebraska', 'University of Nevada at Las Vegas', 'University of Nevada at Reno',
                       'University of New Mexico', 'University of North Carolina at Chapel Hill',
                       'University of North Carolina at Charlotte', 'University of North Texas',
                       'University of Notre Dame', 'University of Oklahoma', 'University of Oregon',
                       'University of Pittsburgh', 'University of South Alabama', 'University of South Carolina',
                       'University of South Florida', 'University of Southern California',
                       'University of Southern Mississippi', 'University of Tennessee', 'University of Texas at Austin',
                       'University of Texas at El Paso', 'University of Texas at San Antonio', 'University of Toledo',
                       'University of Tulsa', 'University of Utah', 'University of Virginia',
                       'University of Washington', 'University of Wisconsin', 'University of Wyoming',
                       'Utah State University', 'Vanderbilt University', 'Virginia Tech', 'Wake Forest University',
                       'Washington State University', 'West Virginia University', 'Western Kentucky University',
                       'Western Michigan University']

    fcs_school_list = ['Alabama A&M University', 'Alabama State University', 'Alcorn State University',
                       'Austin Peay State University', 'Bethune-Cookman University', 'Brown University',
                       'Bryant University', 'Bucknell University', 'Butler University',
                       'California Polytechnic State University at San Luis Obispo',
                       'California State University at Sacramento', 'Campbell University',
                       'Central Connecticut State University', 'Charleston Southern University', 'Colgate University',
                       'College of the Holy Cross', 'Columbia University', 'Cornell University', 'Dartmouth College',
                       'Davidson College', 'Delaware State University', 'Dixie State University', 'Drake University',
                       'Duquesne University', 'East Tennessee State University', 'Eastern Illinois University',
                       'Eastern Kentucky University', 'Eastern Washington University', 'Elon University',
                       'Florida A&M University', 'Fordham University', 'Furman University', 'Gardner-Webb University',
                       'Georgetown University', 'Grambling State University', 'Hampton University',
                       'Harvard University', 'Houston Baptist University', 'Howard University',
                       'Idaho State University', 'Illinois State University', 'Indiana State University',
                       'Jackson State University', 'Jacksonville State University', 'James Madison University',
                       'Kennesaw State University', 'Lafayette College', 'Lamar University', 'Lehigh University',
                       'Long Island University', 'Marist College', 'McNeese State University', 'Mercer University',
                       'Merrimack College', 'Mississippi Valley State University', 'Missouri State University',
                       'Monmouth University', 'Montana State University', 'Morehead State University',
                       'Morgan State University', 'Murray State University', 'Nicholls State University',
                       'Norfolk State University', 'North Carolina A&T State University',
                       'North Carolina Central University', 'North Dakota State University',
                       'Northern Arizona University', 'Northwestern State University of Louisiana',
                       'Portland State University', 'Prairie View A & M University', 'Presbyterian College',
                       'Princeton University', 'Robert Morris University at Pennsylvania', 'Sacred Heart University',
                       'Saint Francis University', 'Sam Houston State University', 'Samford University',
                       'South Carolina State University', 'South Dakota State University',
                       'Southeast Missouri State University', 'Southeastern Louisiana University',
                       'Southern Illinois University Carbondale', 'Southern University & A&M College',
                       'Southern Utah University', 'Stephen F Austin State University', 'Stetson University',
                       'SUNY Stony Brook University', 'SUNY University at Albany', 'Tarleton State University',
                       'Tennessee State University', 'Tennessee Technological University', 'Texas Southern University',
                       'The Citadel', 'Towson University', 'University of Arkansas at Pine Bluff',
                       'University of California at Davis', 'University of Central Arkansas', 'University of Dayton',
                       'University of Delaware', 'University of Idaho', 'University of Maine', 'University of Montana',
                       'University of New Hampshire', 'University of North Alabama', 'University of North Dakota',
                       'University of Northern Colorado', 'University of Northern Iowa',
                       'University of Pennsylvania – Penn', 'University of Rhode Island', 'University of Richmond',
                       'University of San Diego', 'University of South Dakota', 'University of St. Thomas at Minnesota',
                       'University of Tennessee at Chattanooga', 'University of Tennessee at Martin',
                       'University of the Incarnate Word', 'Valparaiso University', 'Villanova University',
                       'Virginia Military Institute', 'Wagner College', 'Weber State University',
                       'Western Carolina University', 'Western Illinois University', 'William & Mary',
                       'Wofford College', 'Yale University', 'Youngstown State University']

    d2_school_list = ['Adams State University', 'Albany State University', 'Alderson Broaddus University',
                      'Allen University', 'American International College', 'Anderson University at South Carolina',
                      'Angelo State University', 'Arkansas Tech University', 'Ashland University',
                      'Assumption University', 'Augustana University at South Dakota', 'Barton College',
                      'Bemidji State University', 'Benedict College', 'Bentley University',
                      'Black Hills State University', 'Bloomsburg University of Pennsylvania',
                      'Bluefield State College', 'Bowie State University', 'California University of Pennsylvania',
                      'Carson-Newman University', 'Catawba College', 'Central State University',
                      'Central Washington University', 'Chadron State College', 'Chowan University',
                      'Clarion University of Pennsylvania', 'Clark Atlanta University', 'Colorado Mesa University',
                      'Colorado School of Mines', 'Colorado State University at Pueblo', 'Concord University',
                      'Concordia University, St. Paul at Minnesota', 'Davenport University', 'Delta State University',
                      'East Central University', 'East Stroudsburg University of Pennsylvania',
                      'Eastern New Mexico University', 'Edinboro University', 'Edward Waters University',
                      'Elizabeth City State University', 'Emporia State University', 'Erskine College',
                      'Fairmont State University', 'Fayetteville State University', 'Ferris State University',
                      'Fort Hays State University', 'Fort Lewis College', 'Fort Valley State University',
                      'Franklin Pierce University', 'Frostburg State University', 'Gannon University',
                      'Glenville State College', 'Grand Valley State University', 'Harding University',
                      'Henderson State University', 'Hillsdale College', 'Indiana University of Pennsylvania',
                      'Johnson C. Smith University', 'Kentucky State University', 'Kentucky Wesleyan College',
                      'Kutztown University of Pennsylvania', 'Lake Erie College', 'Lane College',
                      'Lenoir-Rhyne University', 'Limestone University', 'Lincoln University at Missouri',
                      'Lincoln University Pennsylvania', 'Lindenwood University', 'Livingstone College',
                      'Lock Haven University', 'Mars Hill University', 'McKendree University', 'Mercyhurst University',
                      'Michigan Technological University', 'Midwestern State University', 'Miles College',
                      'Millersville University of Pennsylvania', 'Minnesota State University at Mankato',
                      'Minnesota State University at Moorhead', 'Minot State University', 'Mississippi College',
                      'Missouri Southern State University', 'Missouri University of Science & Technology',
                      'Missouri Western State University', 'Morehouse College', 'New Mexico Highlands University',
                      'Newberry College', 'North Greenville University', 'Northeastern State University',
                      'Northern Michigan University', 'Northern State University',
                      'Northwest Missouri State University', 'Northwestern Oklahoma State University',
                      'Northwood University at Michigan', 'Notre Dame College', 'Ohio Dominican University',
                      'Oklahoma Baptist University', 'Ouachita Baptist University', 'Pace University',
                      'Pittsburg State University', 'Post University', 'Quincy University',
                      'Saginaw Valley State University', 'Saint Anselm College', "Saint Augustine's University",
                      'Savannah State University', 'Seton Hill University', 'Shaw University', 'Shepherd University',
                      'Shippensburg University of Pennsylvania', 'Shorter University', 'Slippery Rock University',
                      'South Dakota Mines', 'Southeastern Oklahoma State University', 'Southern Arkansas University',
                      'Southern Connecticut State University', 'Southern Nazarene University',
                      'Southwest Baptist University', 'Southwest Minnesota State University',
                      'Southwestern Oklahoma State University', 'Stonehill College', 'Texas A&M University - Commerce',
                      'Texas A&M University at Kingsville', "The University of Virginia's College at Wise",
                      'Tiffin University', 'Truman State University', 'Tusculum University', 'Tuskegee University',
                      'University of Arkansas at Monticello', 'University of Central Missouri',
                      'University of Central Oklahoma', 'University of Charleston', 'University of Findlay',
                      'University of Indianapolis', 'University of Mary', 'University of Minnesota at Duluth',
                      'University of Nebraska at Kearney', 'University of New Haven',
                      'University of North Carolina at Pembroke', 'University of Sioux Falls',
                      'University of Texas at Permian Basin', 'University of West Alabama', 'University of West Florida',
                      'University of West Georgia', 'Upper Iowa University', 'Valdosta State University',
                      'Virginia State University', 'Virginia Union University', 'Walsh University',
                      'Washburn University', 'Wayne State College', 'Wayne State University',
                      'West Chester University of Pennsylvania', 'West Liberty University', 'West Texas A&M University',
                      'West Virginia State University', 'West Virginia Wesleyan College', 'Western Colorado University',
                      'Western New Mexico University', 'Western Oregon University', 'Wheeling University',
                      'William Jewell College', 'Wingate University', 'Winona State University',
                      'Winston-Salem State University']

    d3_school_list = ['Adrian College', 'Albion College', 'Albright College', 'Alfred University', 'Allegheny College',
                      'Alma College', 'Alvernia University', 'Amherst College', 'Anderson University at Indiana',
                      'Anna Maria College', 'Augsburg University', 'Augustana College at Illinois', 'Aurora University',
                      'Austin College', 'Averett University', 'Baldwin Wallace University', 'Bates College',
                      'Belhaven University', 'Beloit College', 'Benedictine University', 'Berry College',
                      'Bethany College at West Virginia', 'Bethel University at Minnesota', 'Birmingham-Southern College',
                      'Bluffton University', 'Bowdoin College', 'Brevard College', 'Bridgewater College',
                      'Bridgewater State University', 'Buena Vista University', 'California Lutheran University',
                      'Capital University', 'Carleton College', 'Carnegie Mellon University', 'Carroll University',
                      'Carthage College', 'Case Western Reserve University', 'Castleton University',
                      'Catholic University of America', 'Central College', 'Centre College', 'Chapman University',
                      'Christopher Newport University', 'Claremont-Mudd-Scripps Colleges', 'Coe College',
                      'Colby College', 'College of Wooster', 'Concordia College at Minnesota',
                      'Concordia University at Chicago', 'Concordia University Wisconsin', 'Cornell College',
                      'Crown College', 'Curry College', 'Dean College', 'Defiance College',
                      'Delaware Valley University', 'Denison University', 'DePauw University', 'Dickinson College',
                      'East Texas Baptist University', 'Elmhurst University', 'Endicott College', 'Eureka College',
                      'Fairleigh Dickinson University – College at Florham', 'Ferrum College', 'Finlandia University',
                      'Fitchburg State University', 'Framingham State University', 'Franklin & Marshall College',
                      'Franklin College', 'Gallaudet University', 'Geneva College', 'George Fox University',
                      'Gettysburg College', 'Greensboro College', 'Greenville University', 'Grinnell College',
                      'Grove City College', 'Guilford College', 'Gustavus Adolphus College', 'Hamilton College',
                      'Hamline University', 'Hampden-Sydney College', 'Hanover College', 'Hardin-Simmons University',
                      'Hartwick College', 'Heidelberg University', 'Hendrix College', 'Hilbert College',
                      'Hiram College', 'Hobart & William Smith College', 'Hope College', 'Howard Payne University',
                      'Huntingdon College', 'Husson University', 'Illinois College', 'Illinois Wesleyan University',
                      'Ithaca College', 'John Carroll University', 'Johns Hopkins University', 'Juniata College',
                      'Kalamazoo College', 'Kean University', 'Kenyon College', 'Keystone College',
                      "King's College at Pennsylvania", 'Knox College', 'LaGrange College', 'Lake Forest College',
                      'Lakeland University', 'Lawrence University', 'Lebanon Valley College', 'Lewis & Clark College',
                      'Linfield University', 'Loras College', 'Luther College', 'Lycoming College',
                      'Macalester College', 'Manchester University', 'Marietta College', 'Martin Luther College',
                      'Maryville College', 'Massachusetts Institute of Technology – MIT', 'McDaniel College',
                      'McMurry University', 'Methodist University', 'Middlebury College', 'Millikin University',
                      'Millsaps College', 'Misericordia University', 'Monmouth College', 'Montclair State University',
                      'Moravian University', 'Mount St. Joseph University', 'Muhlenberg College',
                      'Muskingum University', 'Nebraska Wesleyan University', 'Nichols College',
                      'North Carolina Wesleyan College', 'North Central College', 'North Park University',
                      'Norwich University', 'Oberlin College', 'Ohio Northern University', 'Ohio Wesleyan University',
                      'Olivet College', 'Otterbein University', 'Pacific Lutheran University', 'Pacific University',
                      'Plymouth State University', 'Pomona-Pitzer Colleges', 'Randolph-Macon College',
                      'Rensselaer Polytechnic Institute', 'Rhodes College', 'Ripon College',
                      'Rockford University', 'Rose-Hulman Institute of Technology', 'Rowan University',
                      "Saint John's University at Minnesota", 'Saint Vincent College at Pennsylvania',
                      'Salisbury University', 'Salve Regina University', 'Sewanee at The University of the South',
                      'Shenandoah University', 'Simpson College', 'Southern Virginia University',
                      'Southwestern University', 'Springfield College', 'St. John Fisher College',
                      'St. Lawrence University', 'St. Norbert College', 'St. Olaf College', 'Stevenson University',
                      'Sul Ross State University', 'SUNY Buffalo State College', 'SUNY College at Brockport',
                      'SUNY Cortland', 'SUNY Maritime College', 'SUNY Morrisville', 'Susquehanna University',
                      'Texas Lutheran University', 'The College of New Jersey', 'The College of St. Scholastica',
                      'Thiel College', 'Trine University', 'Trinity College at Connecticut',
                      'Trinity University at Texas', 'Tufts University', 'Union College at New York',
                      'United States Coast Guard Academy', 'United States Merchant Marine Academy',
                      'University of Chicago', 'University of Dubuque', 'University of La Verne',
                      'University of Mary Hardin-Baylor', 'University of Massachusetts – Dartmouth',
                      'University of Minnesota at Morris', 'University of Mount Union', 'University of New England',
                      'University of Northwestern at St. Paul', 'University of Puget Sound', 'University of Redlands',
                      'University of Rochester', 'University of Wisconsin at Eau Claire',
                      'University of Wisconsin at La Crosse', 'University of Wisconsin at Oshkosh',
                      'University of Wisconsin at Platteville', 'University of Wisconsin at River Falls',
                      'University of Wisconsin at Stevens Point', 'University of Wisconsin at Stout',
                      'University of Wisconsin at Whitewater', 'Ursinus College', 'Utica College', 'Wabash College',
                      'Wartburg College', 'Washington & Jefferson College', 'Washington & Lee University',
                      'Washington University in St. Louis', 'Waynesburg University', 'Wesleyan University',
                      'Western Connecticut State University', 'Western New England University',
                      'Westfield State University', 'Westminster College at Missouri',
                      'Westminster College at Pennsylvania', 'Wheaton College at Illinois', 'Whittier College',
                      'Whitworth University', 'Widener University', 'Wilkes University', 'Willamette University',
                      'William Paterson University of New Jersey', 'Williams College', 'Wilmington College',
                      'Wittenberg University', 'Worcester Polytechnic Institute', 'Worcester State University']

    # player ability normal distribution for most players and abilities
    player_ability_norm_dist_obj = get_truncated_normal(mean=80, sd=6.7, low=50, upp=100)

    # distributions used for fb speed, elusiveness and strength
    fb_speed_elusiveness_norm_dist_obj = get_truncated_normal(mean=65, sd=6.7, low=50, upp=85)
    fb_strength_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

    # distributions used for te - speed is slower, strength and block power are higher than average
    te_speed_norm_dist_obj = get_truncated_normal(mean=65, sd=6.7, low=50, upp=85)
    te_strength_bpwr_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

    # distribution used for wr - speed is higher than normal
    wr_speed_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

    # distribution used for sf - speed is higher than normal
    sf_speed_norm_dist_obj = get_truncated_normal(mean=88, sd=6.7, low=75, upp=100)

    # distribution used for lb - tackle_rating is higher than normal
    lb_tackle_norm_dist_obj = get_truncated_normal(mean=85, sd=6.7, low=70, upp=100)

    # age normal distribution for punters and kickers
    pk_age_norm_dist_obj = get_truncated_normal(mean=35, sd=6.7, low=19, upp=50)

    # age normal distribution for running backs
    rb_age_norm_dist_obj = get_truncated_normal(mean=27, sd=6.7, low=19, upp=40)

    # age normal distribution for all other player positions
    otherpos_age_norm_dist_obj = get_truncated_normal(mean=30, sd=4.5, low=19, upp=46)

    # height dists
    six_feet_tall_inches_norm_dist_obj = get_truncated_normal(mean=3, sd=2, low=0, upp=11)
    five_feet_tall_inches_norm_dist_obj = get_truncated_normal(mean=10, sd=2, low=5, upp=11)

    # weight dists
    low_5_ft_lb_weight_dist = get_truncated_normal(mean=225, sd=20, low=200, upp=250)
    high_5_ft_lb_weight_dist = get_truncated_normal(mean=265, sd=20, low=235, upp=285)
    low_6_ft_lb_weight_dist = get_truncated_normal(mean=300, sd=20, low=275, upp=325)
    high_6_ft_lb_weight_dist = get_truncated_normal(mean=340, sd=20, low=315, upp=365)
    low_6_ft_te_weight_dist = get_truncated_normal(mean=250, sd=10, low=235, upp=265)
    high_6_ft_te_weight_dist = get_truncated_normal(mean=275, sd=10, low=260, upp=290)
    low_5_ft_nlb_weight_dist = get_truncated_normal(mean=160, sd=10, low=140, upp=180)
    high_5_ft_nlb_weight_dist = get_truncated_normal(mean=190, sd=20, low=170, upp=210)
    low_6_ft_nlb_weight_dist = get_truncated_normal(mean=220, sd=20, low=190, upp=250)
    high_6_ft_nlb_weight_dist = get_truncated_normal(mean=275, sd=20, low=250, upp=300)

    # create list of player positions that will represent the number of players to create for each team
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
    roster_position_count_sto_list = ["sto"] * 2
    roster_position_count_std_list = ["std"] * 2

    roster_position_count_draft_qb_list = ["qb"] * 1
    roster_position_count_draft_rb_list = ["rb"] * 1
    roster_position_count_draft_te_list = ["te"] * 1
    roster_position_count_draft_fb_list = ["fb"] * 1
    roster_position_count_draft_wr_list = ["wr"] * 1
    roster_position_count_draft_ol_list = ["ol"] * 1
    roster_position_count_draft_k_list = ["k"] * 1
    roster_position_count_draft_p_list = ["p"] * 1
    roster_position_count_draft_dl_list = ["dl"] * 1
    roster_position_count_draft_lb_list = ["lb"] * 1
    roster_position_count_draft_cb_list = ["cb"] * 1
    roster_position_count_draft_sf_list = ["sf"] * 1
    roster_position_count_draft_sto_list = ["sto"] * 1
    roster_position_count_draft_std_list = ["std"] * 1

    roster_position_count_league_list = roster_position_count_qb_list + roster_position_count_rb_list + roster_position_count_te_list + roster_position_count_fb_list + \
                                 roster_position_count_wr_list + roster_position_count_ol_list + roster_position_count_k_list + roster_position_count_p_list + \
                                 roster_position_count_dl_list + roster_position_count_lb_list + roster_position_count_cb_list + roster_position_count_sf_list + \
                                 roster_position_count_sto_list + roster_position_count_std_list

    roster_position_count_draft_list = roster_position_count_draft_qb_list + roster_position_count_draft_rb_list + roster_position_count_draft_te_list + roster_position_count_draft_fb_list + \
                                 roster_position_count_draft_wr_list + roster_position_count_draft_ol_list + roster_position_count_draft_k_list + roster_position_count_draft_p_list + \
                                 roster_position_count_draft_dl_list + roster_position_count_draft_lb_list + roster_position_count_draft_cb_list + roster_position_count_draft_sf_list + \
                                 roster_position_count_draft_sto_list + roster_position_count_draft_std_list

    #store player career arc data here
    player_name_to_career_arc_list_dict = {}

    #player arcs differ based on position and age
    #a player will improve from their rookie year to their peak, then they will regress until the end of their career
    #the rate at which this improvement and degradation occur depends on the position and randomness
    #for simplicity, I will broadly define an improvement period (rookie year to near peak), a peak period, and then a slow decline until retirement
    #for most positions, the peak period will be in the midpoint of a career. Exception is running back and wide receiver, which has a peak about 1/4 into the career

    rb_rookie_to_peak_growth_number = 3
    rb_peak_growth_number = 4
    rb_peak_to_eoc_number = 3

    wr_rookie_to_peak_growth_number = 2.5
    wr_peak_growth_number = 3
    wr_peak_to_eoc_number = 2.5

    pk_rookie_to_peak_growth_number = 1.5
    pk_peak_growth_number = 2
    pk_peak_to_eoc_number = 1.5

    qb_rookie_to_peak_growth_number = 2
    qb_peak_growth_number = 2.5
    qb_peak_to_eoc_number = 2

    other_pos_rookie_to_peak_growth_number = 2
    other_pos_peak_growth_number = 2.5
    other_pos_peak_to_eoc_number = 2

    rb_peak_age_interval = [23,26]
    wr_peak_age_interval = [24,28]
    pk_peak_age_interval = [30,34]
    qb_peak_age_interval = [28,32]
    other_pos_peak_age_interval = [26,30]

    rb_last_year_interval = [33,38]
    wr_last_year_interval = [33,40]
    pk_last_year_interval = [38,48]
    qb_last_year_interval = [37,45]
    other_players_last_year_interval = [35, 42]

def create_player_career_arc(player_position, player_age, player_name, combined_attr_score_dict):

    if player_position == 'rb':
        this_player_last_year_interval = PlayerCreation.rb_last_year_interval
    elif player_position == 'wr':
        this_player_last_year_interval = PlayerCreation.wr_last_year_interval
    elif player_position in ['p', 'k']:
        this_player_last_year_interval = PlayerCreation.pk_last_year_interval
    elif player_position == 'qb':
        this_player_last_year_interval = PlayerCreation.qb_last_year_interval
    else:
        this_player_last_year_interval = PlayerCreation.other_players_last_year_interval


    # account for if the player's age is already in or exceeding the last year interval
    if player_age > this_player_last_year_interval[0] and player_age < this_player_last_year_interval[1]:
        this_player_last_year_interval = [int(player_age), this_player_last_year_interval[1]]

    # in the situation where the generated age exceeds the last year interval, then make the interval the last year
    if player_age > this_player_last_year_interval[1]:
        this_player_last_year_interval = [int(player_age), int(player_age + 1)]

    # we need to determine the last year for a given player
    # as we go deeper into the player's last_year interval, the less likely they will be still playing

    this_player_last_year = -1
    all_players_yoy_retirement_growth_pct = 100.0 / (this_player_last_year_interval[1] - this_player_last_year_interval[0])

    this_player_retirement_pct = 0

    exception_str = ""

    for this_last_year_candidate in range(this_player_last_year_interval[0], this_player_last_year_interval[1] + 1):

        if this_last_year_candidate == this_player_last_year_interval[1]:
            # this is the player's final season
            this_player_last_year = this_last_year_candidate
            break

        if this_last_year_candidate < this_player_last_year_interval[1]:
            this_player_retirement_pct += all_players_yoy_retirement_growth_pct

        retire_this_year_randgen = random.randint(1, 100)

        if retire_this_year_randgen >= (100 - this_player_retirement_pct):
            this_player_last_year = this_last_year_candidate
            break

    # now create the career arc from player_age to this_player_last_year
    combined_attr_score_career_arc_list_dict = [combined_attr_score_dict]

    for this_age in range(int(player_age), this_player_last_year + 1):

        # we will assign this year's ability numbers based on last year's ability numbers
        previous_year_combined_attr_score_dict = combined_attr_score_career_arc_list_dict[-1]

        # sign that indicates whether a player is on the rise or on the decline
        # by default it is upside
        this_age_upside_downside_sign = 1

        this_age_combined_attr_score_dict = {}

        this_age_attribute_change_interval = 0

        # the player_age and player_position will determine which growth numbers we use
        if player_position == 'rb':

            if this_age < PlayerCreation.rb_peak_age_interval[0]:
                this_age_attribute_change_interval = PlayerCreation.rb_rookie_to_peak_growth_number
            elif this_age >= PlayerCreation.rb_peak_age_interval[0] and this_age <= PlayerCreation.rb_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.rb_peak_growth_number
            elif this_age > PlayerCreation.rb_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.rb_peak_to_eoc_number
                this_age_upside_downside_sign = -1

        elif player_position == 'wr':

            if this_age < PlayerCreation.wr_peak_age_interval[0]:
                this_age_attribute_change_interval = PlayerCreation.wr_rookie_to_peak_growth_number
            elif this_age >= PlayerCreation.wr_peak_age_interval[0] and this_age <= PlayerCreation.wr_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.wr_peak_growth_number
            elif this_age > PlayerCreation.wr_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.wr_peak_to_eoc_number
                this_age_upside_downside_sign = -1

        elif player_position in ['p', 'k']:

            if this_age < PlayerCreation.pk_peak_age_interval[0]:
                this_age_attribute_change_interval = PlayerCreation.pk_rookie_to_peak_growth_number
            elif this_age >= PlayerCreation.pk_peak_age_interval[0] and this_age <= PlayerCreation.pk_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.pk_peak_growth_number
            elif this_age > PlayerCreation.pk_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.pk_peak_to_eoc_number
                this_age_upside_downside_sign = -1

        elif player_position == 'qb':

            if this_age < PlayerCreation.qb_peak_age_interval[0]:
                this_age_attribute_change_interval = PlayerCreation.qb_rookie_to_peak_growth_number
            elif this_age >= PlayerCreation.qb_peak_age_interval[0] and this_age <= PlayerCreation.qb_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.qb_peak_growth_number
            elif this_age > PlayerCreation.qb_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.qb_peak_to_eoc_number
                this_age_upside_downside_sign = -1

        else:

            if this_age < PlayerCreation.other_pos_peak_age_interval[0]:
                this_age_attribute_change_interval = PlayerCreation.other_pos_rookie_to_peak_growth_number
            elif this_age >= PlayerCreation.other_pos_peak_age_interval[0] and this_age <= PlayerCreation.other_pos_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.other_pos_peak_growth_number
            elif this_age > PlayerCreation.other_pos_peak_age_interval[1]:
                this_age_attribute_change_interval = PlayerCreation.other_pos_peak_to_eoc_number
                this_age_upside_downside_sign = -1

        # create this year attribute dict for this player
        for this_attribute in combined_attr_score_dict.keys():

            if this_attribute == 'intelligence_rating' and this_age_upside_downside_sign == -1:
                this_age_attribute_change = 0
            else:
                this_age_attribute_change = round((1 + random.randint(0, this_age_attribute_change_interval * 100)) / 100.0,2) * this_age_upside_downside_sign

            this_age_combined_attr_score_dict[this_attribute] = round(previous_year_combined_attr_score_dict[this_attribute] + this_age_attribute_change, 2)

        # finally, assign this_age_combined_attr_score_dict as the latest entry in combined_attr_score_career_arc_list_dict
        combined_attr_score_career_arc_list_dict.append(this_age_combined_attr_score_dict)

    return combined_attr_score_career_arc_list_dict


def initialize_spec_db_table_ids(player_position_list):

    player_position_to_db_id_dict = {}

    for this_position in player_position_list:
        player_position_to_db_id_dict[this_position] = -1

    # get initial db table ids for all position spec db tables
    try:
        player_specs_dl_id = int(
            PlayerSpecsDl.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_dl_id = 1

    player_position_to_db_id_dict['dl'] = player_specs_dl_id

    try:
        player_specs_cb_id = int(
            PlayerSpecsCb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_cb_id = 1

    player_position_to_db_id_dict['cb'] = player_specs_cb_id

    try:
        player_specs_fb_id = int(
            PlayerSpecsFb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_fb_id = 1

    player_position_to_db_id_dict['fb'] = player_specs_fb_id

    try:
        player_specs_k_id = int(
            PlayerSpecsK.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_k_id = 1

    player_position_to_db_id_dict['k'] = player_specs_k_id

    try:
        player_specs_lb_id = int(
            PlayerSpecsLb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_lb_id = 1

    player_position_to_db_id_dict['lb'] = player_specs_lb_id

    try:
        player_specs_ol_id = int(
            PlayerSpecsOl.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_ol_id = 1

    player_position_to_db_id_dict['ol'] = player_specs_ol_id

    try:
        player_specs_p_id = int(
            PlayerSpecsP.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_p_id = 1

    player_position_to_db_id_dict['p'] = player_specs_p_id

    try:
        player_specs_qb_id = int(
            PlayerSpecsQb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_qb_id = 1

    player_position_to_db_id_dict['qb'] = player_specs_qb_id

    try:
        player_specs_rb_id = int(
            PlayerSpecsRb.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_rb_id = 1

    player_position_to_db_id_dict['rb'] = player_specs_rb_id

    try:
        player_specs_sf_id = int(
            PlayerSpecsSf.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_sf_id = 1

    player_position_to_db_id_dict['sf'] = player_specs_sf_id

    try:
        player_specs_std_id = int(
            PlayerSpecsStd.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_std_id = 1

    player_position_to_db_id_dict['std'] = player_specs_std_id

    try:
        player_specs_sto_id = int(
            PlayerSpecsSto.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_sto_id = 1

    player_position_to_db_id_dict['sto'] = player_specs_sto_id

    try:
        player_specs_te_id = int(
            PlayerSpecsTe.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_te_id = 1

    player_position_to_db_id_dict['te'] = player_specs_te_id

    try:
        player_specs_wr_id = int(
            PlayerSpecsWr.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_specs_wr_id = 1

    player_position_to_db_id_dict['wr'] = player_specs_wr_id

    return player_position_to_db_id_dict


def create_players(team_name_list, team_name_to_team_id_dict, league_id, female_setting, db_commit_to_delete_id_dict, mode):

    exception_str = ""
    status_code = 1

    # get latest id value of player
    try:
        player_id = int(Player.objects.using('xactly_dev').latest('id').id) + 1
    except Exception:
        player_id = 1

    first_player_id = player_id

    try:
        player_team_id = int(PlayerTeam.objects.using('xactly_dev').latest('player_team_id').player_team_id) + 1
    except Exception:
        player_team_id = 1

    first_player_team_id = player_team_id

    player_name_to_info_dict_dict = {}
    player_name_to_combined_attr_score_dict = {}

    player_position_to_db_id_dict = initialize_spec_db_table_ids(PlayerCreation.player_position_list)

    first_ids_player_position_to_db_id_dict = copy.deepcopy(player_position_to_db_id_dict)

    #depending upon the mode, we will assign roster_position_count_list
    roster_position_count_list = []

    if mode == "league":
        roster_position_count_list = PlayerCreation.roster_position_count_league_list
    else:
        #draft mode
        roster_position_count_list = PlayerCreation.roster_position_count_draft_list

    for this_team_name in team_name_list:

        this_team_id = team_name_to_team_id_dict[this_team_name]
        team_numbers_used = set()

        for player_position in roster_position_count_list:

            player_name_uniqueness_verified = False
            player_number_uniqueness_verified = False

            # age is dependent on the player_position
            player_age = -1

            if player_position in ['p', 'k']:
                player_age = round(float(PlayerCreation.pk_age_norm_dist_obj.rvs()))
            elif player_position == 'rb':
                player_age = round(float(PlayerCreation.rb_age_norm_dist_obj.rvs()))
            else:
                player_age = round(float(PlayerCreation.otherpos_age_norm_dist_obj.rvs()))

            #secondary position will be chosen at random
            secondary_position_list = [this_position for this_position in PlayerCreation.player_position_list if
                                       this_position != player_position]

            secondary_position_random_value = random.randint(0, len(secondary_position_list) - 1)
            secondary_position = secondary_position_list[secondary_position_random_value]

            #assign number based on position
            while player_number_uniqueness_verified == False:

                this_position_number_bounds_list = PlayerCreation.position_to_number_bounds_list_dict[player_position]
                player_number = random.randint(this_position_number_bounds_list[0],
                                               this_position_number_bounds_list[1])

                if player_number not in team_numbers_used:
                    team_numbers_used.add(player_number)
                    player_number_uniqueness_verified = True

            #height in inches is determined via a normal dist

            height_feet = -1
            height_inches = -1

            height_feet_random_value = random.randint(0, 9)

            if height_feet_random_value <= 7 or player_position in ['ol', 'dl', 'te']:
                height_feet = 6
                height_inches = round(float(PlayerCreation.six_feet_tall_inches_norm_dist_obj.rvs()))
            else:
                height_feet = 5
                height_inches = round(float(PlayerCreation.five_feet_tall_inches_norm_dist_obj.rvs()))

            #sometimes, we get -1 inches, so let's fix that
            if height_inches == -1:
                height_inches = 0

            # weight in lbs is position dependent - ol, dl and te have one dist, everyone else has another
            # it is also height dependent - the taller the player, the more the player is likely to weigh

            if height_feet == 5 and height_inches <= 8 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_5_ft_lb_weight_dist.rvs())
            elif height_feet == 5 and height_inches <= 8 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_5_ft_nlb_weight_dist.rvs())
            elif height_feet == 5 and height_inches > 8 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_5_ft_lb_weight_dist.rvs())
            elif height_feet == 5 and height_inches > 8 and player_position not in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_5_ft_nlb_weight_dist.rvs())
            elif height_feet == 6 and height_inches <= 6 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.low_6_ft_lb_weight_dist.rvs())
            elif height_feet == 6 and height_inches <= 6 and player_position == 'te':
                weight_lbs = round(PlayerCreation.low_6_ft_te_weight_dist.rvs())
            elif height_feet == 6 and height_inches <= 6 and player_position not in ['dl', 'ol', 'te']:
                weight_lbs = round(PlayerCreation.low_6_ft_nlb_weight_dist.rvs())
            elif height_feet == 6 and height_inches > 6 and player_position in ['dl', 'ol']:
                weight_lbs = round(PlayerCreation.high_6_ft_lb_weight_dist.rvs())
            elif height_feet == 6 and height_inches > 6 and player_position == 'te':
                weight_lbs = round(PlayerCreation.high_6_ft_te_weight_dist.rvs())
            elif height_feet == 6 and height_inches > 6 and player_position not in ['dl', 'ol', 'te']:
                weight_lbs = round(PlayerCreation.high_6_ft_nlb_weight_dist.rvs())

            while player_name_uniqueness_verified == False:

                if female_setting == True:
                    gender_value = random.randint(0, 1)
                else:
                    gender_value = 0

                if gender_value == 0:
                    given_gender = "male"
                else:
                    given_gender = "female"

                # let's say that 1 out of every 50 players uses a middle initial
                using_middle_initial_value = random.randint(0, 49)

                if using_middle_initial_value == 25:
                    middle_initial_letter_idx = random.randint(0, 25)
                    middle_initial = chr(ord('A') + middle_initial_letter_idx) + ". "
                else:
                    middle_initial = ""

                player_name = names.get_full_name(gender=given_gender)

                if middle_initial != "":
                    player_name_parts = player_name.split()
                    player_name = player_name_parts[0] + ' ' + middle_initial + player_name_parts[1]

                if player_name not in list(player_name_to_info_dict_dict.keys()):
                    player_name_uniqueness_verified = True

            player_name_parts = player_name.split()
            player_first_name = player_name_parts[0]
            player_last_name = player_name_parts[-1]

            # alma mater
            school_random_value = random.randint(0, 99)
            fbs_random_value = random.randint(0, len(PlayerCreation.fbs_school_list) - 1)
            fcs_random_value = random.randint(0, len(PlayerCreation.fcs_school_list) - 1)
            d2_random_value = random.randint(0, len(PlayerCreation.d2_school_list) - 1)
            d3_random_value = random.randint(0, len(PlayerCreation.d3_school_list) - 1)

            school_name = ""
            school_value = -1

            if school_value <= 74:
                school_name = PlayerCreation.fbs_school_list[fbs_random_value]
            elif school_value > 74 and school_value <= 92:
                school_name = PlayerCreation.fcs_school_list[fcs_random_value]
            elif school_value > 92 and school_value < 99:
                school_name = PlayerCreation.d2_school_list[d2_random_value]
            else:
                school_name = PlayerCreation.d3_school_list[d3_random_value]

            this_player_attribute_list = []
            this_player_attribute_list = PlayerCreation.position_to_player_attribute_list_dict[player_position]
            this_player_attribute_value_dict = {}

            player_name_to_combined_attr_score_dict[player_name] = -1

            for this_attribute in this_player_attribute_list:

                # check for customized distributions
                if player_position == "fb" and this_attribute in ['speed_rating', 'elusiveness_rating']:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.fb_speed_elusiveness_norm_dist_obj.rvs()), 2)
                elif player_position == "fb" and this_attribute == 'strength_rating':
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.fb_strength_norm_dist_obj.rvs()), 2)
                elif player_position == "te" and this_attribute == 'speed_rating':
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.te_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "te" and this_attribute in ['strength_rating', 'block_power_rating']:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.te_strength_bpwr_dist_obj.rvs()), 2)
                elif player_position == "wr" and this_attribute == "speed_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.wr_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "sf" and this_attribute == "speed_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.sf_speed_norm_dist_obj.rvs()), 2)
                elif player_position == "sf" and this_attribute == "tackle_rating":
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.lb_tackle_norm_dist_obj.rvs()), 2)
                else:
                    this_player_attribute_value_dict[this_attribute] = round(float(PlayerCreation.player_ability_norm_dist_obj.rvs()),2)

                player_name_to_combined_attr_score_dict[player_name] += this_player_attribute_value_dict[this_attribute]

            #create player career arc
            this_player_career_arc_list_dict = create_player_career_arc(player_position, player_age, player_name, this_player_attribute_value_dict)

            #first, create and save Player db object
            this_player_dict = {}
            this_player_dict["id"] = player_id
            this_player_dict["first_name"] = player_first_name
            this_player_dict["middle_initial"] = middle_initial
            this_player_dict["last_name"] = player_last_name

            #we only assign a number to a player in league mode
            if mode == "league":
                this_player_dict["number"] = player_number
            else:
                this_player_dict["number"] = None

            if mode == "league":
                this_player_dict["age"] = int(player_age)
            else:
                this_player_dict["age"] = random.randint(19, 22)

            this_player_dict["first_season_id"] = 1
            this_player_dict["last_season_id"] = -1
            this_player_dict["injury_status"] = 0
            this_player_dict["alma_mater"] = school_name
            this_player_dict["primary_position"] = player_position
            this_player_dict["secondary_position"] = secondary_position
            this_player_dict["draft_position"] = "0.0"
            this_player_dict["salary"] = 0
            this_player_dict["height"] = str(int(height_feet)) + "'" + str(int(height_inches))
            this_player_dict["weight"] = weight_lbs
            this_player_dict["league_id"] = league_id
            this_player_dict["draft_value"] = 0.0

            if mode == "league":
                this_player_dict["playing_status"] = PlayingStatus.ROSTER
            else:
                this_player_dict["playing_status"] = PlayingStatus.DRAFT

            #create Player db object
            try:
                this_player_db_obj = Player(**this_player_dict)
                this_player_db_obj.save(using="xactly_dev")
                db_commit_to_delete_id_dict["Player"] = first_player_id
            except Exception as e:
                exception_str = str(e)
                status_code = -6
                return status_code, exception_str, db_commit_to_delete_id_dict

            #only assign a player to a team in league mode
            if mode == "league":

                #Create PlayerTeam db object
                try:
                    this_player_team_db_obj = PlayerTeam(player_team_id=player_team_id, player_id=player_id, team_id=this_team_id, season_id=1, league_id=league_id)
                    this_player_team_db_obj.save(using="xactly_dev")
                    db_commit_to_delete_id_dict["PlayerTeam"] = first_player_team_id
                except Exception as e:
                    exception_str = str(e)
                    status_code = -7
                    return status_code, exception_str, db_commit_to_delete_id_dict

            #Create specs object for this player_position
            this_player_position_specs_db_obj = None

            player_specs_db_obj = None
            exception_str = ""

            try:

                if player_position == 'qb':
                    player_specs_db_obj = PlayerSpecsQb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'rb':
                    player_specs_db_obj = PlayerSpecsRb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'fb':
                    player_specs_db_obj = PlayerSpecsFb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'wr':
                    player_specs_db_obj = PlayerSpecsWr(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'te':
                    player_specs_db_obj = PlayerSpecsTe(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'k':
                    player_specs_db_obj = PlayerSpecsK(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'lb':
                    player_specs_db_obj = PlayerSpecsLb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'ol':
                    player_specs_db_obj = PlayerSpecsOl(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'p':
                    player_specs_db_obj = PlayerSpecsP(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'cb':
                    player_specs_db_obj = PlayerSpecsCb(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'dl':
                    player_specs_db_obj = PlayerSpecsDl(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'sf':
                    player_specs_db_obj = PlayerSpecsSf(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'sto':
                    player_specs_db_obj = PlayerSpecsSto(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)
                elif player_position == 'std':
                    player_specs_db_obj = PlayerSpecsStd(id=player_position_to_db_id_dict[player_position], player_id=player_id, career_arc_dict=str(this_player_career_arc_list_dict), **this_player_attribute_value_dict)

                player_specs_db_obj.save(using="xactly_dev")
                db_commit_to_delete_id_dict["PlayerSpec"] = first_ids_player_position_to_db_id_dict

            except Exception as e:
                exception_str = str(e)
                status_code = -8
                return status_code, exception_str, db_commit_to_delete_id_dict

            player_position_to_db_id_dict[player_position] += 1

            player_id += 1
            player_team_id += 1

    return status_code, exception_str, db_commit_to_delete_id_dict
