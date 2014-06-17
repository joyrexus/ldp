Tally
=====

**Tally your feature space!**

A quick and dirty approach to defining [feature vectors](http://en.wikipedia.org/wiki/Statistical_classification#Feature_vectors)
and tallying their value combinations.


    {FeatureSpace} = require './index'
    {ok, eq, arrayEq} = require 'testy'


## Stored samples and fast matching

The `FeatureSpace` class has a "fast matching" option, which can be turned on
or off when creating an instance: `storedSpace = new FeatureSpace 'x y z', on`.

When "on", the the `total` and `match` methods defer to their "fast"
counterparts, which utilize the cache of stored samples for somewhat faster
matching.

When "off" The default methods reconstitute samples from the `count` object, which holds key/value pairs: unique samples (i.e., value combinations observed) as stringified keys and their total instances as values.

For example, given the following counts ...

    survey = new FeatureSpace 'state age sex'
    count = survey.add
    count 'IL', 40, 'M'
    count 'NY', 25, 'F'
    count 'CA', 25, 'F'
    count 'CA', 25, 'F'

Let's create and test the necessary methods for reconstructing the "rows"
(i.e., arrays of feature value combinations observed).  The only difference
between rows returned by such a `rows` method and those returned by the `store`
is their ordering, which shouldn't matter for our purposes.

First, let's create a `row` method to convert `(KEY_OF_VALUES, N)` to `N` value
arrays.

    arrayEq survey.makeRows('x,y,z', 3),
      [ [ 'x', 'y', 'z' ], [ 'x', 'y', 'z' ], [ 'x', 'y', 'z' ] ]

OK, before testing `rows()` we need to stringify the numbers in the feature
value arrays returned from `store`.  Since `rows()` is reconstituting the rows
from the unique keys in the `count` dict, everything is coming back as a
string.  

    d = {}
    d[5] = "five"
    arrayEq ['5'], Object.keys d

    stringify = (x) -> x.toString()   
    ok '5', stringify(5)

    storedSurvey = new FeatureSpace 'state age sex', store="on"
    count = storedSurvey.add
    count 'IL', 40, 'M'
    count 'NY', 25, 'F'
    count 'CA', 25, 'F'
    count 'CA', 25, 'F'
    
The base class has a `rows` method as well, which is just an alias for the
`store` dict.

    ok storedSurvey.rows().length is 4
    ok storedSurvey.rows(3).length is 3
    ok storedSurvey.rows(2).length is 2
    ok storedSurvey.rows(1).length is 1

Rows of feature values returned by `rows()` should equal those in `store`.

    arrayEq storedSurvey.rows(), storedSurvey.store
    arrayEq storedSurvey.rows(2), storedSurvey.store[...2]

The rows produced by the unstored survey should of course match those produced
by the stored version.

    arrayEq (x.map stringify for x in storedSurvey.rows()), 
      survey.rows(), 'rows should equal store'

    arrayEq (x.map stringify for x in storedSurvey.rows(2)),
      survey.rows(2), 'rows should equal store'

Now we need to test the alternative `match` and `total` methods. Recall that we
counted and stored the following observations:
    
>                  [ 'IL', 40, 'M' ]
>                  [ 'NY', 25, 'F' ]
>                  [ 'CA', 25, 'F' ] *  
>                  [ 'CA', 25, 'F' ] *

    ok survey.total('*', '*', 'F') is 3
    ok storedSurvey.total('*', '*', 'F') is 3

    arrayEq survey.match('*', '*', 'F'),
      [ [ 'NY,25,F', 1 ], [ 'CA,25,F', 2 ] ]

Note how the match results from the stored survey, which caches all the
observations in their raw state:

    arrayEq storedSurvey.match('*', '*', 'F'),
      [ [ 'NY', 25, 'F' ], [ 'CA', 25, 'F' ], [ 'CA', 25, 'F' ] ]


## Reporting

We still need to setup some simple reporting.  Basic summaries with an optional
breakdown.
    
    print = console.log
    print survey.report()

The `report` should produce ...

> state age sex TOTAL
> IL  40  M 1
> NY  25  F 1
> CA  25  F 2


You can pass `report` the name of a feature to get a breakdown. 

    print survey.report('sex')

This should produce ...

> state age M F 
> IL    40  1 0
> NY    25  0 1
> CA    25  0 2

    print survey.report('age')

This should produce ...

> state sex 25 40
> CA    F   2  0
> IL    M   1  0
> NY    F   1  0

    survey = new FeatureSpace 'state age sex'
    survey.add 'CA', 35, 'F'
    survey.add 'IL', 40, 'M'
    survey.add 'NY', 25, 'F'
    survey.add 'CA', 25, 'F'
    survey.add 'CA', 25, 'F'
    print survey.report('age')

## Notes

    count = new FeatureSpace 'state age sex'

    count.add 'IL', 40, 'M'
    count.add 'IL', 35, 'M'
    count.add 'NY', 25, 'F'
    count.add 'CA', 25, 'F'
    count.add 'CA', 25, 'F'


    arrayEq count.state.values(), [ 'CA', 'IL', 'NY' ]
    arrayEq count.age.values(), [ '25', '35', '40' ]
    arrayEq count.sex.values(), [ 'F', 'M' ]

Note that we can specify globs ("\*") to match *any* value for a given feature. 

    eq count.total('*', '*', 'M'), 2
    eq count.total('*', 25, 'F'), 3
    eq count.total('*', 35, 'M'), 1
    eq count.total('*', '*', 'M'), 2
    eq count.total('*', 35, 'Q'), 0

Important points:

* These are totals of **feature value combinations**. That is, we're 
  searching for the total number of instances of a certain pattern; 
  the `total` method is querying the store of observed feature values 
  for the given pattern.  

* You specify a value for a feature by position.  Recall that features 
  are specified by position when a counter is initialized.
