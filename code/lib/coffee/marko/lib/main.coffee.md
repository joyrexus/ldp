Marko
=====

    fs = require 'fs'
    marked = require 'marked'
    coffee = require 'coffee-script'

    marked.setOptions
      gfm: true
      breaks: false
      pedantic: false
      sanitize: false

    top = '''
          <!DOCTYPE html>
          <meta charset="utf-8">

          '''


Return CSS styling from file.

    style = (file="#{__dirname}/style.css") -> 
      if file.match /\.css/i
        css = fs.readFileSync file, 'utf8'
        return "<style>\n#{css}\n</style>\n"
      else
        return '<link rel="stylesheet" href="style.css">'

Convert markdown to styled HTML.

    convert = (text, css) ->
      top + style(css) + '<body>\n' + marked text

Run code blocks in markdown.

    evaluate = (text) ->
      tokens = marked.lexer text
      code = (t.text for t in tokens when t.type == 'code').join "\n"
      coffee.eval code

Render a markdown file with embedded coffeescript.

    render = (file, run, css) -> 
      if file.match /\.(litcoffee|md)/i
        text = fs.readFileSync file, 'utf8'
        if run then evaluate(text) else convert(text, css)

    exports.run = evaluate
    exports[key] = value for key, value of {convert, render}
