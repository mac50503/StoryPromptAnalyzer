# CssIfTripLegalityRuleFlow

## Metadata
- **Categoría**: Legality
- **Ubicación**: `CrewRulesRepository\DecisionServices\CSS\Inflight\LegalityRuleFlows\CssIfTripLegalityRuleFlow`
- **Funciones orquestadas**: 32

## ¿Qué hace este RuleFlow?

Este RuleFlow orquesta la validación de legalidad para un viaje específico (trip).

## Funciones y Rulesets Orquestados

Este RuleFlow llama a las siguientes 32 funciones/rulesets:

### Funciones (16)

- [fcnAddToAllLegs](../functions/fcnAddToAllLegs.md)
- [fcnAssembleTripLegalityReturnValues](../functions/fcnAssembleTripLegalityReturnValues.md)
- [fcnAssignDP](../functions/fcnAssignDP.md)
- [fcnAssignLeg](../functions/fcnAssignLeg.md)
- [fcnBuildDutyPeriodCalculatedValuesLists](../functions/fcnBuildDutyPeriodCalculatedValuesLists.md)
- [fcnBuildTripCalculatedValuesList](../functions/fcnBuildTripCalculatedValuesList.md)
- [fcnDetermineCombinedDutyDurationForDutyPeriod](../functions/fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnDetermineDutyPeriodRest](../functions/fcnDetermineDutyPeriodRest.md)
- [fcnDetermineDutyPeriodTransientTerms](../functions/fcnDetermineDutyPeriodTransientTerms.md)
- [fcnDetermineLegTranisentTerms](../functions/fcnDetermineLegTranisentTerms.md)
- [fcnDetermineTripTransientTerms](../functions/fcnDetermineTripTransientTerms.md)
- [fcnGetLegalityTripList](../functions/fcnGetLegalityTripList.md)
- [fcnGetPreviousDutyPeriod](../functions/fcnGetPreviousDutyPeriod.md)
- [fcnGetPreviousLeg](../functions/fcnGetPreviousLeg.md)
- [fcnXrefLegalityDutyPeriodToLegalityTrip](../functions/fcnXrefLegalityDutyPeriodToLegalityTrip.md)
- [fcnXrefLegalityLegToLegalityDutyPeriod](../functions/fcnXrefLegalityLegToLegalityDutyPeriod.md)

### Rulesets (15)

- [rsFAARestCalculationForDutyPeriod](../functions/rsFAARestCalculationForDutyPeriod.md)
- [rsTripIntegrityDutyPeriod](../functions/rsTripIntegrityDutyPeriod.md)
- `rsTripIntegrityLegRuleset_CC` *(documentación no disponible)*
- [rsUpdatePriorDutyRelease](../functions/rsUpdatePriorDutyRelease.md)
- `rstDutyPeriodDutyDayLimit_CC` *(documentación no disponible)*
- `rstDutyPeriodDutyDayLimit_FAR` *(documentación no disponible)*
- [rstDutyPeriodDutyReserve](../functions/rstDutyPeriodDutyReserve.md)
- `rstDutyPeriodRest_CC` *(documentación no disponible)*
- `rstDutyPeriodRest_FAR` *(documentación no disponible)*
- `rstNoOfLegsIn24Hours_CC` *(documentación no disponible)*
- `rstPlnTripIntegrity_CC` *(documentación no disponible)*
- `rstRedEyeMaxDuty_CC` *(documentación no disponible)*
- `rstRestInWindow_DutyPeriod_FAR` *(documentación no disponible)*
- `rstTripDutyDayLimit_CC` *(documentación no disponible)*
- [rstTripIntegrity](../functions/rstTripIntegrity.md)

### Decision Tables (1)

- `dtRuleFilters_Inflight` *(documentación no disponible)*

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
