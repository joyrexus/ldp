{hilite} = require 'hilite'

text = '''

hi = (name) ->
  console.log name

square = (x) -> x * x

for i in [1..3]
  console.log square i

'''

console.log hilite text
