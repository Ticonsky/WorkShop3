# Informe Técnico: Desarrollo de Aplicación para Fábrica de Carros

## Introducción

El presente informe detalla el desarrollo de una aplicación para la gestión de una fábrica de carros. El objetivo principal de esta aplicación es facilitar la gestión de vehículos, motores y usuarios, permitiendo crear, modificar y eliminar registros, así como calcular el consumo de combustible y medir el tiempo de ejecución de ciertas funciones.

## Estructura del Proyecto

El proyecto se ha estructurado en varios módulos:

- `engines.py`: Contiene las clases relacionadas con los motores de los vehículos.
- `vehicles.py`: Contiene las clases relacionadas con los diferentes tipos de vehículos.
- `catalog.py`: Contiene la clase `Catalog` para gestionar el catálogo de vehículos.
- `user_factory.py`: Contiene las clases para gestionar los usuarios de la fábrica.
- `decorators.py`: Contiene los decoradores para medir el tiempo de ejecución y escribir en un archivo.

## Decisiones de Diseño y Desarrollo

1. **Clases y Estructuras de Datos**: Se han creado clases para representar los diferentes componentes de la fábrica de carros, como motores, vehículos y usuarios. Esto permite una representación más estructurada de los datos y facilita su manipulación.

2. **Uso de Decoradores**: Se han utilizado decoradores para añadir funcionalidades como la medición del tiempo de ejecución y el registro de llamadas a funciones en un archivo. Esto permite añadir estas funcionalidades de forma transparente a las funciones existentes, sin modificar su código.

3. **Gestión de Memoria**: En el caso de la gestión de memoria, se ha utilizado una cola (`deque`) para mantener un registro de las últimas llamadas y limitar el tamaño del caché. Esto evita que el caché crezca indefinidamente y consume más memoria de la necesaria.

4. **Estructura del Código**: Se ha seguido una estructura modular para organizar el código en diferentes archivos según su funcionalidad. Esto facilita la mantenibilidad y la escalabilidad del proyecto.

# Archivos de Texto en el Proyecto

En el proyecto se utilizan varios archivos de texto para almacenar información específica. Cada archivo tiene funciones dedicadas para la lectura y escritura de datos. A continuación se describe el propósito de cada archivo:

- **actions.txt**: Este archivo guarda información sobre las acciones realizadas en la aplicación, como por ejemplo, la creación, modificación o eliminación de vehículos. Las funciones asociadas a este archivo permiten registrar y recuperar estas acciones.

- **users.txt**: En este archivo se almacena la información de los usuarios de la aplicación, incluyendo su rol, nombre, email y contraseña. Las funciones correspondientes permiten gestionar la creación, modificación y eliminación de usuarios.

- **admins.txt**: Similar al archivo de usuarios, este archivo guarda información específica de los administradores de la aplicación. Las funciones asociadas permiten gestionar los administradores y sus acciones en la aplicación.

- **cache_performance.txt**: Este archivo se utiliza para almacenar información relacionada con el rendimiento del caché de la aplicación, como por ejemplo, el tiempo de ejecución de ciertas operaciones. Las funciones asociadas permiten registrar y consultar esta información de manera eficiente.

Cada archivo tiene su conjunto de funciones dedicadas para la manipulación de los datos, garantizando un acceso seguro y eficiente a la información almacenada.

## Conclusiones

La aplicación desarrollada proporciona una solución efectiva para la gestión de una fábrica de carros, ofreciendo funcionalidades clave como la gestión de vehículos, motores y usuarios, así como la medición del tiempo de ejecución y el registro de llamadas a funciones. La estructura modular y las decisiones de diseño tomadas permiten una fácil extensión y mantenimiento de la aplicación en el futuro.

## Recomendaciones

Se recomienda realizar pruebas exhaustivas para garantizar el correcto funcionamiento de la aplicación en diferentes escenarios y con diferentes cargas de trabajo. Además, se puede considerar la implementación de más funcionalidades, como la generación de reportes o la integración con sistemas externos, para mejorar la utilidad y versatilidad de la aplicación.

## Referencias

- Documentación oficial de Python: [https://docs.python.org/3/](https://docs.python.org/3/)
- Documentación de psutil: [https://psutil.readthedocs.io/en/latest/](https://psutil.readthedocs.io/en/latest/)

**Josue Urrego Lopez** - [@Ticonsky](https://github.com/Ticonsky)
