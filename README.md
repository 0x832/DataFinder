# DataFindder

DataFinder es un script sencillo que te permite realizar búsquedas avanzadas en Google 
utilizando técnicas de Google Dorking. Con esta herramienta, puedes encontrar información específica en sitios web concretos,
archivos de un tipo particular (como PDF), términos dentro de URLs o en el contenido de las páginas, 
entre muchas otras opciones, aprovechando los operadores avanzados de búsqueda de Google.



## Características principales:
- **Guardar resultados** en un archivo: Después de realizar una búsqueda, los resultados encontrados se guardarán automáticamente en un archivo de texto, lo que te permite revisar los enlaces en cualquier momento.

- **Búsquedas avanzadas:** DataFinder te permite ser muy específico en tus búsquedas, para que puedas encontrar exactamente lo que necesitas.

## Funcionalidades de búsqueda:
- **Filtrar por dominios específicos:** Puedes buscar contenido solo en sitios web específicos, como dominios educativos (por ejemplo, .edu).
- **Buscar archivos por tipo:** Encuentra archivos de un tipo específico, como PDF, documentos de Word o archivos de Excel.
- **Filtrar por fecha:** Limita los resultados a información publicada antes o después de una fecha determinada.
- **Búsqueda avanzada:** Encuentra resultados que contengan ciertas palabras en el título, en la URL o en el contenido de la página.
- **Opción de búsqueda directa o específica:** Puedes realizar búsquedas generales escribiendo directamente lo que deseas encontrar o utilizar argumentos más específicos para mejorar tu búsqueda.


## Ejemplo de uso:
Este comando buscará en sitios con dominio **.edu** información sobre vulnerabilidades en formato **PDF**, y guardará los **primeros 10 resultados** en un archivo llamado **"documento.txt"**.


```python
  python datafinder.py -si "edu" -in "vulnerability" -t "pdf" -na "documento" --nu "10"
```

## Para qué te puede servir este script?
- **Investigación académica:** Si necesitas información técnica o específica (como artículos académicos o documentación), DataFinder te ayudará a encontrar archivos PDF y documentos relevantes.

- **Búsqueda de recursos técnicos:** Encuentra documentación técnica, guías y otros recursos relacionados con temas específicos como vulnerabilidades o redes.

- **Exploración rápida:** Utiliza DataFinder para obtener información estructurada sin necesidad de hacerlo mediante argumentos.




# Responsabilidad y Uso Ético
El autor de este software no asume ninguna responsabilidad por el uso indebido del 
software o cualquier daño que pueda resultar del uso de este software. El usuario es el único 
responsable de su uso y debe utilizarlo de manera ética y legal.

El autor de este software no será responsable de ninguna pérdida, daño o consecuencia que resulte del uso de este software.
Por favor, utilice este software con responsabilidad y de acuerdo con las leyes y regulaciones aplicables en su jurisdicción.

