# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Alumno(models.Model):
    _name = 'agenda.alumno'
    _description = 'alumno'

    _inherits = {'res.partner': 'contacto_id'}

    contacto_id = fields.Many2one(
        string='contacto',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
    )

    # Relación inversa hacia Padre
    padre_id = fields.Many2one(
        comodel_name='agenda.padre',
        string='Padre',
        ondelete='set null'
    )

    curso_id = fields.Many2one(
        'agenda.curso',
        string='Curso',
        required=True,
        ondelete='restrict',
        help="Curso al que pertenece el alumno"
    )
    
    grado = fields.Selection([
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('inicial', 'Inicial'),
        ('nidito', 'Nidito')
    ], string='Nivel Educativo', required=True)

    fecha_nacimiento = fields.Date(
        string='Fecha de Nacimiento'  # Campo editable sin cálculo
    )

    edad = fields.Integer(
        string='Edad',
        compute='_compute_edad',
        store=True
    )

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                today = date.today()
                birth_date = record.fecha_nacimiento
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.edad = age
            else:
                record.edad = 0
    
    @api.constrains('curso_id', 'contacto_id')
    def _check_unique_alumno_curso(self):
        """Validate that a student is not enrolled in the same course more than once."""
        for record in self:
            existing_enrollment = self.search([
                ('curso_id', '=', record.curso_id.id),
                ('contacto_id', '=', record.contacto_id.id),
                ('id', '!=', record.id)  # Exclude the current record
            ])
            if existing_enrollment:
                raise ValidationError(
                    "El alumno ya está inscrito en este curso. No puede estar inscrito en el mismo curso más de una vez."
                )