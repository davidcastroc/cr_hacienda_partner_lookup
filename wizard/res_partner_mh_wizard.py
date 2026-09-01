# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartnerMHWizard(models.TransientModel):
    _name = "res.partner.mh.wizard"
    _description = "Resultado consulta Ministerio de Hacienda"

    partner_id = fields.Many2one("res.partner", string="Contacto", readonly=True)
    identification = fields.Char(string="Identificación", readonly=True)
    name = fields.Char(string="Nombre en Hacienda", readonly=True)
    identification_type = fields.Char(string="Tipo de identificación", readonly=True)
    regime = fields.Char(string="Régimen", readonly=True)
    defaulter = fields.Boolean(string="Moroso", readonly=True)
    omitted = fields.Boolean(string="Omiso", readonly=True)
    state = fields.Char(string="Estado", readonly=True)
    tax_administration = fields.Char(string="Administración tributaria", readonly=True)
    activity_ids = fields.One2many("res.partner.mh.activity.wizard", "wizard_id", string="Actividades económicas", readonly=True)
    registry_ids = fields.One2many("res.partner.mh.registry.wizard", "wizard_id", string="Registros especiales", readonly=True)


class ResPartnerMHActivityWizard(models.TransientModel):
    _name = "res.partner.mh.activity.wizard"
    _description = "Actividad económica consultada en Hacienda"

    wizard_id = fields.Many2one("res.partner.mh.wizard", required=True, ondelete="cascade")
    code = fields.Char(string="Código", readonly=True)
    name = fields.Char(string="Actividad", readonly=True)


class ResPartnerMHRegistryWizard(models.TransientModel):
    _name = "res.partner.mh.registry.wizard"
    _description = "Registro especial consultado en Hacienda"

    wizard_id = fields.Many2one("res.partner.mh.wizard", required=True, ondelete="cascade")
    registry_type = fields.Selection([
        ("mag", "MAG"),
        ("incopesca", "INCOPESCA"),
        ("acuicultores", "Acuicultores"),
    ], string="Registro", readonly=True)
    due_date = fields.Date(string="Fecha", readonly=True)
    active_registry = fields.Boolean(string="Activo", readonly=True)
