Tests
=====

    {test, eq, ok, arrayEq} = require 'testy'


## Feature Tests

Quick test of the **Feature** class.

    {Feature} = require '../tally'

    test 'feature counter', ->
      x = new Feature 'x'
      eq x.name, 'x'
      x.add(i) for i in 'a b c c c a d d d d'.split(' ')
      eq x.total.a, 2
      eq x.total.b, 1
      eq x.total.c, 3
      eq x.total.d, 4
      arrayEq x.top(2), ['d', 'c']
      arrayEq x.top(3), ['d', 'c', 'a']
      arrayEq x.values(), ['a', 'b', 'c', 'd']


## FeatureSpace Tests

Testing various aspects of the **FeatureSpace** class.

    {FeatureSpace} = require 'tally'


Miscellaneous tests demonstrating sample usage.  Note that we can initialize
our space by specifying our feature set as a string or an array.

    test 'misc', ->
      for features in ['x y z', ['x','y','z']]
        space = new FeatureSpace features
        samples = ['a m q', 'b m q', 'c n q', 'c n r']
        space.add(sample.split(' ')...) for sample in samples
        eq space.x.total.a, 1
        eq space.y.total.m, 2
        eq space.z.total.q, 3
        arrayEq space.x.values(), ['a', 'b', 'c']
        arrayEq space.y.values(), ['m', 'n']
        arrayEq space.z.values(), ['q', 'r']
        arrayEq space.match('c', 'n'), 
          [ [ 'c,n,q', 1 ], 
            [ 'c,n,r', 1 ] ]
        arrayEq space.match('*', 'm', 'q'), 
          [ [ 'a,m,q', 1 ], 
            [ 'b,m,q', 1 ] ]


Use the `insert` method to add hashes to the space.

    test 'hash insertions', ->
      space = new FeatureSpace 'x y z'
      space.insert
        x: 'a'
        y: 'b'
        z: 'c'
      eq space.x.total.a, 1
      eq space.y.total.b, 1
      eq space.z.total.c, 1
      arrayEq space.z.values(), ['c']

      space.insert
        x: 'a'
        y: 'b'
        z: 'q'
      eq space.x.total.a, 2
      eq space.y.total.b, 2
      eq space.z.total.c, 1
      eq space.z.total.q, 1
      arrayEq space.z.values(), ['c', 'q']


Testing conversion of sample-key string to row representation (array of values).

    test 'sample-key string to row conversion', ->

      for store in [on, off]  # test both options

        space = new FeatureSpace 'x y z', store
        arrayEq space.makeRows('a,b,c', 3),
          [ [ 'a', 'b', 'c' ], 
            [ 'a', 'b', 'c' ], 
            [ 'a', 'b', 'c' ] ]
        space.add 'a', 'b', 'c'

        arrayEq space.rows(1), [ [ 'a', 'b', 'c' ] ]
        if store is on
          arrayEq space.rows(1), space.store


Testing the example used in the README.

    test 'survey example', ->

      for store in [on, off]  # test both options

        survey = new FeatureSpace 'state age sex', store
        survey.add 'IL', 40, 'M'
        survey.add 'NY', 25, 'M'
        survey.add 'CA', 25, 'F'
        survey.add 'CA', 25, 'F'

        eq survey.rows().length, 4
        eq survey.rows(3).length, 3
        eq survey.rows(2).length, 2
        eq survey.rows(1).length, 1

        eq survey.state.total.IL, 1
        eq survey.state.total.NY, 1
        eq survey.state.total.CA, 2

        eq survey.age.total[40], 1
        eq survey.age.total[25], 3

        eq survey.total('*', 25), 3
        eq survey.total('CA', 25), 2
        eq survey.total('*', 25, 'M'), 1

        survey.insert
          state: 'CA'
          age: 25
          sex: 'F'

        eq survey.total('CA', 25), 3


Let's test sample matching both when storing samples and without.
Note that we're setting up a space with features `x`, `y`, and `z`:

>  x  y  z
>  -------
>  a  b  c
>  a  b  r 
>  p  q  c
>  p  b  r

    testsFor = (stored) ->

      space = new FeatureSpace 'x y z', stored
      space.add 'a', 'b', 'c'
      space.add 'a', 'b', 'r' 
      space.add 'p', 'q', 'c' 
      space.add 'p', 'b', 'r' 

      test 'totals of particular feature values', ->
        eq space.x.total.a, 2
        eq space.x.total.q, undefined
        eq space.x.total.p, 2

        eq space.y.total.b, 3
        eq space.y.total.q, 1

        eq space.z.total.c, 2
        eq space.z.total.r, 2

      test 'unique values of particular features', ->
        arrayEq space.x.values(), ['a', 'p']
        arrayEq space.y.values(), ['b', 'q']
        arrayEq space.z.values(), ['c', 'r']

      ###

      x  y  z
      -------
      a  b  c
      a  b  r 
      p  q  c
      p  b  r

      ###

      test 'value pattern totals', ->
        eq space.total('a', 'b', 'c'), 1
        eq space.total('a', 'b', '*'), 2
        eq space.total('a', 'b'), 2
        eq space.total('p'), 2
        eq space.total('q'), 0

        eq space.total('p', 'b', 'r'), 1
        eq space.total('a', 'b', 'r'), 1
        eq space.total('*', 'b', 'r'), 2

        eq space.total('*', 'b', 'c'), 1
        eq space.total('*', 'q', 'c'), 1
        eq space.total('*', '*', 'c'), 2
        eq space.total('*', '*', '*'), 4

      test 'value pattern matching', ->
        if stored
          arrayEq space.match('a', 'b'), 
            [ ['a','b','c'], ['a','b','r'] ]
          arrayEq space.match('*', 'b', '*'), 
            [ ['a','b','c'], ['a','b','r'], ['p', 'b', 'r'] ]
          arrayEq space.match('a', '*', 'c'), 
            [ ['a','b','c'] ]
        else
          arrayEq space.match('a', 'b'), 
            [ ['a,b,c', 1], ['a,b,r', 1] ]
          arrayEq space.match('*', 'b', '*'), 
            [ ['a,b,c', 1], ['a,b,r', 1], ['p,b,r', 1] ]
          arrayEq space.match('a', '*', 'c'), 
            [ ['a,b,c', 1] ]

      test 'queries', ->
        queries = [
          {
            query: 'x = a' 
            expected: 'Total "a" values of feature "x" is 2' 
          }
          {
            query: 'y = b' 
            expected: 'Total "b" values of feature "y" is 3' 
          }
          {
            query: 'z = c' 
            expected: 'Total "c" values of feature "z" is 2' 
          }
        ]

        for q in queries
          [feature, v] = q.query.split(' = ')
          result = space[feature].total[v] or 0
          eq q.expected,
            """Total "#{v}" values of feature "#{feature}" is #{result}"""

    testsFor storing=on
    testsFor storing=off


Let's do some report testing.

    test 'reporting', ->

      survey = new FeatureSpace 'state age sex'
      survey.add 'IL', 40, 'M'
      survey.add 'NY', 25, 'F'
      survey.add 'CA', 25, 'F'
      survey.add 'CA', 25, 'F'

      mend = (lines) -> 
        lines
          .replace(/^\n|\n$/, '')
          .replace(/\ +/g, '\t')

      lines = '''
        state age sex TOTAL
        IL    40  M   1
        NY    25  F   1
        CA    25  F   2
        '''
      expected = mend lines
      eq survey.report(), expected

      lines = '''
        state age F M
        IL    40  0 1
        NY    25  1 0
        CA    25  2 0
        '''
      expected = mend lines
      eq survey.report('sex'), expected

      lines = '''
        state sex 25 40
        IL    M   0  1
        NY    F   1  0
        CA    F   2  0
        '''

      expected = mend lines
      eq survey.report('age'), expected

      lines = '''
        age sex  CA  IL  NY
        40  M    0   1   0
        25  F    2   0   1
        '''
      expected = mend lines
      eq survey.report('state'), expected


How'd we do?

    test.status()
