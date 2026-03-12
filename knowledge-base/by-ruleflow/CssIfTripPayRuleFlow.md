# CssIfTripPayRuleFlow

## Metadata
- **Categoría**: Pay
- **Ubicación**: `CrewRulesRepository\DecisionServices\CSS\Inflight\PayRuleFlows\CssTripPayRuleFlow`
- **Funciones orquestadas**: 51

## ¿Qué hace este RuleFlow?

Este RuleFlow orquesta el cálculo de pago para un viaje específico (trip).

## Funciones y Rulesets Orquestados

Este RuleFlow llama a las siguientes 51 funciones/rulesets:

### Funciones (37)

- [fcnAddToDutyPeriodSumOfLegPremimum](../functions/fcnAddToDutyPeriodSumOfLegPremimum.md)
- [fcnAssociateAirportStandbyWithOverlappingTrip](../functions/fcnAssociateAirportStandbyWithOverlappingTrip.md)
- [fcnAssociateAirportStandbyWithReserve](../functions/fcnAssociateAirportStandbyWithReserve.md)
- [fcnCalculateActualDutyDuration](../functions/fcnCalculateActualDutyDuration.md)
- [fcnCalculateConusAndOconusPay](../functions/fcnCalculateConusAndOconusPay.md)
- [fcnCalculateDutyPeriodRig](../functions/fcnCalculateDutyPeriodRig.md)
- [fcnCalculateLegDutyHours](../functions/fcnCalculateLegDutyHours.md)
- [fcnCalculateLegInitalOperatingExperienceBonusPay](../functions/fcnCalculateLegInitalOperatingExperienceBonusPay.md)
- [fcnCalculateThrAndAdgAndDhr](../functions/fcnCalculateThrAndAdgAndDhr.md)
- [fcnCalculateTripCpCodePay](../functions/fcnCalculateTripCpCodePay.md)
- [fcnCalculateTripDutyHours](../functions/fcnCalculateTripDutyHours.md)
- [fcnConvertLegToTripDomicileTimeZone](../functions/fcnConvertLegToTripDomicileTimeZone.md)
- [fcnCreateTripPayInflightAnalytics](../functions/fcnCreateTripPayInflightAnalytics.md)
- [fcnDetermineCarryOverTripCredits](../functions/fcnDetermineCarryOverTripCredits.md)
- [fcnGetDutyPeriodPayByIndex](../functions/fcnGetDutyPeriodPayByIndex.md)
- [fcnGetLegPayByIndex](../functions/fcnGetLegPayByIndex.md)
- [fcnGetNextSchedulePeriodPay](../functions/fcnGetNextSchedulePeriodPay.md)
- [fcnGetPayDutyPeriodByIndex](../functions/fcnGetPayDutyPeriodByIndex.md)
- [fcnGetPayLegByIndex](../functions/fcnGetPayLegByIndex.md)
- [fcnGetPayTripList](../functions/fcnGetPayTripList.md)
- [fcnGetPreviousSchedulePeriodPay](../functions/fcnGetPreviousSchedulePeriodPay.md)
- [fcnGetTripPayList](../functions/fcnGetTripPayList.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](../functions/fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnPopulateSchedulePeriodPayList](../functions/fcnPopulateSchedulePeriodPayList.md)
- [fcnRemoveInflightFilteredDataAnalytics](../functions/fcnRemoveInflightFilteredDataAnalytics.md)
- [fcnSetHighestRigAmounts](../functions/fcnSetHighestRigAmounts.md)
- [fcnSetLegPositionA](../functions/fcnSetLegPositionA.md)
- [fcnSetLegPremiumThisMonth](../functions/fcnSetLegPremiumThisMonth.md)
- [fcnSetPayDutyPeriodTransientTerms](../functions/fcnSetPayDutyPeriodTransientTerms.md)
- [fcnSetRigsGreaterThanPremiumForTrip](../functions/fcnSetRigsGreaterThanPremiumForTrip.md)
- [fcnSetTripPositionA](../functions/fcnSetTripPositionA.md)
- [fcnShowTripPaySummary](../functions/fcnShowTripPaySummary.md)
- [fcnXrefPayDutyPeriodToDutyPeriodPay](../functions/fcnXrefPayDutyPeriodToDutyPeriodPay.md)
- [fcnXrefPayDutyPeriodToPayTrip](../functions/fcnXrefPayDutyPeriodToPayTrip.md)
- [fcnXrefPayLegToLegPay](../functions/fcnXrefPayLegToLegPay.md)
- [fcnXrefPayLegToPayDutyPeriod](../functions/fcnXrefPayLegToPayDutyPeriod.md)
- [fcnXrefPayTripToTripPay](../functions/fcnXrefPayTripToTripPay.md)

### Rulesets (13)

- [rsAssignReserveBlockTFP](../functions/rsAssignReserveBlockTFP.md)
- [rsCalculateDutyPeriodCredits](../functions/rsCalculateDutyPeriodCredits.md)
- [rsCalculateDutyPeriodDurationAndRest](../functions/rsCalculateDutyPeriodDurationAndRest.md)
- [rsCalculateDutyPeriodRIGS](../functions/rsCalculateDutyPeriodRIGS.md)
- [rsCalculateHolidayPayBucket](../functions/rsCalculateHolidayPayBucket.md)
- [rsCalculateLegBaseCredits](../functions/rsCalculateLegBaseCredits.md)
- [rsCalculateRONDutyPeriodCredits](../functions/rsCalculateRONDutyPeriodCredits.md)
- [rsDetermineCarryOverDutyPeriodCredits](../functions/rsDetermineCarryOverDutyPeriodCredits.md)
- [rsDetermineNonflyAssignmentCredits](../functions/rsDetermineNonflyAssignmentCredits.md)
- [rsInflightDutyPeriodDataAnalytics](../functions/rsInflightDutyPeriodDataAnalytics.md)
- [rsInflightLegDataAnalytics](../functions/rsInflightLegDataAnalytics.md)
- [rsInflightTripDataAnalytics](../functions/rsInflightTripDataAnalytics.md)
- [rsLegPremiumsGreaterThanRIGS](../functions/rsLegPremiumsGreaterThanRIGS.md)

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
