
from extensions import projects_gettext

PROJECTS = {

    "zarzalejo-boulder": {

        "title": "Zarzalejo Boulder On-Line",

        "category": projects_gettext("Plataforma web · Escalada en bloque"),

        "short_description": projects_gettext(
            "Plataforma web para la gestión, consulta y comunidad de "
            "la escalada en bloque de Zarzalejo."
        ),

        "description": projects_gettext(
            "Aplicación web desarrollada para centralizar la información "
            "sobre la escalada en bloque de Zarzalejo y ofrecer una "
            "plataforma para consultar bloques y sectores, registrar "
            "encadenamientos, participar en la comunidad y gestionar "
            "el contenido de la aplicación."
        ),

        "role": projects_gettext(
            "Desarrollo integral del proyecto: arquitectura, backend, "
            "frontend, base de datos, mapas, funcionalidades de usuario, "
            "administración, seguridad y despliegue."
        ),

        "architecture": projects_gettext(
            "Arquitectura web basada en Nginx, Gunicorn, Flask y "
            "PostgreSQL/PostGIS."
        ),

        "backend": [
            "Python",
            "Flask",
            "SQLAlchemy",
            "Flask-Login",
            "Alembic",
        ],

        "frontend": [
            "HTML",
            "CSS",
            "JavaScript",
            "Leaflet",
            "Plotly",
        ],

        "database": [
            "PostgreSQL",
            "PostGIS",
        ],

        "infrastructure": [
            "Linux",
            "Nginx",
            "Gunicorn",
            "Redis",
        ],

        "features": [
            projects_gettext("Gestión de sectores y bloques"),
            projects_gettext("Información y localización geográfica"),
            projects_gettext("Mapas interactivos con Leaflet"),
            projects_gettext("Registro de encadenamientos"),
            projects_gettext("Estadísticas y rankings"),
            projects_gettext("Perfiles de usuario"),
            projects_gettext("Amistades y likes"),
            projects_gettext("Mensajería"),
            projects_gettext("Propuestas y votaciones"),
            projects_gettext("Galerías de imágenes"),
            projects_gettext("Insignias"),
            projects_gettext("Panel de administración"),
        ],

        "geospatial": projects_gettext(
            "Uso de PostgreSQL/PostGIS para almacenar y gestionar "
            "información geográfica de sectores y bloques, integrada "
            "con mapas interactivos mediante Leaflet."
        ),

        "statistics": projects_gettext(
            "Sistema de estadísticas y visualización de datos relacionados "
            "con la actividad de los usuarios y los encadenamientos."
        ),

        "users": projects_gettext(
            "Sistema de usuarios con perfiles, autenticación, "
            "confirmación de correo electrónico, privacidad y "
            "control de acceso."
        ),

        "security": projects_gettext(
            "Implementación de autenticación, control de acceso, "
            "protección de sesiones, confirmación de correo, "
            "limitación de peticiones y medidas de seguridad HTTP."
        ),

        "administration": projects_gettext(
            "Panel de administración para la gestión y moderación "
            "del contenido y de los usuarios de la plataforma."
        ),

        "deployment": projects_gettext(
            "Aplicación desplegada en Linux mediante Nginx y Gunicorn, "
            "con PostgreSQL/PostGIS como sistema de base de datos y "
            "Redis para servicios auxiliares."
        ),

        "technologies": [
            "Python",
            "Flask",
            "PostgreSQL",
            "PostGIS",
            "SQLAlchemy",
            "JavaScript",
            "Leaflet",
            "Plotly",
            "Pillow",
            "Redis",
            "Nginx",
            "Gunicorn",
            "Linux",
        ],

        "highlights": [
            projects_gettext("Desarrollo integral de la aplicación"),
            projects_gettext("Arquitectura modular con Flask"),
            projects_gettext("Integración de información geoespacial"),
            projects_gettext("Mapas interactivos"),
            projects_gettext("Sistema de usuarios y comunidad"),
            projects_gettext("Estadísticas y visualización de datos"),
            projects_gettext("Administración y moderación"),
            projects_gettext("Despliegue en servidor Linux"),
        ],

        "images": [
            "screenshots/zarzalejo-boulder/zarza1.png",
            "screenshots/zarzalejo-boulder/zarza2.png",
            "screenshots/zarzalejo-boulder/zarza3.png",
            "screenshots/zarzalejo-boulder/zarza4.png",
            "screenshots/zarzalejo-boulder/zarza5.png",
            "screenshots/zarzalejo-boulder/zarza6.png",
            "screenshots/zarzalejo-boulder/zarza7.png",
            "screenshots/zarzalejo-boulder/zarza8.png",
        ],

    },

        "manduca": {

        "title": projects_gettext("Manduca Gastronomía en Movimiento"),

        "category": projects_gettext("Aplicación web · Catering"),

        "short_description": projects_gettext(
            "Aplicación web para la presentación de servicios de catering "
            "y la gestión de solicitudes de presupuesto."
        ),

        "description": projects_gettext(
            "Aplicación web desarrollada para Manduca Gastronomía en "
            "Movimiento, orientada a presentar sus servicios y productos "
            "y facilitar a los clientes la solicitud y gestión de "
            "presupuestos para eventos."
        ),

        "role": projects_gettext(
            "Desarrollo integral del proyecto: arquitectura, backend, "
            "frontend, base de datos, gestión de presupuestos, "
            "administración, seguridad y despliegue."
        ),

        "architecture": projects_gettext(
            "Aplicación web desarrollada con Flask y organizada mediante "
            "Blueprints, con una separación modular de las distintas "
            "áreas funcionales de la aplicación."
        ),

        "backend": [
            "Python",
            "Flask",
            "SQLAlchemy",
            "Flask-Login",
            "Flask-Migrate",
            "Alembic",
        ],

        "frontend": [
            "HTML",
            "CSS",
            "JavaScript",
        ],

        "database": [
            "PostgreSQL",
            "SQLAlchemy",
        ],

        "infrastructure": [
            "Linux",
            "Nginx",
            "Gunicorn",
            "systemd",
        ],

        "features": [
            projects_gettext("Presentación de servicios de catering"),
            projects_gettext("Gestión de productos"),
            projects_gettext("Gestión de packs"),
            projects_gettext("Solicitudes de presupuesto"),
            projects_gettext("Seguimiento del estado de los presupuestos"),
            projects_gettext("Confirmación de presupuestos"),
            projects_gettext("Panel de administración"),
            projects_gettext("Gestión de contenido"),
            projects_gettext("Envío de correos electrónicos"),
        ],

        "statistics": projects_gettext(
            "Estadísticas creadas para controlar el flujo solo para el "
            "administrador de la aplicación, incluyendo el número de "
            "solicitudes de presupuesto."
        ),

        "users": projects_gettext(
            "Sistema de acceso y control de las funciones administrativas "
            "de la aplicación."
        ),

        "security": projects_gettext(
            "Protección de formularios mediante CSRF, limitación de "
            "peticiones en las rutas sensibles y control de acceso "
            "a las funciones administrativas."
        ),

        "administration": projects_gettext(
            "Panel de administración para gestionar productos, packs "
            "y solicitudes de presupuesto, incluyendo el seguimiento "
            "de sus diferentes estados."
        ),

        "deployment": projects_gettext(
            "Aplicación desplegada en Linux mediante Nginx y Gunicorn, "
            "gestionada como servicio mediante systemd."
        ),

        "technologies": [
            "Python",
            "Flask",
            "PostgreSQL",
            "SQLAlchemy",
            "Flask-Login",
            "Flask-Migrate",
            "Alembic",
            "JavaScript",
            "Nginx",
            "Gunicorn",
            "Linux",
        ],

        "highlights": [
            projects_gettext("Desarrollo integral de la aplicación"),
            projects_gettext("Arquitectura modular mediante Blueprints"),
            projects_gettext("Gestión de productos y packs"),
            projects_gettext("Flujo completo de presupuestos"),
            projects_gettext("Panel de administración"),
            projects_gettext("Protección CSRF"),
            projects_gettext("Limitación de peticiones"),
            projects_gettext("Despliegue en servidor Linux"),
        ],

        "images": [
                    "screenshots/manduca/manduca1.png",
                    "screenshots/manduca/manduca2.png",
                    "screenshots/manduca/manduca3.png",
                    "screenshots/manduca/manduca4.png",
                    "screenshots/manduca/manduca5.png",
                    "screenshots/manduca/manduca6.png",
                    "screenshots/manduca/manduca7.png",

                ],

    },

    "reclamaciones-calidad": {

        "title": projects_gettext("Automatización de reclamaciones de calidad"),

        "category": projects_gettext("Aplicación empresarial · Automatización y trazabilidad"),

        "short_description": projects_gettext(
            "Aplicación para automatizar el análisis y la trazabilidad "
            "de reclamaciones de calidad a partir de documentación PDF "
            "y Excel."
        ),

        "description": projects_gettext(
            "Aplicación empresarial desarrollada para automatizar el "
            "procesamiento y análisis de reclamaciones de calidad. El "
            "sistema permite cargar la documentación asociada a una "
            "reclamación, incluyendo información de calidad en puerto, "
            "reclamaciones, albaranes y datos de barcos en puerto, para "
            "relacionar y cotejar la información de las distintas fuentes."
        ),

        "role": projects_gettext(
            "Desarrollo integral del proyecto: arquitectura de la "
            "aplicación, lógica de procesamiento y automatización, "
            "frontend, gestión de usuarios, procesamiento de documentos, "
            "persistencia de resultados, estadísticas y despliegue."
        ),

        "architecture": projects_gettext(
            "Arquitectura modular compuesta por una aplicación Django "
            "para la interfaz y servicios desarrollados en Python para "
            "la lógica y el procesamiento de la información, organizados "
            "y desplegados mediante Docker Compose. La configuración "
            "sensible y específica del entorno se gestiona mediante "
            "variables de entorno."
        ),

        "processing": projects_gettext(
            "El sistema recibe documentación en PDF y Excel relacionada "
            "con cada reclamación y la procesa para extraer y relacionar "
            "la información necesaria. Los datos de calidad en puerto se "
            "cotejan con la información de los barcos en puerto para "
            "establecer la trazabilidad y posteriormente se comparan con "
            "los datos de calidad indicados en la reclamación. El resultado "
            "del análisis se transforma en un informe preparado para su "
            "revisión y posterior incorporación al registro de "
            "reclamaciones."
        ),

        "backend": [
            "Python",
            "Django",
            "Procesamiento de PDF",
            "Procesamiento de Excel",
        ],

        "frontend": [
            "Django",
            "HTML",
            "CSS",
            "JavaScript",
        ],

        "database": [
            "PostgreSQL",
        ],

        "infrastructure": [
            "Docker",
            "Docker Compose",
            "Linux",
        ],

        "features": [
            projects_gettext("Autenticación de usuarios"),
            projects_gettext("Perfiles diferenciados para administradores y trabajadores"),
            projects_gettext("Carga de documentación PDF"),
            projects_gettext("Carga de archivos Excel"),
            projects_gettext("Procesamiento automatizado de documentación"),
            projects_gettext("Cotejo de información de calidad en puerto"),
            projects_gettext("Cotejo con información de barcos en puerto"),
            projects_gettext("Trazabilidad de la mercancía"),
            projects_gettext("Comparación de calidad entre puerto y reclamación"),
            projects_gettext("Generación automatizada de informes"),
            projects_gettext("Almacenamiento de resultados en PostgreSQL"),
            projects_gettext("Registro histórico de reclamaciones procesadas"),
            projects_gettext("Consulta de registros"),
            projects_gettext("Visualización de estadísticas"),
            projects_gettext("Listados de reclamaciones y resultados"),
            projects_gettext("Preparación de resultados para su incorporación a Excel"),
        ],

        "statistics":  projects_gettext(
            "Sistema de estadísticas basado en los registros almacenados "
            "en PostgreSQL. La aplicación consulta los resultados de las "
            "reclamaciones procesadas para generar estadísticas y mostrar "
            "información agregada sobre la actividad y los resultados "
            "obtenidos."
        ),

        "users": projects_gettext(
            "Sistema de autenticación con diferentes perfiles de acceso "
            "para administradores y trabajadores, permitiendo adaptar "
            "las funciones disponibles según el tipo de usuario."
        ),

        "security": projects_gettext(
            "Control de acceso mediante autenticación y gestión de "
            "permisos diferenciados para los distintos perfiles de "
            "usuario."
        ),

        "administration": projects_gettext(
            "Funciones de administración para la gestión de usuarios "
            "y el acceso a la información y funcionalidades destinadas "
            "a los administradores."
        ),

        "deployment": projects_gettext(
            "Aplicación desplegada mediante Docker Compose, con los "
            "distintos componentes organizados como servicios "
            "independientes y configuración específica del entorno "
            "gestionada mediante variables de entorno."
        ),

        "technologies": [
            "Python",
            "Django",
            "PostgreSQL",
            "Docker",
            "Docker Compose",
            "Excel",
            "PDF",
            "HTML",
            "CSS",
            "JavaScript",
            "Linux",
        ],

        "highlights": [
            projects_gettext("Automatización de un proceso empresarial"),
            projects_gettext("Arquitectura modular"),
            projects_gettext("Procesamiento automatizado de PDF y Excel"),
            projects_gettext("Cotejo de información procedente de diferentes fuentes"),
            projects_gettext("Trazabilidad de la mercancía"),
            projects_gettext("Comparación automatizada de datos de calidad"),
            projects_gettext("Generación de informes"),
            projects_gettext("Persistencia de resultados en PostgreSQL"),
            projects_gettext("Registro histórico de reclamaciones"),
            projects_gettext("Estadísticas basadas en datos reales del registro"),
            projects_gettext("Listados y consulta de resultados"),
            projects_gettext("Sistema de usuarios con diferentes perfiles"),
            projects_gettext("Despliegue mediante Docker Compose"),
        ],

        "images": [
            "screenshots/iren/iren1.png",
            "screenshots/iren/iren2.png",
            "screenshots/iren/iren3.png",
            "screenshots/iren/iren4.png",
            "screenshots/iren/iren5.png",
            "screenshots/iren/iren6.png",
        ],

    },



    "localops-ai": {

        "title": "LocalOps AI",

        "category": projects_gettext(
            "Monitorización de infraestructura · Automatización"
        ),

        "short_description": projects_gettext(
            "Plataforma distribuida para recopilar, centralizar y "
            "visualizar información de infraestructura Linux mediante "
            "recolectores Python, Django y PostgreSQL."
        ),

        "description": projects_gettext(
            "Proyecto de monitorización de infraestructura que permite "
            "recopilar información de servidores Linux, centralizar "
            "informes y consultar su evolución desde una plataforma web. "
            "La arquitectura separa la generación de informes en el "
            "servidor monitorizado de su recepción, almacenamiento y "
            "visualización en una plataforma central."
        ),

        "role": projects_gettext(
            "Diseño y desarrollo de la arquitectura distribuida, "
            "recolectores de información, comunicación SSH, integración "
            "con Django ORM, persistencia en PostgreSQL y desarrollo "
            "de la interfaz de monitorización."
        ),

        "architecture": projects_gettext(
            "Arquitectura distribuida entre dos equipos. El servidor "
            "Kakaroto ejecuta recolectores Python independientes que "
            "generan informes JSON. Un collector Python, desplegado "
            "en el equipo central mediante Docker Compose, recupera "
            "los informes mediante SSH y los incorpora a PostgreSQL "
            "utilizando los modelos de Django ORM. La aplicación Django "
            "consulta y presenta la información mediante su dashboard."
        ),

        "processing": projects_gettext(
            "El procesamiento se divide en dos etapas. En Kakaroto, "
            "los recolectores obtienen información de los registros "
            "y servicios del sistema y generan informes estructurados "
            "en JSON. Posteriormente, el collector central recupera "
            "esos informes mediante SSH y los procesa para incorporarlos "
            "a la base de datos a través de Django ORM."
        ),

        "backend": [
            "Python",
            "Django",
            "Django ORM",
            "Python Collector",
            "SSH",
        ],

        "frontend": [
            "Django Templates",
            "HTML",
        ],

        "database": [
            "PostgreSQL",
        ],

        "infrastructure": [
            "Docker",
            "Docker Compose",
            "Linux",
        ],

        "features": [
            projects_gettext("Recopilación automatizada de información de infraestructura"),
            projects_gettext("Generación de informes estructurados en JSON"),
            projects_gettext("Comunicación entre equipos mediante SSH"),
            projects_gettext("Transferencia centralizada de informes"),
            projects_gettext("Persistencia de información mediante Django ORM"),
            projects_gettext("Almacenamiento histórico en PostgreSQL"),
            projects_gettext("Modelos para la gestión de informes de monitorización"),
            projects_gettext("Dashboard web para consultar la información"),
        ],

        "administration": projects_gettext(
            "Aplicación Django organizada mediante modelos y vistas "
            "para gestionar los informes recibidos y presentar la "
            "información almacenada en la plataforma central."
        ),

        "deployment": projects_gettext(
            "Entorno central desplegado mediante Docker Compose, "
            "con una aplicación Django y un collector Python organizados "
            "como componentes independientes. El servidor monitorizado "
            "mantiene sus propios recolectores y genera los informes "
            "que posteriormente se recuperan mediante SSH."
        ),

        "technologies": [
            "Python",
            "Django",
            "Django ORM",
            "PostgreSQL",
            "Docker",
            "Docker Compose",
            "SSH",
            "JSON",
            "Linux",
        ],

        "highlights": [
            projects_gettext("Arquitectura distribuida entre dos equipos"),
            projects_gettext("Separación entre recopilación y procesamiento central"),
            projects_gettext("Comunicación segura mediante SSH"),
            projects_gettext("Procesamiento de informes JSON"),
            projects_gettext("Persistencia mediante Django ORM"),
            projects_gettext("Almacenamiento histórico en PostgreSQL"),
            projects_gettext("Desarrollo de dashboard de monitorización"),
            projects_gettext("Despliegue mediante Docker Compose"),
        ],

        "images": [
            "screenshots/localops-ai/arquitectura.png",
        ],

    },



"servidor-domestico": {

    "title": projects_gettext("Servidor doméstico e infraestructura"),

    "category": projects_gettext("Infraestructura · Administración de sistemas"),

    "short_description": projects_gettext(
        "Infraestructura Linux administrada para desplegar aplicaciones "
        "web, gestionar servicios, redes, contenedores, seguridad y "
        "procesos automatizados de mantenimiento."
    ),

    "description": projects_gettext(
        "Servidor Linux utilizado como infraestructura real para el "
        "despliegue y funcionamiento permanente de aplicaciones web "
        "y servicios. El entorno centraliza la ejecución de aplicaciones "
        "Python, servidores web, bases de datos, contenedores, servicios "
        "de red, acceso remoto, herramientas de inteligencia artificial "
        "y tareas automatizadas de mantenimiento."
    ),

    "role": projects_gettext(
        "Administración integral de la infraestructura, incluyendo la "
        "instalación y configuración del sistema, despliegue de "
        "aplicaciones, gestión de servicios, configuración de red, "
        "seguridad, acceso remoto, contenedores, bases de datos, "
        "automatización de tareas, copias de seguridad y mantenimiento "
        "del entorno."
    ),

    "architecture": projects_gettext(
        "Infraestructura basada en Debian Linux que integra Nginx como "
        "servidor web y proxy inverso, Gunicorn para ejecutar aplicaciones "
        "Python, PostgreSQL como servicio de base de datos, systemd para "
        "la gestión de servicios y Docker y Docker Compose para ejecutar "
        "aplicaciones y herramientas contenedorizadas. Las tareas "
        "periódicas de mantenimiento se automatizan mediante cron."
    ),


    "services": [
        "Nginx",
        "Gunicorn",
        "PostgreSQL",
        "systemd",
        "Docker",
        "Docker Compose",
        "WireGuard",
        "Fail2ban",
        "Ollama",
        "cron",
    ],

    "networking": projects_gettext(
        "Configuración de red local y acceso remoto mediante WireGuard. "
        "El servidor dispone de una red local privada y una red VPN "
        "independiente para el acceso remoto. Nginx actúa como punto "
        "de entrada para las aplicaciones web, mientras que los "
        "servicios internos permanecen restringidos a las redes o "
        "interfaces necesarias."
    ),

    "remote_access": projects_gettext(
        "Acceso remoto mediante WireGuard, proporcionando una red VPN "
        "privada para administrar el servidor y acceder a servicios "
        "internos sin necesidad de exponer directamente los servicios "
        "de administración a Internet."
    ),

    "port_forwarding": projects_gettext(
        "Configuración del router para publicar únicamente los servicios "
        "necesarios hacia el servidor. El acceso web se canaliza mediante "
        "Nginx y el acceso remoto mediante WireGuard, manteniendo los "
        "servicios de administración fuera de la exposición directa "
        "a Internet."
    ),

    "security": projects_gettext(
        "Infraestructura protegida mediante varias capas de seguridad. "
        "UFW controla el tráfico de red mediante reglas específicas, "
        "mientras que Fail2ban monitoriza los servicios protegidos y "
        "aplica bloqueos automáticos ante determinados patrones de "
        "acceso malicioso o intentos reiterados de autenticación. "
        "El acceso SSH está restringido a redes de confianza y el "
        "acceso remoto se realiza mediante WireGuard. Nginx incorpora "
        "además configuraciones específicas de seguridad y control "
        "del tráfico de las aplicaciones publicadas."
    ),

    "firewall": projects_gettext(
        "UFW utilizado como firewall principal del servidor, con reglas "
        "específicas para controlar el tráfico entrante y limitar el "
        "acceso a los diferentes servicios según su origen y necesidad."
    ),

    "fail2ban": projects_gettext(
        "Fail2ban configurado para monitorizar servicios protegidos, "
        "detectar patrones de acceso no deseados y aplicar bloqueos "
        "automáticos frente a determinados intentos reiterados de "
        "autenticación o actividad sospechosa."
    ),

    "nginx_security": projects_gettext(
        "Nginx configurado como punto de entrada de las aplicaciones "
        "web y proxy inverso, incorporando medidas de seguridad, "
        "restricciones de acceso y configuración específica para "
        "reducir la superficie de exposición de los servicios publicados."
    ),

    "administration": projects_gettext(
        "Administración del sistema Linux mediante terminal y servicios "
        "systemd, incluyendo gestión de procesos, configuración de "
        "servicios, supervisión del estado del sistema, mantenimiento "
        "y resolución de incidencias de infraestructura."
    ),

    "automation": projects_gettext(
        "Automatización de tareas periódicas mediante cron, incluyendo "
        "la ejecución programada de copias de seguridad y la actualización "
        "automática de la dirección IP dinámica utilizada para mantener "
        "la conectividad remota."
    ),

    "backups": projects_gettext(
        "Sistema de copias de seguridad automatizadas mediante tareas "
        "programadas, permitiendo mantener copias periódicas de la "
        "información y servicios relevantes de la infraestructura."
    ),

    "dynamic_ip": projects_gettext(
        "Actualización automática de la dirección IP pública mediante "
        "una tarea programada, manteniendo actualizada la información "
        "necesaria para el acceso remoto y los servicios asociados "
        "a la conexión doméstica."
    ),

    "technologies": [
        "Debian",
        "Linux",
        "Nginx",
        "Gunicorn",
        "PostgreSQL",
        "systemd",
        "Docker",
        "Docker Compose",
        "UFW",
        "Fail2ban",
        "WireGuard",
        "Cloudflare",
        "cron",
        "Ollama",
        "Python",
    ],

    "highlights": [
        projects_gettext("Administración de servidor Linux"),
        projects_gettext("Despliegue de aplicaciones web reales"),
        projects_gettext("Configuración de Nginx y Gunicorn"),
        projects_gettext("Gestión de servicios mediante systemd"),
        projects_gettext("Administración de PostgreSQL"),
        projects_gettext("Contenedores Docker y Docker Compose"),
        projects_gettext("Configuración de firewall mediante UFW"),
        projects_gettext("Protección automática mediante Fail2ban"),
        projects_gettext("Configuración de seguridad de Nginx"),
        projects_gettext("Control de servicios expuestos a Internet"),
        projects_gettext("Configuración de port forwarding"),
        projects_gettext("Acceso remoto mediante WireGuard"),
        projects_gettext("Gestión de redes y servicios internos"),
        projects_gettext("Automatización de tareas mediante cron"),
        projects_gettext("Copias de seguridad programadas"),
        projects_gettext("Actualización automática de IP dinámica"),
        projects_gettext("DDNS mediante Cloudflare"),
        projects_gettext("Ejecución local de herramientas de inteligencia artificial"),
        projects_gettext("Infraestructura utilizada para aplicaciones reales"),
    ],

    "deployment": projects_gettext(
        "Las aplicaciones web se ejecutan mediante Gunicorn y son "
        "publicadas mediante Nginx como servidor web y proxy inverso. "
        "Los servicios persistentes se gestionan mediante systemd, "
        "mientras que las aplicaciones y herramientas que requieren "
        "contenedorización se ejecutan mediante Docker Compose. "
        "Las tareas periódicas de mantenimiento, copias de seguridad "
        "y actualización de la IP dinámica se ejecutan automáticamente "
        "mediante cron."
    ),

    "database": [],

    "images": [
        "screenshots/servidor/servidor1.jpeg",
    ],
},

}