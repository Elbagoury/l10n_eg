from openerp import models, fields

class estmation_lines(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    estmation_id= fields.One2many('xervon.bu','order_id')


class xervon_bu(models.Model):
    _name = 'xervon.bu'
    bucode = fields.Char(string="BU")
    order_id = fields.Many2one('sale.order')
    directcost= fields.Float(string="Direct Cost ")
    indirectcost = fields.Float(string="Indirect Cost ")
    salesamount = fields.Float(string="Sales Amount ")
    salesmargin = fields.Float(string="Sales Margin ")
