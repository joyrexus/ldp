coffee = require 'coffee-script'

exports.hilite = (text) -> 
  indent = 0
  code = ""
  for t in coffee.tokens text, {rewrite: off}
    [tag, value, line] = t[0..3]
    if tag is "INDENT"
      indent += value
      code += (" " for i in [1 .. indent]).join ""
    else if tag is "OUTDENT"  
      indent -= value
    else if tag is "TERMINATOR"
      if indent
        code += (" " for i in [1 .. indent]).join ""
    else
      switch tag
        when 'IDENTIFIER'
          token = "<span>#{value}</span>"
        else
          token = value
      token += " " if t.spaced
      token += "\n" if t.newLine
      code += token
  "<pre><code>#{code}\n</pre></code>\n"
