# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random
import string

class Padre(models.Model):
    _name = 'agenda.padre'
    _description = 'Padre de Familia'

    _inherits = {'res.partner': 'contacto_id'}

    contacto_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='restrict',
        required=True,
        string='Contacto'
    )

    # Relación con alumnos (hijos)
    hijos_ids = fields.One2many(
        comodel_name='agenda.alumno',
        inverse_name='padre_id',
        string='Hijos'
    )

    # Datos adicionales
    oficio = fields.Char(string='Oficio')

    user_id = fields.Many2one(
        'res.users', 
        string='Usuario', 
        readonly=True)

    
    @api.model
    def create(self, vals):
        # Crear el registro de padre usando super()
        padre = super(Padre, self).create(vals)
        
        # Verificar que el contacto tenga correo electrónico y que no exista ya un usuario asignado
        if padre.contacto_id.email and padre.contacto_id.vat and not padre.user_id:
            # Usar el campo vat como contraseña
            temp_password = padre.contacto_id.vat

            # Datos del nuevo usuario
            user_vals = {
                'name': padre.contacto_id.name,         # Nombre del usuario
                'login': padre.contacto_id.email,       # Login del usuario (usando el correo)
                'email': padre.contacto_id.email,       # Email del usuario
                'partner_id': padre.contacto_id.id,     # Asociar el usuario con el contacto de res.partner
                # 'password': temp_password,
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],  # Asignar al grupo básico de usuario interno
                'rol_usuario': 'padre'  # Asignar el rol específico
            }

            # Crear el usuario en res.users
            user = self.env['res.users'].create(user_vals)
            # Asignar el valor de vat como la contraseña del usuario directamente en _set_password
            user.sudo().write({'password': padre.contacto_id.vat})
            # Asociar el usuario recién creado al campo user_id en el registro de padre
            padre.user_id = user.id  

        return padre