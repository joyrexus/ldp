
CREATE TABLE log (
    table_name TEXT NOT NULL CHECK (table_name in ("subjects", "sessions", "visits", "transcripts", "utterances")),
    id INTEGER NOT NULL,
    action TEXT NOT NULL CHECK (action in ("INSERTED", "UPDATED", "DELETED")),
    timestamp DATETIME NOT NULL
);
CREATE TABLE measures (
    subject INTEGER NOT NULL,
    session INTEGER NOT NULL,
    speaker TEXT CHECK (speaker in ("P", "C")),
    protocol TEXT CHECK (protocol in ("H", "L")),
    last_update DATE,
    utterances INTEGER,
    word_tokens INTEGER,
    word_types INTEGER,
    mlu REAL
);
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY NOT NULL CHECK(id > 0 and id < 100),
    protocol TEXT CHECK (protocol in ("H", "L")),
    alias TEXT,
    grade TEXT CHECK (grade in ("","PS","KG","1G","2G","3G","4G","5G","6G")),
    season TEXT CHECK (season in ("", "FALL", "WINTER", "SPRING")),
    desc TEXT
);
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY NOT NULL CHECK(id > 0 and id < 300),
    dob DATE NOT NULL,
    sex TEXT NOT NULL CHECK (sex in ("M", "F")),
    race TEXT NOT NULL CHECK (race in ("AI","AS","BL","PI","WH","2+","OT")),
    ethn TEXT NOT NULL CHECK (ethn in ("H", "N")),
    lesion TEXT CHECK (lesion in ("R", "L", "")),
    project INTEGER NOT NULL CHECK (project > 0 and project < 10),
    active BOOLEAN NOT NULL,
    control BOOLEAN NOT NULL,
    note TEXT
);
CREATE TABLE transcripts (
    /* id = 1 || 3-digit subject || 2-digit session */
    id INTEGER PRIMARY KEY NOT NULL
    /* check that the PK correlates with the relevant columns */
    CHECK (id = 1 || substr('000' || subject, -3, 3)
                  || substr('00'  || session, -2, 2)),
    subject INTEGER NOT NULL REFERENCES subjects(id),
    session INTEGER NOT NULL REFERENCES sessions(id),
    last_update DATE,
    minutes INTEGER CHECK (minutes = "" or (minutes > 0 and minutes < 200)),
    pcg TEXT CHECK (pcg in ("", "M", "F", "B", "O")),
    cast TEXT,
    note TEXT,
    anno_sr_p BOOLEAN,
    anno_sr_c BOOLEAN,
    anno_gs_p BOOLEAN,
    anno_gs_c BOOLEAN,
    anno_gx_p BOOLEAN,
    anno_gx_c BOOLEAN,
    anno_mor_p BOOLEAN,
    anno_mor_c BOOLEAN,
    anno_syn_p BOOLEAN,
    anno_syn_c BOOLEAN,
    anno_max_p BOOLEAN,
    anno_max_c BOOLEAN
);
CREATE TABLE utterances (
    /* id = 1 || 3-digit subject || 2-digit session || 5-digit row */
    id INTEGER PRIMARY KEY NOT NULL
    /* check that the PK correlates with the relevant columns */
    CHECK (id = 1 || substr('000'   || subject, -3, 3)
                  || substr('00'    || session, -2, 2)
                  || substr('00000' || row, -5, 5)),
    subject INTEGER NOT NULL CHECK (subject > 0 and subject < 500),
    session INTEGER NOT NULL CHECK (session > 0 and session < 100),
    row INTEGER NOT NULL CHECK (row > 0 and row < 50000),
    last_update DATE,
    time TEXT,
    line TEXT,
    key TEXT,
    p_utts_orig TEXT,
    p_utts TEXT,
    p_chat TEXT,
    p_enum TEXT,
    p_mor TEXT,
    p_syn TEXT,
    p_clauses TEXT,
    p_np TEXT,
    p_pp TEXT,
    p_dpp TEXT,
    p_wpu TEXT,
    p_passives TEXT,
    p_syntype TEXT,
    p_form TEXT,
    p_lrb TEXT,
    p_obj TEXT,
    p_gloss TEXT,
    p_orient TEXT,
    p_mspd TEXT,
    p_g_type TEXT,
    p_gs_rel TEXT,
    p_time TEXT,
    p_time_gen TEXT,
    p_word TEXT,
    p_word_num TEXT,
    p_sem_role TEXT,
    p_pres_ref TEXT,
    p_reinf TEXT,
    p_added TEXT,
    p_persp TEXT,
    c_utts_orig TEXT,
    c_utts TEXT,
    c_chat TEXT,
    c_enum TEXT,
    c_mor TEXT,
    c_syn TEXT,
    c_clauses TEXT,
    c_np TEXT,
    c_pp TEXT,
    c_dpp TEXT,
    c_wpu TEXT,
    c_passives TEXT,
    c_syntype TEXT,
    c_form TEXT,
    c_lrb TEXT,
    c_obj TEXT,
    c_gloss TEXT,
    c_orient TEXT,
    c_mspd TEXT,
    c_g_type TEXT,
    c_gs_rel TEXT,
    c_time TEXT,
    c_time_gen TEXT,
    c_word TEXT,
    c_word_num TEXT,
    c_sem_role TEXT,
    c_pres_ref TEXT,
    c_reinf TEXT,
    c_added TEXT,
    c_persp TEXT,
    context TEXT,
    edit TEXT CHECK (edit in ("", "O", "I", "F")),
    edit_note TEXT
);
CREATE TABLE visits (
    /* id = 1 || 3-digit subject || 2-digit session */
    id INTEGER PRIMARY KEY NOT NULL
    /* check that the PK correlates with the relevant columns */
    CHECK (id = 1 || substr('000' || subject, -3, 3)
                  || substr('00'  || session, -2, 2)),
    subject INTEGER NOT NULL REFERENCES subjects(id),
    session INTEGER NOT NULL REFERENCES sessions(id),
    last_update DATE,
    completed BOOLEAN,
    expected BOOLEAN,
    missed BOOLEAN,
    repeated BOOLEAN,
    replaced_transcript BOOLEAN,
    protocol TEXT CHECK (protocol in ("H", "L")),
    date DATE,
    note TEXT,
    child_age TEXT,
    child_age_years FLOAT,
    child_age_months FLOAT,
    pcg TEXT CHECK (pcg in ("", "M", "F", "B", "O")),
    income INTEGER CHECK (income = "" or (income > 0 and income < 7)),
    mother_pcg BOOLEAN,
    mother_education INTEGER,
    father_pcg BOOLEAN,
    father_education INTEGER,
    other_pcg BOOLEAN,
    other_education INTEGER
);
CREATE TRIGGER log_delete_from_sessions AFTER DELETE ON sessions
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('sessions', old.id, 'DELETED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_delete_from_subjects AFTER DELETE ON subjects
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('subjects', old.id, 'DELETED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_delete_from_transcripts AFTER DELETE ON transcripts
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('transcripts', old.id, 'DELETED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_delete_from_utterances AFTER DELETE ON utterances
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('utterances', old.id, 'DELETED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_delete_from_visits AFTER DELETE ON visits
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('visits', old.id, 'DELETED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_insert_to_sessions AFTER INSERT ON sessions
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('sessions', new.id, 'INSERTED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_insert_to_subjects AFTER INSERT ON subjects
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('subjects', new.id, 'INSERTED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_insert_to_transcripts AFTER INSERT ON transcripts
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('transcripts', new.id, 'INSERTED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_insert_to_visits AFTER INSERT ON visits
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('visits', new.id, 'INSERTED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_update_to_sessions AFTER UPDATE ON sessions
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('sessions', new.id, 'UPDATED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_update_to_subjects AFTER UPDATE ON subjects
    BEGIN
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('subjects', new.id, 'UPDATED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_update_to_transcripts AFTER UPDATE ON transcripts
    BEGIN
        UPDATE transcripts SET last_update = DATETIME('NOW') WHERE id = new.id;
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('transcripts', new.id, 'UPDATED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_update_to_utterances AFTER UPDATE ON utterances
    BEGIN
        UPDATE utterances SET last_update = DATETIME('NOW') WHERE id = new.id;
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('utterances', new.id, 'UPDATED', DATETIME('NOW'));
    END;
CREATE TRIGGER log_update_to_visits AFTER UPDATE ON visits
    BEGIN
        UPDATE visits SET last_update = DATETIME('NOW') WHERE id = new.id;
        INSERT INTO log (table_name, id, action, timestamp) 
                    values ('visits', new.id, 'UPDATED', DATETIME('NOW'));
    END;
