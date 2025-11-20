# Sistema de Reservas de Canchas Deportivas

**Autores:**  
- Juan David Palencia Cárdenas  
- Thomas Vásquez  
- Jaime Luis Rueda  
- Andrés Muñoz  

**Docente:** Antonio Rodríguez Linares  
**Asignatura:** Ingeniería de Software II  
**Universidad:** Universidad Autónoma de Bucaramanga  
**Fecha:** Noviembre 2025  

---

## 🏟️ Descripción

El **Sistema de Reservas de Canchas Deportivas** es una aplicación web diseñada para facilitar la **reserva, gestión y administración de canchas** en diferentes horarios.  
Permite a los usuarios registrarse, visualizar la disponibilidad de espacios, realizar reservas y cancelarlas.  
El administrador puede gestionar canchas, horarios y generar reportes del uso de las mismas.

### ✨ Funcionalidades principales

- Registro e inicio de sesión de usuarios.  
- Visualización de disponibilidad de canchas en un calendario.  
- Reserva, modificación y cancelación de reservas.  
- Gestión de canchas y horarios (Administrador).  
- Envío de notificaciones de confirmación o cancelación.  

> *Funcionalidades no incluidas en esta versión:*  
> Pago en línea, integración con aplicaciones externas, inteligencia artificial para sugerencias de horarios.

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/sistema_reservas_canchas.git
   cd sistema_reservas_canchas

Tabla de Contenido 

 

​​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​ 

​​ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Alcance del Proyecto (Sistema de Reservas de Canchas Deportivas) 

El sistema permitirá a los usuarios registrarse, reservar y gestionar canchas deportivas en diferentes horarios. 
El administrador podrá gestionar canchas, horarios y reservas, además de generar reportes de uso. 

Funciones principales en el alcance inicial: 

Registro e inicio de sesión de usuarios. 

Visualización de disponibilidad de canchas. 

Reserva de canchas por fecha y hora. 

Cancelación o modificación de reservas. 

Gestión de canchas y horarios por parte del administrador. 

Notificaciones básicas (confirmación/cancelación). 

No incluidas en esta primera versión: 

Pago en línea. 

Integración con aplicaciones externas. 

Inteligencia artificial para sugerencia de horarios. 

 

 Backlog inicial del proyecto (Historias de Usuario) 

 

 

HU1: Como cliente, quiero registrarme en el sistema para poder reservar canchas. 

HU2: Como cliente, quiero iniciar sesión para acceder a mis reservas. 

HU3: Como cliente, quiero visualizar la disponibilidad de canchas en un calendario para elegir un horario. 

HU4: Como cliente, quiero reservar una cancha indicando la fecha y hora para asegurar mi espacio. 

HU5: Como cliente, quiero cancelar o modificar una reserva para ajustar mi horario. 

HU6: Como administrador, quiero agregar, modificar o eliminar canchas para mantener el sistema actualizado. 

HU7: Como administrador, quiero ver un listado de todas las reservas para llevar el control de la ocupación. 

HU8: Como cliente, quiero recibir una notificación de confirmación al hacer una reserva. 

Breve lista de requerimientos iniciales (mínimo 5) 

 

El sistema debe permitir que los clientes se registren e inicien sesión. 

El sistema debe mostrar a los clientes la disponibilidad de canchas en un calendario. 

El sistema debe permitir que los clientes creen, modifiquen y cancelen reservas. 

El sistema debe permitir que los administradores gestionen canchas (alta, baja y modificación). 

El sistema debe permitir que los administradores consulten un listado de reservas. 

El sistema debe enviar confirmaciones de reserva a los clientes. 

El sistema debe almacenar todas las reservas en una base de datos segura. 

Enlace Plan de gestión en tablero: 

 

 https://trello.com/invite/b/68c4719355de7516f1baf632/ATTIeee81e1ead41c672a2d5912a64d020beE26B4657/my-trello-board 

 

Diagrama y Código UML Simple 

 

@startuml 

class Usuario { 

  - idUsuario: int 

  - nombre: string 

  - email: string 

  - contraseña: string 

  + registrarse() 

  + iniciarSesion() 

} 

  

abstract class Cliente { 

  + reservarCancha() 

  + cancelarReserva() 

} 

  

class Administrador { 

  + gestionarCancha() 

  + verReservas() 

  + modificarReserva() 

} 

  

class Reserva { 

  - idReserva: int 

  - fecha: Date 

  - hora: Time 

  - estado: string 

  + crearReserva() 

  + cancelarReserva() 

  + modificarReserva() 

} 

  

Usuario <|-- Cliente 

Usuario <|-- Administrador 

  

Cliente "1" --> "0..*" Reserva : crea 

Administrador "1" --> "0..*" Reserva : gestiona 

@enduml 

 

 

 

Diagrama de Casos de Uso y Código 

 

@startuml 

actor Cliente 

actor Administrador 

  

rectangle "Sistema de Reservas de Canchas Deportivas" { 

   

  Cliente --> (Registrarse) 

  Cliente --> (Iniciar Sesión) 

  Cliente --> (Visualizar Disponibilidad) 

  Cliente --> (Reservar Cancha) 

  Cliente --> (Cancelar Reserva) 

   

  Administrador --> (Gestionar Canchas) 

  Administrador --> (Ver Reservas) 

  Administrador --> (Modificar o Eliminar Reservas) 

} 

@enduml 

 

 

 

 

Diagrama de Clases y Código 

 

 

@startuml 

class Usuario { 

  - idUsuario: int 

  - nombre: string 

  - email: string 

  - contraseña: string 

  + registrarse() 

  + iniciarSesion() 

} 

  

class Cliente { 

  + reservarCancha() 

  + cancelarReserva() 

} 

  

class Administrador { 

  + gestionarCancha() 

  + verReservas() 

  + modificarReserva() 

} 

  

class Reserva { 

  - idReserva: int 

  - fecha: Date 

  - hora: Time 

  - estado: string 

  + crearReserva() 

  + cancelarReserva() 

  + modificarReserva() 

} 

  

class Cancha { 

  - idCancha: int 

  - nombre: string 

  - tipo: string 

  - disponibilidad: string 

  + actualizarDisponibilidad() 

} 

  

Usuario <|-- Cliente 

Usuario <|-- Administrador 

  

Cliente "1" --> "0..*" Reserva : crea 

Administrador "1" --> "0..*" Reserva : gestiona 

Reserva "1" --> "1" Cancha : asignada a 

@enduml 

 

 

 

Flujo crítico del sistema 

 

 

Participantes: 

Cliente → solicita la reserva. 

Interfaz → medio de comunicación con el sistema. 

ControladorReserva → gestiona la lógica de reservas. 

Base de Datos → guarda la información. 

Administrador → consulta o gestiona la reserva después de su creación. 

Pasos: 

El Cliente solicita reservar cancha indicando fecha y hora. 

La Interfaz envía la solicitud al ControladorReserva. 

El ControladorReserva consulta disponibilidad en la Base de Datos. 

La Base de Datos responde con disponibilidad. 

El ControladorReserva registra la reserva en la Base de Datos. 

La Interfaz notifica al Cliente que la reserva fue creada. 

Posteriormente, el Administrador consulta las reservas en el sistema. 

El ControladorReserva obtiene la lista de reservas desde la Base de Datos y se la muestra al Administrador. 

 

Diagrama de Secuencia y Código 

 

@startuml 

actor Cliente 

actor Administrador 

boundary "Interfaz" as UI 

control "ControladorReserva" as CR 

database "Base de Datos" as DB 

  

Cliente -> UI: Solicitar reserva(fecha, hora) 

UI -> CR: Enviar datos de reserva 

CR -> DB: Consultar disponibilidad 

DB --> CR: Disponibilidad 

CR -> DB: Registrar reserva 

DB --> CR: Confirmación 

CR -> UI: Confirmar reserva 

UI -> Cliente: Notificación de reserva 

  

Administrador -> UI: Consultar reservas 

UI -> CR: Solicitud de listado 

CR -> DB: Obtener reservas 

DB --> CR: Lista de reservas 

CR -> UI: Mostrar reservas 

UI -> Administrador: Visualización reservas 

@enduml 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

10. Despliegue del Sistema en Entorno Local (Laragon 6) 

El sistema de reservas fue desplegado en un entorno local utilizando Laragon 6.0, el cual ofrece un stack de desarrollo integrado con Apache, PHP, MySQL y herramientas adicionales para facilitar la ejecución de aplicaciones web basadas en Laravel. 

1. Requisitos Previos 

Para ejecutar el sistema localmente, el entorno debe contar con: 

Laragon 6.0 o superior 

PHP 8.1 o superior (incluido en Laragon Full) 

Composer instalado (incluido en Laragon) 

Node.js y NPM (para compilar los assets con Vite, si se usa Breeze u otra solución) 

2. Configuración del Entorno 

Instalar Laragon desde el sitio oficial. 

Iniciar los servicios del entorno mediante el botón: 

Start All 
 

Verificar que los servicios de: 

Apache 

MySQL 

estén corriendo correctamente. 

3. Importar el Proyecto 

Colocar el proyecto dentro de la carpeta: 

C:\laragon\www\cancha-reservas 
 

Laragon detecta la carpeta automáticamente y asigna un dominio local del tipo: 

http://cancha-reservas.test 
 

4. Configuración de la Base de Datos 

Acceder a phpMyAdmin desde Laragon: 

Menu → MySQL → phpMyAdmin 
 

Crear una base de datos con el nombre: 

cancha_reservas 
 

Editar el archivo .env del proyecto Laravel con los siguientes valores: 

 

DB_CONNECTION=mysql 
DB_HOST=127.0.0.1 
DB_PORT=3306 
DB_DATABASE=cancha_reservas 
DB_USERNAME=root 
DB_PASSWORD= 
 

5. Instalación de Dependencias 

Abrir una consola dentro de la carpeta del proyecto: 

cd C:\laragon\www\cancha-reservas 
 

Ejecutar: 

composer install 
 

(En caso de usar Breeze, Inertia, Livewire o Vite se deben instalar los paquetes JS) 

npm install 
 

y para levantar el entorno de desarrollo: 

npm run dev 
 

6. Generación de Clave de Aplicación 

En caso de ser necesario, ejecutar: 

php artisan key:generate 
 

7. Ejecución de Migraciones 

Para crear las tablas en la base de datos: 

php artisan migrate 
 

Si el proyecto incluye datos iniciales: 

php artisan db:seed 
 

8. Puesta en Marcha del Sistema 

Con todos los pasos anteriores correctos, el sistema ya puede ejecutarse accediendo a: 

http://cancha-reservas.test 
 

Desde allí, el usuario puede: 

Registrarse o iniciar sesión 

Gestionar canchas (si es administrador) 

Crear y administrar reservas 

9. Ventajas del Despliegue en Laragon 

Configuración automática de virtualhosts 

Servicios integrados en un solo gestor 

Entorno portable y rápido 

Compatible con Composer, PHP, MySQL, Node y NPM 

Ideal para entornos de prácticas. 

 

 

Modelo del Proceso de Desarrollo (SCRUM) 

Metodología Aplicada 

Para el desarrollo del sistema se utilizó SCRUM, un marco de trabajo ágil orientado a la mejora continua, colaboración y entregas incrementales del software. 

 

SCRUM permite desarrollar el sistema en iteraciones cortas llamadas Sprints, en los cuales se planifican, desarrollan y entregan funcionalidades del producto. 

 

Roles Utilizados 

Product Owner (PO): Define los requisitos y prioriza el backlog. 

 

Scrum Master (SM): Facilita el proceso, elimina impedimentos y asegura cumplimiento de SCRUM. 

 

Equipo de Desarrollo: Diseña, programa, prueba y entrega funcionalidades. 

Artefactos 

Product Backlog: Lista priorizada de funcionalidades del sistema (las historias de usuario que ya documentaste). 

 

Sprint Backlog: Funciones seleccionadas para desarrollarse en el sprint actual. 

Incremento: Módulo del sistema completamente funcional al finalizar cada sprint. 

 

Eventos de SCRUM 

Sprint Planning: Se seleccionan las funcionalidades que se desarrollarán. 

Daily Meeting: Reunión diaria de seguimiento (qué hice ayer, qué haré hoy, impedimentos). 

 

Sprint Review: Presentación del avance funcional. 

Sprint Retrospective: Evaluar lo que funcionó y qué se debe mejorar. 

 

Diagrama del Ciclo de Vida SCRUM 

Planificación → Desarrollo → Daily Scrum → Pruebas → Revisión → Retrospectiva → Nuevo Sprint 
 
 

Diseño Orientado a Objetos 

El sistema de reservas sigue principios modernos de diseño orientado a objetos implementados a través de Laravel y MVC. 

 

Patrón Arquitectónico Usado: MVC 

 

Model: 
Representa las entidades como User, Court, Reservation y maneja la conexión con la BD. 

 

View: 
Representada por las vistas Blade, donde se visualizan las pantallas del sistema. 

 

Controller: 
Contiene la lógica de aplicación, validación, cálculo de precios, acceso a datos, etc. 

 

Este patrón facilita: 

 

Separación de responsabilidades 

Escalabilidad 

Mantenibilidad 

Testeabilidad 

Aplicación de Principios SOLID 

 

S — Single Responsibility Principle 

 

Cada controlador cumple un rol único: 

CourtController solo gestiona canchas. 

 

ReservationController solo gestiona reservas. 

O — Open/Closed Principle 

 

El sistema permite agregar nuevas funcionalidades sin modificar el código base (por ejemplo, pagos futuros). 

 

L — Liskov Substitution Principle 

Las clases del sistema pueden reemplazarse sin romper comportamiento. 

 

I — Interface Segregation 

Las clases poseen métodos específicos, evitando interfaces gigantes innecesarias. 

 

D — Dependency Inversion 

Los controladores trabajan contra modelos y servicios, no contra implementaciones rígidas. 

 

Ejemplo real (Laravel) 

public function store(Request $req) 
{ 
   $data = $req->validate([ 
       'court_id' => 'required|exists:courts,id', 
       'start_at' => 'required|date', 
       'end_at'   => 'required|date|after:start_at' 
   ]); 
 
   $court = Court::find($data['court_id']); 
   $price = $court->price_per_hour; 
 
   Reservation::create([ 
       'user_id' => auth()->id(), 
       'court_id' => $court->id, 
       'start_at' => $data['start_at'], 
       'end_at' => $data['end_at'], 
       'price_total' => $price 
   ]); 
 
   return redirect()->route('reservations.index'); 
} 
 
 

Pruebas de Software 

 

Tipos de Pruebas Realizadas 

 

Pruebas Unitarias 

Verifican métodos aislados del sistema (controladores y modelos). 

Ejemplo en PHPUnit: 

public function test_crear_reserva() 
{ 
   $this->actingAs(User::factory()->create()); 
 
   $response = $this->post('/reservations',[ 
       'court_id' => 1, 
       'start_at' => '2025-11-20 10:00', 
       'end_at'   => '2025-11-20 11:00' 
   ]); 
 
   $response->assertRedirect('/reservations'); 
} 
 

 Pruebas de Integración 

Verifican interacción entre: 

Controladores 

Modelos 

Base de datos 

 Pruebas Funcionales / Aceptación 

Se realizaron probando el sistema manualmente mediante: 

Crear usuario 

Crear cancha 

Crear reserva 

Cancelar reserva 

Resultado 

 

El sistema responde correctamente a: 

 

Validaciones 

Registros 

Actualizaciones 

Evita reservas en horarios solapados 

 

12   Integración Continua (CI) – GitHub Actions 

Incluso si aún no lo subes, esta sección te deja bien documentado. 

Descripción 

El sistema puede integrarse con GitHub Actions para ejecutar pruebas automáticamente cada vez que se haga un push. 

Archivo .github/workflows/laravel.yml 

name: Laravel Tests 
 
on: [push, pull_request] 
 
jobs: 
 laravel-tests: 
   runs-on: ubuntu-latest 
 
   steps: 
   - uses: actions/checkout@v2 
 
   - name: Setup PHP 
     uses: shivammathur/setup-php@v2 
     with: 
       php-version: '8.1' 
 
   - name: Install Dependencies 
     run: composer install --prefer-dist 
 
   - name: Run Tests 
     run: php artisan test 
 

Ventajas 

Detecta errores automáticamente 

Asegura estabilidad del código 

Mejora la calidad del producto 

 

13. Manual Técnico 

Tecnologías Utilizadas 

PHP 8.1 (Laragon) 

Laravel 10 

MySQL 

Bootstrap / Blade 

Node.js + Vite (para assets) 

14. Estructura del Proyecto (Resumen) 

 

cancha-reservas/ 
│ 
├── app/ 
│   ├── Models/ (Court, Reservation, User) 
│   ├── Http/Controllers/ 
│   └── Providers/ 
│ 
├── resources/ 
│   └── views/ 
│       ├── courts/ 
│       ├── reservations/ 
│       └── layouts/ 
│ 
├── database/ 
│   ├── migrations/ 
│   └── seeders/ 
│ 
├── public/ 
├── routes/ 
│   └── web.php 
└── vendor/ 
 
 

6. Manual de Usuario 

 

 

Uso como Usuario Normal 

Acceder a 

http://cancha-reservas.test 
 

Registrarse o iniciar sesión 

Seleccionar “Reservas” 

Crear una nueva reserva 

Elegir cancha, fecha y hora 

Guardar 

Consultar reservas creadas 

Uso como Administrador 

Iniciar sesión como admin 

Entrar a Canchas 

Crear 

Editar 

Eliminar 

Gestionar reservas 

Consultar reportes del día 

 

 14   Conclusiones 

El desarrollo del sistema permitió: 

Aplicar arquitectura MVC real en un entorno de producción local. 

Implementar interacción completa con base de datos mediante Eloquent ORM. 

Aplicar principios SOLID y buenas prácticas de diseño. 

Implementar autenticación y roles. 

Realizar pruebas funcionales, unitarias e integradas. 

El proyecto puede escalarse fácilmente con: 

Pasarela de pagos 

Reportes gráficos 

Deploy en la nube 

API para aplicaciones móviles 

 

 15    Referencias APA 

Laravel. (2025). Laravel Framework Documentation. https://laravel.com/docs 
Beck, K. (2000). Extreme Programming Explained. Addison-Wesley. 
Scrum.org. (2025). Scrum Guide. https://scrumguides.org 
Martin, R. (2009). Clean Code. Prentice Hall. 

 
