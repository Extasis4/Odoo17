# -*- coding: utf-8 -*-

import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

class MicroServicio(models.Model):
    _name = 'micro_servicio.micro_servicio'
    _description = 'Micro Servicio'

    name = fields.Char(string="Nombre")
    inf = fields.Char(string="Información")  # Campo para almacenar el dato que se enviará
    active = fields.Boolean(string="Activo", 
    default=True
    )

    
    def despedida(self):
        raise UserError('Adios')

    #@api.multi
    def action_access_microservice(self):
            # raise UserError('TEST')
        
            # URL del microservicio
            url = "https://6e44-181-41-156-182.ngrok-free.app/api/tu_microservicio"  # Cambia esta URL por la del microservicio

            # Dato que se enviará en el cuerpo de la solicitud
            data = {
                "inf": self.inf,  # Envía el valor del campo inf en el cuerpo de la solicitud POST
                "name": self.name
            }

            # Realizar la solicitud POST
            try:
                response = requests.post(url, json=data, timeout=5)
                response.raise_for_status()
                result = response.json()  # Si el microservicio devuelve un JSON
                # Procesar los datos recibidos según lo necesites
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Microservicio Accedido',
                        'message': f"Respuesta del microservicio: {result}",
                        'type': 'success',
                        'sticky': False,
                    }
                }
            except requests.exceptions.RequestException as e:
                # Captura de error mejorada
                response_text = e.response.text if e.response else 'Sin respuesta del servidor'
                raise UserError(f"Error al acceder al microservicio: {response_text}")
