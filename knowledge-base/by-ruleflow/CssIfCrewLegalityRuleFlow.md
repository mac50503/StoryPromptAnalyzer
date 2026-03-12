# CssIfCrewLegalityRuleFlow

## Metadata
- **Categoría**: Legality
- **Ubicación**: `CrewRulesRepository\DecisionServices\CSS\Inflight\LegalityRuleFlows\CssIfCrewLegalityRuleFlow`
- **Funciones orquestadas**: 63

## ¿Qué hace este RuleFlow?

Este RuleFlow orquesta la validación de legalidad para tripulación (crew).

## Funciones y Rulesets Orquestados

Este RuleFlow llama a las siguientes 63 funciones/rulesets:

### Funciones (27)

- [fcnAddToAllLegs](../functions/fcnAddToAllLegs.md)
- [fcnAssignAssignment](../functions/fcnAssignAssignment.md)
- [fcnAssignDP](../functions/fcnAssignDP.md)
- [fcnAssignLeg](../functions/fcnAssignLeg.md)
- [fcnAssignLegalitySchedulePeriod](../functions/fcnAssignLegalitySchedulePeriod.md)
- [fcnDetermineCombinedDutyDurationForDutyPeriod](../functions/fcnDetermineCombinedDutyDurationForDutyPeriod.md)
- [fcnDetermineCombinedDutyDurationForTrip](../functions/fcnDetermineCombinedDutyDurationForTrip.md)
- [fcnDetermineDutyPeriodRest](../functions/fcnDetermineDutyPeriodRest.md)
- [fcnDetermineDutyPeriodTransientTerms](../functions/fcnDetermineDutyPeriodTransientTerms.md)
- [fcnDetermineLegTranisentTerms](../functions/fcnDetermineLegTranisentTerms.md)
- [fcnDetermineNonflyTripRest](../functions/fcnDetermineNonflyTripRest.md)
- [fcnDetermineTripAdditionalTransientTerms](../functions/fcnDetermineTripAdditionalTransientTerms.md)
- [fcnDetermineWorkingDay](../functions/fcnDetermineWorkingDay.md)
- [fcnDetermineWorkingDayWithDomicileTime](../functions/fcnDetermineWorkingDayWithDomicileTime.md)
- [fcnGetPreviousDutyPeriod](../functions/fcnGetPreviousDutyPeriod.md)
- [fcnGetPreviousLeg](../functions/fcnGetPreviousLeg.md)
- [fcnGetPreviousTripAdjustedForAirportStandby](../functions/fcnGetPreviousTripAdjustedForAirportStandby.md)
- [fcnGetTrainingGracePeriod](../functions/fcnGetTrainingGracePeriod.md)
- [fcnGetTrainingRenewDate](../functions/fcnGetTrainingRenewDate.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](../functions/fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnReserveBlockReserveBlockConflictLegality` *(documentación no disponible)*
- [fcnReserveBlockTripConflictLegality](../functions/fcnReserveBlockTripConflictLegality.md)
- `fcnReserveTripTripConflictLegality` *(documentación no disponible)*
- [fcnSetLodoQualification](../functions/fcnSetLodoQualification.md)
- `fcnStandbyDutyLimit` *(documentación no disponible)*
- [fcnTripConflictLegality](../functions/fcnTripConflictLegality.md)
- [fcnXrefLegalityLegToLegalityDutyPeriod](../functions/fcnXrefLegalityLegToLegalityDutyPeriod.md)

### Rulesets (35)

- [rsAssociateCrewSchedulePeriodToTrip](../functions/rsAssociateCrewSchedulePeriodToTrip.md)
- [rsAssociateWithReserveBlockDutyPeriods](../functions/rsAssociateWithReserveBlockDutyPeriods.md)
- [rsBlockToBlock](../functions/rsBlockToBlock.md)
- [rsBuildReserveLists](../functions/rsBuildReserveLists.md)
- [rsFAARestCalculationForDutyPeriod](../functions/rsFAARestCalculationForDutyPeriod.md)
- [rsFAARestCalculationForNonfly](../functions/rsFAARestCalculationForNonfly.md)
- [rsLodoQualified](../functions/rsLodoQualified.md)
- [rsTripCoda](../functions/rsTripCoda.md)
- [rsTripDutyReserve_CC](../functions/rsTripDutyReserve_CC.md)
- [rsTripIntegrityDutyPeriod](../functions/rsTripIntegrityDutyPeriod.md)
- `rsTripIntegrityLegRuleset_CC` *(documentación no disponible)*
- [rsUpdatePriorDutyRelease](../functions/rsUpdatePriorDutyRelease.md)
- [rsUpdatePriorNonflyRelease](../functions/rsUpdatePriorNonflyRelease.md)
- `rstDayOffViolation_CC` *(documentación no disponible)*
- `rstDutyPeriodDutyDayLimit_CC` *(documentación no disponible)*
- `rstDutyPeriodDutyDayLimit_FAR` *(documentación no disponible)*
- [rstDutyPeriodDutyReserve](../functions/rstDutyPeriodDutyReserve.md)
- `rstDutyPeriodRest_CC` *(documentación no disponible)*
- `rstDutyPeriodRest_FAR` *(documentación no disponible)*
- `rstDutyQualifications_CC` *(documentación no disponible)*
- `rstFAARest_NonFly_CC` *(documentación no disponible)*
- `rstFAARest_NonFly_FAR` *(documentación no disponible)*
- `rstInternationalTrade_FAR` *(documentación no disponible)*
- `rstLegCoda` *(documentación no disponible)*
- `rstMCLHold` *(documentación no disponible)*
- `rstNoOfLegsIn24Hours_CC` *(documentación no disponible)*
- `rstRedEyeMaxDuty_CC` *(documentación no disponible)*
- `rstRestInWindow_DutyPeriod_CC` *(documentación no disponible)*
- `rstRestInWindow_DutyPeriod_FAR` *(documentación no disponible)*
- `rstRestInWindow_NonFly_FAR` *(documentación no disponible)*
- [rstTrainingQualifications_FAR](../functions/rstTrainingQualifications_FAR.md)
- `rstTripDutyDayLimit_CC` *(documentación no disponible)*
- `rstTripDutyDayLimit_FAR` *(documentación no disponible)*
- [rstTripIntegrity](../functions/rstTripIntegrity.md)
- `rstTripQualifications_CC` *(documentación no disponible)*

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
