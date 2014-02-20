from datastore.table import Reader
from collections import defaultdict


ses = Reader('ses.xls')
subjects = defaultdict(dict)
ses_cols = 'SUBJ SEX EDU INC RACE ETHN'.split()

for row in ses:
    subjects[row['SUBJ']] = row


outcomes = Reader('outcomes.tsv')
out = defaultdict(dict)
columns = 'SUBJ SESS VOCAB READ_WJ READ_GM'.split()

for subj, sess, voc, rwj, rgm in outcomes.values(*columns):
    if not out.has_key(subj):
        out[subj] = {
                'SUBJ': subj,
                'VOCB1': '',
                'VOCB2': '', 
                'VOCB3': '', 
                'VOCB4': '', 
                'READ1': '', 
                'READ2': '', 
                'READ3': '', 
                'READ4': '', 
                'READ5': ''
                }
    if sess == "5" and voc:
        out[subj]['VOCB1'] = voc
    elif sess == "8" and voc:
        out[subj]['VOCB2'] = voc
    elif sess == "11" and voc:
        out[subj]['VOCB3'] = voc
    elif sess == "22":
        if rwj:
            out[subj]['READ1'] = rwj 
        if rgm:
            out[subj]['READ3'] = rgm
    elif sess == "25":
        if rwj:
            out[subj]['READ2'] = rwj 
        if rgm:
            out[subj]['READ4'] = rgm
    elif sess == "27" and voc:
        out[subj]['VOCB4'] = voc

out_cols = 'VOCB1 VOCB2 VOCB3 VOCB4 READ1 READ2 READ3 READ4'.split()

print "\t".join(ses_cols + out_cols)

for subj, data in out.items():
    SES = "\t".join(subjects[subj][attr] for attr in ses_cols)
    OUT = "\t".join(str(data[attr]) for attr in out_cols)
    print SES + "\t" + OUT
