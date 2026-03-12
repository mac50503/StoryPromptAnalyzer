# CssIfCrewPayRuleFlow

## Metadata
- **Categoría**: Pay
- **Ubicación**: `CrewRulesRepository\DecisionServices\CSS\Inflight\PayRuleFlows\CssCrewPayRuleFlow`
- **Funciones orquestadas**: 106

## ¿Qué hace este RuleFlow?

Este RuleFlow orquesta el cálculo completo de pago para tripulación (crew). Procesa múltiples períodos de programación, viajes, períodos de servicio y tramos.

## Funciones y Rulesets Orquestados

Este RuleFlow llama a las siguientes 106 funciones/rulesets:

### Funciones (67)

- [fcnAddToDutyPeriodSumOfLegPremimum](../functions/fcnAddToDutyPeriodSumOfLegPremimum.md)
- [fcnApplyStaffBankAdjustments](../functions/fcnApplyStaffBankAdjustments.md)
- [fcnAssociateAirportStandbyWithOverlappingTrip](../functions/fcnAssociateAirportStandbyWithOverlappingTrip.md)
- [fcnAssociateAirportStandbyWithReserve](../functions/fcnAssociateAirportStandbyWithReserve.md)
- [fcnBuildUnutilizedReserveList](../functions/fcnBuildUnutilizedReserveList.md)
- [fcnCalculateActualDutyDuration](../functions/fcnCalculateActualDutyDuration.md)
- [fcnCalculateConusAndOconusLimitsForInflightTripset](../functions/fcnCalculateConusAndOconusLimitsForInflightTripset.md)
- [fcnCalculateConusAndOconusPay](../functions/fcnCalculateConusAndOconusPay.md)
- [fcnCalculateCrewMealPerdiem](../functions/fcnCalculateCrewMealPerdiem.md)
- [fcnCalculateDutyPeriodRig](../functions/fcnCalculateDutyPeriodRig.md)
- [fcnCalculateExperiencePayBucket](../functions/fcnCalculateExperiencePayBucket.md)
- [fcnCalculateHolidayPayBucketFromReserve](../functions/fcnCalculateHolidayPayBucketFromReserve.md)
- [fcnCalculateILabelTrip](../functions/fcnCalculateILabelTrip.md)
- [fcnCalculateLegDutyHours](../functions/fcnCalculateLegDutyHours.md)
- [fcnCalculateLongevityBucket](../functions/fcnCalculateLongevityBucket.md)
- [fcnCalculateReserveSingleAndMultiDayGuarantee](../functions/fcnCalculateReserveSingleAndMultiDayGuarantee.md)
- [fcnCalculateThrAndAdgAndDhr](../functions/fcnCalculateThrAndAdgAndDhr.md)
- [fcnCalculateTotalPayBucket](../functions/fcnCalculateTotalPayBucket.md)
- [fcnCalculateTripCpCodePay](../functions/fcnCalculateTripCpCodePay.md)
- [fcnCalculateTripDutyHours](../functions/fcnCalculateTripDutyHours.md)
- [fcnConvertLegToTripDomicileTimeZone](../functions/fcnConvertLegToTripDomicileTimeZone.md)
- [fcnCreateSchedulePeriodPayInflightAnalytics](../functions/fcnCreateSchedulePeriodPayInflightAnalytics.md)
- [fcnDetermineCarryOverTripCredits](../functions/fcnDetermineCarryOverTripCredits.md)
- [fcnDetermineDutyTripExcess](../functions/fcnDetermineDutyTripExcess.md)
- [fcnDetermineTripTransientTerms](../functions/fcnDetermineTripTransientTerms.md)
- [fcnDistributeDutyHoursToPayBucket](../functions/fcnDistributeDutyHoursToPayBucket.md)
- [fcnDistributeRemainingReserveGuarantee](../functions/fcnDistributeRemainingReserveGuarantee.md)
- [fcnDistributeToLateReturnBuckets](../functions/fcnDistributeToLateReturnBuckets.md)
- [fcnDistributeToPerDiemBuckets](../functions/fcnDistributeToPerDiemBuckets.md)
- [fcnDutyContainsAllLimosOfZeroDuration](../functions/fcnDutyContainsAllLimosOfZeroDuration.md)
- [fcnGetDutyPeriodPayByIndex](../functions/fcnGetDutyPeriodPayByIndex.md)
- [fcnGetFlightLegDisplayString](../functions/fcnGetFlightLegDisplayString.md)
- [fcnGetLegPayByIndex](../functions/fcnGetLegPayByIndex.md)
- [fcnGetNextSchedulePeriodPay](../functions/fcnGetNextSchedulePeriodPay.md)
- [fcnGetPayCrewMember](../functions/fcnGetPayCrewMember.md)
- [fcnGetPayDutyPeriodByIndex](../functions/fcnGetPayDutyPeriodByIndex.md)
- [fcnGetPayLegByIndex](../functions/fcnGetPayLegByIndex.md)
- [fcnGetPayTripByIndex](../functions/fcnGetPayTripByIndex.md)
- [fcnGetPayTripListForSchedulePeriod](../functions/fcnGetPayTripListForSchedulePeriod.md)
- [fcnGetPreviousSchedulePeriodPay](../functions/fcnGetPreviousSchedulePeriodPay.md)
- [fcnGetSchedulePeriodByIndex](../functions/fcnGetSchedulePeriodByIndex.md)
- [fcnGetSchedulePeriodPayByIndex](../functions/fcnGetSchedulePeriodPayByIndex.md)
- [fcnGetTripPayByIndex](../functions/fcnGetTripPayByIndex.md)
- [fcnGetTripPayList](../functions/fcnGetTripPayList.md)
- [fcnGetTripPayListForSchedulePeriodPay](../functions/fcnGetTripPayListForSchedulePeriodPay.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](../functions/fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnResetSharedTripSetsConusOconusLimits](../functions/fcnResetSharedTripSetsConusOconusLimits.md)
- [fcnRoundCrewPayValues](../functions/fcnRoundCrewPayValues.md)
- [fcnSetHighestRigAmounts](../functions/fcnSetHighestRigAmounts.md)
- [fcnSetLegPositionA](../functions/fcnSetLegPositionA.md)
- [fcnSetLegPremiumThisMonth](../functions/fcnSetLegPremiumThisMonth.md)
- [fcnSetLodoQualification](../functions/fcnSetLodoQualification.md)
- [fcnSetPayBucketRate](../functions/fcnSetPayBucketRate.md)
- [fcnSetPayDutyPeriodTransientTerms](../functions/fcnSetPayDutyPeriodTransientTerms.md)
- [fcnSetReserveBlockDutyPeriodDutyAmount](../functions/fcnSetReserveBlockDutyPeriodDutyAmount.md)
- [fcnSetRigsGreaterThanPremiumForTrip](../functions/fcnSetRigsGreaterThanPremiumForTrip.md)
- [fcnSetTripPositionA](../functions/fcnSetTripPositionA.md)
- [fcnSetTripSetConusAndOconusDays](../functions/fcnSetTripSetConusAndOconusDays.md)
- [fcnSetYearsOfExperience](../functions/fcnSetYearsOfExperience.md)
- [fcnShow](../functions/fcnShow.md)
- [fcnShowSchedulePeriodSummary](../functions/fcnShowSchedulePeriodSummary.md)
- [fcnSortReserveBlockDayList](../functions/fcnSortReserveBlockDayList.md)
- [fcnXrefPayDutyPeriodToDutyPeriodPay](../functions/fcnXrefPayDutyPeriodToDutyPeriodPay.md)
- [fcnXrefPayDutyPeriodToPayTrip](../functions/fcnXrefPayDutyPeriodToPayTrip.md)
- [fcnXrefPayLegToLegPay](../functions/fcnXrefPayLegToLegPay.md)
- [fcnXrefPayLegToPayDutyPeriod](../functions/fcnXrefPayLegToPayDutyPeriod.md)
- [fcnXrefPayTripToTripPay](../functions/fcnXrefPayTripToTripPay.md)

### Rulesets (37)

- [rsApplyLastRRRLegPremiumCode](../functions/rsApplyLastRRRLegPremiumCode.md)
- [rsAssignReserveBlockTFP](../functions/rsAssignReserveBlockTFP.md)
- [rsBuildReserveBlockDayList](../functions/rsBuildReserveBlockDayList.md)
- [rsCalculateDutyPeriodCredits](../functions/rsCalculateDutyPeriodCredits.md)
- [rsCalculateDutyPeriodDurationAndRest](../functions/rsCalculateDutyPeriodDurationAndRest.md)
- [rsCalculateDutyPeriodRIGS](../functions/rsCalculateDutyPeriodRIGS.md)
- [rsCalculateHolidayPayBucket](../functions/rsCalculateHolidayPayBucket.md)
- [rsCalculateLegBaseCredits](../functions/rsCalculateLegBaseCredits.md)
- [rsCalculateLegTotalCredits](../functions/rsCalculateLegTotalCredits.md)
- [rsCalculateNonFlyPayBuckets](../functions/rsCalculateNonFlyPayBuckets.md)
- [rsCalculatePayBucketsRigs](../functions/rsCalculatePayBucketsRigs.md)
- [rsCalculateRONDutyPeriodCredits](../functions/rsCalculateRONDutyPeriodCredits.md)
- [rsCalculateRegularPayBucket](../functions/rsCalculateRegularPayBucket.md)
- [rsCalculateTotalMinimumGuarantee](../functions/rsCalculateTotalMinimumGuarantee.md)
- [rsDeriveCharterTripPremiumPayCode](../functions/rsDeriveCharterTripPremiumPayCode.md)
- [rsDeriveRONPremiumPayCode](../functions/rsDeriveRONPremiumPayCode.md)
- [rsDeriveRRRPremiumPayCode](../functions/rsDeriveRRRPremiumPayCode.md)
- [rsDeriveRegularPremiumPayCode](../functions/rsDeriveRegularPremiumPayCode.md)
- [rsDetermineCarryOverDutyPeriodCredits](../functions/rsDetermineCarryOverDutyPeriodCredits.md)
- [rsDetermineNonflyAssignmentCredits](../functions/rsDetermineNonflyAssignmentCredits.md)
- [rsDetermineRemainingSplitGuaranty](../functions/rsDetermineRemainingSplitGuaranty.md)
- [rsDetermineSLabelPremiumPayCode](../functions/rsDetermineSLabelPremiumPayCode.md)
- [rsDistributeToGenericPayBucketsLeg](../functions/rsDistributeToGenericPayBucketsLeg.md)
- [rsDistributeToPremiumPayBuckets](../functions/rsDistributeToPremiumPayBuckets.md)
- [rsDistributeTripPayToBuckets](../functions/rsDistributeTripPayToBuckets.md)
- [rsDistributeZeroCreditDutyHoursToPayBuckets](../functions/rsDistributeZeroCreditDutyHoursToPayBuckets.md)
- [rsInflightDataAnalyticsFiltering](../functions/rsInflightDataAnalyticsFiltering.md)
- [rsInflightDutyPeriodDataAnalytics](../functions/rsInflightDutyPeriodDataAnalytics.md)
- [rsInflightLegDataAnalytics](../functions/rsInflightLegDataAnalytics.md)
- [rsInflightTripDataAnalytics](../functions/rsInflightTripDataAnalytics.md)
- [rsInitializeReseveBlocks](../functions/rsInitializeReseveBlocks.md)
- [rsLegPremiumsGreaterThanRIGS](../functions/rsLegPremiumsGreaterThanRIGS.md)
- [rsLodoQualified](../functions/rsLodoQualified.md)
- [rsPopulateSchedulePeriodWithReservePayrollReport](../functions/rsPopulateSchedulePeriodWithReservePayrollReport.md)
- [rsProductivityPay](../functions/rsProductivityPay.md)
- [rsRONAfterRRR](../functions/rsRONAfterRRR.md)
- [rsReservesProductivityPay](../functions/rsReservesProductivityPay.md)

### Decision Tables (1)

- `dtInflightSetPerDiemBucketForBucketNonFlyCodes_Instance` *(documentación no disponible)*

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
