# models.py
from datetime import date, time


class ReservaInvalida(Exception):
    """Excepción para errores al crear/modificar reservas."""
    pass


class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str, contrasena: str):
        self.idUsuario = id_usuario
        self.nombre = nombre
        self.email = email
        # Evito la ñ en el código por comodidad: contrasena
        self.contrasena = contrasena

    def registrarse(self) -> bool:
        """
        En una app real aquí se guardaría el usuario en BD.
        Por ahora solo devolvemos True como simulación.
        """
        return True

    def iniciarSesion(self, email: str, contrasena: str) -> bool:
        """
        Retorna True si las credenciales coinciden con las del usuario.
        """
        return self.email == email and self.contrasena == contrasena


class Cancha:
    def __init__(self, id_cancha: int, nombre: str, tipo: str, disponibilidad: str = "DISPONIBLE"):
        self.idCancha = id_cancha
        self.nombre = nombre
        self.tipo = tipo
        self.disponibilidad = disponibilidad

    def actualizarDisponibilidad(self, nueva_disponibilidad: str):
        self.disponibilidad = nueva_disponibilidad


class Reserva:
    def __init__(self, id_reserva: int, fecha: date, hora: time,
                 estado: str, cliente: "Cliente", cancha: Cancha):
        self.idReserva = id_reserva
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.cliente = cliente
        self.cancha = cancha

    def crearReserva(self):
        """
        Marca la reserva como CONFIRMADA y ocupa la cancha.
        """
        self.estado = "CONFIRMADA"
        self.cancha.actualizarDisponibilidad("OCUPADA")

    def cancelarReserva(self):
        """
        Marca la reserva como CANCELADA y libera la cancha.
        """
        self.estado = "CANCELADA"
        self.cancha.actualizarDisponibilidad("DISPONIBLE")

    def modificarReserva(self, nueva_fecha: date, nueva_hora: time):
        self.fecha = nueva_fecha
        self.hora = nueva_hora


class Cliente(Usuario):
    def __init__(self, id_usuario: int, nombre: str, email: str, contrasena: str):
        super().__init__(id_usuario, nombre, email, contrasena)
        self.reservas: list[Reserva] = []

    def reservarCancha(self, cancha: Cancha, fecha: date, hora: time) -> Reserva:
        """
        Crea una nueva reserva para una cancha y la marca como CONFIRMADA.
        No permite reservas en la misma cancha, fecha y hora si ya hay una CONFIRMADA.
        """
        # Validar conflicto de horario
        for r in self.reservas:
            if (
                r.cancha.idCancha == cancha.idCancha
                and r.fecha == fecha
                and r.hora == hora
                and r.estado == "CONFIRMADA"
            ):
                raise ReservaInvalida("La cancha ya está ocupada en ese horario.")

        nuevo_id = len(self.reservas) + 1
        reserva = Reserva(
            id_reserva=nuevo_id,
            fecha=fecha,
            hora=hora,
            estado="CONFIRMADA",
            cliente=self,
            cancha=cancha
        )
        self.reservas.append(reserva)
        cancha.actualizarDisponibilidad("OCUPADA")
        return reserva

    def cancelarReserva(self, reserva: Reserva) -> Reserva:
        """
        Cancela una reserva existente del cliente.
        """
        reserva.cancelarReserva()
        return reserva


class Administrador(Usuario):
    def gestionarCancha(self, cancha: Cancha, nueva_disponibilidad: str):
        """
        Cambia el estado de disponibilidad de una cancha.
        """
        cancha.actualizarDisponibilidad(nueva_disponibilidad)

    def verReservas(self, reservas: list[Reserva]):
        """
        Devuelve la lista de reservas (por ejemplo, todas las del sistema).
        """
        return reservas

    def modificarReserva(self, reserva: Reserva, nueva_fecha: date, nueva_hora: time):
        """
        Modifica fecha y hora de una reserva.
        """
        reserva.modificarReserva(nueva_fecha, nueva_hora)
        return reserva
