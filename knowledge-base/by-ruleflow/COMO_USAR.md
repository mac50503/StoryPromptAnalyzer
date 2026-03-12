# Cómo Usar la Vista por RuleFlows

## ¿Qué es un RuleFlow?

Un **RuleFlow** es como un "director de orquesta" que coordina la ejecución de múltiples funciones y rulesets en un orden específico para completar un proceso de negocio.

Por ejemplo:
- **CssIfCrewPayRuleFlow** orquesta 106 funciones para calcular el pago completo de una tripulación
- **CssIfTripLegalityRuleFlow** orquesta 32 funciones para validar la legalidad de un viaje

## ¿Por qué usar esta vista?

### Ventajas sobre la vista alfabética:

1. **Contexto completo**: Ves todas las funciones de un proceso juntas
2. **Orden lógico**: Las funciones están en el orden que se ejecutan
3. **Análisis de impacto**: Sabes qué procesos afectas al modificar una función
4. **Debugging más fácil**: Identificas dónde está fallando un proceso

## Casos de uso

### 1. Entender un proceso completo

**Escenario**: Necesitas entender cómo se calcula el pago de tripulación.

**Pasos**:
1. Abre `CssIfCrewPayRuleFlow.md`
2. Lee la lista de 106 funciones orquestadas
3. Haz clic en las funciones que te interesan
4. Entiende el flujo completo

**Con IA**:
```
1. Abre CssIfCrewPayRuleFlow.md
2. Copia TODO (Ctrl+A, Ctrl+C)
3. Pega en ChatGPT:

"Aquí está el RuleFlow de pago de tripulación.
¿Puedes explicarme cómo se calculan los premiums?"
```

### 2. Análisis de impacto

**Escenario**: Vas a modificar `fcnCalculateTripDutyHours` y necesitas saber qué se afecta.

**Pasos**:
1. Abre `function-index.md`
2. Busca `fcnCalculateTripDutyHours`
3. Verás que la usan:
   - CssIfCrewPayRuleFlow
   - CssIfTripPayRuleFlow
4. Ahora sabes que tu cambio afecta ambos procesos de pago

**Con IA**:
```
1. Copia CssIfCrewPayRuleFlow.md
2. Copia CssIfTripPayRuleFlow.md
3. Pega ambos en ChatGPT:

"Voy a modificar fcnCalculateTripDutyHours.
Esta función es usada por estos RuleFlows:

[pegar ambos RuleFlows]

¿Qué impacto tendrá mi cambio?"
```

### 3. Debugging

**Escenario**: El cálculo de pago de un viaje está fallando.

**Pasos**:
1. Identifica el RuleFlow: `CssIfTripPayRuleFlow`
2. Abre `CssIfTripPayRuleFlow.md`
3. Revisa las 51 funciones en orden
4. Identifica dónde puede estar el problema
5. Revisa esas funciones específicas

### 4. Onboarding de nuevos desarrolladores

**Escenario**: Un nuevo desarrollador necesita entender el sistema.

**Pasos**:
1. Empieza con `README.md` (este directorio)
2. Lee la descripción de cada RuleFlow
3. Profundiza en el RuleFlow más relevante para su trabajo
4. Usa la documentación de funciones individuales como referencia

## Estructura de archivos

```
by-ruleflow/
├── README.md                      # Índice principal
├── COMO_USAR.md                   # Esta guía
├── DEPENDENCIAS.md                # ⭐ Análisis de dependencias
├── CssIfCrewPayRuleFlow.md        # 106 funciones de pago de tripulación
├── CssIfTripPayRuleFlow.md        # 51 funciones de pago de viaje
├── CssIfTripPaySubFlow.md         # 7 funciones (sub-flujo)
├── CssIfCrewLegalityRuleFlow.md   # 63 funciones de legalidad de tripulación
├── CssIfTripLegalityRuleFlow.md   # 32 funciones de legalidad de viaje
└── function-index.md              # Índice inverso (función → RuleFlows)
```

## Navegación rápida

### Para entender procesos:
- [CssIfCrewPayRuleFlow](CssIfCrewPayRuleFlow.md) - Pago completo de tripulación
- [CssIfTripPayRuleFlow](CssIfTripPayRuleFlow.md) - Pago de un viaje
- [CssIfCrewLegalityRuleFlow](CssIfCrewLegalityRuleFlow.md) - Legalidad de tripulación
- [CssIfTripLegalityRuleFlow](CssIfTripLegalityRuleFlow.md) - Legalidad de viaje

### Para análisis de impacto:
- [function-index.md](function-index.md) - Ver qué RuleFlows usan cada función
- [DEPENDENCIAS.md](DEPENDENCIAS.md) - Análisis completo de dependencias

### Para búsqueda alfabética:
- [../README.md](../README.md) - Vista por entidad (lista alfabética)

### Para análisis de dependencias globales:
- [../architecture/dependency-map.md](../architecture/dependency-map.md) - Top funciones más usadas

## Tips

1. **Usa Ctrl+F** para buscar funciones específicas dentro de un RuleFlow
2. **Copia RuleFlows completos** a ChatGPT para análisis profundos
3. **Revisa function-index.md** antes de modificar cualquier función
4. **Combina vistas**: usa RuleFlows para contexto, funciones individuales para detalles

## Preguntas frecuentes

### ¿Cuál es la diferencia con la vista alfabética?

- **Vista alfabética** (`../README.md`): Lista todas las funciones de A-Z
- **Vista por RuleFlows** (aquí): Agrupa funciones por proceso de negocio

### ¿Cuándo usar cada vista?

- **RuleFlows**: Cuando necesitas entender un proceso completo o analizar impacto
- **Alfabética**: Cuando buscas una función específica por nombre

### ¿Los RuleFlows muestran el orden de ejecución?

No exactamente. Muestran qué funciones son orquestadas, pero el orden exacto depende de la lógica interna del RuleFlow. Para ver el orden exacto, necesitas revisar el archivo XML del RuleFlow.

### ¿Puedo modificar estos archivos?

Estos archivos son generados automáticamente. Si modificas el código Blaze, regenera la documentación:

```bash
python knowledge-base-extractor/extract_blaze_knowledge.py
python knowledge-base-extractor/reorganize_by_ruleflow.py
```

## Soporte

Si tienes dudas:
1. Revisa [README.md](README.md) para el índice completo
2. Consulta [../README.md](../README.md) para la vista alfabética
3. Lee [../../knowledge-base-extractor/README.md](../../knowledge-base-extractor/README.md) para regenerar la documentación
