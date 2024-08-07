Sistema web de Inventario y Solicitud en línea para Municipalidad de San Pedro de Melipilla, para el área de DIDECO.

- Programado en Python, con Django, usando herramienta Visual Studio Code. 
- Base de datos primeramente en Oracle SQL Developer, pero después fue migrado a SQL Server (SSMS).

El sistema se desarrolló para digitalizar los registros de los productos usados por DIDECO guardados en el almacén de la Municiaplidad. Se necesitaba llevar el stock de los productos, de manera actualizada,
para así saber cuáles estaban disponibles para entregar a ciudadanos en situaciones de necesidad que lo requirieran. El sistema está pensado para ser usado por la encargada de DIDECO, su asistente, las trabajadoras
sociales, y el encargado de bodega. Los ciudadanos que lo requieran llenan junto con la trabajadora social la solicitud de productos o materiales. Si algún material no está disponible en el momento, la trabajadora
social lo puede visualizar en el mismo sistema, y puede quedar reservado y notificarse cuando esté disponible. Una vez lista la solicitud, se agrega a la lista, la encargada de DIDECO con su perfil revisa lo
solicitado, y una vez que lo aprueba, se notifica al encargado de bodega, quien con su usuario revisa la solicitud, prepara los productos, y estando listos notifica para que sean retirados por cliente.
 El encargado de bodega tiene completo control sobre los productos y materiales registrados, manteniendo actualizado el stock, agregando productos nuevos, o modificando, si es necesario. La asistente de la jefa de
 DIDECO con su usuario también tiene control sobre algunos productos específicos. Adicionalmente, el sistema también lleva el inventario de materiales que son exclusivos para el uso laboral de los departamentos 
de la Municipalidad (materiales de aseo, de oficina, etc), y estos también pueden ser solicitados por medio del sistema.

 El sistema está realizado sólo hasta la fase de desarrollo, y se desplegó en un servidor de pruebas de Django (comando "python manage.py runserver" desde VSC).
 También se tuvo que crear completamente la base de datos, ya que casi todo el inventario y formularios de solicitud estaban en papel.
 El sistema fue de agrado y aceptado por la asistente de la jefa de DIDECO de la Municipalidad, y también fue aprobado como Portafolio de Título de Ingeniería en informática en Duoc UC.
