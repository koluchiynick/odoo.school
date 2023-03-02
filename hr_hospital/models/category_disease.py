from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DiseaseCategory(models.Model):
    _name = 'hr.hospital.disease.category'
    _description = 'Category disease'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(index=True, required=True)
    complete_name = fields.Char(compute='_compute_complete_name',
                                recursive=True,
                                store=True)
    parent_id = fields.Many2one(comodel_name='hr.hospital.disease.category',
                                string='Parent Category',
                                index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(comodel_name='hr.hospital.disease.category',
                               inverse_name='parent_id',
                               string='Child Categories')
    disease_count = fields.Integer(compute='_compute_disease_count')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        for categ in self:
            categ.disease_count = self.env[
                'hr.hospital.type.disease'].search_count([
                    ('category_id', 'child_of', categ.id)
                ])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
