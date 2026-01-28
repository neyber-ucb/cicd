# 🚀 Quick Start Guide - CI/CD Implementation

## ⚡ Instalación Rápida

### 1. Clonar el Repositorio
```bash
git clone [URL_DEL_REPO]
cd CICD_Tasks
```

### 2. Backend Setup

```bash
cd backend

# Instalar uv (si no lo tienes)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync --all-extras

# Configurar variables de entorno
cp .env.example .env

# Iniciar servidor
uv run uvicorn main:app --reload
```

El backend estará disponible en: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/api/health

### 3. Frontend Setup

```bash
cd frontend

# Instalar dependencias
npm ci

# Iniciar servidor de desarrollo
npm run dev
```

El frontend estará disponible en: http://localhost:5173

---

## ✅ Verificación Pre-Push (OBLIGATORIO)

### Opción 1: Usar Makefile (Backend)
```bash
cd backend
make all    # Ejecuta quality gates + tests
```

### Opción 2: Comandos Individuales

#### Backend
```bash
cd backend
uv run black --check .      # Formato
uv run ruff check .         # Lint
uv run mypy .               # Tipos
uv run pytest               # Tests
```

#### Frontend
```bash
cd frontend
npm run lint                # Lint
npm run test                # Tests
npm run build               # Build
```

---

## 🔄 Flujo de Trabajo Típico

### 1. Crear Feature Branch
```bash
git checkout main
git pull origin main
git checkout -b feature/mi-funcionalidad
```

### 2. Desarrollar
- Escribe código
- Escribe tests
- Ejecuta quality gates localmente

### 3. Commit (Convención Semántica)
```bash
git add .
git commit -m "feat: add user profile endpoint"
```

### 4. Verificar Localmente
```bash
# Backend
cd backend && make all

# Frontend
cd frontend && npm run lint && npm run test && npm run build
```

### 5. Push y PR
```bash
git push origin feature/mi-funcionalidad
```
- Crear Pull Request en GitHub
- Completar template
- Esperar CI en verde ✅
- Solicitar review

### 6. Merge
- Después de aprobación y CI verde
- Merge a main

---

## 🐛 Troubleshooting

### Backend

**Error: `uv: command not found`**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

**Error: Tests fallan con DB**
```bash
# Verificar que .env existe
cp .env.example .env

# Limpiar base de datos de test
rm -f todo.db
```

**Error: Black falla**
```bash
# Formatear automáticamente
uv run black .
```

**Error: Ruff falla**
```bash
# Intentar auto-fix
uv run ruff check --fix .
```

### Frontend

**Error: `npm ci` falla**
```bash
# Limpiar y reinstalar
rm -rf node_modules package-lock.json
npm install
```

**Error: Tests fallan**
```bash
# Limpiar cache
npm run test -- --clearCache
npm run test
```

**Error: Build falla**
```bash
# Verificar errores de TypeScript
npx tsc --noEmit
```

---

## 📝 Comandos Útiles

### Backend
```bash
make help           # Ver todos los comandos disponibles
make install        # Instalar dependencias
make format         # Formatear código
make lint-fix       # Corregir lint automáticamente
make test-cov       # Tests con coverage HTML
make clean          # Limpiar archivos temporales
```

### Frontend
```bash
npm run dev         # Desarrollo
npm run build       # Build producción
npm run preview     # Preview build
npm run test:watch  # Tests en modo watch
npm run test:coverage  # Coverage HTML
```

---

## 🎯 Checklist Antes de Crear PR

- [ ] Código formateado (Black/ESLint)
- [ ] Sin errores de lint (Ruff/ESLint)
- [ ] Sin errores de tipos (MyPy/TypeScript)
- [ ] Todos los tests pasan
- [ ] Build exitoso (frontend)
- [ ] Commit con convención semántica
- [ ] Branch actualizado con main
- [ ] .env.example actualizado (si aplica)
- [ ] Documentación actualizada (si aplica)

---

## 🔗 Enlaces Rápidos

- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/health
- **Frontend**: http://localhost:5173
- **GitHub Actions**: [URL]/actions
- **README Completo**: [README.md](./README.md)
- **Evidencias**: [EVIDENCIAS.md](./EVIDENCIAS.md)

---

## 💡 Tips

1. **Usa el Makefile**: Simplifica comandos del backend
2. **Ejecuta tests en watch mode**: `npm run test:watch` mientras desarrollas
3. **Revisa coverage**: Mantén > 80% en backend, > 70% en frontend
4. **Commits pequeños**: Facilita code review
5. **Tests primero**: Escribe tests antes de implementar (TDD)

---

## 🆘 Ayuda

Si encuentras problemas:
1. Revisa [README.md](./README.md) para documentación completa
2. Revisa [EVIDENCIAS.md](./EVIDENCIAS.md) para ejemplos
3. Verifica logs de CI en GitHub Actions
4. Ejecuta `make clean` (backend) para limpiar cache

---

## 📚 Próximos Pasos

1. Configura protección de rama main en GitHub
2. Ejecuta el pipeline CI al menos una vez
3. Practica el flujo completo con un PR de prueba
4. Familiarízate con los comandos del Makefile
5. Revisa la documentación de FastAPI y Vitest

---

**¡Listo para empezar! 🎉**
