# Ejemplo de pipeline de pruebas de github actions

En este proyecto se encuentra el código de ejemplo para ejecutar un pipeline de github que valida que el código esté cubierto en un mínimo de 80% en pruebas.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura
````
├── .github/workflows
|   └── ci_pipeline.yml # Configuración del pipeline
├── component1 # Archivos de la aplicación componente 1
|   ├── src # código de la aplicación
|   ├── tests # Paquete de pruebas
|   ├── Pipfile # Dependencias de la aplicación
|   ├── Pipfile.lock # Archivo lock de dependencias
|   └── pytest.ini # Configuración de pruebas
└── README.md # Estás aquí
````

En archivo ````ci_pipeline.yml```` contiene el pipeline que ejecuta las pruebas. Se recomienda revisar como está configurado y las notas en el.

## Como ejecutar localmente las pruebas

1. Install pipenv
2. Ejecutar pruebas
```
cd component1
pipenv shell
pipenv install --dev
pipenv run pytest --cov=src -v -s --cov-fail-under=80
deactivate
```
