from django.db import models

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=50)
    city_weather_profile_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'city'


class Coach(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=35)
    risk_profile_id = models.IntegerField()
    time_management_skills_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'coach'


class Conference(models.Model):
    id = models.IntegerField(primary_key=True)
    conference_name = models.CharField(max_length=35)
    first_season_id = models.IntegerField()
    league_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'conference'

class DefaultTeams(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.ForeignKey(City)
    nickname = models.CharField(max_length=25)
    logo_file_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'default_teams'

class Division(models.Model):
    id = models.IntegerField(primary_key=True)
    division_name = models.CharField(max_length=25)
    conference_id = models.IntegerField()
    first_season_id = models.IntegerField()
    league_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'division'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Draft(models.Model):
    id = models.IntegerField(primary_key=True)
    host_city_id = models.IntegerField()
    season_id = models.IntegerField()
    num_rounds = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'draft'


class DraftPick(models.Model):
    id = models.IntegerField(primary_key=True)
    draft_id = models.IntegerField()
    round = models.IntegerField()
    pick_number = models.IntegerField()
    selected_player_id = models.IntegerField()
    team_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'draft_pick'


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    season_id = models.IntegerField()
    gamedate = models.DateField()
    visiting_team_id = models.IntegerField()
    home_team_id = models.IntegerField()
    home_team_city_id = models.IntegerField()
    week = models.IntegerField()
    game_type_id = models.IntegerField()
    visiting_team_points = models.IntegerField()
    home_team_points = models.IntegerField()
    num_overtimes = models.IntegerField()
    stadium_id = models.IntegerField()
    attendance = models.IntegerField()
    league_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game'


class GameDlStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_block_wins = models.IntegerField()
    num_block_losses = models.IntegerField()
    num_block_draws = models.IntegerField()
    num_sacks = models.IntegerField()
    num_times_pancaked = models.IntegerField()
    num_fumble_recoveries = models.IntegerField()
    num_interceptions = models.IntegerField()
    interception_return_yards = models.IntegerField()
    interception_return_tds = models.IntegerField()
    interception_return_2_point_conversions = models.IntegerField()
    fumble_return_yards = models.IntegerField()
    num_tackles = models.IntegerField()
    num_forced_fumbles = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_dl_stats'


class GameKStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_xps = models.IntegerField()
    num_xp_attempts = models.IntegerField()
    num_fgs = models.IntegerField()
    num_fg_attempts = models.IntegerField()
    rushing_yards = models.IntegerField()
    rushing_attempts = models.IntegerField()
    rushing_tds = models.IntegerField()
    passing_yards = models.IntegerField()
    passing_attempts = models.IntegerField()
    passing_tds = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_k_stats'


class GameOlStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_block_wins = models.IntegerField()
    num_block_losses = models.IntegerField()
    num_block_draws = models.IntegerField()
    pancake_blocks = models.IntegerField()
    sacks_allowed = models.IntegerField()
    fumble_recoveries = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_ol_stats'


class GamePStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_punts = models.IntegerField()
    yards_per_punt = models.IntegerField()
    rushing_yards = models.IntegerField()
    rushing_attempts = models.IntegerField()
    rushing_tds = models.IntegerField()
    passing_yards = models.IntegerField()
    passing_attempts = models.IntegerField()
    passing_tds = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_p_stats'


class GamePlayerPenalty(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    penalty_play_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_player_penalty'


class GamePlays(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    play_type = models.SmallIntegerField()
    play_yards = models.IntegerField()
    play_points = models.SmallIntegerField()
    turnover_type = models.SmallIntegerField(blank=True, null=True)
    source_play_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'game_plays'


class GameQbStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    passing_yards = models.IntegerField()
    rushing_yards = models.IntegerField()
    num_pass_completions = models.IntegerField()
    num_pass_attempts = models.IntegerField()
    num_interceptions = models.IntegerField()
    num_fumbles = models.IntegerField()
    passing_tds = models.IntegerField()
    rushing_tds = models.IntegerField()
    qbr = models.FloatField()
    num_times_sacked = models.IntegerField()
    passing_2_point_conversions = models.IntegerField()
    rushing_2_point_conversions = models.IntegerField()
    receiving_yards = models.IntegerField()
    num_receptions = models.IntegerField()
    rush_attempts = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_qb_stats'


class GameRbStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    rushing_yards = models.IntegerField()
    rushing_attempts = models.IntegerField()
    receiving_yards = models.IntegerField()
    rushing_tds = models.IntegerField()
    receiving_tds = models.IntegerField()
    rushing_2_point_conversions = models.IntegerField()
    receiving_2_point_conversions = models.IntegerField()
    num_fumbles = models.IntegerField()
    num_block_wins = models.IntegerField()
    num_block_losses = models.IntegerField()
    num_block_draws = models.IntegerField()
    passing_yards = models.IntegerField()
    passing_tds = models.IntegerField()
    passing_attempts = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_rb_stats'


class GameSecStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_receptions_allowed = models.IntegerField()
    num_challenges = models.IntegerField()
    num_interceptions = models.IntegerField()
    int_return_yards = models.IntegerField()
    int_return_tds = models.IntegerField()
    num_fumbles_recovered = models.IntegerField()
    fumble_return_yards = models.IntegerField()
    num_tackles = models.IntegerField()
    num_forced_fumbles = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_sec_stats'


class GameStdStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    num_tackles = models.IntegerField()
    num_forced_fumbles = models.IntegerField()
    num_fumble_recoveries = models.IntegerField()
    fumble_recovery_yards = models.IntegerField()
    fumble_recovery_tds = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_std_stats'


class GameStoStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    kickoff_return_yards = models.IntegerField()
    kickoff_return_attempts = models.IntegerField()
    kickoff_return_tds = models.IntegerField()
    punt_return_yards = models.IntegerField()
    punt_return_attempts = models.IntegerField()
    punt_return_tds = models.IntegerField()
    num_fumbles = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_sto_stats'


class GameTeStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    receiving_yards = models.IntegerField()
    num_receptions = models.IntegerField()
    num_receiving_tds = models.IntegerField()
    num_receiving_2_point_conversions = models.IntegerField()
    num_block_wins = models.IntegerField()
    num_block_losses = models.IntegerField()
    num_block_draws = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_te_stats'


class GameTeamStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    home_or_visitor = models.CharField(max_length=1)
    team_id = models.IntegerField()
    points = models.IntegerField()
    rushing_yards = models.IntegerField()
    passing_yards = models.IntegerField()
    num_penalties = models.IntegerField()
    penalty_yards = models.IntegerField()
    kickoff_return_yards = models.IntegerField()
    punt_return_yards = models.IntegerField()
    num_first_downs = models.IntegerField()
    num_touchdowns = models.IntegerField()
    num_fgs = models.IntegerField()
    num_safeties = models.IntegerField()
    num_sacks = models.IntegerField()
    num_interceptions = models.IntegerField()
    num_fumbles = models.IntegerField()
    num_blocked_punts = models.IntegerField()
    num_blocked_fgs = models.IntegerField()
    num_fg_attempts = models.IntegerField()
    num_punts = models.IntegerField()
    num_third_down_conversions = models.IntegerField()
    num_third_down_attempts = models.IntegerField()
    num_fourth_down_conversions = models.IntegerField()
    num_fourth_down_attempts = models.IntegerField()
    num_kickoff_return_tds = models.IntegerField()
    num_punt_return_tds = models.IntegerField()
    num_two_point_conversions = models.IntegerField()
    num_two_point_attempts = models.IntegerField()
    num_pass_completions = models.IntegerField()
    num_pass_attempts = models.IntegerField()
    num_rush_attempts = models.IntegerField()
    num_times_in_red_zone = models.IntegerField()
    num_tds_in_red_zone = models.IntegerField()
    num_xps = models.IntegerField()
    num_xp_attempts = models.IntegerField()
    num_blocked_xps = models.IntegerField()
    num_blocked_fg_tds = models.IntegerField()
    num_blocked_punt_tds = models.IntegerField()
    num_blocked_xp_scores = models.IntegerField()
    ol_team_block_wins = models.IntegerField()
    ol_team_block_losses = models.IntegerField()
    ol_team_block_draws = models.IntegerField()
    pancake_blocks = models.IntegerField()
    num_sacks_allowed = models.IntegerField()
    num_tackles = models.IntegerField()
    num_forced_fumbles = models.IntegerField()
    num_2_point_conversions = models.IntegerField()
    num_2_point_conversion_attempts = models.IntegerField()
    dl_team_block_wins = models.IntegerField()
    dl_team_block_losses = models.IntegerField()
    dl_team_block_draws = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_team_stats'


class GameType(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_type'


class GameWrStats(models.Model):
    id = models.IntegerField(primary_key=True)
    game_id = models.IntegerField()
    player_id = models.IntegerField()
    receiving_yards = models.IntegerField()
    num_receptions = models.IntegerField()
    rushing_yards = models.IntegerField()
    rushing_attempts = models.IntegerField()
    num_receiving_tds = models.IntegerField()
    num_receiving_2_point_conversions = models.IntegerField()
    num_rushing_tds = models.IntegerField()
    num_rushing_2_point_conversions = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'game_wr_stats'


class League(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=4, blank=True, null=True)
    weather_setting = models.BooleanField()
    injury_setting = models.BooleanField()
    female_setting = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'league'


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=45)
    number = models.IntegerField()
    age = models.IntegerField()
    first_season_id = models.IntegerField()
    last_season_id = models.IntegerField()
    injury_status = models.IntegerField()
    alma_mater = models.CharField(max_length=75)
    primary_position = models.IntegerField()
    secondary_position = models.IntegerField(blank=True, null=True)
    draft_position = models.CharField(max_length=5, blank=True, null=True)
    salary = models.IntegerField()
    height = models.CharField(max_length=4)
    weight = models.IntegerField()
    league_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player'


class PlayerGamePlays(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    game_play_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player_game_plays'


class PlayerPool(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    status = models.IntegerField()
    league_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player_pool'


class PlayerSpecsDl(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    block_power_rating = models.IntegerField()
    block_agility_rating = models.IntegerField()
    speed_rating = models.IntegerField()
    pass_knockdown_rating = models.IntegerField()
    penalty_avoidance_rating = models.IntegerField()
    tackle_rating = models.IntegerField()
    fumble_inducement_rating = models.IntegerField()
    fumble_recovery_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_dl'


class PlayerSpecsK(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    leg_rating = models.IntegerField()
    accuracy_rating = models.IntegerField()
    adjustment_rating = models.IntegerField()
    onside_kick_rating = models.IntegerField()
    directionality_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_k'


class PlayerSpecsOl(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    block_power_rating = models.IntegerField()
    block_agility_rating = models.IntegerField()
    penalty_avoidance_rating = models.IntegerField()
    fumble_recovery_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_ol'


class PlayerSpecsP(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    leg_rating = models.IntegerField()
    directionality_rating = models.IntegerField()
    hangtime_rating = models.IntegerField()
    precision_rating = models.IntegerField()
    consistency_rating = models.IntegerField()
    surehands_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_p'


class PlayerSpecsQb(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    arm_strength_rating = models.IntegerField()
    arm_accuracy_rating = models.IntegerField()
    intelligence_rating = models.IntegerField()
    speed_rating = models.IntegerField()
    elusiveness_rating = models.IntegerField()
    stamina_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_qb'


class PlayerSpecsRb(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    speed_rating = models.IntegerField()
    elusiveness_rating = models.IntegerField()
    strength_rating = models.IntegerField()
    ball_protection_rating = models.IntegerField()
    catching_rating = models.IntegerField()
    stamina_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_rb'


class PlayerSpecsSec(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    speed_rating = models.IntegerField()
    route_rating = models.IntegerField()
    pass_defense_rating = models.IntegerField()
    interception_rating = models.IntegerField()
    fumble_inducement_rating = models.IntegerField()
    tackle_rating = models.IntegerField()
    penalty_avoidance_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_sec'


class PlayerSpecsStd(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    speed_rating = models.IntegerField()
    agility_rating = models.IntegerField()
    tackle_rating = models.IntegerField()
    fumble_inducment_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_std'


class PlayerSpecsSto(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    speed_rating = models.IntegerField()
    elusiveness_rating = models.IntegerField()
    strength_rating = models.IntegerField()
    ball_protection_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_sto'


class PlayerSpecsTe(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    catching_rating = models.IntegerField()
    route_rating = models.IntegerField()
    speed_rating = models.IntegerField()
    ball_protection_rating = models.IntegerField()
    strength_rating = models.IntegerField()
    stamina_rating = models.IntegerField()
    block_power_rating = models.IntegerField()
    block_agility_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_te'


class PlayerSpecsWr(models.Model):
    id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    catching_rating = models.IntegerField()
    route_rating = models.IntegerField()
    jumping_rating = models.IntegerField()
    speed_rating = models.IntegerField()
    ball_protection_rating = models.IntegerField()
    stamina_rating = models.IntegerField()
    penalty_avoidance_rating = models.IntegerField()
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_wr'


class PlayerTeam(models.Model):
    player_team_id = models.IntegerField(primary_key=True)
    player_id = models.IntegerField()
    team_id = models.IntegerField()
    season_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player_team'


class Season(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    season_year = models.IntegerField()
    league_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'season'


class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.CharField(max_length=60)
    stadium_capacity = models.IntegerField()
    city_id = models.IntegerField()
    is_dome = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'stadium'


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    first_season_id = models.IntegerField()
    current_season_wins = models.IntegerField()
    current_season_losses = models.IntegerField()
    stadium_id = models.IntegerField()
    conference_id = models.IntegerField()
    division_id = models.IntegerField()
    league_id = models.IntegerField()
    nickname = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'team'


class TeamCity(models.Model):
    team_city_id = models.IntegerField(primary_key=True)
    team_id = models.IntegerField()
    city_id = models.IntegerField()
    first_season_id = models.IntegerField()
    stadium_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'team_city'


class TeamSeason(models.Model):
    id = models.IntegerField(primary_key=True)
    team_id = models.IntegerField()
    season_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'team_season'
