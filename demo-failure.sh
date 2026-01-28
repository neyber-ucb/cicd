#!/bin/bash

# Script para demostrar fallo intencional en CI
# Este script ayuda a demostrar el enforcement del pipeline

set -e

echo "🎭 Demostración de Fallo Intencional en CI"
echo "=========================================="
echo ""

# Verificar que estamos en la rama correcta
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" = "main" ]; then
    echo "❌ Error: No puedes ejecutar esto en la rama main"
    exit 1
fi

echo "📝 Paso 1: Introducir código mal formateado en backend"
echo "def broken_function(  x,y,   z  ):return x+y+z" > backend/app/demo_broken.py
echo "✅ Archivo creado: backend/app/demo_broken.py"
echo ""

echo "📝 Paso 2: Commit del código roto"
git add backend/app/demo_broken.py
git commit -m "ci: break pipeline intentionally for demo"
echo "✅ Commit realizado"
echo ""

echo "📝 Paso 3: Push a la rama remota"
echo "Ejecuta: git push origin $CURRENT_BRANCH"
echo ""
echo "📝 Paso 4: Crear Pull Request en GitHub"
echo "Ve a GitHub y crea un PR desde $CURRENT_BRANCH a main"
echo ""
echo "📝 Paso 5: Observar CI fallando"
echo "El job 'backend_quality' debería fallar en el check de Black"
echo ""
echo "⏸️  Presiona Enter cuando hayas verificado que CI falló..."
read

echo ""
echo "🔧 Paso 6: Corregir el problema"
rm backend/app/demo_broken.py
git add backend/app/demo_broken.py
git commit -m "ci: fix formatting issues"
echo "✅ Archivo eliminado y commit de corrección realizado"
echo ""

echo "📝 Paso 7: Push de la corrección"
echo "Ejecuta: git push origin $CURRENT_BRANCH"
echo ""
echo "📝 Paso 8: Verificar CI en verde"
echo "Regresa a GitHub y verifica que todos los checks pasen ✅"
echo ""
echo "✅ Demostración completada!"
echo ""
echo "Recuerda: Este proceso demuestra que el CI enforcement funciona correctamente"
echo "y que no se puede hacer merge sin que todos los checks pasen."
