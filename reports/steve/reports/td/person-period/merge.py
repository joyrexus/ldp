from datastore.table import Reader
from collections import defaultdict


sess_map = dict([(1,14), (2,18), (3,22), (4,26), (5,30), (6,34), 
                 (7,38), (8,42), (9,46), (10,50), (11,54), (12,58), 
                 (13,62), (14,66), (15,70), (16,74), (17,78), (18,82), 
                 (19,86), (20,90)])

speech = Reader('speech.xls')
ses = Reader('ses.xls')

subjects = defaultdict(dict)
ses_cols = 'SUBJ SEX EDU INC RACE ETHN'.split()

for row in ses:
    subjects[row['SUBJ']] = row


visits = defaultdict(dict)
columns = 'subject session speaker word_types'.split()

for subj, sess, spkr, wt in speech.values(*columns):
    age = sess_map[int(sess)]
    if not visits.has_key((subj, sess)):
        visits[subj, sess] = {'SUBJ': subj, 'SESS': sess, 'AGE': age,
                              'CWT': '', 'PWT': ''}
    if spkr == "child":
        visits[subj, sess]['CWT'] = wt
    else:
        visits[subj, sess]['PWT'] = wt

viz_cols = 'SESS AGE PWT CWT'.split()

print "\t".join(ses_cols + viz_cols)

for id, data in visits.items():
    subj, sess = id
    SES = "\t".join(subjects[subj][attr] for attr in ses_cols)
    VISIT = "\t".join(str(data[attr]) for attr in viz_cols)
    print SES + "\t" + VISIT
