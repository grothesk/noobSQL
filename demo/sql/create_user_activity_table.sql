-- Table: public.user_activity

-- DROP TABLE public.user_activity;

CREATE TABLE public.user_activity
(
    id character varying(64) COLLATE pg_catalog."default" NOT NULL,
    user_id character varying(32) COLLATE pg_catalog."default" NOT NULL,
    event_name character varying(32) COLLATE pg_catalog."default" NOT NULL,
    event_time timestamp without time zone NOT NULL,
    CONSTRAINT user_activity_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.user_activity
    OWNER to pgdocker;