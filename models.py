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

class GameFbStats(models.Model):
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
        db_table = 'game_fb_stats'


class GameLbStats(models.Model):
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
        db_table = 'game_lb_stats'

class GameCbStats(models.Model):
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
        db_table = 'game_cb_stats'

class GameSfStats(models.Model):
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
        db_table = 'game_sf_stats'

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
    type_name = models.CharField(max_length=50)

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
    neutral_site_setting = models.BooleanField()
    num_playoff_teams_per_conference = models.IntegerField()
    num_weeks_regular_season = models.IntegerField()
    num_teams_per_conference = models.IntegerField()
    num_divisions_per_conference = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'league'


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=3, blank=True, null=True)
    last_name = models.CharField(max_length=45)
    number = models.IntegerField()
    age = models.IntegerField()
    first_season_id = models.IntegerField()
    last_season_id = models.IntegerField()
    injury_status = models.IntegerField()
    alma_mater = models.CharField(max_length=75)
    primary_position = models.CharField(max_length=3)
    secondary_position = models.CharField(blank=True, null=True, max_length=3)
    draft_position = models.CharField(max_length=5, blank=True, null=True)
    salary = models.IntegerField()
    height = models.CharField(max_length=4)
    weight = models.IntegerField()
    league = models.ForeignKey(League)
    playing_status = models.IntegerField()
    draft_value = models.FloatField()
    draft_rank = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player'


class PlayerGamePlays(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    game_play_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'player_game_plays'


class PlayerPool(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    status = models.IntegerField()
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'player_pool'


class PlayerSpecsDl(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    block_power_rating = models.DecimalField(max_digits=5, decimal_places=2)
    block_agility_rating = models.DecimalField(max_digits=5, decimal_places=2)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    pass_knockdown_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    tackle_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_inducement_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_recovery_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_dl'


class PlayerSpecsK(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    leg_rating = models.DecimalField(max_digits=5, decimal_places=2)
    accuracy_rating = models.DecimalField(max_digits=5, decimal_places=2)
    adjustment_rating = models.DecimalField(max_digits=5, decimal_places=2)
    onside_kick_rating = models.DecimalField(max_digits=5, decimal_places=2)
    directionality_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_k'


class PlayerSpecsOl(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    block_power_rating = models.DecimalField(max_digits=5, decimal_places=2)
    block_agility_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_recovery_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_ol'


class PlayerSpecsP(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    leg_rating = models.DecimalField(max_digits=5, decimal_places=2)
    directionality_rating = models.DecimalField(max_digits=5, decimal_places=2)
    hangtime_rating = models.DecimalField(max_digits=5, decimal_places=2)
    precision_rating = models.DecimalField(max_digits=5, decimal_places=2)
    consistency_rating = models.DecimalField(max_digits=5, decimal_places=2)
    surehands_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_p'


class PlayerSpecsQb(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    arm_strength_rating = models.DecimalField(max_digits=5, decimal_places=2)
    arm_accuracy_rating = models.DecimalField(max_digits=5, decimal_places=2)
    intelligence_rating = models.DecimalField(max_digits=5, decimal_places=2)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    elusiveness_rating = models.DecimalField(max_digits=5, decimal_places=2)
    stamina_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_qb'


class PlayerSpecsRb(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    elusiveness_rating = models.DecimalField(max_digits=5, decimal_places=2)
    strength_rating = models.DecimalField(max_digits=5, decimal_places=2)
    ball_protection_rating = models.DecimalField(max_digits=5, decimal_places=2)
    catching_rating = models.DecimalField(max_digits=5, decimal_places=2)
    stamina_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_rb'

class PlayerSpecsFb(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    elusiveness_rating = models.DecimalField(max_digits=5, decimal_places=2)
    strength_rating = models.DecimalField(max_digits=5, decimal_places=2)
    ball_protection_rating = models.DecimalField(max_digits=5, decimal_places=2)
    catching_rating = models.DecimalField(max_digits=5, decimal_places=2)
    stamina_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_fb'


class PlayerSpecsLb(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    route_rating = models.DecimalField(max_digits=5, decimal_places=2)
    pass_defense_rating = models.DecimalField(max_digits=5, decimal_places=2)
    interception_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_inducement_rating = models.DecimalField(max_digits=5, decimal_places=2)
    tackle_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_lb'

class PlayerSpecsCb(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    route_rating = models.DecimalField(max_digits=5, decimal_places=2)
    pass_defense_rating = models.DecimalField(max_digits=5, decimal_places=2)
    interception_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_inducement_rating = models.DecimalField(max_digits=5, decimal_places=2)
    tackle_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_cb'

class PlayerSpecsSf(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    route_rating = models.DecimalField(max_digits=5, decimal_places=2)
    pass_defense_rating = models.DecimalField(max_digits=5, decimal_places=2)
    interception_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_inducement_rating = models.DecimalField(max_digits=5, decimal_places=2)
    tackle_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_sf'

class PlayerSpecsStd(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    agility_rating = models.DecimalField(max_digits=5, decimal_places=2)
    tackle_rating = models.DecimalField(max_digits=5, decimal_places=2)
    fumble_inducement_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_std'


class PlayerSpecsSto(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    elusiveness_rating = models.DecimalField(max_digits=5, decimal_places=2)
    strength_rating = models.DecimalField(max_digits=5, decimal_places=2)
    ball_protection_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_sto'


class PlayerSpecsTe(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    catching_rating = models.DecimalField(max_digits=5, decimal_places=2)
    route_rating = models.DecimalField(max_digits=5, decimal_places=2)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    ball_protection_rating = models.DecimalField(max_digits=5, decimal_places=2)
    strength_rating = models.DecimalField(max_digits=5, decimal_places=2)
    stamina_rating = models.DecimalField(max_digits=5, decimal_places=2)
    block_power_rating = models.DecimalField(max_digits=5, decimal_places=2)
    block_agility_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_te'


class PlayerSpecsWr(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    catching_rating = models.DecimalField(max_digits=5, decimal_places=2)
    route_rating = models.DecimalField(max_digits=5, decimal_places=2)
    jumping_rating = models.DecimalField(max_digits=5, decimal_places=2)
    speed_rating = models.DecimalField(max_digits=5, decimal_places=2)
    ball_protection_rating = models.DecimalField(max_digits=5, decimal_places=2)
    stamina_rating = models.DecimalField(max_digits=5, decimal_places=2)
    penalty_avoidance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    career_arc_dict = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'player_specs_wr'


class Season(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    season_year = models.IntegerField()
    league = models.ForeignKey(League)
    created_draft_list = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'season'


class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.CharField(max_length=60)
    stadium_capacity = models.IntegerField()
    city = models.ForeignKey(City)
    is_dome = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'stadium'


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=50)
    first_season_id = models.IntegerField()
    current_season_wins = models.IntegerField()
    current_season_losses = models.IntegerField()
    stadium = models.ForeignKey(Stadium)
    conference = models.ForeignKey(Conference)
    division = models.ForeignKey(Division)
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'team'

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    season = models.ForeignKey(Season)
    gamedate = models.DateField()
    first_team_id = models.IntegerField()
    second_team_id = models.IntegerField()
    home_team_city_id = models.ForeignKey(City, db_column='home_team_city_id')
    week = models.IntegerField()
    game_type = models.ForeignKey(GameType)
    first_team_points = models.IntegerField()
    second_team_points = models.IntegerField()
    num_overtimes = models.IntegerField()
    stadium = models.ForeignKey(Stadium)
    attendance = models.IntegerField()
    league = models.ForeignKey(League)
    is_neutral_site_game = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'game'

class Draft(models.Model):
    id = models.IntegerField(primary_key=True)
    host_city_id = models.IntegerField()
    season_id = models.IntegerField()
    num_rounds = models.IntegerField()
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'draft'

class DraftPick(models.Model):
    id = models.IntegerField(primary_key=True)
    draft = models.ForeignKey(Draft)
    round = models.IntegerField()
    pick_number = models.IntegerField()
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player)

    class Meta:
        managed = True
        db_table = 'draft_pick'

class PlayerTeam(models.Model):
    player_team_id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    season_id = models.IntegerField()
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'player_team'

class TeamCity(models.Model):
    team_city_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team)
    city = models.ForeignKey(City)
    first_season_id = models.IntegerField()
    stadium = models.ForeignKey(Stadium)
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'team_city'


class TeamSeason(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Team)
    season = models.ForeignKey(Season)
    league = models.ForeignKey(League)

    class Meta:
        managed = True
        db_table = 'team_season'
