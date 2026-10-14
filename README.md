# FibraLab — Explorador FTTH

Interfaz educativa de telecomunicaciones con Vue 3, Vite y Lucide. Diseño claymórfico, adaptable a móviles, con búsqueda, filtros, mapa interactivo y fichas exportables.

## Ejecutar en Windows

```powershell
npm.cmd install
npm.cmd run dev
```

Abre la dirección que muestra Vite. Para generar la versión de producción:

```powershell
npm.cmd run build
npm.cmd run preview
```

El resultado se genera en `dist/`. Usa un servidor HTTP para servirlo.

## Contenido

- `src/App.vue`: interfaz e interacciones.
- `src/style.css`: diseño y reglas adaptables.
- `src/data.json`: seis fichas conservadas del proyecto original.
- `mapeo_red_ftth.png`: mapa original conservado como respaldo.
- `src/assets/mapa-ftth-*.webp`: mapas optimizados para la web.
- `index.original.html`: copia de seguridad de la página anterior.

Las fichas contienen valores de referencia del proyecto original, sin auditoría técnica del fabricante. Se omiten del nuevo panel los enlaces a PDF que no existen en la carpeta; todas las fichas se pueden exportar como texto. Google Fonts es opcional: se utilizan fuentes del sistema cuando no hay conexión. Las dependencias se incluyen en la compilación de Vite.

## Optimización del mapa y Netlify

El PNG original pesa 2.179 KB. La web usa WebP de 150 KB (960 px) y 344 KB (1408 px), con selección según pantalla y densidad de píxeles. Al ampliar el mapa se usa la versión completa. Las dimensiones declaradas reservan espacio sin distorsionar el mapa. Vite genera nombres con hash para actualizar correctamente los archivos cuando cambian.

Para actualizar el despliegue manual, ejecuta `npm.cmd run build` y sube la nueva carpeta `dist` al sitio existente de Netlify. No subas la carpeta del proyecto ni el PNG original.

Para regenerar los WebP si cambia el original:

```powershell
python -m pip install --target .tools/image-optimizer Pillow
python scripts/optimize-map.py
npm.cmd run build
```

Pillow solo se usa durante la optimización; no es necesario para ejecutar la web ni para compilar los WebP ya incluidos.
