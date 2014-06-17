{run, convert} = require 'marko'
{test, ok} = require 'testy'

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

test 'running the source returns "hello world!"', ->
  result = run source
  ok result is "hello world!"

test.status()
