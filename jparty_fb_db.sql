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
    selected_player_id integer NOT NULL,
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
    female_setting boolean
);


ALTER TABLE public.league OWNER TO postgres;

--
-- Name: player; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    middle_initial character varying(1),
    last_name character varying(45) NOT NULL,
    number integer NOT NULL,
    age integer NOT NULL,
    first_season_id integer NOT NULL,
    last_season_id integer NOT NULL,
    injury_status integer NOT NULL,
    alma_mater character varying(75) NOT NULL,
    primary_position integer NOT NULL,
    secondary_position integer,
    draft_position character varying(5),
    salary integer NOT NULL,
    height character varying(4) NOT NULL,
    weight integer NOT NULL,
    league_id integer NOT NULL
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
    speed_rating integer NOT NULL,
    route_rating integer NOT NULL,
    pass_defense_rating integer NOT NULL,
    interception_rating integer NOT NULL,
    fumble_inducement_rating integer NOT NULL,
    tackle_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_cb OWNER TO postgres;

--
-- Name: player_specs_dl; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_dl (
    id integer NOT NULL,
    player_id integer NOT NULL,
    block_power_rating integer NOT NULL,
    block_agility_rating integer NOT NULL,
    speed_rating integer NOT NULL,
    pass_knockdown_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    tackle_rating integer NOT NULL,
    fumble_inducement_rating integer NOT NULL,
    fumble_recovery_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_dl OWNER TO postgres;

--
-- Name: player_specs_fb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_fb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    elusiveness_rating integer NOT NULL,
    strength_rating integer NOT NULL,
    ball_protection_rating integer NOT NULL,
    catching_rating integer NOT NULL,
    stamina_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_fb OWNER TO postgres;

--
-- Name: player_specs_k; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_k (
    id integer NOT NULL,
    player_id integer NOT NULL,
    leg_rating integer NOT NULL,
    accuracy_rating integer NOT NULL,
    adjustment_rating integer NOT NULL,
    onside_kick_rating integer NOT NULL,
    directionality_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_k OWNER TO postgres;

--
-- Name: player_specs_lb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_lb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    route_rating integer NOT NULL,
    pass_defense_rating integer NOT NULL,
    interception_rating integer NOT NULL,
    fumble_inducement_rating integer NOT NULL,
    tackle_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_lb OWNER TO postgres;

--
-- Name: player_specs_ol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_ol (
    id integer NOT NULL,
    player_id integer NOT NULL,
    block_power_rating integer NOT NULL,
    block_agility_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    fumble_recovery_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_ol OWNER TO postgres;

--
-- Name: player_specs_p; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_p (
    id integer NOT NULL,
    player_id integer NOT NULL,
    leg_rating integer NOT NULL,
    directionality_rating integer NOT NULL,
    hangtime_rating integer NOT NULL,
    precision_rating integer NOT NULL,
    consistency_rating integer NOT NULL,
    surehands_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_p OWNER TO postgres;

--
-- Name: player_specs_qb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_qb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    arm_strength_rating integer NOT NULL,
    arm_accuracy_rating integer NOT NULL,
    intelligence_rating integer NOT NULL,
    speed_rating integer NOT NULL,
    elusiveness_rating integer NOT NULL,
    stamina_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_qb OWNER TO postgres;

--
-- Name: player_specs_rb; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_rb (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    elusiveness_rating integer NOT NULL,
    strength_rating integer NOT NULL,
    ball_protection_rating integer NOT NULL,
    catching_rating integer NOT NULL,
    stamina_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_rb OWNER TO postgres;

--
-- Name: player_specs_sf; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_sf (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    route_rating integer NOT NULL,
    pass_defense_rating integer NOT NULL,
    interception_rating integer NOT NULL,
    fumble_inducement_rating integer NOT NULL,
    tackle_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_sf OWNER TO postgres;

--
-- Name: player_specs_std; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_std (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    agility_rating integer NOT NULL,
    tackle_rating integer NOT NULL,
    fumble_inducment_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_std OWNER TO postgres;

--
-- Name: player_specs_sto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_sto (
    id integer NOT NULL,
    player_id integer NOT NULL,
    speed_rating integer NOT NULL,
    elusiveness_rating integer NOT NULL,
    strength_rating integer NOT NULL,
    ball_protection_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_sto OWNER TO postgres;

--
-- Name: player_specs_te; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_te (
    id integer NOT NULL,
    player_id integer NOT NULL,
    catching_rating integer NOT NULL,
    route_rating integer NOT NULL,
    speed_rating integer NOT NULL,
    ball_protection_rating integer NOT NULL,
    strength_rating integer NOT NULL,
    stamina_rating integer NOT NULL,
    block_power_rating integer NOT NULL,
    block_agility_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_te OWNER TO postgres;

--
-- Name: player_specs_wr; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_wr (
    id integer NOT NULL,
    player_id integer NOT NULL,
    catching_rating integer NOT NULL,
    route_rating integer NOT NULL,
    jumping_rating integer NOT NULL,
    speed_rating integer NOT NULL,
    ball_protection_rating integer NOT NULL,
    stamina_rating integer NOT NULL,
    penalty_avoidance_rating integer NOT NULL,
    career_arc_dict json NOT NULL
);


ALTER TABLE public.player_specs_wr OWNER TO postgres;

--
-- Name: player_team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_team (
    player_team_id integer NOT NULL,
    player_id integer NOT NULL,
    team_id integer NOT NULL,
    season_id integer NOT NULL
);


ALTER TABLE public.player_team OWNER TO postgres;

--
-- Name: season; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.season (
    id integer NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone NOT NULL,
    season_year integer NOT NULL,
    league_id integer NOT NULL
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
    stadium_id integer NOT NULL
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


--
-- Data for Name: coach; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: conference; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.conference VALUES (1, 'Eastern', 1, NULL);
INSERT INTO public.conference VALUES (2, 'Western', 1, NULL);
INSERT INTO public.conference VALUES (3, 'Eastern', 2, NULL);
INSERT INTO public.conference VALUES (4, 'Western', 2, NULL);
INSERT INTO public.conference VALUES (5, 'Eastern', 3, NULL);
INSERT INTO public.conference VALUES (6, 'Western', 3, NULL);
INSERT INTO public.conference VALUES (7, 'Eastern', 4, NULL);
INSERT INTO public.conference VALUES (8, 'Western', 4, NULL);
INSERT INTO public.conference VALUES (9, 'Eastern', 5, NULL);
INSERT INTO public.conference VALUES (10, 'Western', 5, NULL);
INSERT INTO public.conference VALUES (11, 'Eastern', 6, NULL);
INSERT INTO public.conference VALUES (12, 'Western', 6, NULL);
INSERT INTO public.conference VALUES (13, 'Eastern', 7, NULL);
INSERT INTO public.conference VALUES (14, 'Western', 7, NULL);
INSERT INTO public.conference VALUES (15, 'Eastern', 8, NULL);
INSERT INTO public.conference VALUES (16, 'Western', 8, NULL);
INSERT INTO public.conference VALUES (17, 'Eastern', 9, NULL);
INSERT INTO public.conference VALUES (18, 'Western', 9, NULL);


--
-- Data for Name: default_teams; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.default_teams VALUES (1, 1, 'Titans', 'new_york_titans.png');
INSERT INTO public.default_teams VALUES (2, 2, 'Swordfish', 'miami_swordfish.png');
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


--
-- Data for Name: division; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.division VALUES (1, 'Eastern Division 1', 1, -1, 1);
INSERT INTO public.division VALUES (2, 'Western Division 1', 2, -1, 1);
INSERT INTO public.division VALUES (3, 'Eastern Division 2', 1, -1, 1);
INSERT INTO public.division VALUES (4, 'Western Division 2', 2, -1, 1);
INSERT INTO public.division VALUES (5, 'Eastern Division 1', 3, -1, 2);
INSERT INTO public.division VALUES (6, 'Western Division 1', 4, -1, 2);
INSERT INTO public.division VALUES (7, 'Eastern Division 2', 3, -1, 2);
INSERT INTO public.division VALUES (8, 'Western Division 2', 4, -1, 2);
INSERT INTO public.division VALUES (9, 'Eastern Division 1', 5, -1, 3);
INSERT INTO public.division VALUES (10, 'Western Division 1', 6, -1, 3);
INSERT INTO public.division VALUES (11, 'Eastern Division 2', 5, -1, 3);
INSERT INTO public.division VALUES (12, 'Western Division 2', 6, -1, 3);
INSERT INTO public.division VALUES (13, 'Eastern Division 1', 7, -1, 4);
INSERT INTO public.division VALUES (14, 'Western Division 1', 8, -1, 4);
INSERT INTO public.division VALUES (15, 'Eastern Division 2', 7, -1, 4);
INSERT INTO public.division VALUES (16, 'Western Division 2', 8, -1, 4);
INSERT INTO public.division VALUES (17, 'Eastern Division 1', 9, -1, 5);
INSERT INTO public.division VALUES (18, 'Western Division 1', 10, -1, 5);
INSERT INTO public.division VALUES (19, 'Eastern Division 2', 9, -1, 5);
INSERT INTO public.division VALUES (20, 'Western Division 2', 10, -1, 5);
INSERT INTO public.division VALUES (21, 'Eastern Division 1', 11, -1, 6);
INSERT INTO public.division VALUES (22, 'Western Division 1', 12, -1, 6);
INSERT INTO public.division VALUES (23, 'Eastern Division 2', 11, -1, 6);
INSERT INTO public.division VALUES (24, 'Western Division 2', 12, -1, 6);
INSERT INTO public.division VALUES (25, 'Eastern Division 1', 13, -1, 7);
INSERT INTO public.division VALUES (26, 'Western Division 1', 14, -1, 7);
INSERT INTO public.division VALUES (27, 'Eastern Division 2', 13, -1, 7);
INSERT INTO public.division VALUES (28, 'Western Division 2', 14, -1, 7);
INSERT INTO public.division VALUES (29, 'Eastern Division 1', 15, -1, 8);
INSERT INTO public.division VALUES (30, 'Western Division 1', 16, -1, 8);
INSERT INTO public.division VALUES (31, 'Eastern Division 2', 15, -1, 8);
INSERT INTO public.division VALUES (32, 'Western Division 2', 16, -1, 8);
INSERT INTO public.division VALUES (33, 'Eastern Division 1', 17, -1, 9);
INSERT INTO public.division VALUES (34, 'Western Division 1', 18, -1, 9);
INSERT INTO public.division VALUES (35, 'Eastern Division 2', 17, -1, 9);
INSERT INTO public.division VALUES (36, 'Western Division 2', 18, -1, 9);


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

INSERT INTO public.league VALUES (1, 'Jeff Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (2, 'Jeffy Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (3, 'Jeffy Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (4, 'Jeffy Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (5, 'Jeffy Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (6, 'Jeffy Football League', 'JFL', true, true, true);
INSERT INTO public.league VALUES (7, 'sasdadas sdaads League', 'SSL', true, true, true);
INSERT INTO public.league VALUES (8, 'adsdsa dsasad LwfSD', 'ADL', true, true, true);
INSERT INTO public.league VALUES (9, 'adsdsa dsasad LwfSD', 'ADL', true, true, true);


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
INSERT INTO public.stadium VALUES (25, 'Aurora Borealis Field', 69800, 25, false);
INSERT INTO public.stadium VALUES (26, 'Queen Elizabeth Stadium', 102000, 26, false);
INSERT INTO public.stadium VALUES (27, 'Chennai Stadium', 115000, 27, false);
INSERT INTO public.stadium VALUES (28, 'Rumble in the Jungle Field', 80000, 28, false);
INSERT INTO public.stadium VALUES (29, 'some stadium', 100000, 29, false);


--
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.team VALUES (1, 'Titans', -1, 0, 0, 1, 1, 1, 1);
INSERT INTO public.team VALUES (2, 'Swordfish', -1, 0, 0, 2, 1, 1, 1);
INSERT INTO public.team VALUES (3, 'Talons', -1, 0, 0, 3, 1, 1, 1);
INSERT INTO public.team VALUES (4, 'Bison', -1, 0, 0, 4, 1, 1, 1);
INSERT INTO public.team VALUES (5, 'Melody', -1, 0, 0, 11, 2, 2, 1);
INSERT INTO public.team VALUES (6, 'Steel', -1, 0, 0, 9, 2, 2, 1);
INSERT INTO public.team VALUES (7, 'Cheeseheads', -1, 0, 0, 10, 2, 2, 1);
INSERT INTO public.team VALUES (8, 'Inferno', -1, 0, 0, 12, 2, 2, 1);
INSERT INTO public.team VALUES (9, 'Fascists', -1, 0, 0, 5, 1, 3, 1);
INSERT INTO public.team VALUES (10, 'Vermin', -1, 0, 0, 6, 1, 3, 1);
INSERT INTO public.team VALUES (11, 'Soldiers', -1, 0, 0, 7, 1, 3, 1);
INSERT INTO public.team VALUES (12, 'Autos', -1, 0, 0, 8, 1, 3, 1);
INSERT INTO public.team VALUES (13, 'Lone Stars', -1, 0, 0, 13, 2, 4, 1);
INSERT INTO public.team VALUES (14, 'Nordics', -1, 0, 0, 14, 2, 4, 1);
INSERT INTO public.team VALUES (15, 'Tomahawks', -1, 0, 0, 15, 2, 4, 1);
INSERT INTO public.team VALUES (16, '14ers', -1, 0, 0, 16, 2, 4, 1);
INSERT INTO public.team VALUES (17, 'Titans', -1, 0, 0, 1, 3, 5, 2);
INSERT INTO public.team VALUES (18, 'Swordfish', -1, 0, 0, 2, 3, 5, 2);
INSERT INTO public.team VALUES (19, 'Talons', -1, 0, 0, 3, 3, 5, 2);
INSERT INTO public.team VALUES (20, 'Bison', -1, 0, 0, 4, 3, 5, 2);
INSERT INTO public.team VALUES (21, 'Steel', -1, 0, 0, 9, 4, 6, 2);
INSERT INTO public.team VALUES (22, 'Cheeseheads', -1, 0, 0, 10, 4, 6, 2);
INSERT INTO public.team VALUES (23, 'Melody', -1, 0, 0, 11, 4, 6, 2);
INSERT INTO public.team VALUES (24, 'Inferno', -1, 0, 0, 12, 4, 6, 2);
INSERT INTO public.team VALUES (25, 'Fascists', -1, 0, 0, 5, 3, 7, 2);
INSERT INTO public.team VALUES (26, 'Vermin', -1, 0, 0, 6, 3, 7, 2);
INSERT INTO public.team VALUES (27, 'Soldiers', -1, 0, 0, 7, 3, 7, 2);
INSERT INTO public.team VALUES (28, 'Autos', -1, 0, 0, 8, 3, 7, 2);
INSERT INTO public.team VALUES (29, 'Lone Stars', -1, 0, 0, 13, 4, 8, 2);
INSERT INTO public.team VALUES (30, 'Nordics', -1, 0, 0, 14, 4, 8, 2);
INSERT INTO public.team VALUES (31, 'Tomahawks', -1, 0, 0, 15, 4, 8, 2);
INSERT INTO public.team VALUES (32, '14ers', -1, 0, 0, 16, 4, 8, 2);
INSERT INTO public.team VALUES (33, 'Titans', -1, 0, 0, 1, 5, 9, 3);
INSERT INTO public.team VALUES (34, 'Swordfish', -1, 0, 0, 2, 5, 9, 3);
INSERT INTO public.team VALUES (35, 'Talons', -1, 0, 0, 3, 5, 9, 3);
INSERT INTO public.team VALUES (36, 'Bison', -1, 0, 0, 4, 5, 9, 3);
INSERT INTO public.team VALUES (37, 'Steel', -1, 0, 0, 9, 6, 10, 3);
INSERT INTO public.team VALUES (38, 'Cheeseheads', -1, 0, 0, 10, 6, 10, 3);
INSERT INTO public.team VALUES (39, 'Melody', -1, 0, 0, 11, 6, 10, 3);
INSERT INTO public.team VALUES (40, 'Inferno', -1, 0, 0, 12, 6, 10, 3);
INSERT INTO public.team VALUES (41, 'Fascists', -1, 0, 0, 5, 5, 11, 3);
INSERT INTO public.team VALUES (42, 'Vermin', -1, 0, 0, 6, 5, 11, 3);
INSERT INTO public.team VALUES (43, 'Soldiers', -1, 0, 0, 7, 5, 11, 3);
INSERT INTO public.team VALUES (44, 'Autos', -1, 0, 0, 8, 5, 11, 3);
INSERT INTO public.team VALUES (45, 'Lone Stars', -1, 0, 0, 13, 6, 12, 3);
INSERT INTO public.team VALUES (46, 'Nordics', -1, 0, 0, 14, 6, 12, 3);
INSERT INTO public.team VALUES (47, 'Tomahawks', -1, 0, 0, 15, 6, 12, 3);
INSERT INTO public.team VALUES (48, '14ers', -1, 0, 0, 16, 6, 12, 3);
INSERT INTO public.team VALUES (49, 'Titans', -1, 0, 0, 1, 7, 13, 4);
INSERT INTO public.team VALUES (50, 'Swordfish', -1, 0, 0, 2, 7, 13, 4);
INSERT INTO public.team VALUES (51, 'Talons', -1, 0, 0, 3, 7, 13, 4);
INSERT INTO public.team VALUES (52, 'Bison', -1, 0, 0, 4, 7, 13, 4);
INSERT INTO public.team VALUES (53, 'Steel', -1, 0, 0, 9, 8, 14, 4);
INSERT INTO public.team VALUES (54, 'Cheeseheads', -1, 0, 0, 10, 8, 14, 4);
INSERT INTO public.team VALUES (55, 'Melody', -1, 0, 0, 11, 8, 14, 4);
INSERT INTO public.team VALUES (56, 'Inferno', -1, 0, 0, 12, 8, 14, 4);
INSERT INTO public.team VALUES (57, 'Fascists', -1, 0, 0, 5, 7, 15, 4);
INSERT INTO public.team VALUES (58, 'Vermin', -1, 0, 0, 6, 7, 15, 4);
INSERT INTO public.team VALUES (59, 'Soldiers', -1, 0, 0, 7, 7, 15, 4);
INSERT INTO public.team VALUES (60, 'Autos', -1, 0, 0, 8, 7, 15, 4);
INSERT INTO public.team VALUES (61, 'Lone Stars', -1, 0, 0, 13, 8, 16, 4);
INSERT INTO public.team VALUES (62, 'Nordics', -1, 0, 0, 14, 8, 16, 4);
INSERT INTO public.team VALUES (63, 'Tomahawks', -1, 0, 0, 15, 8, 16, 4);
INSERT INTO public.team VALUES (64, '14ers', -1, 0, 0, 16, 8, 16, 4);
INSERT INTO public.team VALUES (65, 'Titans', -1, 0, 0, 1, 9, 17, 5);
INSERT INTO public.team VALUES (66, 'Swordfish', -1, 0, 0, 2, 9, 17, 5);
INSERT INTO public.team VALUES (67, 'Talons', -1, 0, 0, 3, 9, 17, 5);
INSERT INTO public.team VALUES (68, 'Bison', -1, 0, 0, 4, 9, 17, 5);
INSERT INTO public.team VALUES (69, 'Steel', -1, 0, 0, 9, 10, 18, 5);
INSERT INTO public.team VALUES (70, 'Cheeseheads', -1, 0, 0, 10, 10, 18, 5);
INSERT INTO public.team VALUES (71, 'Melody', -1, 0, 0, 11, 10, 18, 5);
INSERT INTO public.team VALUES (72, 'Inferno', -1, 0, 0, 12, 10, 18, 5);
INSERT INTO public.team VALUES (73, 'Fascists', -1, 0, 0, 5, 9, 19, 5);
INSERT INTO public.team VALUES (74, 'Vermin', -1, 0, 0, 6, 9, 19, 5);
INSERT INTO public.team VALUES (75, 'Soldiers', -1, 0, 0, 7, 9, 19, 5);
INSERT INTO public.team VALUES (76, 'Autos', -1, 0, 0, 8, 9, 19, 5);
INSERT INTO public.team VALUES (77, 'Lone Stars', -1, 0, 0, 13, 10, 20, 5);
INSERT INTO public.team VALUES (78, 'Nordics', -1, 0, 0, 14, 10, 20, 5);
INSERT INTO public.team VALUES (79, 'Tomahawks', -1, 0, 0, 15, 10, 20, 5);
INSERT INTO public.team VALUES (80, '14ers', -1, 0, 0, 16, 10, 20, 5);
INSERT INTO public.team VALUES (81, 'Titans', -1, 0, 0, 1, 11, 21, 6);
INSERT INTO public.team VALUES (82, 'Swordfish', -1, 0, 0, 2, 11, 21, 6);
INSERT INTO public.team VALUES (83, 'Talons', -1, 0, 0, 3, 11, 21, 6);
INSERT INTO public.team VALUES (84, 'Bison', -1, 0, 0, 4, 11, 21, 6);
INSERT INTO public.team VALUES (85, 'Steel', -1, 0, 0, 9, 12, 22, 6);
INSERT INTO public.team VALUES (86, 'Cheeseheads', -1, 0, 0, 10, 12, 22, 6);
INSERT INTO public.team VALUES (87, 'Melody', -1, 0, 0, 11, 12, 22, 6);
INSERT INTO public.team VALUES (88, 'Inferno', -1, 0, 0, 12, 12, 22, 6);
INSERT INTO public.team VALUES (89, 'Fascists', -1, 0, 0, 5, 11, 23, 6);
INSERT INTO public.team VALUES (90, 'Vermin', -1, 0, 0, 6, 11, 23, 6);
INSERT INTO public.team VALUES (91, 'Soldiers', -1, 0, 0, 7, 11, 23, 6);
INSERT INTO public.team VALUES (92, 'Autos', -1, 0, 0, 8, 11, 23, 6);
INSERT INTO public.team VALUES (93, 'Lone Stars', -1, 0, 0, 13, 12, 24, 6);
INSERT INTO public.team VALUES (94, 'Nordics', -1, 0, 0, 14, 12, 24, 6);
INSERT INTO public.team VALUES (95, 'Tomahawks', -1, 0, 0, 15, 12, 24, 6);
INSERT INTO public.team VALUES (96, '14ers', -1, 0, 0, 16, 12, 24, 6);
INSERT INTO public.team VALUES (97, 'Titans', -1, 0, 0, 1, 13, 25, 7);
INSERT INTO public.team VALUES (98, 'Swordfish', -1, 0, 0, 2, 13, 25, 7);
INSERT INTO public.team VALUES (99, 'Talons', -1, 0, 0, 3, 13, 25, 7);
INSERT INTO public.team VALUES (100, 'Bison', -1, 0, 0, 4, 13, 25, 7);
INSERT INTO public.team VALUES (101, 'Steel', -1, 0, 0, 9, 14, 26, 7);
INSERT INTO public.team VALUES (102, 'Cheeseheads', -1, 0, 0, 10, 14, 26, 7);
INSERT INTO public.team VALUES (103, 'Melody', -1, 0, 0, 11, 14, 26, 7);
INSERT INTO public.team VALUES (104, 'Inferno', -1, 0, 0, 12, 14, 26, 7);
INSERT INTO public.team VALUES (105, 'Fascists', -1, 0, 0, 5, 13, 27, 7);
INSERT INTO public.team VALUES (106, 'Vermin', -1, 0, 0, 6, 13, 27, 7);
INSERT INTO public.team VALUES (107, 'Soldiers', -1, 0, 0, 7, 13, 27, 7);
INSERT INTO public.team VALUES (108, 'Autos', -1, 0, 0, 8, 13, 27, 7);
INSERT INTO public.team VALUES (109, 'Lone Stars', -1, 0, 0, 13, 14, 28, 7);
INSERT INTO public.team VALUES (110, 'Nordics', -1, 0, 0, 14, 14, 28, 7);
INSERT INTO public.team VALUES (111, 'Tomahawks', -1, 0, 0, 15, 14, 28, 7);
INSERT INTO public.team VALUES (112, '14ers', -1, 0, 0, 16, 14, 28, 7);
INSERT INTO public.team VALUES (113, 'Titans', -1, 0, 0, 1, 15, 29, 8);
INSERT INTO public.team VALUES (114, 'Swordfish', -1, 0, 0, 2, 15, 29, 8);
INSERT INTO public.team VALUES (115, 'Talons', -1, 0, 0, 3, 15, 29, 8);
INSERT INTO public.team VALUES (116, 'Bison', -1, 0, 0, 4, 15, 29, 8);
INSERT INTO public.team VALUES (117, 'Steel', -1, 0, 0, 9, 16, 30, 8);
INSERT INTO public.team VALUES (118, 'Cheeseheads', -1, 0, 0, 10, 16, 30, 8);
INSERT INTO public.team VALUES (119, 'Melody', -1, 0, 0, 11, 16, 30, 8);
INSERT INTO public.team VALUES (120, 'Inferno', -1, 0, 0, 12, 16, 30, 8);
INSERT INTO public.team VALUES (121, 'Fascists', -1, 0, 0, 5, 15, 31, 8);
INSERT INTO public.team VALUES (122, 'Vermin', -1, 0, 0, 6, 15, 31, 8);
INSERT INTO public.team VALUES (123, 'Soldiers', -1, 0, 0, 7, 15, 31, 8);
INSERT INTO public.team VALUES (124, 'Autos', -1, 0, 0, 8, 15, 31, 8);
INSERT INTO public.team VALUES (125, 'Lone Stars', -1, 0, 0, 13, 16, 32, 8);
INSERT INTO public.team VALUES (126, 'Nordics', -1, 0, 0, 14, 16, 32, 8);
INSERT INTO public.team VALUES (127, 'Tomahawks', -1, 0, 0, 15, 16, 32, 8);
INSERT INTO public.team VALUES (128, '14ers', -1, 0, 0, 16, 16, 32, 8);
INSERT INTO public.team VALUES (129, 'Titans', -1, 0, 0, 1, 17, 33, 9);
INSERT INTO public.team VALUES (130, 'Swordfish', -1, 0, 0, 2, 17, 33, 9);
INSERT INTO public.team VALUES (131, 'Talons', -1, 0, 0, 3, 17, 33, 9);
INSERT INTO public.team VALUES (132, 'Bison', -1, 0, 0, 4, 17, 33, 9);
INSERT INTO public.team VALUES (133, 'Steel', -1, 0, 0, 9, 18, 34, 9);
INSERT INTO public.team VALUES (134, 'Cheeseheads', -1, 0, 0, 10, 18, 34, 9);
INSERT INTO public.team VALUES (135, 'Melody', -1, 0, 0, 11, 18, 34, 9);
INSERT INTO public.team VALUES (136, 'Inferno', -1, 0, 0, 12, 18, 34, 9);
INSERT INTO public.team VALUES (137, 'Fascists', -1, 0, 0, 5, 17, 35, 9);
INSERT INTO public.team VALUES (138, 'Vermin', -1, 0, 0, 6, 17, 35, 9);
INSERT INTO public.team VALUES (139, 'Soldiers', -1, 0, 0, 7, 17, 35, 9);
INSERT INTO public.team VALUES (140, 'Autos', -1, 0, 0, 8, 17, 35, 9);
INSERT INTO public.team VALUES (141, 'Lone Stars', -1, 0, 0, 13, 18, 36, 9);
INSERT INTO public.team VALUES (142, 'Nordics', -1, 0, 0, 14, 18, 36, 9);
INSERT INTO public.team VALUES (143, 'Tomahawks', -1, 0, 0, 15, 18, 36, 9);
INSERT INTO public.team VALUES (144, '14ers', -1, 0, 0, 16, 18, 36, 9);


--
-- Data for Name: team_city; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.team_city VALUES (1, 1, 1, -1, 1);
INSERT INTO public.team_city VALUES (2, 2, 2, -1, 2);
INSERT INTO public.team_city VALUES (3, 3, 3, -1, 3);
INSERT INTO public.team_city VALUES (4, 4, 4, -1, 4);
INSERT INTO public.team_city VALUES (5, 5, 11, -1, 11);
INSERT INTO public.team_city VALUES (6, 6, 9, -1, 9);
INSERT INTO public.team_city VALUES (7, 7, 10, -1, 10);
INSERT INTO public.team_city VALUES (8, 8, 12, -1, 12);
INSERT INTO public.team_city VALUES (9, 9, 5, -1, 5);
INSERT INTO public.team_city VALUES (10, 10, 6, -1, 6);
INSERT INTO public.team_city VALUES (11, 11, 7, -1, 7);
INSERT INTO public.team_city VALUES (12, 12, 8, -1, 8);
INSERT INTO public.team_city VALUES (13, 13, 13, -1, 13);
INSERT INTO public.team_city VALUES (14, 14, 14, -1, 14);
INSERT INTO public.team_city VALUES (15, 15, 15, -1, 15);
INSERT INTO public.team_city VALUES (16, 16, 16, -1, 16);
INSERT INTO public.team_city VALUES (17, 17, 1, -1, 1);
INSERT INTO public.team_city VALUES (18, 18, 2, -1, 2);
INSERT INTO public.team_city VALUES (19, 19, 3, -1, 3);
INSERT INTO public.team_city VALUES (20, 20, 4, -1, 4);
INSERT INTO public.team_city VALUES (21, 21, 9, -1, 9);
INSERT INTO public.team_city VALUES (22, 22, 10, -1, 10);
INSERT INTO public.team_city VALUES (23, 23, 11, -1, 11);
INSERT INTO public.team_city VALUES (24, 24, 12, -1, 12);
INSERT INTO public.team_city VALUES (25, 25, 5, -1, 5);
INSERT INTO public.team_city VALUES (26, 26, 6, -1, 6);
INSERT INTO public.team_city VALUES (27, 27, 7, -1, 7);
INSERT INTO public.team_city VALUES (28, 28, 8, -1, 8);
INSERT INTO public.team_city VALUES (29, 29, 13, -1, 13);
INSERT INTO public.team_city VALUES (30, 30, 14, -1, 14);
INSERT INTO public.team_city VALUES (31, 31, 15, -1, 15);
INSERT INTO public.team_city VALUES (32, 32, 16, -1, 16);
INSERT INTO public.team_city VALUES (33, 33, 1, -1, 1);
INSERT INTO public.team_city VALUES (34, 34, 2, -1, 2);
INSERT INTO public.team_city VALUES (35, 35, 3, -1, 3);
INSERT INTO public.team_city VALUES (36, 36, 4, -1, 4);
INSERT INTO public.team_city VALUES (37, 37, 9, -1, 9);
INSERT INTO public.team_city VALUES (38, 38, 10, -1, 10);
INSERT INTO public.team_city VALUES (39, 39, 11, -1, 11);
INSERT INTO public.team_city VALUES (40, 40, 12, -1, 12);
INSERT INTO public.team_city VALUES (41, 41, 5, -1, 5);
INSERT INTO public.team_city VALUES (42, 42, 6, -1, 6);
INSERT INTO public.team_city VALUES (43, 43, 7, -1, 7);
INSERT INTO public.team_city VALUES (44, 44, 8, -1, 8);
INSERT INTO public.team_city VALUES (45, 45, 13, -1, 13);
INSERT INTO public.team_city VALUES (46, 46, 14, -1, 14);
INSERT INTO public.team_city VALUES (47, 47, 15, -1, 15);
INSERT INTO public.team_city VALUES (48, 48, 16, -1, 16);
INSERT INTO public.team_city VALUES (49, 49, 1, -1, 1);
INSERT INTO public.team_city VALUES (50, 50, 2, -1, 2);
INSERT INTO public.team_city VALUES (51, 51, 3, -1, 3);
INSERT INTO public.team_city VALUES (52, 52, 4, -1, 4);
INSERT INTO public.team_city VALUES (53, 53, 9, -1, 9);
INSERT INTO public.team_city VALUES (54, 54, 10, -1, 10);
INSERT INTO public.team_city VALUES (55, 55, 11, -1, 11);
INSERT INTO public.team_city VALUES (56, 56, 12, -1, 12);
INSERT INTO public.team_city VALUES (57, 57, 5, -1, 5);
INSERT INTO public.team_city VALUES (58, 58, 6, -1, 6);
INSERT INTO public.team_city VALUES (59, 59, 7, -1, 7);
INSERT INTO public.team_city VALUES (60, 60, 8, -1, 8);
INSERT INTO public.team_city VALUES (61, 61, 13, -1, 13);
INSERT INTO public.team_city VALUES (62, 62, 14, -1, 14);
INSERT INTO public.team_city VALUES (63, 63, 15, -1, 15);
INSERT INTO public.team_city VALUES (64, 64, 16, -1, 16);
INSERT INTO public.team_city VALUES (65, 65, 1, -1, 1);
INSERT INTO public.team_city VALUES (66, 66, 2, -1, 2);
INSERT INTO public.team_city VALUES (67, 67, 3, -1, 3);
INSERT INTO public.team_city VALUES (68, 68, 4, -1, 4);
INSERT INTO public.team_city VALUES (69, 69, 9, -1, 9);
INSERT INTO public.team_city VALUES (70, 70, 10, -1, 10);
INSERT INTO public.team_city VALUES (71, 71, 11, -1, 11);
INSERT INTO public.team_city VALUES (72, 72, 12, -1, 12);
INSERT INTO public.team_city VALUES (73, 73, 5, -1, 5);
INSERT INTO public.team_city VALUES (74, 74, 6, -1, 6);
INSERT INTO public.team_city VALUES (75, 75, 7, -1, 7);
INSERT INTO public.team_city VALUES (76, 76, 8, -1, 8);
INSERT INTO public.team_city VALUES (77, 77, 13, -1, 13);
INSERT INTO public.team_city VALUES (78, 78, 14, -1, 14);
INSERT INTO public.team_city VALUES (79, 79, 15, -1, 15);
INSERT INTO public.team_city VALUES (80, 80, 16, -1, 16);
INSERT INTO public.team_city VALUES (81, 81, 1, -1, 1);
INSERT INTO public.team_city VALUES (82, 82, 2, -1, 2);
INSERT INTO public.team_city VALUES (83, 83, 3, -1, 3);
INSERT INTO public.team_city VALUES (84, 84, 4, -1, 4);
INSERT INTO public.team_city VALUES (85, 85, 9, -1, 9);
INSERT INTO public.team_city VALUES (86, 86, 10, -1, 10);
INSERT INTO public.team_city VALUES (87, 87, 11, -1, 11);
INSERT INTO public.team_city VALUES (88, 88, 12, -1, 12);
INSERT INTO public.team_city VALUES (89, 89, 5, -1, 5);
INSERT INTO public.team_city VALUES (90, 90, 6, -1, 6);
INSERT INTO public.team_city VALUES (91, 91, 7, -1, 7);
INSERT INTO public.team_city VALUES (92, 92, 8, -1, 8);
INSERT INTO public.team_city VALUES (93, 93, 13, -1, 13);
INSERT INTO public.team_city VALUES (94, 94, 14, -1, 14);
INSERT INTO public.team_city VALUES (95, 95, 15, -1, 15);
INSERT INTO public.team_city VALUES (96, 96, 16, -1, 16);
INSERT INTO public.team_city VALUES (97, 97, 1, -1, 1);
INSERT INTO public.team_city VALUES (98, 98, 2, -1, 2);
INSERT INTO public.team_city VALUES (99, 99, 3, -1, 3);
INSERT INTO public.team_city VALUES (100, 100, 4, -1, 4);
INSERT INTO public.team_city VALUES (101, 101, 9, -1, 9);
INSERT INTO public.team_city VALUES (102, 102, 10, -1, 10);
INSERT INTO public.team_city VALUES (103, 103, 11, -1, 11);
INSERT INTO public.team_city VALUES (104, 104, 12, -1, 12);
INSERT INTO public.team_city VALUES (105, 105, 5, -1, 5);
INSERT INTO public.team_city VALUES (106, 106, 6, -1, 6);
INSERT INTO public.team_city VALUES (107, 107, 7, -1, 7);
INSERT INTO public.team_city VALUES (108, 108, 8, -1, 8);
INSERT INTO public.team_city VALUES (109, 109, 13, -1, 13);
INSERT INTO public.team_city VALUES (110, 110, 14, -1, 14);
INSERT INTO public.team_city VALUES (111, 111, 15, -1, 15);
INSERT INTO public.team_city VALUES (112, 112, 16, -1, 16);
INSERT INTO public.team_city VALUES (113, 113, 1, -1, 1);
INSERT INTO public.team_city VALUES (114, 114, 2, -1, 2);
INSERT INTO public.team_city VALUES (115, 115, 3, -1, 3);
INSERT INTO public.team_city VALUES (116, 116, 4, -1, 4);
INSERT INTO public.team_city VALUES (117, 117, 9, -1, 9);
INSERT INTO public.team_city VALUES (118, 118, 10, -1, 10);
INSERT INTO public.team_city VALUES (119, 119, 11, -1, 11);
INSERT INTO public.team_city VALUES (120, 120, 12, -1, 12);
INSERT INTO public.team_city VALUES (121, 121, 5, -1, 5);
INSERT INTO public.team_city VALUES (122, 122, 6, -1, 6);
INSERT INTO public.team_city VALUES (123, 123, 7, -1, 7);
INSERT INTO public.team_city VALUES (124, 124, 8, -1, 8);
INSERT INTO public.team_city VALUES (125, 125, 13, -1, 13);
INSERT INTO public.team_city VALUES (126, 126, 14, -1, 14);
INSERT INTO public.team_city VALUES (127, 127, 15, -1, 15);
INSERT INTO public.team_city VALUES (128, 128, 16, -1, 16);
INSERT INTO public.team_city VALUES (129, 129, 1, -1, 1);
INSERT INTO public.team_city VALUES (130, 130, 2, -1, 2);
INSERT INTO public.team_city VALUES (131, 131, 3, -1, 3);
INSERT INTO public.team_city VALUES (132, 132, 4, -1, 4);
INSERT INTO public.team_city VALUES (133, 133, 9, -1, 9);
INSERT INTO public.team_city VALUES (134, 134, 10, -1, 10);
INSERT INTO public.team_city VALUES (135, 135, 11, -1, 11);
INSERT INTO public.team_city VALUES (136, 136, 12, -1, 12);
INSERT INTO public.team_city VALUES (137, 137, 5, -1, 5);
INSERT INTO public.team_city VALUES (138, 138, 6, -1, 6);
INSERT INTO public.team_city VALUES (139, 139, 7, -1, 7);
INSERT INTO public.team_city VALUES (140, 140, 8, -1, 8);
INSERT INTO public.team_city VALUES (141, 141, 13, -1, 13);
INSERT INTO public.team_city VALUES (142, 142, 14, -1, 14);
INSERT INTO public.team_city VALUES (143, 143, 15, -1, 15);
INSERT INTO public.team_city VALUES (144, 144, 16, -1, 16);


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

