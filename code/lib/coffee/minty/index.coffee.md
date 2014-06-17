Minty
=====

*Minimalist templating.*

The `render` method returns a template from template text or an 
interpolated template if passed a data object. Ex:

```coffeescript
text = '<div class="#{ data.group }">#{ data.name }</div>'
data =
  group: 'accounting'
  name: 'Dave'

console.log render text, data

# ... or ...

template = render text
console.log template data
```

## Source

    fs = require 'fs'
    coffee = require 'coffee-script'

    render = (text, data) -> 
      t = text.replace(/\n/g, '\\n').replace(/"/g, '\\"')
      f = coffee.eval '(data) -> "' + t + '"'
      if data then f(data) else f

The `renderFile` method takes the name of a template file and returns a
template or an interpolated template if passed a data object.

    renderFile = (file, data) -> 
      source = fs.readFileSync(file, 'utf8').toString()
      render source, data

Export our methods.

    exports[key] = value for key, value of {render, renderFile}
