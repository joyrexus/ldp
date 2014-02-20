select subject, session, count(*)
    from utterances 
    where (p_utts = "---" or p_utts = "--")
        and subject in (select id from subjects where project=2) 
    group by subject, session;
