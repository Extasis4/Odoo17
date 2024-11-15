# -*- coding: utf-8 -*-

from odoo import models, fields

class AlumnoRevisado(models.Model):
    _name = 'agenda.alumno_revisado'
    _description = 'Registro de Tareas Revisadas para Alumnos'

    # Relación hacia Alumno (un alumno puede tener múltiples registros de tareas revisadas)
    alumno_id = fields.Many2one(
        'agenda.alumno',
        string='Alumno',
        required=True,
        ondelete='cascade',
        help="El alumno que ha recibido la tarea."
    )

    # Relación hacia Tarea (una tarea puede ser revisada por varios alumnos)
    tarea_id = fields.Many2one(
        'agenda.tarea',
        string='Tarea',
        required=True,
        ondelete='cascade',
        help="La tarea asignada al alumno."
    )

    # Campo adicional para almacenar el estado de la tarea (ej. completada, pendiente, etc.)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('atrasada', 'Atrasada')
    ], string='Estado de la Tarea', default='pendiente')

    # Campo para agregar una fecha de entrega específica por alumno, si es necesario
    fecha_entrega_real = fields.Date(
        string='Fecha de Entrega Real',
        help="Fecha en la que el alumno completó la tarea."
    )

    # Campo para comentarios adicionales
    comentario = fields.Text(string='Comentario')

    # SQL Constraint para evitar duplicados de tarea para el mismo alumno
    _sql_constraints = [
        ('unique_alumno_tarea', 'UNIQUE(alumno_id, tarea_id)', 'Cada alumno solo puede tener un registro único por tarea.')
    ]
