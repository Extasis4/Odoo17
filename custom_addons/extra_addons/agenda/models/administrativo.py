# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Administrativo(models.Model):
    _name = 'agenda.administrativo'
    _description = 'Administrativo'

    _inherits = {'res.partner': 'contacto_id'}

    contacto_id = fields.Many2one(
        string='Contacto',
        comodel_name='res.partner',
        ondelete='restrict',
        required=True,
    )

    rol = fields.Selection([
        ('director', 'Director'),
        ('subdirector', 'Subdirector'),
        ('secretario', 'Secretario'),
        ('coordinador', 'Coordinador'),
        ('otro', 'Otro')
    ], string='Rol', required=True, help="Rol del administrativo en la institución")

    fecha_ingreso = fields.Date(
        string='Fecha de Ingreso',
        help="Fecha en la que el administrativo se unió a la institución."
    )

    user_id = fields.Many2one('res.users', string='Usuario', readonly=True)

    @api.model
    def create(self, vals):
        administrativo = super(Administrativo, self).create(vals)
        if administrativo.contacto_id.email and administrativo.contacto_id.vat:
            user_vals = {
                'name': administrativo.contacto_id.name,
                'login': administrativo.contacto_id.email,
                'email': administrativo.contacto_id.email,
                'partner_id': administrativo.contacto_id.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
            }
            user = self.env['res.users'].create(user_vals)
            user.sudo().write({'password': administrativo.contacto_id.vat})  # Utiliza el vat como contraseña
            administrativo.user_id = user.id
        return administrativo

    
