# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tarea(models.Model):
    _name = 'agenda.tarea'
    _description = 'Tarea para Materia y Curso Específico'

    name = fields.Char(string='Título de la Tarea', required=True)
    descripcion = fields.Text(string='Descripción de la Tarea')
    fecha_entrega = fields.Date(string='Fecha de Entrega', required=True)

    # Relación hacia curso-materia específico
    curso_materia_id = fields.Many2one(
        'agenda.curso_materia',
        string="Curso y Materia",
        required=True,
        ondelete='cascade'
    )

    # Relación con el modelo AlumnoRevisado para seguimiento de tareas por alumno
    alumno_revisado_ids = fields.One2many(
        'agenda.alumno_revisado',
        'tarea_id',
        string="Revisiones de Alumnos",
        help="Progreso de los alumnos en esta tarea"
    )

    @api.model
    def create(self, vals_list):
        # Crear la tarea y luego agregar automáticamente los registros de AlumnoRevisado
        tareas = super(Tarea, self).create(vals_list)
        for tarea in tareas:
            tarea.asignar_tarea_a_alumnos()
        return tareas

    def asignar_tarea_a_alumnos(self):
        # Buscar todos los alumnos del curso específico relacionado
        alumnos = self.curso_materia_id.curso_id.alumno_ids  # Asumiendo que hay una relación curso_id -> alumno_ids
        alumno_revisado_vals = []

        for alumno in alumnos:
            alumno_revisado_vals.append({
                'alumno_id': alumno.id,
                'tarea_id': self.id,
                'estado': 'pendiente'
            })

        # Crear registros en AlumnoRevisado en una sola operación
        self.env['agenda.alumno_revisado'].create(alumno_revisado_vals)