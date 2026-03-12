# Base de Conocimiento - Organizada por RuleFlow

## ¿Qué es esto?

Esta es una vista alternativa de la base de conocimiento, organizada por **RuleFlows**.

Un **RuleFlow** es como un "director de orquesta" que coordina la ejecución de múltiples funciones y rulesets en un orden específico.

📖 **[Lee la guía completa de uso](COMO_USAR.md)** para aprender a usar esta vista efectivamente.

## RuleFlows Disponibles

### RuleFlows de Pago (Pay)

- [CssIfCrewPayRuleFlow](CssIfCrewPayRuleFlow.md) - Orquesta 106 funciones/rulesets
- [CssIfTripPayRuleFlow](CssIfTripPayRuleFlow.md) - Orquesta 51 funciones/rulesets
- [CssIfTripPaySubFlow](CssIfTripPaySubFlow.md) - Orquesta 7 funciones/rulesets

### RuleFlows de Legalidad (Legality)

- [CssIfCrewLegalityRuleFlow](CssIfCrewLegalityRuleFlow.md) - Orquesta 63 funciones/rulesets
- [CssIfTripLegalityRuleFlow](CssIfTripLegalityRuleFlow.md) - Orquesta 32 funciones/rulesets


## Estadísticas

- **Total de RuleFlows**: 5
- **RuleFlows de Pago**: 3
- **RuleFlows de Legalidad**: 2
- **Total de funciones únicas**: 184

## Navegación

- [Índice de funciones](function-index.md) - Ver qué RuleFlows usan cada función
- [Análisis de dependencias](DEPENDENCIAS.md) - Entender dependencias entre funciones
- [Base de conocimiento original](../README.md) - Vista por tipo de entidad
- [Mapa de dependencias global](../architecture/dependency-map.md) - Top funciones más usadas

## Cómo usar

1. **Encuentra el RuleFlow** que te interesa (ej: CssIfCrewPayRuleFlow)
2. **Abre su página** para ver qué funciones/rulesets orquesta
3. **Haz clic en una función** para ver su documentación completa
4. **Revisa dependencias** en [DEPENDENCIAS.md](DEPENDENCIAS.md) para análisis de impacto
5. **Entiende el flujo** completo del proceso

## Casos de uso

### Entender un proceso completo
Si quieres entender cómo se calcula el pago de tripulación:
1. Ve a [CssIfCrewPayRuleFlow](CssIfCrewPayRuleFlow.md)
2. Verás todas las funciones involucradas en orden
3. Puedes seguir el flujo paso a paso

### Análisis de impacto
Si necesitas modificar una función:
1. Ve al [Índice de funciones](function-index.md)
2. Busca tu función
3. Verás qué RuleFlows la usan
4. Sabrás qué procesos se afectan

### Debugging
Si hay un error en un proceso:
1. Identifica el RuleFlow involucrado
2. Ve su página para ver el flujo
3. Identifica dónde puede estar el problema
4. Revisa las funciones específicas
