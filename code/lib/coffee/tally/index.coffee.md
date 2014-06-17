Tally
=====

The `tally` module is handy for tallying selections of tabular data.

In what follows, keep the following in mind:

* a *feature* is like a column header
* a *sample* is like a row (or some subset of columns from the row)
* a *sample space* is like a table (or some subset of columns from the table)

The **Feature** class is used to name a scalar variable and tally its observed values.  It's just a simple counter.  You can think of it as one *dimension* of a
"feature space" or one "column" of a data table.

The **FeatureSpace** class is used to name a vector of features and tally samples.  A sample is just a vector of feature *values*.

So, the latter class lets us instantiate a feature vector and then observe instances of feature value patterns (samples).  The resulting collection of samples is often called a "sample space".  In this context we can think of it as a "feature space".  After collecting our samples we typically generate a summary report of this sample space.  


    {arrayEgal} = require 'testy'


    class Feature

      constructor: (@name) -> @total = {}

      add: (value) -> 
        @total[value] ?= 0
        @total[value] += 1
        @total

      top: (n = 5) -> 
        byTotal = (x, y) -> x[1] < y[1]
        sorted = ([v, total] for v, total of @total).sort byTotal
        x[0] for x in sorted[...n]

      values: -> Object.keys(@total).sort()


    class FeatureSpace

      constructor: (features, @storing=false) ->
        @features = if typeof features is 'string' \
          then features.split(' ') else features
        @counters = (new Feature(f) for f in @features)
        @count = {}  # counter w/ totals for each unique sample
        @store = []  # store of all samples; use for fast matching
        @[f] = @counters[i] for i, f of @features

      add: (values...) => 
        # Add a sample (an ordered list of values) to the space.
        @store.push values if @storing
        @count[values] ?= 0
        @count[values] += 1
        @counters[i].add(v) for i, v of values

      insert: (hash) ->
        # Insert a hash-formatted sample into the space.
        values = (hash[f] for f in @features)
        @add values...

      flatten: (arr) -> arr.reduce ((x, y) -> x.concat y), []

      makeRows: (sample, total) -> 
        # Convert sample-key string of values to `total` rows.
        sample.split(',') for i in [0...total]

      rows: (max) ->
        # A row is a sample represented as an array of values.
        if @storing
          if max then @store[...max] else @store
        else 
          # convert sample-key strings of count dict to rows
          max or= Object.keys(@count).length + 1
          @flatten(@makeRows(k, total) for k, total of @count)[...max]

      toString: (x) -> x.toString()

      match: (values...) ->
        ### 
        Return samples matching pattern of values.
        Globs ("*") match any value.
        ###
        return @fastMatch(values...) if @storing
        [v, t] for v, t of @count \
          when @isMatch(v.split(','), values.map @toString) 
      
      total: (values...) -> 
        # Total samples matching pattern of values.
        return @fastTotal(values...) if @storing
        matched = @match(values...) # array of sample-key/total pairs
        if matched.length > 1       # sum totals if more than one match
          sum = (x, y) -> x + y[1]
          matched.reduce sum, 0
        else
          matched[0]?[1] or 0       # total of first and only element

      isTruthy: (x) -> x

      isMatch: (row, values) ->
        (row[i] is v for i, v of values when v isnt '*').every @isTruthy

      fastMatch: (values...) ->
        # Uses stored samples for faster matching.
        row for row in @store when @isMatch(row, values)

      fastTotal: (values...) -> @fastMatch(values...).length 

      report: (feature, header=true, delim="\t") ->
        table = []
        if not feature
          header = @features.join(delim) + '\tTOTAL'
          for pattern, total of @count
            values = pattern.split ','
            values.push total
            table.push values.join delim

        else # show breakdown of target feature values
          i = @features.indexOf(feature).toString()   # target index
          cols = (v for j, v of @features when j isnt i)
          uniq = @[feature].values()                  # unique target values
          header = cols.concat(uniq).join(delim)

          seen = {}                                   # cache of seen results
          for pattern, total of @count
            values = pattern.split(',')
            values.splice(i, 1)                       # remove target value
            totals = []                               # target breakdown totals
            for value in uniq                         # iterate over values
              pattern = values[..]                    # to get totals for pattern
              pattern.splice(i, 0, value)
              total = @count[pattern]
              totals.push total or 0
            
            result = values.concat(totals).join delim
            table.push result if result not of seen   # no repeats
            seen[result] = true                       # cache seen

        header += '\n'
        results = table.join '\n'
        if header then header + results else results

      # extra stuff not yet needed ...
      
      product: (sets) -> 
        # cartesian product
        merge = (X, Y) => @flatten(x.concat y for y in Y for x in X)
        sets.reduce merge, [[]]

      combosExcluding: (feature) -> 
          # possible value combinations excluding values of target feature
          @product(@[f].values() for f in @features when f isnt feature)


    exports.Feature = Feature
    exports.FeatureSpace = FeatureSpace

