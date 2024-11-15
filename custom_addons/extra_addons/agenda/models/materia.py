# -*- coding: utf-8 -*-

from odoo import models, fields

class Materia(models.Model):
    _name = 'agenda.materia'
    _description = 'Materia'

    name = fields.Char(string='Nombre de la Materia', required=True)

    codigo = fields.Char(string='Código', required=True)

    descripcion = fields.Text(string='Descripción')

    curso_materia_ids = fields.One2many(
        'agenda.curso_materia', 
        'materia_id', 
        string="Cursos Asociados")
    
    
