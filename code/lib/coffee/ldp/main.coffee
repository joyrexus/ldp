sqlite = require 'sqlite3'


class Dataset
  '''LDP Dataset'''
  print = console.log

  constructor: (@path) -> 
    path ?= process.env.LDP_DB
    @db = new sqlite.Database(path)

  select: (columns='*', where='', limit='', table='', callback=@print) -> 
    sql = "SELECT #{columns} FROM #{table}"
    sql += " WHERE #{where}" if where
    sql += " LIMIT #{limit}" if limit
    @db.all(sql, (err, rows) -> callback rows)

  query: ({columns, where, limit, table, callback}) -> 
    columns ?= '*'
    where ?= ''
    limit ?= ''
    table ?= 'utterances'
    callback ?= console.log
    @select columns, where, limit, table, callback

  close: -> @db.close()


class Utterances extends Dataset

  select: (columns='*', where='', limit='', callback=@print) -> 
    super columns, where, limit, 'utterances', callback


ds = new Dataset
exports.query = (args) -> ds.query args
exports.dataset = ds
exports.utterances = new Utterances
