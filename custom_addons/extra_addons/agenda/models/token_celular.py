# -*- coding: utf-8 -*-
from odoo import models, fields

class TokenCelular(models.Model):
    _name = 'agenda.token_celular'
    _description = 'Token Celular'

    token = fields.Char(string='token', required=True)

    # Relación uno a uno con res.partner
    res_user_id = fields.Many2one(
        'res.users',  # Relación con el modelo de usuarios de Odoo
        string='Usuario',
        ondelete='cascade',
        required=True
    )

    # Agregar un campo inverso en res.partner para el token celular
    _sql_constraints = [
        ('unique_res_user', 'unique(res_user_id)', 'Cada usuario solo puede tener un token celular.'),
    ]
