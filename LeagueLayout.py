# coding: utf-8

from jpartyfb.models import TeamCity, DefaultTeams


def add_new_divisions_and_teams(division_num_to_division_name_dict, division_num_to_team_list_dict,
                                number_of_divisions_select, number_of_teams_conf_select,
                                previous_num_divisions_per_conference, previous_num_teams_per_conference):

    # we will add teams to divisions and add new divisions on a case by case basis
    # depending on the values of number_of_divisions_select, number_of_teams_conf_select, previous_num_divisions_per_conference and previous_num_teams_per_conference

    max_division_num = max(division_num_to_division_name_dict.keys())

    # first, we will handle the cases were the number of divisions stays the same
    if number_of_divisions_select == previous_num_divisions_per_conference:

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 10:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 12:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 14:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 10 and number_of_teams_conf_select == 12:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 10 and number_of_teams_conf_select == 14:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 10 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 12 and number_of_teams_conf_select == 14:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 12 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 2 and previous_num_teams_per_conference == 14 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 3 and previous_num_teams_per_conference == 9 and number_of_teams_conf_select == 12:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 3 and previous_num_teams_per_conference == 9 and number_of_teams_conf_select == 15:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 3 and previous_num_teams_per_conference == 12 and number_of_teams_conf_select == 15:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 4 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 12:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 4 and previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")
                this_team_list.append("New Team")

        if previous_num_divisions_per_conference == 4 and previous_num_teams_per_conference == 12 and number_of_teams_conf_select == 16:

            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

    elif previous_num_divisions_per_conference == 2 and number_of_divisions_select == 3:

        # here and beyond, the user wants a new number of divisions per conference. There is no use in trying to calculate this, since
        # a user may want to make an arbitrary range of changes to the division/conference alignment. So I will
        # simply create the new number of divisions per conference and ensure that we have an equal number of teams
        # in each division. The details of division membership will be left to the user

        if previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 12:
            # we need to add 1 new division per conference, with those divisions having all the new teams
            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []

            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")

            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")

        if previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 15:

            # we need to add 1 new division per conference, and those divisions will have 5 new teams
            # the existing divisions will each add one team
            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []

            # add one new team to each division
            for this_division_num, this_team_list in division_num_to_team_list_dict.items():
                this_team_list.append("New Team")

            # add remaining teams to existing divisions
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")

            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")

    elif previous_num_divisions_per_conference == 2 and number_of_divisions_select == 4:

        if previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 8:

            # in this use case, we need to take teams out of existing divisions and put them into new divisions
            # "new team" append() operations will not take place here

            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"
            division_num_to_division_name_dict[max_division_num + 3] = "New Division 3"
            division_num_to_division_name_dict[max_division_num + 4] = "New Division 4"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []
            division_num_to_team_list_dict[max_division_num + 3] = []
            division_num_to_team_list_dict[max_division_num + 4] = []

            for i in range(1, max_division_num + 1):
                # first pop two teams from division i

                division_i_team_1 = division_num_to_team_list_dict[i].pop()
                division_i_team_2 = division_num_to_team_list_dict[i].pop()

                # and add these teams to new division max_division_num + i
                division_num_to_team_list_dict[max_division_num + i].append(division_i_team_1)
                division_num_to_team_list_dict[max_division_num + i].append(division_i_team_2)

        if previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 12:

            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"
            division_num_to_division_name_dict[max_division_num + 3] = "New Division 3"
            division_num_to_division_name_dict[max_division_num + 4] = "New Division 4"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []
            division_num_to_team_list_dict[max_division_num + 3] = []
            division_num_to_team_list_dict[max_division_num + 4] = []

            # we will pop out one team from an existing division and add to a new division

            for i in range(1, max_division_num + 1):
                # first pop two teams from division i

                division_i_team_1 = division_num_to_team_list_dict[i].pop()

                # and add these teams to new division max_division_num + i
                division_num_to_team_list_dict[max_division_num + i].append(division_i_team_1)

            # we will now add 2 new teams to each new division
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 3].append("New Team")
            division_num_to_team_list_dict[max_division_num + 3].append("New Team")
            division_num_to_team_list_dict[max_division_num + 4].append("New Team")
            division_num_to_team_list_dict[max_division_num + 4].append("New Team")

        if previous_num_teams_per_conference == 8 and number_of_teams_conf_select == 16:

            # this one is easy - just add 2 divisions, and add all new conference teams to those divisions
            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"
            division_num_to_division_name_dict[max_division_num + 3] = "New Division 3"
            division_num_to_division_name_dict[max_division_num + 4] = "New Division 4"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []
            division_num_to_team_list_dict[max_division_num + 3] = []
            division_num_to_team_list_dict[max_division_num + 4] = []

            for i in range(max_division_num + 1, max_division_num + 4 + 1):
                division_num_to_team_list_dict[i].append("New Team")
                division_num_to_team_list_dict[i].append("New Team")
                division_num_to_team_list_dict[i].append("New Team")
                division_num_to_team_list_dict[i].append("New Team")

    elif previous_num_divisions_per_conference == 3 and number_of_divisions_select == 4:

        if previous_num_teams_per_conference == 9 and number_of_teams_conf_select == 12:

            # we will have 4 divisions of 3 teams each per conference
            # all we have to do is add one new division per conference, and put all new teams in those new divisions
            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []

            for i in range(max_division_num + 1, max_division_num + 2 + 1):
                division_num_to_team_list_dict[i].append("New Team")
                division_num_to_team_list_dict[i].append("New Team")
                division_num_to_team_list_dict[i].append("New Team")

        if previous_num_teams_per_conference == 9 and number_of_teams_conf_select == 16:

            # we will have 4 divisions of 4 teams each per conference
            # we have to do is add one new team to each existing division, and 4 new teams to the new divisions
            division_num_to_division_name_dict[max_division_num + 1] = "New Division 1"
            division_num_to_division_name_dict[max_division_num + 2] = "New Division 2"

            division_num_to_team_list_dict[max_division_num + 1] = []
            division_num_to_team_list_dict[max_division_num + 2] = []

            for i in range(1, max_division_num + 1):
                division_num_to_team_list_dict[i].append("New Team")

            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 1].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")
            division_num_to_team_list_dict[max_division_num + 2].append("New Team")

    return division_num_to_division_name_dict, division_num_to_team_list_dict

def build_choose_teams_html(number_of_divisions_select, number_of_teams_conf_select, number_of_teams_per_division,
                            source_page, league_id):

    division_num_to_team_list_dict = {}
    city_nickname_to_city_id_dict = {}
    conf_division_name_list = []

    team_html_str = ""
    color_to_rgb_list_dict = {'blue': ['#CCE5FF', '#99CCFF'], 'red': ['#FFCCCC', '#FFAAAA']}

    if source_page == 'els':

        try:
            team_city_obj_tuple = TeamCity.objects.using("xactly_dev").filter(league_id=league_id)
        except Exception:
            pass

        division_id_to_division_name_dict = {}
        conference_id_to_conference_name_dict = {}

        # get team properties for this league
        for this_team_city_obj in team_city_obj_tuple:

            this_team_nickname = this_team_city_obj.team.nickname
            this_team_city = this_team_city_obj.city.city_name
            this_team_city_id = this_team_city_obj.city_id
            this_team_conference_id = this_team_city_obj.team.conference_id
            this_team_conference_name = this_team_city_obj.team.conference.conference_name
            this_team_division_id = this_team_city_obj.team.division_id
            this_team_division_name = this_team_city_obj.team.division.division_name

            if this_team_division_id not in division_id_to_division_name_dict:
                division_id_to_division_name_dict[this_team_division_id] = this_team_division_name

            if this_team_conference_id not in conference_id_to_conference_name_dict:
                conference_id_to_conference_name_dict[this_team_conference_id] = this_team_conference_name

            if this_team_division_id not in division_num_to_team_list_dict:
                division_num_to_team_list_dict[this_team_division_id] = [this_team_city + " " + this_team_nickname]
            else:
                division_num_to_team_list_dict[this_team_division_id].append(
                    this_team_city + " " + this_team_nickname)

            city_nickname_to_city_id_dict[this_team_nickname] = this_team_city_id

        for i in range(1, number_of_divisions_select + 1):
            conf_division_name_list.append("Division " + str(i))

        # get conference names ready for context
        eastern_conference_name = conference_id_to_conference_name_dict[
            min(conference_id_to_conference_name_dict.keys())]
        western_conference_name = conference_id_to_conference_name_dict[
            max(conference_id_to_conference_name_dict.keys())]
        conference_name_list = [eastern_conference_name, western_conference_name]

        # convert division ids to division nums
        smallest_division_id_value = min(division_num_to_team_list_dict.keys())

        division_num_to_team_list_dict = {division_num - smallest_division_id_value + 1: team_list for
                                          division_num, team_list in division_num_to_team_list_dict.items()}

        # do same for division_num_to_division_name_dict
        division_num_to_division_name_dict = {division_num - smallest_division_id_value + 1: division_name for
                                              division_num, division_name in
                                              division_id_to_division_name_dict.items()}

        previous_num_divisions_per_conference = len(division_num_to_division_name_dict.keys()) / 2
        previous_num_teams_per_conference = len(team_city_obj_tuple) / 2

        # if we want to expand the number of divisions, we need to add dummy division names and teams to those divisions
        division_num_to_division_name_dict, division_num_to_team_list_dict = add_new_divisions_and_teams(
            division_num_to_division_name_dict, division_num_to_team_list_dict, number_of_divisions_select,
            number_of_teams_conf_select, previous_num_divisions_per_conference, previous_num_teams_per_conference)

        # package the division names into team_html_str below
        division_name_lol = []
        division_sublist = []
        division_sublist_counter = 0

        for this_division_idx, this_division_name in enumerate(division_num_to_division_name_dict.values()):

            if this_division_idx > 0 and this_division_idx % 2 == 0:
                division_name_lol.append(division_sublist)
                division_sublist = []

            division_sublist.append(this_division_name)

        division_name_lol.append(division_sublist)

        # create html tables here
        for conf_division_idx, conf_division_list in enumerate(division_name_lol, 1):
            team_html_str += "<table cellpadding='5' width='100%' border='1'><tr>"

            eastern_conference_division_name = conf_division_list[0]
            western_conference_division_name = conf_division_list[1]

            # print out division header html - first eastern division
            team_html_str += "<td width='50%' align='center' style='background-color: blue;' id='td_division_eastern_" + str(
                conf_division_idx) + "' class='td_division'>"
            team_html_str += "<input type='text' id='Eastern_division_" + str(
                conf_division_idx) + "' name='eastern_division_" + str(
                conf_division_idx) + "' class='division' maxlength='35' value='" + eastern_conference_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
            team_html_str += "</td>"

            # now western division
            team_html_str += "<td width='50%' align='center' style='background-color: red;' id='td_division_western_" + str(
                conf_division_idx) + "' class='td_division'>"
            team_html_str += "<input type='text' id='Western_division_" + str(
                conf_division_idx) + "' name='western_division_" + str(
                conf_division_idx) + "' class='division' maxlength='35' value='" + western_conference_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
            team_html_str += "</td>"

            # close division html row
            team_html_str += "</tr>"

            # open team html row - each row is a conference division of teams
            color_key_str = ""
            conference_str = ""

            for actual_division_number, division_team_list in division_num_to_team_list_dict.items():

                if actual_division_number == conf_division_idx or actual_division_number == conf_division_idx + number_of_divisions_select:

                    if actual_division_number < conf_division_idx * 2:
                        team_html_str += "<tr>"
                        color_list = color_to_rgb_list_dict["blue"]
                        conference_str = "Eastern"
                    else:
                        color_list = color_to_rgb_list_dict["red"]
                        conference_str = "Western"

                    team_html_str += "<td><table align='center' style='background-color: white;' width='100%'>"
                    for this_team_div_idx, this_team_name in enumerate(division_team_list, 1):

                        if this_team_div_idx % 2 == 1:
                            this_team_row_color = color_list[0]
                        else:
                            this_team_row_color = color_list[1]

                        team_html_str += "<tr style='background-color: " + this_team_row_color + ";'>"

                        team_html_str += "<td width='50%' align='center' id='td_team_" + str(
                            this_team_div_idx) + "_" + conference_str + "_division_" + str(
                            conf_division_idx) + "' class='td_team'>"
                        team_html_str += "<input type='text' id='" + conference_str + "_division_" + str(
                            conf_division_idx) + "_team_" + str(
                            this_team_div_idx) + "' name='" + conference_str + "_division_" + str(
                            conf_division_idx) + "_team_" + str(
                            this_team_div_idx) + "' class='team' maxlength='35' value='" + this_team_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold;' />"
                        team_html_str += "</td></tr>"

                    team_html_str += "</table></td>"

                    if conf_division_idx * 2 == actual_division_number:
                        team_html_str += "</tr>"

        team_html_str += "</table>"

    else:

        for i in range(1, number_of_divisions_select * 2 + 1):
            division_num_to_team_list_dict[i] = []

        # if user wants 28, 30 or 32 teams, then we will need to provide dummy teams, since we only have 24 teams
        # by default
        if number_of_teams_conf_select == 14:
            # add on teams to last division
            division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 4)
            division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in
                                                                              division_num_to_team_list_dict[
                                                                                  number_of_divisions_select * 2]
                                                                              for item in sublist]

        if number_of_teams_conf_select == 15:
            # add 1 new team to second to last division and add 5 new teams to last division
            division_num_to_team_list_dict[number_of_divisions_select * 2 - 1].append(["Add Team Name"])
            division_num_to_team_list_dict[number_of_divisions_select * 2 - 1] = [item for sublist in
                                                                                  division_num_to_team_list_dict[
                                                                                      number_of_divisions_select * 2 - 1]
                                                                                  for item in sublist]
            division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 5)
            division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in
                                                                              division_num_to_team_list_dict[
                                                                                  number_of_divisions_select * 2]
                                                                              for item in sublist]

        if number_of_teams_conf_select == 16:

            if number_of_divisions_select == 2:
                division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 8)
                division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in
                                                                                  division_num_to_team_list_dict[
                                                                                      number_of_divisions_select * 2]
                                                                                  for item in sublist]

            if number_of_divisions_select == 4:
                division_num_to_team_list_dict[number_of_divisions_select * 2 - 1].append(["Add Team Name"] * 4)
                division_num_to_team_list_dict[number_of_divisions_select * 2].append(["Add Team Name"] * 4)
                division_num_to_team_list_dict[number_of_divisions_select * 2 - 1] = [item for sublist in
                                                                                      division_num_to_team_list_dict[
                                                                                          number_of_divisions_select * 2 - 1]
                                                                                      for item in sublist]
                division_num_to_team_list_dict[number_of_divisions_select * 2] = [item for sublist in
                                                                                  division_num_to_team_list_dict[
                                                                                      number_of_divisions_select * 2]
                                                                                  for item in sublist]

        division_counter = 1

        for this_default_team in DefaultTeams.objects.using("xactly_dev").filter(
                id__lte=(number_of_teams_conf_select * 2)).order_by("id"):
            this_default_team_nickname = this_default_team.nickname
            this_default_team_city_name = this_default_team.city.city_name
            this_default_team_city_id = this_default_team.city.city_id

            city_nickname_to_city_id_dict[this_default_team_nickname] = this_default_team_city_id

            division_num_to_team_list_dict[division_counter].append(
                this_default_team_city_name + " " + this_default_team_nickname)

            if len(division_num_to_team_list_dict[division_counter]) == number_of_teams_per_division:
                division_counter += 1

        eastern_conference_name = "Eastern"
        western_conference_name = "Western"
        conference_name_list = [eastern_conference_name, western_conference_name]

        for i in range(1, number_of_divisions_select + 1):
            conf_division_name_list.append("Division " + str(i))

        # create table html for show_teams.html here - it's too complex for django templating language

        for conf_division_idx, conf_division_name in enumerate(conf_division_name_list, 1):
            team_html_str += "<table cellpadding='5' width='100%' border='1'><tr>"

            # print out division header html - first easter division
            team_html_str += "<td width='50%' align='center' style='background-color: blue;' id='td_division_eastern_" + str(
                conf_division_idx) + "' class='td_division'>"
            team_html_str += "<input type='text' id='Eastern_division_" + str(
                conf_division_idx) + "' name='eastern_division_" + str(
                conf_division_idx) + "' class='division' maxlength='35' value='" + "Eastern " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
            team_html_str += "</td>"

            # now western division
            team_html_str += "<td width='50%' align='center' style='background-color: red;' id='td_division_western_" + str(
                conf_division_idx) + "' class='td_division'>"
            team_html_str += "<input type='text' id='Western_division_" + str(
                conf_division_idx) + "' name='western_division_" + str(
                conf_division_idx) + "' class='division' maxlength='35' value='" + "Western " + conf_division_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold; color: white;' />"
            team_html_str += "</td>"

            # close division html row
            team_html_str += "</tr>"

            # open team html row - each row is a conference division of teams
            color_key_str = ""
            conference_str = ""

            for actual_division_number, division_team_list in division_num_to_team_list_dict.items():

                if actual_division_number == conf_division_idx or actual_division_number == conf_division_idx + number_of_divisions_select:

                    if actual_division_number < conf_division_idx * 2:
                        team_html_str += "<tr>"
                        color_list = color_to_rgb_list_dict["blue"]
                        conference_str = "Eastern"
                    else:
                        color_list = color_to_rgb_list_dict["red"]
                        conference_str = "Western"

                    team_html_str += "<td><table align='center' style='background-color: white;' width='100%'>"
                    for this_team_div_idx, this_team_name in enumerate(division_team_list, 1):

                        if this_team_div_idx % 2 == 1:
                            this_team_row_color = color_list[0]
                        else:
                            this_team_row_color = color_list[1]

                        team_html_str += "<tr style='background-color: " + this_team_row_color + ";'>"

                        team_html_str += "<td width='50%' align='center' id='td_team_" + str(
                            this_team_div_idx) + "_" + conference_str + "_division_" + str(
                            conf_division_idx) + "' class='td_team'>"
                        team_html_str += "<input type='text' id='" + conference_str + "_division_" + str(
                            conf_division_idx) + "_team_" + str(
                            this_team_div_idx) + "' name='" + conference_str + "_division_" + str(
                            conf_division_idx) + "_team_" + str(
                            this_team_div_idx) + "' class='team' maxlength='35' value='" + this_team_name + "' style='width: 220px; border: none; background: transparent; text-align:center; font-weight: bold;' />"
                        team_html_str += "</td></tr>"

                    team_html_str += "</table></td>"

                    if conf_division_idx * 2 == actual_division_number:
                        team_html_str += "</tr>"

        team_html_str += "</table>"

    return team_html_str, city_nickname_to_city_id_dict, conference_name_list
