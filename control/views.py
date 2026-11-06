import logging

from django.db import OperationalError, connection
from django.shortcuts import render

from .models import Mensaje

logger = logging.getLogger(__name__)


def home(request):
    database_connected = False
    total_registros = None
    mensajes_recientes = []

    try:
        connection.ensure_connection()
        database_connected = True
        total_registros = Mensaje.objects.count()
        mensajes_recientes = list(Mensaje.objects.order_by("-id")[:5])
    except OperationalError:
        logger.exception("No se pudo consultar la base de datos para el panel.")

    context = {
        "database_connected": database_connected,
        "total_registros": total_registros,
        "mensajes_recientes": mensajes_recientes,
    }
    return render(request, "control/index.html", context)