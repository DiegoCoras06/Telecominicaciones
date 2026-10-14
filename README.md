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
- `public/mapeo_red_ftth.png`: mapa original.
- `index.original.html`: copia de seguridad de la página anterior.

Las fichas contienen valores de referencia del proyecto original, sin auditoría técnica del fabricante. Se omiten del nuevo panel los enlaces a PDF que no existen en la carpeta; todas las fichas se pueden exportar como texto. Google Fonts es opcional: se utilizan fuentes del sistema cuando no hay conexión. Las dependencias se incluyen en la compilación de Vite.
