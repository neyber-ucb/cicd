## Qué cambia
<!-- Selecciona el tipo de cambio -->
- [ ] feat - Nueva funcionalidad
- [ ] fix - Corrección de bug
- [ ] refactor - Refactorización de código
- [ ] ci - Cambios en CI/CD
- [ ] docs - Documentación
- [ ] test - Pruebas
- [ ] style - Formato de código

## Descripción
<!-- Describe brevemente los cambios realizados -->

## Evidencia
- [ ] CI en verde (todos los checks pasaron)
- [ ] Tests ejecutados localmente (backend)
- [ ] Tests ejecutados localmente (frontend)
- [ ] Linter ejecutado localmente (backend)
- [ ] Linter ejecutado localmente (frontend)
- [ ] Build exitoso localmente (frontend)

## Comandos ejecutados localmente
```bash
# Backend
cd backend
uv sync
uv run black --check .
uv run ruff check .
uv run mypy .
uv run pytest

# Frontend
cd frontend
npm ci
npm run lint
npm run test
npm run build
```

## Riesgo / Rollback
**Riesgo:** 
<!-- Describe los riesgos potenciales de este cambio -->

**Rollback:** 
<!-- Describe cómo revertir este cambio si es necesario -->

## Checklist adicional
- [ ] No hay secretos o credenciales en el código
- [ ] La documentación está actualizada
- [ ] Los commits siguen convención semántica
- [ ] Branch actualizado con main
