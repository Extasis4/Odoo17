# -*- coding: utf-8 -*-
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Campo para definir el rol del usuario
    rol_usuario = fields.Selection([
        ('padre', 'Padre'),
        ('profesor', 'Profesor'),
        ('administrativo', 'Administrativo')
    ], string='Rol del Usuario')

    token_celular_ids = fields.One2many(
        'agenda.token_celular',
        'res_user_id',
        string='Token Celular'
    )