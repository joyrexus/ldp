from ldp.speech import Report

speech = Report()
speech.query('session in ("11", "12")', project=2)
speech.report(header=True)
