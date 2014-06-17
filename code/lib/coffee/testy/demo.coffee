{ok, eq, arrayEq, log, test} = require 'testy'

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

###

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

###
