{test, eq} = require 'testy'
{render, renderFile} = require 'minty'


expected = '''
<!-- SAMPLE COFFEESCRIPT TEMPLATE -->
<div class="ALPHA">
    <div class="BETA"></div>
    <div class="GAMMA"></div>
    ALPHA-GAMMA
</div>

'''
data =
  foo: 'ALPHA'
  bar: 'BETA'
  baz: 'GAMMA'

test 'renderFile as template', ->
  template = renderFile 'sample.cst'
  eq expected, template(data)

test 'renderFile with interpolated data', ->
  eq expected, renderFile('sample.cst', data)

test 'render method', ->
  expected = '<div class="ALPHA">'
  template = '<div class="#{ data.foo }">'
  eq expected, render(template, data)
text = '<div class="#{data.group}">#{ data.name }</div>'

test.status()
