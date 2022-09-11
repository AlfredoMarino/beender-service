CREATE TABLE bee (
	id SERIAL PRIMARY KEY,
	firstname VARCHAR,
	lastname VARCHAR,
	interested_in VARCHAR,
	experience_years INT,
	picture VARCHAR,
	bio VARCHAR
)

CREATE TABLE hive (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	description VARCHAR,
	queen_bee VARCHAR,
	picture VARCHAR
)

CREATE TABLE match (
    id serial PRIMARY KEY,
    hive_id integer,
    bee_id integer,
    hive_accept boolean,
    bee_accept boolean,
    CONSTRAINT bee_id FOREIGN KEY (bee_id)
        REFERENCES public.bee (id),
    CONSTRAINT hive_id FOREIGN KEY (hive_id)
        REFERENCES public.hive (id)
)
