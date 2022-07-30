--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    city_id integer NOT NULL,
    city_name character varying(50) NOT NULL,
    city_weather_profile_id integer NOT NULL
);


ALTER TABLE public.city OWNER TO postgres;

--
-- Name: coach; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coach (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    middle_initial character varying(1) NOT NULL,
    last_name character varying(35) NOT NULL,
    risk_profile_id integer NOT NULL,
    time_management_skills_id integer NOT NULL
);


ALTER TABLE public.coach OWNER TO postgres;

--
-- Name: conference; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.conference (
    id integer NOT NULL,
    conference_name character varying(35) NOT NULL,
    league_id integer,
    first_season_id integer
);


ALTER TABLE public.conference OWNER TO postgres;

--
-- Name: default_teams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.default_teams (
    id integer NOT NULL,
    city_id integer NOT NULL,
    nickname character varying(25) NOT NULL,
    logo_file_name text
);


ALTER TABLE public.default_teams OWNER TO postgres;

--
-- Name: division; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.division (
    id integer NOT NULL,
    division_name character varying(25) NOT NULL,
    conference_id integer NOT NULL,
    first_season_id integer NOT NULL,
    league_id integer NOT NULL
);


ALTER TABLE public.division OWNER TO postgres;

--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO django;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO django;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: django
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: draft; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.draft (
    id integer NOT NULL,
    host_city_id integer NOT NULL,
    season_id integer NOT NULL,
    num_rounds integer NOT NULL,
    league_id integer
);


ALTER TABLE public.draft OWNER TO postgres;

--
-- Name: draft_pick; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.draft_pick (
    id integer NOT NULL,
    draft_id integer NOT NULL,
    round integer NOT NULL,
    pick_number integer NOT NULL,
    player_id integer NOT NULL,
    team_id integer NOT NULL
);


ALTER TABLE public.draft_pick OWNER TO postgres;

--
-- Name: game; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game (
    id integer NOT NULL,
    season_id integer NOT NULL,
    gamedate date NOT NULL,
    visiting_team_id integer NOT NULL,
    home_team_id integer NOT NULL,
    home_team_city_id integer NOT NULL,
    week integer NOT NULL,
    game_type_id integer NOT NULL,
    visiting_team_points integer NOT NULL,
    home_team_points integer NOT NULL,
    num_overtimes integer NOT NULL,
    stadium_id integer NOT NULL,
    attendance integer NOT NULL,
    league_id integer NOT NULL
);


ALTER TABLE public.game OWNER TO postgres;

--
-- Name: game_cb_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_cb_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_receptions_allowed integer NOT NULL,
    num_challenges integer NOT NULL,
    num_interceptions integer NOT NULL,
    int_return_yards integer NOT NULL,
    int_return_tds integer NOT NULL,
    num_fumbles_recovered integer NOT NULL,
    fumble_return_yards integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL
);


ALTER TABLE public.game_cb_stats OWNER TO postgres;

--
-- Name: game_dl_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_dl_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_block_wins integer NOT NULL,
    num_block_losses integer NOT NULL,
    num_block_draws integer NOT NULL,
    num_sacks integer NOT NULL,
    num_times_pancaked integer NOT NULL,
    num_fumble_recoveries integer NOT NULL,
    num_interceptions integer NOT NULL,
    interception_return_yards integer NOT NULL,
    interception_return_tds integer NOT NULL,
    interception_return_2_point_conversions integer NOT NULL,
    fumble_return_yards integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL
);


ALTER TABLE public.game_dl_stats OWNER TO postgres;

--
-- Name: game_fb_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_fb_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    rushing_yards integer NOT NULL,
    rushing_attempts integer NOT NULL,
    receiving_yards integer NOT NULL,
    rushing_tds integer NOT NULL,
    receiving_tds integer NOT NULL,
    rushing_2_point_conversions integer NOT NULL,
    receiving_2_point_conversions integer NOT NULL,
    num_fumbles integer NOT NULL,
    num_block_wins integer NOT NULL,
    num_block_losses integer NOT NULL,
    num_block_draws integer NOT NULL,
    passing_yards integer NOT NULL,
    passing_tds integer NOT NULL,
    passing_attempts integer NOT NULL
);


ALTER TABLE public.game_fb_stats OWNER TO postgres;

--
-- Name: game_k_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_k_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_xps integer NOT NULL,
    num_xp_attempts integer NOT NULL,
    num_fgs integer NOT NULL,
    num_fg_attempts integer NOT NULL,
    rushing_yards integer NOT NULL,
    rushing_attempts integer NOT NULL,
    rushing_tds integer NOT NULL,
    passing_yards integer NOT NULL,
    passing_attempts integer NOT NULL,
    passing_tds integer NOT NULL
);


ALTER TABLE public.game_k_stats OWNER TO postgres;

--
-- Name: game_lb_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_lb_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_receptions_allowed integer NOT NULL,
    num_challenges integer NOT NULL,
    num_interceptions integer NOT NULL,
    int_return_yards integer NOT NULL,
    int_return_tds integer NOT NULL,
    num_fumbles_recovered integer NOT NULL,
    fumble_return_yards integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL
);


ALTER TABLE public.game_lb_stats OWNER TO postgres;

--
-- Name: game_ol_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_ol_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_block_wins integer NOT NULL,
    num_block_losses integer NOT NULL,
    num_block_draws integer NOT NULL,
    pancake_blocks integer NOT NULL,
    sacks_allowed integer NOT NULL,
    fumble_recoveries integer NOT NULL
);


ALTER TABLE public.game_ol_stats OWNER TO postgres;

--
-- Name: game_p_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_p_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_punts integer NOT NULL,
    yards_per_punt integer NOT NULL,
    rushing_yards integer NOT NULL,
    rushing_attempts integer NOT NULL,
    rushing_tds integer NOT NULL,
    passing_yards integer NOT NULL,
    passing_attempts integer NOT NULL,
    passing_tds integer NOT NULL
);


ALTER TABLE public.game_p_stats OWNER TO postgres;

--
-- Name: game_player_penalty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_player_penalty (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    penalty_play_id integer NOT NULL
);


ALTER TABLE public.game_player_penalty OWNER TO postgres;

--
-- Name: game_plays; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_plays (
    id integer NOT NULL,
    game_id integer NOT NULL,
    play_type smallint NOT NULL,
    play_yards integer NOT NULL,
    play_points smallint NOT NULL,
    turnover_type smallint,
    source_play_id integer
);


ALTER TABLE public.game_plays OWNER TO postgres;

--
-- Name: game_qb_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_qb_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    passing_yards integer NOT NULL,
    rushing_yards integer NOT NULL,
    num_pass_completions integer NOT NULL,
    num_pass_attempts integer NOT NULL,
    num_interceptions integer NOT NULL,
    num_fumbles integer NOT NULL,
    passing_tds integer NOT NULL,
    rushing_tds integer NOT NULL,
    qbr double precision NOT NULL,
    num_times_sacked integer NOT NULL,
    passing_2_point_conversions integer NOT NULL,
    rushing_2_point_conversions integer NOT NULL,
    receiving_yards integer NOT NULL,
    num_receptions integer NOT NULL,
    rush_attempts integer NOT NULL
);


ALTER TABLE public.game_qb_stats OWNER TO postgres;

--
-- Name: game_rb_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_rb_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    rushing_yards integer NOT NULL,
    rushing_attempts integer NOT NULL,
    receiving_yards integer NOT NULL,
    rushing_tds integer NOT NULL,
    receiving_tds integer NOT NULL,
    rushing_2_point_conversions integer NOT NULL,
    receiving_2_point_conversions integer NOT NULL,
    num_fumbles integer NOT NULL,
    num_block_wins integer NOT NULL,
    num_block_losses integer NOT NULL,
    num_block_draws integer NOT NULL,
    passing_yards integer NOT NULL,
    passing_tds integer NOT NULL,
    passing_attempts integer NOT NULL
);


ALTER TABLE public.game_rb_stats OWNER TO postgres;

--
-- Name: game_sf_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_sf_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_receptions_allowed integer NOT NULL,
    num_challenges integer NOT NULL,
    num_interceptions integer NOT NULL,
    int_return_yards integer NOT NULL,
    int_return_tds integer NOT NULL,
    num_fumbles_recovered integer NOT NULL,
    fumble_return_yards integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL
);


ALTER TABLE public.game_sf_stats OWNER TO postgres;

--
-- Name: game_std_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_std_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL,
    num_fumble_recoveries integer NOT NULL,
    fumble_recovery_yards integer NOT NULL,
    fumble_recovery_tds integer NOT NULL
);


ALTER TABLE public.game_std_stats OWNER TO postgres;

--
-- Name: game_sto_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_sto_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    kickoff_return_yards integer NOT NULL,
    kickoff_return_attempts integer NOT NULL,
    kickoff_return_tds integer NOT NULL,
    punt_return_yards integer NOT NULL,
    punt_return_attempts integer NOT NULL,
    punt_return_tds integer NOT NULL,
    num_fumbles integer NOT NULL
);


ALTER TABLE public.game_sto_stats OWNER TO postgres;

--
-- Name: game_te_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_te_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    receiving_yards integer NOT NULL,
    num_receptions integer NOT NULL,
    num_receiving_tds integer NOT NULL,
    num_receiving_2_point_conversions integer NOT NULL,
    num_block_wins integer NOT NULL,
    num_block_losses integer NOT NULL,
    num_block_draws integer NOT NULL
);


ALTER TABLE public.game_te_stats OWNER TO postgres;

--
-- Name: game_team_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_team_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    home_or_visitor character varying(1) NOT NULL,
    team_id integer NOT NULL,
    points integer NOT NULL,
    rushing_yards integer NOT NULL,
    passing_yards integer NOT NULL,
    num_penalties integer NOT NULL,
    penalty_yards integer NOT NULL,
    kickoff_return_yards integer NOT NULL,
    punt_return_yards integer NOT NULL,
    num_first_downs integer NOT NULL,
    num_touchdowns integer NOT NULL,
    num_fgs integer NOT NULL,
    num_safeties integer NOT NULL,
    num_sacks integer NOT NULL,
    num_interceptions integer NOT NULL,
    num_fumbles integer NOT NULL,
    num_blocked_punts integer NOT NULL,
    num_blocked_fgs integer NOT NULL,
    num_fg_attempts integer NOT NULL,
    num_punts integer NOT NULL,
    num_third_down_conversions integer NOT NULL,
    num_third_down_attempts integer NOT NULL,
    num_fourth_down_conversions integer NOT NULL,
    num_fourth_down_attempts integer NOT NULL,
    num_kickoff_return_tds integer NOT NULL,
    num_punt_return_tds integer NOT NULL,
    num_two_point_conversions integer NOT NULL,
    num_two_point_attempts integer NOT NULL,
    num_pass_completions integer NOT NULL,
    num_pass_attempts integer NOT NULL,
    num_rush_attempts integer NOT NULL,
    num_times_in_red_zone integer NOT NULL,
    num_tds_in_red_zone integer NOT NULL,
    num_xps integer NOT NULL,
    num_xp_attempts integer NOT NULL,
    num_blocked_xps integer NOT NULL,
    num_blocked_fg_tds integer NOT NULL,
    num_blocked_punt_tds integer NOT NULL,
    num_blocked_xp_scores integer NOT NULL,
    ol_team_block_wins integer NOT NULL,
    ol_team_block_losses integer NOT NULL,
    ol_team_block_draws integer NOT NULL,
    pancake_blocks integer NOT NULL,
    num_sacks_allowed integer NOT NULL,
    num_tackles integer NOT NULL,
    num_forced_fumbles integer NOT NULL,
    num_2_point_conversions integer NOT NULL,
    num_2_point_conversion_attempts integer NOT NULL,
    dl_team_block_wins integer NOT NULL,
    dl_team_block_losses integer NOT NULL,
    dl_team_block_draws integer NOT NULL
);


ALTER TABLE public.game_team_stats OWNER TO postgres;

--
-- Name: game_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_type (
    id integer NOT NULL,
    type_id integer NOT NULL
);


ALTER TABLE public.game_type OWNER TO postgres;

--
-- Name: game_wr_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_wr_stats (
    id integer NOT NULL,
    game_id integer NOT NULL,
    player_id integer NOT NULL,
    receiving_yards integer NOT NULL,
    num_receptions integer NOT NULL,
    rushing_yards integer NOT NULL,
    rushing_attempts integer NOT NULL,
    num_receiving_tds integer NOT NULL,
    num_receiving_2_point_conversions integer NOT NULL,
    num_rushing_tds integer NOT NULL,
    num_rushing_2_point_conversions integer NOT NULL
);


ALTER TABLE public.game_wr_stats OWNER TO postgres;

--
-- Name: league; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.league (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    abbreviation character varying(4),
    weather_setting boolean,
    injury_setting boolean,
    female_setting boolean,
    neutral_site_setting boolean,
    num_playoff_teams_per_conference integer,
    num_weeks_regular_season integer,
    num_teams_per_conference integer,
    num_divisions_per_conference integer
);


ALTER TABLE public.league OWNER TO postgres;

--
-- Name: player; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    middle_initial character varying(3),
    last_name character varying(45) NOT NULL,
    number integer,
    age integer NOT NULL,
    first_season_id integer NOT NULL,
    last_season_id integer NOT NULL,
    injury_status integer NOT NULL,
    alma_mater character varying(75) NOT NULL,
    primary_position character varying(3) NOT NULL,
    secondary_position character varying(3),
    draft_position character varying(5),
    salary integer NOT NULL,
    height character varying(4) NOT NULL,
    weight integer NOT NULL,
    league_id integer NOT NULL,
    playing_status integer,
    draft_value real,
    draft_rank integer
);


ALTER TABLE public.player OWNER TO postgres;

--
-- Name: player_game_plays; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_game_plays (
    id integer NOT NULL,
    player_id integer NOT NULL,
    game_play_id integer NOT NULL
);


ALTER TABLE public.player_game_plays OWNER TO postgres;

--
-- Name: player_pool; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_pool (
    id integer NOT NULL,
    player_id integer NOT NULL,
    status integer NOT NULL,
    league_id integer NOT NULL
);


ALTER TABLE public.player_pool OWNER TO postgres;

--
-- Name: player_specs_cb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_cb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    route_rating real NOT NULL,
    pass_defense_rating real NOT NULL,
    interception_rating real NOT NULL,
    fumble_inducement_rating real NOT NULL,
    tackle_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_cb OWNER TO postgres;

--
-- Name: player_specs_dl; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_dl (
    id integer NOT NULL,
    player_id integer NOT NULL,
    block_power_rating real NOT NULL,
    block_agility_rating real NOT NULL,
    speed_rating real NOT NULL,
    pass_knockdown_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    tackle_rating real NOT NULL,
    fumble_inducement_rating real NOT NULL,
    fumble_recovery_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_dl OWNER TO postgres;

--
-- Name: player_specs_fb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_fb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    elusiveness_rating real NOT NULL,
    strength_rating real NOT NULL,
    ball_protection_rating real NOT NULL,
    catching_rating real NOT NULL,
    stamina_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_fb OWNER TO postgres;

--
-- Name: player_specs_k; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_k (
    id integer NOT NULL,
    player_id integer NOT NULL,
    leg_rating real NOT NULL,
    accuracy_rating real NOT NULL,
    adjustment_rating real NOT NULL,
    onside_kick_rating real NOT NULL,
    directionality_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_k OWNER TO postgres;

--
-- Name: player_specs_lb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_lb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    route_rating real NOT NULL,
    pass_defense_rating real NOT NULL,
    interception_rating real NOT NULL,
    fumble_inducement_rating real NOT NULL,
    tackle_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_lb OWNER TO postgres;

--
-- Name: player_specs_ol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_ol (
    id integer NOT NULL,
    player_id integer NOT NULL,
    block_power_rating real NOT NULL,
    block_agility_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    fumble_recovery_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_ol OWNER TO postgres;

--
-- Name: player_specs_p; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_p (
    id integer NOT NULL,
    player_id integer NOT NULL,
    leg_rating real NOT NULL,
    directionality_rating real NOT NULL,
    hangtime_rating real NOT NULL,
    precision_rating real NOT NULL,
    consistency_rating real NOT NULL,
    surehands_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_p OWNER TO postgres;

--
-- Name: player_specs_qb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_qb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    arm_strength_rating real NOT NULL,
    arm_accuracy_rating real NOT NULL,
    intelligence_rating real NOT NULL,
    speed_rating real NOT NULL,
    elusiveness_rating real NOT NULL,
    stamina_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_qb OWNER TO postgres;

--
-- Name: player_specs_rb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_rb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    elusiveness_rating real NOT NULL,
    strength_rating real NOT NULL,
    ball_protection_rating real NOT NULL,
    catching_rating real NOT NULL,
    stamina_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_rb OWNER TO postgres;

--
-- Name: player_specs_sf; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_sf (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    route_rating real NOT NULL,
    pass_defense_rating real NOT NULL,
    interception_rating real NOT NULL,
    fumble_inducement_rating real NOT NULL,
    tackle_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_sf OWNER TO postgres;

--
-- Name: player_specs_std; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_std (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    agility_rating real NOT NULL,
    tackle_rating real NOT NULL,
    fumble_inducement_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_std OWNER TO postgres;

--
-- Name: player_specs_sto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_sto (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating real NOT NULL,
    elusiveness_rating real NOT NULL,
    strength_rating real NOT NULL,
    ball_protection_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_sto OWNER TO postgres;

--
-- Name: player_specs_te; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_te (
    id integer NOT NULL,
    player_id integer NOT NULL,
    catching_rating real NOT NULL,
    route_rating real NOT NULL,
    speed_rating real NOT NULL,
    ball_protection_rating real NOT NULL,
    strength_rating real NOT NULL,
    stamina_rating real NOT NULL,
    block_power_rating real NOT NULL,
    block_agility_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_te OWNER TO postgres;

--
-- Name: player_specs_wr; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_wr (
    id integer NOT NULL,
    player_id integer NOT NULL,
    catching_rating real NOT NULL,
    route_rating real NOT NULL,
    jumping_rating real NOT NULL,
    speed_rating real NOT NULL,
    ball_protection_rating real NOT NULL,
    stamina_rating real NOT NULL,
    penalty_avoidance_rating real NOT NULL,
    career_arc_dict text NOT NULL
);


ALTER TABLE public.player_specs_wr OWNER TO postgres;

--
-- Name: player_team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_team (
    player_team_id integer NOT NULL,
    player_id integer NOT NULL,
    team_id integer NOT NULL,
    season_id integer NOT NULL,
    league_id integer
);


ALTER TABLE public.player_team OWNER TO postgres;

--
-- Name: season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.season (
    id integer NOT NULL,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    season_year integer NOT NULL,
    league_id integer NOT NULL,
    created_draft_list boolean
);


ALTER TABLE public.season OWNER TO postgres;

--
-- Name: stadium; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stadium (
    stadium_id integer NOT NULL,
    stadium_name character varying(60) NOT NULL,
    stadium_capacity integer NOT NULL,
    city_id integer NOT NULL,
    is_dome boolean NOT NULL
);


ALTER TABLE public.stadium OWNER TO postgres;

--
-- Name: team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team (
    id integer NOT NULL,
    nickname character varying(50) NOT NULL,
    first_season_id integer NOT NULL,
    current_season_wins integer NOT NULL,
    current_season_losses integer NOT NULL,
    stadium_id integer,
    conference_id integer,
    division_id integer,
    league_id integer
);


ALTER TABLE public.team OWNER TO postgres;

--
-- Name: team_city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_city (
    team_city_id integer NOT NULL,
    team_id integer NOT NULL,
    city_id integer NOT NULL,
    first_season_id integer NOT NULL,
    stadium_id integer NOT NULL,
    league_id integer
);


ALTER TABLE public.team_city OWNER TO postgres;

--
-- Name: team_season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.team_season (
    id integer NOT NULL,
    team_id integer NOT NULL,
    season_id integer NOT NULL
);


ALTER TABLE public.team_season OWNER TO postgres;

--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.city VALUES (1, 'New York', 1);
INSERT INTO public.city VALUES (2, 'Miami', 1);
INSERT INTO public.city VALUES (3, 'Atlanta', 1);
INSERT INTO public.city VALUES (4, 'Buffalo', 1);
INSERT INTO public.city VALUES (5, 'Washington', 1);
INSERT INTO public.city VALUES (6, 'Philadelphia', 1);
INSERT INTO public.city VALUES (7, 'Chicago', 1);
INSERT INTO public.city VALUES (8, 'Detroit', 1);
INSERT INTO public.city VALUES (9, 'Pittsburgh', 1);
INSERT INTO public.city VALUES (10, 'Green Bay', 1);
INSERT INTO public.city VALUES (11, 'New Orleans', 1);
INSERT INTO public.city VALUES (12, 'Cincinnati', 1);
INSERT INTO public.city VALUES (13, 'Dallas', 1);
INSERT INTO public.city VALUES (14, 'Minnesota', 1);
INSERT INTO public.city VALUES (15, 'Kansas City', 1);
INSERT INTO public.city VALUES (16, 'Denver', 1);
INSERT INTO public.city VALUES (17, 'St. Louis', 1);
INSERT INTO public.city VALUES (18, 'Houston', 1);
INSERT INTO public.city VALUES (19, 'Seattle', 1);
INSERT INTO public.city VALUES (20, 'San Francisco', 1);
INSERT INTO public.city VALUES (21, 'Oakland', 1);
INSERT INTO public.city VALUES (22, 'San Diego', 1);
INSERT INTO public.city VALUES (23, 'Arizona', 1);
INSERT INTO public.city VALUES (24, 'Las Vegas', 1);
INSERT INTO public.city VALUES (25, 'Boston', 1);
INSERT INTO public.city VALUES (26, 'Indianapolis', 1);
INSERT INTO public.city VALUES (27, 'Oklahoma City', 1);
INSERT INTO public.city VALUES (28, 'Los Angeles', 1);
INSERT INTO public.city VALUES (29, 'Carolina', 1);
INSERT INTO public.city VALUES (30, 'Cleveland', 1);
INSERT INTO public.city VALUES (31, 'Omaha', 1);
INSERT INTO public.city VALUES (32, 'Portland', 1);
INSERT INTO public.city VALUES (33, 'London', 1);
INSERT INTO public.city VALUES (34, 'Chennai', 1);
INSERT INTO public.city VALUES (35, 'Reykjavik', 1);
INSERT INTO public.city VALUES (36, 'Kinshasa', 1);


--
-- Data for Name: coach; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: conference; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: default_teams; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.default_teams VALUES (1, 1, 'Titans', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (3, 3, 'Talons', 'atlanta_talons.png');
INSERT INTO public.default_teams VALUES (4, 4, 'Bison', 'buffalo_bison.png');
INSERT INTO public.default_teams VALUES (5, 5, 'Fascists', 'washington_fascists.png');
INSERT INTO public.default_teams VALUES (6, 6, 'Vermin', 'philadelphia_vermin.png');
INSERT INTO public.default_teams VALUES (7, 7, 'Soldiers', 'chicago_soldiers.png');
INSERT INTO public.default_teams VALUES (8, 8, 'Autos', 'detroit_autos.png');
INSERT INTO public.default_teams VALUES (9, 9, 'Steel', 'pittsburgh_steel.png');
INSERT INTO public.default_teams VALUES (10, 10, 'Cheeseheads', 'green_bay_cheeseheads.png');
INSERT INTO public.default_teams VALUES (11, 11, 'Melody', 'new_orleans_melody.png');
INSERT INTO public.default_teams VALUES (12, 12, 'Inferno', 'cincinnati_inferno.png');
INSERT INTO public.default_teams VALUES (13, 13, 'Lone Stars', 'dallas_lone_stars.png');
INSERT INTO public.default_teams VALUES (14, 14, 'Nordics', 'minnesota_nordics.png');
INSERT INTO public.default_teams VALUES (15, 15, 'Tomahawks', 'kansas_city_tomahawks.png');
INSERT INTO public.default_teams VALUES (18, 18, 'Brawlers', 'houston_brawlers.png');
INSERT INTO public.default_teams VALUES (16, 16, '14ers', 'denver_14ers.png');
INSERT INTO public.default_teams VALUES (17, 17, 'Bighorns', 'st_louis_bighorns.png');
INSERT INTO public.default_teams VALUES (22, 22, 'Sharks', 'san_diego_sharks.png');
INSERT INTO public.default_teams VALUES (21, 21, 'Knights', 'oakland_knights.png');
INSERT INTO public.default_teams VALUES (20, 20, 'Goldens', 'san_francisco_goldens.png');
INSERT INTO public.default_teams VALUES (19, 19, 'Tsunami', 'seattle_tsunami.png');
INSERT INTO public.default_teams VALUES (23, 23, 'Vistas', 'arizona_vistas.png');
INSERT INTO public.default_teams VALUES (24, 24, 'Rollers', 'las_vegas_rollers.png');
INSERT INTO public.default_teams VALUES (25, 25, 'Beaneaters', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (26, 26, 'Peytons', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (27, 27, 'F5s', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (28, 28, 'Alisters', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (29, 29, 'Panteras', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (30, 30, 'Tans', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (31, 31, 'Cornhuskers', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (32, 32, 'Goonies', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (2, 2, 'Agujas', 'miami_agujas.png');


--
-- Data for Name: division; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: django
--



--
-- Data for Name: draft; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: draft_pick; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_cb_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_dl_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_fb_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_k_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_lb_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_ol_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_p_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_player_penalty; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_plays; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_qb_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_rb_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_sf_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_std_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_sto_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_te_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_team_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_type; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: game_wr_stats; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: league; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_game_plays; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_pool; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_cb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_dl; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_fb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_k; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_lb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_ol; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_p; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_qb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_rb; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_sf; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_std; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_sto; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_te; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_specs_wr; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: player_team; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: season; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: stadium; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.stadium VALUES (1, 'Titans Stadium', 75000, 1, false);
INSERT INTO public.stadium VALUES (2, 'South Beach Field', 71500, 2, false);
INSERT INTO public.stadium VALUES (3, 'The Peach Dome', 82000, 3, true);
INSERT INTO public.stadium VALUES (4, 'Bison Park', 80000, 4, false);
INSERT INTO public.stadium VALUES (5, 'Corruption Field', 78500, 5, false);
INSERT INTO public.stadium VALUES (6, 'The Sewers', 74750, 6, false);
INSERT INTO public.stadium VALUES (7, 'Soldier Stadium', 88700, 7, false);
INSERT INTO public.stadium VALUES (8, 'Soul Stadium', 81300, 8, true);
INSERT INTO public.stadium VALUES (9, 'The Foundry', 82450, 9, false);
INSERT INTO public.stadium VALUES (10, 'The Ice Bowl', 94500, 10, false);
INSERT INTO public.stadium VALUES (11, 'The Bourbon Dome', 76500, 11, true);
INSERT INTO public.stadium VALUES (12, 'Nasty Natti Stadium', 73700, 12, false);
INSERT INTO public.stadium VALUES (13, 'Lone Star Stadium', 86000, 13, false);
INSERT INTO public.stadium VALUES (14, 'The Berserker Dome', 80500, 14, true);
INSERT INTO public.stadium VALUES (15, 'Tomahawk Stadium', 88300, 15, false);
INSERT INTO public.stadium VALUES (16, 'Elway Stadium', 83900, 16, false);
INSERT INTO public.stadium VALUES (17, 'The Gateway Dome', 79200, 17, true);
INSERT INTO public.stadium VALUES (18, 'Oiler Stadium', 85600, 18, false);
INSERT INTO public.stadium VALUES (19, 'The Tsunami Dome', 91030, 19, true);
INSERT INTO public.stadium VALUES (20, 'Golden Gate Field', 79830, 20, false);
INSERT INTO public.stadium VALUES (21, 'Thunderdome', 84675, 21, false);
INSERT INTO public.stadium VALUES (22, 'Ocean Beach Field', 81290, 22, false);
INSERT INTO public.stadium VALUES (23, 'Grand Canyon Field', 86250, 23, false);
INSERT INTO public.stadium VALUES (24, 'Caesars Castle', 84350, 24, false);
INSERT INTO public.stadium VALUES (26, 'Queen Elizabeth Stadium', 102000, 33, false);
INSERT INTO public.stadium VALUES (27, 'Chennai Stadium', 115000, 34, false);
INSERT INTO public.stadium VALUES (25, 'Aurora Borealis Field', 69800, 35, false);
INSERT INTO public.stadium VALUES (28, 'Rumble in the Jungle Field', 80000, 36, false);
INSERT INTO public.stadium VALUES (29, 'Hidden Microphone Field', 70000, 25, false);
INSERT INTO public.stadium VALUES (30, 'Peyton Park', 80000, 26, true);
INSERT INTO public.stadium VALUES (31, 'The Tornado Shelter', 72500, 27, true);
INSERT INTO public.stadium VALUES (32, 'The Hollywood Bowl', 80000, 28, false);
INSERT INTO public.stadium VALUES (33, 'Blue Ridge Stadium', 69800, 29, false);
INSERT INTO public.stadium VALUES (34, 'The Dog Bowl', 81000, 30, false);
INSERT INTO public.stadium VALUES (35, 'The Corn Fields', 83600, 31, false);
INSERT INTO public.stadium VALUES (36, 'The Old Warehouse', 70000, 32, false);


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: team_city; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: team_season; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 1, false);


--
-- Name: city city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pkey PRIMARY KEY (city_id);


--
-- Name: coach coach_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coach
    ADD CONSTRAINT coach_pkey PRIMARY KEY (id);


--
-- Name: conference conference_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_pkey PRIMARY KEY (id);


--
-- Name: default_teams default_teams_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.default_teams
    ADD CONSTRAINT default_teams_pkey PRIMARY KEY (id);


--
-- Name: division division_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.division
    ADD CONSTRAINT division_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: draft_pick draft_pick_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.draft_pick
    ADD CONSTRAINT draft_pick_pkey PRIMARY KEY (id);


--
-- Name: draft draft_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.draft
    ADD CONSTRAINT draft_pkey PRIMARY KEY (id);


--
-- Name: game_cb_stats game_cb_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_cb_stats
    ADD CONSTRAINT game_cb_stats_pkey PRIMARY KEY (id);


--
-- Name: game_dl_stats game_dl_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_dl_stats
    ADD CONSTRAINT game_dl_stats_pkey PRIMARY KEY (id);


--
-- Name: game_fb_stats game_fb_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_fb_stats
    ADD CONSTRAINT game_fb_stats_pkey PRIMARY KEY (id);


--
-- Name: game_k_stats game_k_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_k_stats
    ADD CONSTRAINT game_k_stats_pkey PRIMARY KEY (id);


--
-- Name: game_lb_stats game_lb_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_lb_stats
    ADD CONSTRAINT game_lb_stats_pkey PRIMARY KEY (id);


--
-- Name: game_ol_stats game_ol_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_ol_stats
    ADD CONSTRAINT game_ol_stats_pkey PRIMARY KEY (id);


--
-- Name: game_p_stats game_p_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_p_stats
    ADD CONSTRAINT game_p_stats_pkey PRIMARY KEY (id);


--
-- Name: game game_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game
    ADD CONSTRAINT game_pkey PRIMARY KEY (id);


--
-- Name: game_player_penalty game_player_penalty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_player_penalty
    ADD CONSTRAINT game_player_penalty_pkey PRIMARY KEY (id);


--
-- Name: game_plays game_plays_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_plays
    ADD CONSTRAINT game_plays_pkey PRIMARY KEY (id);


--
-- Name: game_qb_stats game_qb_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_qb_stats
    ADD CONSTRAINT game_qb_stats_pkey PRIMARY KEY (id);


--
-- Name: game_rb_stats game_rb_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_rb_stats
    ADD CONSTRAINT game_rb_stats_pkey PRIMARY KEY (id);


--
-- Name: game_sf_stats game_sf_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sf_stats
    ADD CONSTRAINT game_sf_stats_pkey PRIMARY KEY (id);


--
-- Name: game_std_stats game_std_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_std_stats
    ADD CONSTRAINT game_std_stats_pkey PRIMARY KEY (id);


--
-- Name: game_sto_stats game_sto_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sto_stats
    ADD CONSTRAINT game_sto_stats_pkey PRIMARY KEY (id);


--
-- Name: game_te_stats game_te_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_te_stats
    ADD CONSTRAINT game_te_stats_pkey PRIMARY KEY (id);


--
-- Name: game_team_stats game_team_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_team_stats
    ADD CONSTRAINT game_team_stats_pkey PRIMARY KEY (id);


--
-- Name: game_type game_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_type
    ADD CONSTRAINT game_type_pkey PRIMARY KEY (id);


--
-- Name: game_wr_stats game_wr_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_wr_stats
    ADD CONSTRAINT game_wr_stats_pkey PRIMARY KEY (id);


--
-- Name: league league_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.league
    ADD CONSTRAINT league_pkey PRIMARY KEY (id);


--
-- Name: player_game_plays player_game_plays_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_game_plays
    ADD CONSTRAINT player_game_plays_pkey PRIMARY KEY (id);


--
-- Name: player_specs_ol player_ol_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_ol
    ADD CONSTRAINT player_ol_stats_pkey PRIMARY KEY (id);


--
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);


--
-- Name: player_pool player_pool_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_pool
    ADD CONSTRAINT player_pool_pkey PRIMARY KEY (id);


--
-- Name: player_specs_cb player_specs_cb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_cb
    ADD CONSTRAINT player_specs_cb_pkey PRIMARY KEY (id);


--
-- Name: player_specs_dl player_specs_dl_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_dl
    ADD CONSTRAINT player_specs_dl_pkey PRIMARY KEY (id);


--
-- Name: player_specs_fb player_specs_fb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_fb
    ADD CONSTRAINT player_specs_fb_pkey PRIMARY KEY (id);


--
-- Name: player_specs_k player_specs_k_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_k
    ADD CONSTRAINT player_specs_k_pkey PRIMARY KEY (id);


--
-- Name: player_specs_lb player_specs_lb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_lb
    ADD CONSTRAINT player_specs_lb_pkey PRIMARY KEY (id);


--
-- Name: player_specs_p player_specs_p_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_p
    ADD CONSTRAINT player_specs_p_pkey PRIMARY KEY (id);


--
-- Name: player_specs_qb player_specs_qb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_qb
    ADD CONSTRAINT player_specs_qb_pkey PRIMARY KEY (id);


--
-- Name: player_specs_rb player_specs_rb_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_rb
    ADD CONSTRAINT player_specs_rb_pkey PRIMARY KEY (id);


--
-- Name: player_specs_sf player_specs_sf_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_sf
    ADD CONSTRAINT player_specs_sf_pkey PRIMARY KEY (id);


--
-- Name: player_specs_std player_specs_std_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_std
    ADD CONSTRAINT player_specs_std_pkey PRIMARY KEY (id);


--
-- Name: player_specs_sto player_specs_sto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_sto
    ADD CONSTRAINT player_specs_sto_pkey PRIMARY KEY (id);


--
-- Name: player_specs_te player_specs_te_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_te
    ADD CONSTRAINT player_specs_te_pkey PRIMARY KEY (id);


--
-- Name: player_specs_wr player_specs_wr_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_wr
    ADD CONSTRAINT player_specs_wr_pkey PRIMARY KEY (id);


--
-- Name: player_team player_team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_team
    ADD CONSTRAINT player_team_pkey PRIMARY KEY (player_team_id);


--
-- Name: season season_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.season
    ADD CONSTRAINT season_pkey PRIMARY KEY (id);


--
-- Name: stadium stadium_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadium
    ADD CONSTRAINT stadium_pkey PRIMARY KEY (stadium_id);


--
-- Name: team_city team_city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_city
    ADD CONSTRAINT team_city_pkey PRIMARY KEY (team_city_id);


--
-- Name: team team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team
    ADD CONSTRAINT team_pkey PRIMARY KEY (id);


--
-- Name: team_season team_season_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.team_season
    ADD CONSTRAINT team_season_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

