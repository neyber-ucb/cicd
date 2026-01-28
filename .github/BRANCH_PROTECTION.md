# Configuración de Protección de Rama Main

## Instrucciones para configurar la protección de la rama `main`

Para proteger la rama `main` en GitHub, sigue estos pasos:

1. Ve a **Settings** → **Branches** en tu repositorio de GitHub
2. Haz clic en **Add rule** o edita la regla existente para `main`
3. Configura las siguientes opciones:

### Configuración Requerida

#### Branch name pattern
```
main
```

#### Protecciones a habilitar:

- ✅ **Require a pull request before merging**
  - ✅ Require approvals: 1 (mínimo)
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ✅ Require review from Code Owners (opcional)

- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging
  - **Status checks requeridos:**
    - `backend_quality`
    - `backend_tests`
    - `frontend_lint`
    - `frontend_tests`
    - `frontend_build`

- ✅ **Require conversation resolution before merging**

- ✅ **Do not allow bypassing the above settings**
  - Esto previene que incluso los administradores puedan hacer bypass

#### Reglas adicionales recomendadas:

- ✅ **Require linear history** (opcional, para mantener historial limpio)
- ✅ **Include administrators** (aplicar reglas a todos)

## Convención de Commits

Todos los commits deben seguir la convención semántica:

### Formato
```
<tipo>: <descripción>

[cuerpo opcional]

[footer opcional]
```

### Tipos permitidos
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `refactor`: Refactorización de código
- `ci`: Cambios en CI/CD
- `docs`: Documentación
- `test`: Pruebas
- `style`: Formato de código (sin cambios de lógica)
- `perf`: Mejoras de rendimiento
- `chore`: Tareas de mantenimiento

### Ejemplos
```bash
feat: add CRUD productos endpoint
fix: resolve authentication token expiration
test: add product service unit tests
ci: add quality and test gates
docs: update API documentation
refactor: simplify user validation logic
```

## Convención de Ramas

### Formato
```
<tipo>/<descripción-corta>
```

### Ejemplos
```
feature/productos-crud
fix/auth-token-expiration
refactor/database-connection
ci/add-quality-gates
docs/api-documentation
test/integration-tests
```

## Flujo de Trabajo

1. Crear rama desde `main`: `git checkout -b feature/mi-funcionalidad`
2. Hacer commits siguiendo convención semántica
3. Ejecutar tests y linters localmente antes de push
4. Push a la rama: `git push origin feature/mi-funcionalidad`
5. Crear Pull Request usando el template
6. Esperar a que CI pase (todos los checks en verde)
7. Solicitar revisión de código
8. Merge solo después de aprobación y CI verde

## No Bypass Culture

⚠️ **IMPORTANTE**: No se permite hacer bypass de los checks de CI, incluso si eres administrador.

Si el CI falla:
1. Revisar los logs del CI en GitHub Actions
2. Reproducir el error localmente
3. Corregir el problema
4. Hacer commit con la corrección
5. Push y esperar a que CI pase

**Nunca:**
- ❌ Hacer merge sin CI verde
- ❌ Hacer push directo a `main`
- ❌ Usar `--force` en `main`
- ❌ Deshabilitar temporalmente los checks
