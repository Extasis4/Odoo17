# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CursoMateria(models.Model):
    _name = 'agenda.curso_materia'

    _description = 'Curso y materias correspondientes'
    _rec_name = 'display_name'

    curso_id = fields.Many2one(
        'agenda.curso', 
        string="Curso", 
        required=True,
        ondelete='cascade'
        )
    
    materia_id = fields.Many2one(
        'agenda.materia', 
        string="Materia", 
        required=True,
        ondelete='cascade'
        )

    grado = fields.Selection([
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('inicial', 'Inicial'),
        ('nidito', 'nidito')
    ], string='Nivel Educativo', required=True)

    profesor_id = fields.Many2one(
        'agenda.profesor',
        string="Profesor",
        help="Profesor asignado a este curso y materia."
    )
    
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('curso_id.name', 'materia_id.name')
    def _compute_display_name(self):
        """Compute display name to show Curso - Materia without paralelo."""
        for record in self:
            record.display_name = f"{record.curso_id.name} - {record.materia_id.name}"

    @api.constrains('curso_id', 'materia_id', 'grado')
    def _check_unique_curso_materia(self):
        """Validate that the same course doesn't repeat the same subject and grade."""
        for record in self:
            existing = self.search([
                ('curso_id', '=', record.curso_id.id),
                ('materia_id', '=', record.materia_id.id),
                ('grado', '=', record.grado),
                ('id', '!=', record.id)  # Exclude the current record
            ])
            if existing:
                raise ValidationError(
                    "No se puede asignar la misma materia al mismo curso y nivel educativo más de una vez."
                )