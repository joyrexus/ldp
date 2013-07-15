from ldp.jobs.main import Unit, Units

'''
data = [{"id": "10", "value": "ten"},
        {"id": "11", "value": "eleven"},
        {"id": "12", "value": "twelve"},
        {"id": "13", "value": "thirteen"}]

units = Units('units', data)
omits = Units('omits')
edits = Units('edits')

for u in units:
    print u, '...'
    print u.id, u.value, u.edit(lambda x: x.upper())

print
print 'Popping unit 1 and 2 to omits ...'
units.pop_to(omits, 1, 2)
print "OMITS:", omits
print
print 'Popping everything in omits to edits ...'
omits.pop_to(edits)
print "EDITS:", edits
print
print 'Tagging all units in edits queue ...'
edits.tag('TEST')
print edits

print
print 'Lowercasing values of all units in edits queue ...'
edits.edit(lambda x: x.lower())
print edits

print
print 'Reverting values of units in edits queue to their prior values ...'
edits.revert()
print edits

print
print 'Replacing E with I in values of units in edits queue ...'
edits.replace('E', 'I')
print edits

print
print 'Returning sql update statements for units in edits queue ...'
print edits.sql(table='utterances', column='p_utts')

unit = Unit(id=10, value="foo")
print "id:", unit.id
print "value:", unit.value
unit.value = "bar"
print "new value:", unit.value
unit.revert()
print "reverted value:", unit.value
print "tag list:", unit.tags
unit.tag("TEST")
print "new tag list:", unit.tags
del unit.tags
print "deleted tag list:", unit.tags
'''
