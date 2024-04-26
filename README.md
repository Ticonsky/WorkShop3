# Proyecto de Fabrica de Carros

Este proyecto es una aplicación de gestión para una fábrica de carros. Permite gestionar diferentes tipos de vehículos, motores y usuarios con diferentes roles.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- `engines.py`: Contiene las clases relacionadas con los motores de los vehículos.
- `vehicles.py`: Contiene las clases relacionadas con los diferentes tipos de vehículos.
- `catalog.py`: Contiene la clase `Catalog` para gestionar el catálogo de vehículos.
- `user_factory.py`: Contiene las clases para gestionar los usuarios de la fábrica.
- `decorators.py`: Contiene los decoradores para medir el tiempo de ejecución y escribir en un archivo.

## Funcionalidades Principales

- Crear, modificar y eliminar vehículos en el catálogo.
- Calcular el consumo de combustible de los vehículos.
- Gestionar usuarios con diferentes roles (admin, usuario normal).
- Medir el tiempo de ejecución de las funciones.
- Registrar las llamadas a las funciones en un archivo de log.
