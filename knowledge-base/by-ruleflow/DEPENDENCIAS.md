# Análisis de Dependencias por RuleFlow

## ¿Qué son las dependencias?

Las **dependencias** son las funciones que una función llama internamente. Por ejemplo:
- `fcnCreateTripPay` llama a `fcnXrefPayTripToTripPay`
- Entonces `fcnXrefPayTripToTripPay` es una **dependencia** de `fcnCreateTripPay`

## ¿Por qué importan las dependencias en RuleFlows?

Cuando un RuleFlow orquesta funciones, cada función puede tener sus propias dependencias. Esto significa:

1. **Complejidad real**: Un RuleFlow con 50 funciones puede ejecutar 200+ funciones si contamos dependencias
2. **Análisis de impacto**: Modificar una dependencia puede afectar múltiples RuleFlows
3. **Debugging**: Un error puede estar en una dependencia, no en la función principal

## Dependencias en los RuleFlows

### CssIfCrewPayRuleFlow (Pago de Tripulación)

**Funciones orquestadas**: 106
**Dependencias estimadas**: ~300-400 funciones adicionales

**Funciones más usadas como dependencias**:
- `fcn` - Función base llamada 256 veces en todo el proyecto
- `fcnShow` - Función de logging llamada 135 veces
- `fcnRoundUpAt2DecimalPlaces` - Redondeo llamado 56 veces
- `fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime` - Validación de fechas (37 veces)
- `fcnGetTimeDiffInMinutes` - Cálculo de diferencias de tiempo (33 veces)

**Funciones con más dependencias en este RuleFlow**:
- `fcnCalculateTripContributionForProductivityPay` - 15 dependencias
- `fcnDistributeToPerDiemBuckets` - 12 dependencias
- `fcnCalculateConusAndOconusPay` - 12 dependencias
- `fcnCalculateExperiencePayBucket` - 11 dependencias

### CssIfTripPayRuleFlow (Pago de Viaje)

**Funciones orquestadas**: 51
**Dependencias estimadas**: ~150-200 funciones adicionales

**Funciones clave con dependencias**:
- `fcnCreateTripPay` - 9 dependencias (función central)
- `fcnCalculateTripCpCodePay` - 10 dependencias
- `fcnCalculateThrAndAdgAndDhr` - 7 dependencias

### CssIfCrewLegalityRuleFlow (Legalidad de Tripulación)

**Funciones orquestadas**: 63
**Dependencias estimadas**: ~200-250 funciones adicionales

**Funciones clave**:
- Validaciones de FAA Rest
- Cálculos de duty duration
- Verificaciones de qualifications

### CssIfTripLegalityRuleFlow (Legalidad de Viaje)

**Funciones orquestadas**: 32
**Dependencias estimadas**: ~100-150 funciones adicionales

**Funciones clave**:
- Validaciones de trip integrity
- Verificaciones de rest periods
- Validaciones de qualifications

## Cómo analizar dependencias

### Método 1: Ver dependencias de una función específica

1. Abre la función en `knowledge-base/functions/[nombre].md`
2. Ve la sección "Dependencias"
3. Ve la sección "Llamado por"

Ejemplo para `fcnCreateTripPay`:

```
Dependencias (llama a):
- fcnXrefPayTripToTripPay
- fcnXrefPayDutyPeriodToDutyPeriodPay
- fcnXrefPayLegToLegPay
- ... (9 total)

Llamado por:
- fcnCreateCrewPayResponse
- fcnCreateTripPayResponse
- ... (4 total)
```

### Método 2: Ver el mapa de dependencias global

Abre `knowledge-base/architecture/dependency-map.md` para ver:
- Top 20 funciones más llamadas (dependencias comunes)
- Top 20 funciones con más dependencias (funciones complejas)

### Método 3: Análisis de impacto con IA

Para analizar el impacto de modificar una función:

```
1. Abre la función: knowledge-base/functions/fcnCreateTripPay.md
2. Copia su contenido
3. Abre function-index.md y busca qué RuleFlows la usan
4. Copia esos RuleFlows
5. Pega todo en ChatGPT:

"Voy a modificar fcnCreateTripPay.
Aquí está su documentación:

[pegar fcnCreateTripPay.md]

Esta función es usada por estos RuleFlows:

[pegar CssIfCrewPayRuleFlow.md]
[pegar CssIfTripPayRuleFlow.md]

¿Qué impacto tendrá mi cambio en las dependencias?"
```

## Funciones críticas (alta dependencia)

Estas funciones son llamadas por muchas otras. Modificarlas tiene alto impacto:

### Top 10 funciones más llamadas:

1. **fcn** (256 llamadas) - Función base
2. **fcnShow** (135 llamadas) - Logging/debugging
3. **fcnRoundUpAt2DecimalPlaces** (56 llamadas) - Redondeo
4. **fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime** (37 llamadas) - Validación de fechas
5. **fcnGetTimeDiffInMinutes** (33 llamadas) - Cálculo de tiempo
6. **fcnIsDateTimeWithinReportFilterRange** (15 llamadas) - Filtros de reporte
7. **fcnDoesDutyPeriodPayBeginInSchedulePeriodPay** (11 llamadas) - Validación de períodos
8. **fcnGetFirstFlyingLeg** (8 llamadas) - Obtener primer leg
9. **fcnIsReserveBlock** (7 llamadas) - Validación de reserva
10. **fcnGetSumOfLegPremium** (6 llamadas) - Suma de premiums

⚠️ **ADVERTENCIA**: Modificar estas funciones afecta muchas partes del sistema.

## Funciones complejas (muchas dependencias)

Estas funciones llaman a muchas otras. Son complejas de entender y modificar:

### Top 10 funciones con más dependencias:

1. **fcnCalculateTripContributionForProductivityPay** (15 deps)
2. **fcnDistributeToPerDiemBuckets** (12 deps)
3. **fcnCalculateConusAndOconusPay** (12 deps)
4. **fcnCalculateExperiencePayBucket** (11 deps)
5. **fcnGetExperiencePayContribution** (11 deps)
6. **fcnCalculateTripCpCodePay** (10 deps)
7. **fcnShowTripPaySummary** (10 deps)
8. **fcnCalculateDutyPeriodContributionForProductivityPay** (9 deps)
9. **fcnCreateInflightTripSets** (9 deps)
10. **fcnCalculateCrewMealPerdiem** (9 deps)

💡 **TIP**: Estas funciones requieren más tiempo para entender y modificar.

## Patrones de dependencias

### Patrón 1: Funciones de utilidad
Funciones como `fcn`, `fcnShow`, `fcnRoundUpAt2DecimalPlaces` son llamadas por muchas otras.
- **Impacto**: Alto si se modifican
- **Complejidad**: Baja (son simples)

### Patrón 2: Funciones de cálculo
Funciones como `fcnCalculate*` tienen muchas dependencias.
- **Impacto**: Medio (usadas en contextos específicos)
- **Complejidad**: Alta (lógica compleja)

### Patrón 3: Funciones de cross-reference
Funciones como `fcnXref*` conectan objetos.
- **Impacto**: Alto (usadas en muchos flujos)
- **Complejidad**: Baja (solo asignaciones)

### Patrón 4: Funciones de validación
Funciones como `fcnIs*`, `fcnDoes*` validan condiciones.
- **Impacto**: Medio-Alto
- **Complejidad**: Baja-Media

## Casos de uso

### Caso 1: Antes de modificar una función

```
1. Abre knowledge-base/architecture/dependency-map.md
2. Busca tu función en "Funciones más llamadas"
3. Si aparece en el top 20, ten MUCHO cuidado
4. Revisa todos los lugares donde es llamada
5. Considera crear una nueva función en lugar de modificar
```

### Caso 2: Debugging de un RuleFlow

```
1. Identifica la función que falla
2. Abre su documentación
3. Revisa sus dependencias
4. El error puede estar en una dependencia, no en la función principal
5. Revisa las dependencias recursivamente
```

### Caso 3: Optimización de performance

```
1. Identifica funciones con muchas dependencias
2. Revisa si todas las dependencias son necesarias
3. Considera refactorizar para reducir dependencias
4. Usa el mapa de dependencias para encontrar duplicación
```

### Caso 4: Análisis de complejidad

```
Para estimar la complejidad de un RuleFlow:

Complejidad = Funciones orquestadas + Suma de dependencias

Ejemplo CssIfCrewPayRuleFlow:
- 106 funciones orquestadas
- ~300-400 dependencias estimadas
- Complejidad total: ~400-500 funciones ejecutadas
```

## Herramientas de análisis

### 1. Búsqueda de dependencias

```bash
# Buscar todas las funciones que llaman a fcnCreateTripPay
grep -r "fcnCreateTripPay" knowledge-base/functions/

# Buscar todas las dependencias de una función
grep -A 20 "## Dependencias" knowledge-base/functions/fcnCreateTripPay.md
```

### 2. Análisis con IA

```
Prompt para ChatGPT:

"Analiza las dependencias de esta función:

[pegar función completa]

1. ¿Cuáles son las dependencias críticas?
2. ¿Hay dependencias circulares?
3. ¿Qué dependencias podrían optimizarse?
4. ¿Cuál es el orden de ejecución?"
```

### 3. Visualización (futuro)

Próximamente:
- Diagramas de dependencias por RuleFlow
- Grafos de llamadas
- Análisis de dependencias circulares
- Métricas de complejidad ciclomática

## Recomendaciones

### ✅ Buenas prácticas:

1. **Antes de modificar**: Revisa el mapa de dependencias
2. **Funciones críticas**: Crea tests exhaustivos
3. **Nuevas funciones**: Minimiza dependencias
4. **Refactoring**: Reduce dependencias circulares
5. **Documentación**: Actualiza cuando cambies dependencias

### ❌ Evita:

1. Modificar funciones en el top 10 de más llamadas sin análisis
2. Crear dependencias circulares
3. Agregar dependencias innecesarias
4. Modificar funciones de utilidad sin consenso del equipo

## Navegación

- [← Volver al índice de RuleFlows](README.md)
- [Ver mapa de dependencias global](../architecture/dependency-map.md)
- [Ver índice de funciones](function-index.md)
- [Guía de uso](COMO_USAR.md)

## Recursos adicionales

- **Mapa de dependencias**: `knowledge-base/architecture/dependency-map.md`
- **Funciones individuales**: `knowledge-base/functions/[nombre].md`
- **Índice de RuleFlows**: `knowledge-base/by-ruleflow/function-index.md`
