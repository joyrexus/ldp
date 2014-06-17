Tally
=====

**Tally your feature space!**

The `tally` module is handy for tallying selections of tabular data.  It provides a quick and dirty approach to defining [feature vectors](http://en.wikipedia.org/wiki/Statistical_classification#Feature_vectors) and tallying observed value combinations. I've found useful for generating simple summary reports of data tables and in the context of [simple classification tasks](http://nltk.org/book/ch06.html).

I recommend using it in conjunction with [dsv](https://github.com/mbostock/dsv)
if you need to parse CSV/TSV files. 
  
Note that `tally` is minimalist by design, intended for quick counting of
smaller data tables.  For larger datasets and more flexible querying, you're going to want to use a dedicated datastore or something like [crossfilter](https://github.com/square/crossfilter).

Just so we're clear on terminology in what follows ...

* a *feature* is like a column header
* a *sample* is like a row (or some subset of columns from the row)
* a *sample space* is like a table (or some subset of columns from the table)


The `tally` module provides two main classes: **Feature** and **FeatureSpace**.

The **Feature** class is used to name a scalar variable and tally its observed values.  It's just a simple counter.  You can think of it as one *dimension* of a
"feature space" or one "column" of a data table.

```coffeescript
size = new Feature 'Size'
size.add 'a'
size.add 'b'
size.add 'b'
size.add 'c'
size.add 'c'
size.add 'c'

size.total.a      # 1
size.total.b      # 2
size.total.c      # 3
size.top 2        # ['c', 'b']
size.top 3        # ['c', 'b', 'a']
size.values()     # ['a', 'b', 'c', 'd']
```

The **FeatureSpace** class is used to name a vector of features and tally samples.  A sample is just a vector of feature *values*.

So, this class lets us instantiate a feature vector and then observe instances of feature value patterns ("samples").  The resulting collection of samples is often called a "sample space",  but we can also think of it as a "feature space".  

An example should clarify the terminology.

```coffeescript
{FeatureSpace} = require 'tally'

survey = new FeatureSpace 'state age sex'

# ... alternatively ...

survey = new FeatureSpace ['state', 'age', 'sex']
```

So, we've created a new space called `survey` with three features.

Let's populate the space with some samples.

```coffeescript
survey.add 'IL', 40, 'M'    # state: IL, age: 40, sex: M
survey.add 'NY', 25, 'F'
survey.add 'CA', 25, 'F'
survey.add 'CA', 25, 'F'
```

Samples are just ordered lists of values. The order of the values should of course correspond to the feature order used to create the space: `state`, `age`, `sex`.

We now have a feature space consisting of ...

```
state  age  sex
IL     40   M
NY     25   F
CA     25   F
CA     25   F
```

Note that you can also add samples represented as objects using the `insert` method.

```coffeescript
survey.add 'CA', 25, 'F'

# ... or ...

survey.insert 
  state: 'CA'
  age: 25
  sex: 'F'
```

Now that we have a populated feature space, we can do various things with it.

## Return rows
    
```coffeescript
survey.rows()               # returns all rows

survey.rows 2               # [ ['IL', '40', 'M'], ['NY', '25', 'M'] ]
```

## Get individual feature totals

```coffeescript
survey.state.total.IL       # 1
survey.state.total.NY       # 1
survey.state.total.CA       # 2

survey.age.total[40]        # 1
survey.age.total[25]        # 3
```

## Match value patterns

```coffeescript
survey.match '*', 40, 'M'   # [ ['IL,40,M', 1] ]
survey.match '*', 25        # [ ['NY,25,M', 1], ['CA,25,F', 2] ]
```

## Get value patterns totals

```coffeescript
survey.total '*', 25        # 3
survey.total 'CA', 25       # 2
survey.total '*', 25, 'M'   # 1
```

## Generate summary reports

`survey.report()` returns ...

```
state age sex TOTAL
IL    40  M   1
NY    25  F   1
CA    25  F   2
```

`survey.report 'sex'` returns ...

```
state age F M
IL    40  0 1
NY    25  1 0
CA    25  2 0
```

`survey.report 'age'` returns ...

```
state sex 25 40
IL    M   0  1
NY    F   1  0
CA    F   2  0
```

`survey.report 'state'` returns ...

```
age sex  CA  IL  NY
40  M    0   1   0
25  F    2   0   1
```
