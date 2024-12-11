# Sistema de Equipamiento con Login Básico

Este proyecto es un sistema desarrollado en Python que permite gestionar un inventario de equipamientos con un sistema de login básico y operaciones CRUD (Crear, Leer, Actualizar y Eliminar) integrado con una base de datos MySQL.

## Características Principales

- **Sistema de Login Seguro**: Los códigos de acceso son encriptados utilizando el algoritmo MD5 para garantizar mayor seguridad.
- **Gestor de Equipamientos**: Permite registrar, consultar, modificar, y eliminar equipamientos de la base de datos.
- **Consulta Avanzada**: Ofrece funcionalidades para consultar registros dentro de un rango de precios.
- **Conexión a Base de Datos**: Utiliza `pymysql` para interactuar con una base de datos MySQL.
- **Validaciones**: Asegura que no se dupliquen los registros mediante verificaciones en la base de datos.
