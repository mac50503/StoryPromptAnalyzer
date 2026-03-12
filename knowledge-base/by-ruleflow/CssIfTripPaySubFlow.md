# CssIfTripPaySubFlow

## Metadata
- **Categoría**: Pay
- **Ubicación**: `CrewRulesRepository\DecisionServices\CSS\Inflight\PayRuleFlows\CssTripPaySubFlow`
- **Funciones orquestadas**: 7

## ¿Qué hace este RuleFlow?

Este RuleFlow orquesta el cálculo de pago para un viaje específico (trip).

## Funciones y Rulesets Orquestados

Este RuleFlow llama a las siguientes 7 funciones/rulesets:

### Funciones (4)

- [fcnCalculateILabelTrip](../functions/fcnCalculateILabelTrip.md)
- [fcnGetSchedulePeriodPayInScope](../functions/fcnGetSchedulePeriodPayInScope.md)
- [fcnGetSumOfLegPremiumForTrip](../functions/fcnGetSumOfLegPremiumForTrip.md)
- [fcnSetTripRig](../functions/fcnSetTripRig.md)

### Rulesets (3)

- [rsCalculateTAFB](../functions/rsCalculateTAFB.md)
- [rsDetermineRONTripCreditsAndCreditType](../functions/rsDetermineRONTripCreditsAndCreditType.md)
- [rsDetermineTripCreditsAndCreditType](../functions/rsDetermineTripCreditsAndCreditType.md)

## Cómo usar esta información

### Para entender el flujo:
1. Lee la lista de funciones/rulesets en orden
2. Haz clic en cada una para ver su documentación
3. Entiende qué hace cada paso

### Para debugging:
1. Identifica en qué paso está fallando
2. Revisa la función/ruleset específico
3. Verifica sus dependencias

### Para modificaciones:
1. Identifica qué función necesitas cambiar
2. Verifica su posición en el flujo
3. Considera el impacto en pasos posteriores

## Navegación

- [← Volver al índice](README.md)
- [Ver índice de funciones](function-index.md)
