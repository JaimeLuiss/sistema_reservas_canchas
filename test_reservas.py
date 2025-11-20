# tests/test_reservas.py
import os
import sys
import datetime as dt

# Añadir la carpeta padre (donde está models.py) al sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models import Cliente, Administrador, Reserva, Cancha, ReservaInvalida


def test_crear_reserva_exitosa():
    cliente = Cliente(1, "Aleja", "aleja@example.com", "1234")
    cancha = Cancha(1, "Cancha 1", "Fútbol 5")

    fecha = dt.date(2025, 5, 10)
    hora = dt.time(18, 0)

    reserva = cliente.reservarCancha(cancha, fecha, hora)

    assert isinstance(reserva, Reserva)
    assert reserva.estado == "CONFIRMADA"
    assert reserva.cancha.idCancha == cancha.idCancha
    assert reserva.cliente is cliente
    assert cancha.disponibilidad == "OCUPADA"


def test_no_permite_reservas_en_horario_ocupado():
    cliente = Cliente(1, "Aleja", "aleja@example.com", "1234")
    cancha = Cancha(1, "Cancha 1", "Fútbol 5")

    fecha = dt.date(2025, 5, 10)
    hora = dt.time(18, 0)

    # Primera reserva: OK
    cliente.reservarCancha(cancha, fecha, hora)

    # Segunda reserva en mismo horario: debe fallar
    try:
        cliente.reservarCancha(cancha, fecha, hora)
        assert False, "Debería lanzar ReservaInvalida por horario ocupado"
    except ReservaInvalida as e:
        assert "ocupada" in str(e).lower()


def test_cancelar_reserva_actualiza_estado_y_disponibilidad():
    cliente = Cliente(1, "Aleja", "aleja@example.com", "1234")
    cancha = Cancha(1, "Cancha 1", "Fútbol 5")

    fecha = dt.date(2025, 5, 10)
    hora = dt.time(18, 0)

    reserva = cliente.reservarCancha(cancha, fecha, hora)
    cliente.cancelarReserva(reserva)

    assert reserva.estado == "CANCELADA"
    assert cancha.disponibilidad == "DISPONIBLE"
