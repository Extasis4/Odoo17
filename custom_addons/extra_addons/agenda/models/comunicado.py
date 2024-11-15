# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Comunicado(models.Model):
    _name = 'agenda.comunicado'
    _description = 'Comunicado para Usuarios'

    titulo = fields.Text(string='Titulo', required=True, help="Titulo del comunicado")
    # Contenido del comunicado
    contenido = fields.Text(string='Contenido', required=True, help="Contenido del comunicado")

    # Tipo de contenido: texto, imagen, video, enlace, etc.
    tipo_contenido = fields.Selection([
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('enlace', 'Enlace')
    ], string='Tipo de Contenido', required=True, help="Tipo de contenido del comunicado")

    # Tipo de comunicado: general, urgente, recordatorio, etc.
    tipo_comunicado = fields.Selection([
        ('general', 'General'),
        ('urgente', 'Urgente'),
        ('recordatorio', 'Recordatorio')
    ], string='Tipo de Comunicado', help="Tipo de comunicado")

    # Fecha de creación del comunicado
    fecha = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now, readonly=True)

    curso_id = fields.Many2one(
        'agenda.curso', 
        string='Curso', 
        help="Selecciona un curso específico para enviar el comunicado a los padres de los estudiantes de este curso."
    )

    # Relación Many2many con res.users para los destinatarios
    destinatarios_ids = fields.Many2many(
        'res.users', 
        string='Destinatarios',
        help="Usuarios que recibirán este comunicado"
    )

    comunicado_enviado_ids = fields.One2many(
        'agenda.comunicado.enviado', 
        'comunicado_id', 
        string="Envíos"
    )
    comunicado_recepcionado_ids = fields.One2many(
        'agenda.comunicado.recepcionado',  # Modelo relacionado
        'comunicado_id',  # Campo inverso en el modelo relacionado
        string="Recepciones"
    )
    comunicado_leido_ids = fields.One2many(
        'agenda.comunicado.leido',
        'comunicado_id',
        string="Lecturas"
    )


    # Campos adicionales para el contenido multimedia
    imagen = fields.Binary(string="Imagen", help="Carga una imagen si el tipo de contenido es imagen")
    video = fields.Binary(string="Video", attachment=True, help="Carga un video en formato MP4 u otro permitido")
    video_filename = fields.Char(string="Nombre del Video")
    enlace_url = fields.Char(string="Enlace", help="URL externa")

    @api.onchange('curso_id')
    def _onchange_curso_id(self):
        """Actualiza los destinatarios al cambiar el curso seleccionado."""
        if self.curso_id:
            padres_ids = self.env['agenda.padre'].search([
                ('hijos_ids.curso_id', '=', self.curso_id.id)
            ]).mapped('user_id')
            self.destinatarios_ids = padres_ids

    @api.onchange('tipo_contenido')
    def _onchange_tipo_contenido(self):
        if self.tipo_contenido != 'imagen':
            self.imagen = False
        if self.tipo_contenido != 'video':
            self.video = False
            self.video_filename = False
        if self.tipo_contenido != 'enlace':
            self.enlace_url = False

    def enviar_comunicado(self):
        for destinatario in self.destinatarios_ids:
            # Crear un registro de Comunicado Enviado para cada destinatario
            self.env['agenda.comunicado.enviado'].create({
                'comunicado_id': self.id,
                'destinatario_id': destinatario.id,
                'fecha_envio': fields.Datetime.now(),
            })
            print(f"Comunicado enviado a {destinatario.name} con contenido: {self.contenido}")

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Comunicado Enviado',
                'message': 'El comunicado ha sido enviado a los destinatarios seleccionados.',
                'type': 'success',
                'sticky': False,
            },
        }

    # Botón para enviar comunicado
    # def enviar_comunicado(self):
    #     for destinatario in self.destinatarios_ids:
    #         print(f"Enviando comunicado a {destinatario.name} con contenido: {self.contenido}")
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': 'Comunicado Enviado',
    #             'message': 'El comunicado ha sido enviado a los destinatarios seleccionados.',
    #             'type': 'success',
    #             'sticky': False,
    #         },
    #     }
