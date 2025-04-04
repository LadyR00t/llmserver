﻿# ai-challenge

## LLM Server - Servicio de Inferencia Local

Este proyecto implementa un servidor local para ejecutar modelos de lenguaje (LLM) que permite realizar inferencias sin depender de servicios externos.

### Descripción

El `llmserver` es una aplicación que permite ejecutar modelos de lenguaje de gran tamaño en un entorno local. Proporciona una API REST para realizar consultas al modelo y obtener respuestas, todo ejecutándose en contenedores Docker para facilitar la portabilidad y el despliegue.

### Características

- Ejecución local de modelos LLM
- API REST para consultas al modelo
- Contenerizado con Docker para facilitar la implementación
- Puerto de servicio: 31337
- Reconstrucción completa del entorno mediante scripts
- Disponible en versión local y cloud

### Requisitos

- Docker y Docker Compose
- Espacio en disco suficiente para los contenedores y modelos
- Puerto 31337 disponible en la máquina host

### Instalación y Ejecución

1. Clona este repositorio:
   ```
   git clone github.com/LadyR00t/llmserver.git
   cd llmserver
   ```

2. Ejecuta el script de construcción:
   ```
   chmod +x inference/build.sh
   ./inference/build.sh
   ```

3. El servicio estará disponible en `http://localhost:31337`

### Uso

Para realizar consultas al modelo, puedes utilizar el cliente incluido:

```python
python inference/client.py "Tu pregunta aquí"
```

O realizar peticiones HTTP directamente al endpoint:

```
POST http://localhost:31337/api/generate
```

### Versión Cloud

También está disponible una versión cloud del servicio que puede ser accedida remotamente. Para conectarte al servidor cloud:

1. Modifica el archivo `inference/client.py` para usar la IP pública del servidor:

2. Asegúrate de que el puerto 31337 esté abierto en el firewall del servidor cloud.

### Estructura del Proyecto

- `code_runner/`: Contiene los archivos para el servidor LLM
- `inference/`: Scripts y herramientas para la inferencia
- `test/`: Casos de prueba y ejemplos
