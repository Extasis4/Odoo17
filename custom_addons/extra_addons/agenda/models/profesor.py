# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'agenda.profesor'
    _description = 'Profesor'

    _inherits = {'res.partner': 'contacto_id'}

    contacto_id = fields.Many2one(
        comodel_name='res.partner',
        ondelete='restrict',
        required=True,
        string='Contacto'
    )

    # Campo adicional para identificar al profesor dentro de la escuela
    codigo_profesor = fields.Char(
        string='Código de Profesor',
        required=True,
        help="Código único que identifica al profesor en la institución."
    )

    asignatura = fields.Char(
        string='Asignatura',
        help="Asignatura principal que imparte el profesor."
    )

    cursos_asignados_ids = fields.One2many(
        'agenda.curso_materia',
        'profesor_id',
        string="Cursos Asignados",
        help="Cursos en los que el profesor imparte clases."
    )

    # Otros datos de interés
    fecha_ingreso = fields.Date(
        string='Fecha de Ingreso',
        help="Fecha en la que el profesor se unió a la institución."
    )

    user_id = fields.Many2one('res.users', string='Usuario', readonly=True)

    @api.model
    def create(self, vals):
        profesor = super(Profesor, self).create(vals)
        if profesor.contacto_id.email and profesor.contacto_id.vat:
            user_vals = {
                'name': profesor.contacto_id.name,
                'login': profesor.contacto_id.email,
                'email': profesor.contacto_id.email,
                'partner_id': profesor.contacto_id.id,
                'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
            }
            user = self.env['res.users'].create(user_vals)
            user.sudo().write({'password': profesor.contacto_id.vat})
            profesor.user_id = user.id
        return profesor

    # Validación de unicidad en el código de profesor
    _sql_constraints = [
        ('unique_codigo_profesor', 'UNIQUE(codigo_profesor)', 'El código de profesor debe ser único.')
    ]
