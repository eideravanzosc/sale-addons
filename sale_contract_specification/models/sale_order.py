# Copyright 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _domain_draft_condition_tmpl_id(self):
        domain = []
        domain += [('tmpl_model', '=', self._name)]
        domain += [('tmpl_type', 'in', ('quotation', 'both'))]
        return domain

    def _domain_condition_tmpl_id(self):
        domain = []
        domain += [('tmpl_model', '=', self._name)]
        domain += [('tmpl_type', 'in', ('order', 'both'))]
        return domain

    draft_condition_tmpl_id = fields.Many2one(
        comodel_name='contract.condition.template',
        string='Specification Template', copy=False,
        domain=lambda self: self._domain_draft_condition_tmpl_id())
    draft_condition_ids = fields.One2many(
        comodel_name='sale.draft.condition', inverse_name='sale_id',
        string='Sale Conditions')
    condition_tmpl_id = fields.Many2one(
        comodel_name='contract.condition.template',
        string='Specification Template', copy=False,
        domain=lambda self: self._domain_condition_tmpl_id())
    condition_ids = fields.One2many(
        comodel_name='sale.order.condition', inverse_name='sale_id',
        string='Sale Conditions')

    @api.onchange('draft_condition_tmpl_id')
    def _onchange_draft_condition_tmpl_id(self):
        if self.draft_condition_tmpl_id:
            condition_ids = [
                (0, 0, {'condition_id': x.condition_id.id,
                        'description': x.description})
                for x in self.draft_condition_ids]
            condition_ids += [
                (0, 0, {'condition_id': x.id,
                        'description': x.description or x.name})
                for x in self.draft_condition_tmpl_id.condition_ids]
            self.draft_condition_ids = condition_ids
            for condition in self.draft_condition_ids:
                condition._onchange_condition_id()

    @api.onchange('condition_tmpl_id')
    def _onchange_condition_tmpl_id(self):
        if self.condition_tmpl_id:
            condition_ids = [
                (0, 0, {'condition_id': x.condition_id.id,
                        'description': x.description})
                for x in self.condition_ids]
            condition_ids += [
                (0, 0, {'condition_id': x.id,
                        'description': x.description or x.name})
                for x in self.condition_tmpl_id.condition_ids]
            self.condition_ids = condition_ids
            for condition in self.condition_ids:
                condition._onchange_condition_id()
