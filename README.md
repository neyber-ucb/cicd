# CI/CD Implementation - FastAPI + Vite Project

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo de CI/CD para una aplicación web con:
- **Backend**: FastAPI (Python 3.12) con PostgreSQL
- **Frontend**: React + Vite + TypeScript
- **CI/CD**: GitHub Actions con quality gates automatizados

## 🏗️ Estructura del Proyecto

```
.
├── .github/
│   ├── workflows/
│   │   └── ci.yml                    # Pipeline de CI/CD
│   ├── pull_request_template.md      # Template de PR
│   └── BRANCH_PROTECTION.md          # Guía de protección de ramas
├── backend/
│   ├── app/                          # Código de la aplicación
│   ├── tests/                        # Tests unitarios e integración
│   ├── pyproject.toml                # Dependencias y configuración
│   ├── uv.lock                       # Lockfile de dependencias
│   ├── Makefile                      # Comandos de desarrollo
│   └── .env.example                  # Variables de entorno
└── frontend/
    ├── src/                          # Código fuente
    ├── src/test/                     # Tests con Vitest
    ├── package.json                  # Dependencias
    ├── package-lock.json             # Lockfile de dependencias
    └── vite.config.ts                # Configuración de Vite y Vitest
```

## 🚀 Configuración Inicial

### Backend

```bash
cd backend

# Instalar uv (gestor de paquetes Python)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync --all-extras

# Copiar variables de entorno
cp .env.example .env

# Ejecutar migraciones (si aplica)
uv run python -c "from main import Base, engine; Base.metadata.create_all(bind=engine)"

# Iniciar servidor de desarrollo
uv run uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

# Instalar dependencias
npm ci

# Iniciar servidor de desarrollo
npm run dev

# Build para producción
npm run build
```

## ✅ Quality Gates Implementados

### Backend

1. **Black** (Formateo de código)
   - Línea máxima: 88 caracteres
   - Target: Python 3.12
   - Comando: `uv run black --check .`

2. **Ruff** (Linter)
   - Reglas: pycodestyle, pyflakes, isort, flake8-bugbear
   - Comando: `uv run ruff check .`

3. **MyPy** (Análisis estático de tipos)
   - Strict mode parcial
   - Comando: `uv run mypy .`

4. **Pytest** (Tests)
   - Tests unitarios y de integración
   - Coverage mínimo configurado
   - Comando: `uv run pytest --cov=app`

### Frontend

1. **ESLint** (Linter)
   - Configuración TypeScript + React
   - Comando: `npm run lint`

2. **Vitest** (Tests unitarios)
   - Tests de componentes y utilidades
   - Comando: `npm run test`

3. **TypeScript** (Compilación)
   - Verificación de tipos
   - Comando: `tsc -b`

4. **Build** (Construcción)
   - Verificación de build exitoso
   - Comando: `npm run build`

## 🔄 Flujo de Trabajo (Workflow)

### 1. Crear una nueva rama

```bash
git checkout -b feature/nombre-descriptivo
```

### 2. Ejecutar quality gates localmente (ANTES de hacer commit)

#### Backend
```bash
cd backend
make quality    # Ejecuta format-check, lint, static
make test       # Ejecuta tests
```

O individualmente:
```bash
uv run black --check .
uv run ruff check .
uv run mypy .
uv run pytest
```

#### Frontend
```bash
cd frontend
npm run lint
npm run test
npm run build
```

### 3. Hacer commit siguiendo convención semántica

```bash
git add .
git commit -m "feat: add user authentication endpoint"
git push origin feature/nombre-descriptivo
```

### 4. Crear Pull Request

- Usa el template automático de PR
- Completa todos los campos requeridos
- Marca los checkboxes de evidencia

### 5. Esperar CI Pipeline

El pipeline ejecutará automáticamente:
- ✅ Backend Quality Gates
- ✅ Backend Tests (con PostgreSQL)
- ✅ Frontend Lint
- ✅ Frontend Tests
- ✅ Frontend Build

### 6. Merge

Solo se permite merge cuando:
- ✅ Todos los checks de CI están en verde
- ✅ Al menos 1 aprobación de code review
- ✅ Branch actualizado con main
- ✅ Conversaciones resueltas

## 🛡️ Protección de Rama Main

La rama `main` está protegida con las siguientes reglas:

- ❌ No se permite push directo
- ✅ Requiere Pull Request
- ✅ Requiere aprobación de code review
- ✅ Requiere CI en verde
- ✅ Requiere branch actualizado
- ❌ No se permite bypass (ni para admins)

Ver `.github/BRANCH_PROTECTION.md` para instrucciones de configuración.

## 📝 Convención de Commits

### Formato
```
<tipo>: <descripción>

[cuerpo opcional]

[footer opcional]
```

### Tipos
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `refactor`: Refactorización
- `ci`: Cambios en CI/CD
- `docs`: Documentación
- `test`: Tests
- `style`: Formato (sin cambios de lógica)
- `perf`: Mejoras de rendimiento
- `chore`: Mantenimiento

### Ejemplos
```bash
feat: add user registration endpoint
fix: resolve token expiration issue
test: add integration tests for auth
ci: add PostgreSQL service to pipeline
docs: update API documentation
refactor: simplify database connection logic
```

## 🧪 Endpoints de la API

### Health Check
```bash
GET /api/health
```

Respuesta exitosa:
```json
{
  "status": "healthy",
  "database": "connected"
}
```

### Autenticación
- `POST /auth/register` - Registro de usuario
- `POST /auth/login` - Login
- `GET /auth/me` - Usuario actual

### Tasks
- `GET /tasks/` - Listar tareas
- `POST /tasks/` - Crear tarea
- `GET /tasks/{id}` - Obtener tarea
- `PUT /tasks/{id}` - Actualizar tarea
- `DELETE /tasks/{id}` - Eliminar tarea

## 🐛 Demostración de Fallo Intencional

Para demostrar el enforcement del CI:

```bash
# 1. Crear rama de demo
git checkout -b feature/demo-fallo

# 2. Romper el formato intencionalmente
echo "def broken_function( ):pass" >> backend/app/demo.py

# 3. Commit y push
git add .
git commit -m "ci: break pipeline intentionally"
git push origin feature/demo-fallo

# 4. Crear PR y observar CI fallando

# 5. Corregir el problema
rm backend/app/demo.py
git add .
git commit -m "ci: fix pipeline"
git push origin feature/demo-fallo

# 6. Observar CI en verde
```

## 📊 Coverage Reports

### Backend
Los reportes de coverage se generan en:
- Terminal: Durante ejecución de tests
- HTML: `backend/htmlcov/index.html`
- XML: `backend/coverage.xml` (para CI)

```bash
cd backend
uv run pytest --cov=app --cov-report=html
open htmlcov/index.html
```

### Frontend
Los reportes de coverage se generan en:
- Terminal: Durante ejecución de tests
- HTML: `frontend/coverage/index.html`

```bash
cd frontend
npm run test:coverage
open coverage/index.html
```

## 🔧 Comandos Útiles

### Backend (Makefile)
```bash
make install      # Instalar dependencias
make format       # Formatear código
make format-check # Verificar formato
make lint         # Ejecutar linter
make lint-fix     # Corregir problemas de lint
make static       # Análisis estático
make test         # Ejecutar tests
make test-cov     # Tests con coverage
make quality      # Todos los quality gates
make all          # Quality gates + tests
make clean        # Limpiar archivos temporales
```

### Frontend
```bash
npm ci              # Instalar dependencias (CI)
npm run dev         # Servidor de desarrollo
npm run build       # Build para producción
npm run lint        # Ejecutar ESLint
npm run test        # Ejecutar tests
npm run test:watch  # Tests en modo watch
npm run test:coverage # Tests con coverage
```

## 🌍 Variables de Entorno

### Backend (.env)
```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./todo.db
# DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
```

### Frontend
No requiere variables de entorno para desarrollo local.
Para producción, configurar la URL del backend en el código.

## 📦 Dependencias Principales

### Backend
- FastAPI 0.128+
- SQLAlchemy 2.0+
- Pydantic Settings 2.12+
- Python-Jose (JWT)
- Passlib (Hashing)
- Psycopg2-binary (PostgreSQL)
- Pytest 8.3+
- Black 24.0+
- Ruff 0.8+
- MyPy 1.13+

### Frontend
- React 19.2+
- Vite 7.2+
- TypeScript 5.9+
- React Router 7.13+
- Axios 1.13+
- Vitest 3.0+
- Testing Library
- ESLint 9.39+

## 🎯 Criterios de Evaluación Cumplidos

- ✅ Repositorio Git configurado (monorepo)
- ✅ Rama main protegida
- ✅ Template de PR
- ✅ Backend con lockfile (uv.lock)
- ✅ Formateo configurado (Black)
- ✅ Análisis estático (Ruff + MyPy)
- ✅ Endpoint /api/health con validación DB
- ✅ Tests unitarios y de integración
- ✅ Frontend con lockfile (package-lock.json)
- ✅ ESLint configurado
- ✅ Vitest para tests
- ✅ Build exitoso
- ✅ Pipeline CI con jobs separados
- ✅ Caching por lockfiles
- ✅ Pipeline falla ante incumplimiento
- ✅ Convención de commits y ramas
- ✅ Tests con base de datos real (PostgreSQL)

## 📚 Recursos Adicionales

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vite Documentation](https://vitejs.dev/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Python Black](https://black.readthedocs.io/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Vitest](https://vitest.dev/)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/amazing-feature`)
3. Ejecuta quality gates localmente
4. Commit con convención semántica (`git commit -m 'feat: add amazing feature'`)
5. Push a la rama (`git push origin feature/amazing-feature`)
6. Abre un Pull Request usando el template

## 📄 Licencia

Este proyecto es para fines educativos - Maestría en Ingeniería de Software Avanzada.
