from odoo import models, fields


class Person(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'basic information about the person'

    name = fields.Char(string='First name', required=True)
    last_name = fields.Char(string='Last name', required=True)
    phone = fields.Char(size=13)
    email = fields.Char()
    foto = fields.Image(max_width=64, max_height=64)
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')],
                              default='male')


class ContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact person'
    _inherit = 'hr.hospital.person'
