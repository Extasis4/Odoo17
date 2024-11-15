# -*- coding: utf-8 -*-

from odoo import models, fields

class CursoPrincipal(models.Model):
    _name = 'agenda.curso'
    _description = 'Curso Principal'

    name = fields.Char(string='Nombre del Curso', required=True)

    capacidad = fields.Integer(string='Capacidad Máxima de Estudiantes', required=True)

    paralelo = fields.Selection([
        ('paralelo_a', 'Paralelo A'),
        ('paralelo_b', 'Paralelo B'),
        ('paralelo_c', 'Paralelo C'),
        ('otro', 'Otro')
    ], string='Paralelo', required=False)

    alumno_ids = fields.One2many(
        'agenda.alumno',  # Modelo relacionado
        'curso_id',       # Campo en el modelo Alumno que relaciona con Curso
        string="Alumnos Inscritos"
    )

    curso_materia_ids = fields.One2many(
        'agenda.curso_materia', 
        'curso_id', 
        string="Materias Agisnadas del Curso")
    
    

