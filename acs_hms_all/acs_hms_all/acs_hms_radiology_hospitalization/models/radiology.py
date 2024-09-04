# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AcsRadiologyRequest(models.Model):
    _inherit = 'acs.radiology.request'

    hospitalization_id = fields.Many2one('acs.hospitalization', string='Hospitalization', ondelete='restrict')

    def prepare_test_result_data(self, line, patient):
        res = super(AcsRadiologyRequest, self).prepare_test_result_data(line, patient)
        res['hospitalization_id'] = self.hospitalization_id and self.hospitalization_id.id or False
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: