import datetime as dt

from marshmallow import Schema, fields


class Cotation(object):
  def __init__(self, date, group, code, value, open, close, desc, inc, qty, transNumb, capital):
      self.date = date
      self.group = group
      self.code = code
      self.value = value
      self.open = open
      self.close = close
      self.inc = inc
      self.desc = desc
      self.qty = qty
      self.tranNumb = transNumb
      self.capital = capital

  def __repr__(self):
      return '<Cotation(name={self.value!r})>'.format(self=self)


class CotationSchema(Schema):
  date = fields.Str()
  group = fields.Str()
  code = fields.Str()
  value = fields.Str()
  open = fields.Str()
  close = fields.Str()
  inc = fields.Str()
  desc = fields.Str()
  qty = fields.Str()
  transNumb = fields.Str()
  capital = fields.Str()
