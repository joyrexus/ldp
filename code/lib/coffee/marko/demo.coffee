marko = require 'marko'

source = '''

Run Demo
========

Inline HTML:

<pre><code>foo = bar</code></pre>

Fenced code:

```    
hi = (name) -> "hello #{name}!"

```

Code block:

    hi "world"

A link [here](http://joy.com)

End!
'''

print = console.log
print "Converting the source returns: #{marko.convert source}"
print "Running the source returns: #{marko.run source}"
