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
    conference_name character varying NOT NULL,
    first_season_id integer NOT NULL
);


ALTER TABLE public.conference OWNER TO postgres;

--
-- Name: division; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.division (
    id integer NOT NULL,
    division_name character varying(25) NOT NULL,
    conference_id integer NOT NULL,
    first_season_id integer NOT NULL
);


ALTER TABLE public.division OWNER TO postgres;

--
-- Name: draft; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.draft (
    id integer NOT NULL,
    host_city_id integer NOT NULL,
    season_id integer NOT NULL,
    num_rounds integer NOT NULL
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
    attendance integer NOT NULL
);


ALTER TABLE public.game OWNER TO postgres;

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
-- Name: game_sec_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_sec_stats (
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


ALTER TABLE public.game_sec_stats OWNER TO postgres;

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
    weight integer NOT NULL
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
    status integer NOT NULL
);


ALTER TABLE public.player_pool OWNER TO postgres;

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
-- Name: player_specs_sec; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player_specs_sec (
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


ALTER TABLE public.player_specs_sec OWNER TO postgres;

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
    season_number integer NOT NULL
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
    city_id integer NOT NULL,
    name character varying(50) NOT NULL,
    first_season_id integer NOT NULL,
    current_season_wins integer NOT NULL,
    current_season_losses integer NOT NULL,
    stadium_id integer NOT NULL,
    conference_id integer NOT NULL,
    division_id integer NOT NULL
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
-- Name: division division_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.division
    ADD CONSTRAINT division_pkey PRIMARY KEY (id);


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
-- Name: game_dl_stats game_dl_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_dl_stats
    ADD CONSTRAINT game_dl_stats_pkey PRIMARY KEY (id);


--
-- Name: game_k_stats game_k_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_k_stats
    ADD CONSTRAINT game_k_stats_pkey PRIMARY KEY (id);


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
-- Name: game_sec_stats game_sec_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sec_stats
    ADD CONSTRAINT game_sec_stats_pkey PRIMARY KEY (id);


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
-- Name: player_specs_dl player_specs_dl_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_dl
    ADD CONSTRAINT player_specs_dl_pkey PRIMARY KEY (id);


--
-- Name: player_specs_k player_specs_k_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_k
    ADD CONSTRAINT player_specs_k_pkey PRIMARY KEY (id);


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
-- Name: player_specs_sec player_specs_sec_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player_specs_sec
    ADD CONSTRAINT player_specs_sec_pkey PRIMARY KEY (id);


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

