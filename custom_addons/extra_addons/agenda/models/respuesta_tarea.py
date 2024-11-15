# -*- coding: utf-8 -*-
from odoo import models, fields

class RespuestaTarea(models.Model):
    _name = 'agenda.respuesta.tarea'
    _description = 'Respuestas o Comentarios del Padre en Tareas'

    tarea_revisada_id = fields.Many2one(
        'agenda.alumno_revisado',
        string='Tarea Revisada',
        ondelete='cascade',
        required=True,
        help="Referencia a la tarea revisada para el alumno"
    )

    mensaje = fields.Text(
        string="Mensaje del Padre",
        help="Mensaje o comentario del padre en relación con la tarea revisada"
    )
    

    # autor_id = fields.Many2one(
    #     'res.users',
    #     string='Autor',
    #     help="Usuario (padre o profesor) que dejó la respuesta o comentario"
    # )
