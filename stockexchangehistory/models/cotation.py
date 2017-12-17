import datetime as dt

from marshmallow import Schema, fields


class Cotation(object):
  def __init__(self, date, group, code, value, open, close, desc, inc, qty, transNumb, capital):
      self.date = date
      self.group = group
      self.code = code
      self.value = value
      self.open = float(open.replace(',', '.'))
      self.close = float(close.replace(',', '.'))
      self.inc = float(inc.replace(',', '.'))
      self.desc = float(desc.replace(',', '.'))
      self.qty = int(qty)
      self.tranNumb = float(transNumb.replace(',', '.'))
      self.capital = float(capital.replace(',', '.'))

  def __repr__(self):
      return '<Cotation(name={self.value!r})>'.format(self=self)


class CotationSchema(Schema):
  date = fields.Str()
  group = fields.Str()
  code = fields.Str()
  value = fields.Str()
  open = fields.Float()
  close = fields.Float()
  inc = fields.Float()
  desc = fields.Float()
  qty = fields.Integer()
  transNumb = fields.Float()
  capital = fields.Float()
