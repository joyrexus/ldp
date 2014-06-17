Testy
=====

Our simple testing framework, ripped from the CoffeeScript [Cakefile](https://github.com/jashkenas/coffee-script/blob/master/Cakefile).


## Demo

```coffeescript
{ok, eq, arrayEq, log, test} = require 'tester'

log 'red', 'hello'
log 'green', 'hello'
log 'bold', 'hello'

test 'should pass', -> ok true
test 'should pass', -> eq 1, 1
test 'should pass', -> arrayEq [1, 1], [1, 1]

test 'should not pass', -> ok false
test 'should not pass', -> eq 1, 2
test 'should not pass', -> arrayEq [1, 1], [1, 2]

test.status()
```

If you run this file you should get the following output:

    hello (in red)
    hello (in green)
    hell0 (in boldface)

    failed 3 tests and passed 3 tests in 0.00 seconds

    should not pass / undefined
      AssertionError
      Expected true not false
      function () {
        return ok(false);
      }

    should not pass / 1 is not 2
      AssertionError
      Expected true not false
      function () {
        return eq(1, 2);
      }

    should not pass / undefined
      AssertionError
      Expected true not false
      function () {
        return arrayEq([1, 1], [1, 2]);
      }


## Literate Source

Preliminaries.

```coffeescript
{ok} = require 'assert'

print = console.log
start = new Date
total = passed = 0
failures = []
```
Color hash for pretty terminal logging.

```coffeescript
color = 
  bold:  '\x1B[0;1m'
  red:   '\x1B[0;31m'
  green: '\x1B[0;32m'
  reset: '\x1B[0m'
```
Log your message in color.

```coffeescript
log = (name, message) -> print color[name] + message + color.reset
```
Here's the main test method, which takes a description and function to test.

```coffeescript
test = (desc, fn) ->
  ++total
  try
    fn.desc = desc
    fn.call(fn)
    ++passed
  catch e
    e.desc = desc if desc?
    e.source = fn.toString() if fn.toString?
    failures.push e
```
A better comparator.  See [harmony:egal](http://wiki.ecmascript.org/doku.php?id=harmony:egal).

```coffeescript
egal = (a, b) ->
  if a is b
    a isnt 0 or 1/a is 1/b
  else
    a isnt a and b isnt b
```
A recursive functional equivalence helper; uses `egal` for testing equivalence.

```coffeescript
arrayEgal = (a, b) ->
  if egal a, b then yes
  else if a instanceof Array and b instanceof Array
    return no unless a.length is b.length
    return no for el, idx in a when not arrayEgal el, b[idx]
    yes
```
Use `eq` for comparing objects and `arrayEq` for lists.

```coffeescript
eq = (a, b, msg) -> ok egal(a, b), msg ? a + ' is not ' + b
arrayEq = (a, b, msg) -> ok arrayEgal(a,b), msg
```
Invoke `test.status` after testing to indicate how things turned out.

```coffeescript
test.status = ->
  failed = failures.length
  sec = ((Date.now() - start) / 1000).toFixed(2)
  msg = "passed #{passed} tests in #{sec} seconds#{color.reset}"
  return log 'green', msg unless failed
  log 'red', "failed #{failed} tests and #{msg}"
  for fail in failures
    print ""
    log 'red', "#{fail.desc} / #{fail.message}" if fail.desc
    log 'red', "  #{fail.name}" if fail.name
    log 'red', "  Expected #{fail.expected} not #{fail.actual}" if fail.expected
    print ' ', fail.source if fail.source
  return
```
Finally, let's export the main methods.

```coffeescript
exports[key] = value for key, value of {print, color, log, test, ok, eq, arrayEq}
```
