# fcnRoundUpAt2DecimalPlaces

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnRoundUpAt2DecimalPlaces`

## Propósito
Ben Lang - DE6259 - This function rounds 2 decimal places. Up at .005 and down at .004.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| numberToRound | real | |

## Lógica de negocio

```blaze
decimalMoved2Places is a real initially math().floor(numberToRound * 100).remainder is a real initially (numberToRound * 100) - decimalMoved2Places;remainder += 0.0000000001.if (remainder >= 0.5) thenreturn math().ceil(numberToRound * 100) / 100.elsereturn math().floor(numberToRound * 100) / 100.
```

## Dependencias

Esta function llama a:

- [main](main.md)

## Llamado por

- [fcnAddToBaseOfPayBucket](fcnAddToBaseOfPayBucket.md)
- [fcnAddToDutyPeriodSumOfLegPremimum](fcnAddToDutyPeriodSumOfLegPremimum.md)
- [fcnAddToPayValueOfPayBucket](fcnAddToPayValueOfPayBucket.md)
- [fcnAddTripPayBuckets](fcnAddTripPayBuckets.md)
- [fcnAdjustPremiumTripAndDutyPeriodPay](fcnAdjustPremiumTripAndDutyPeriodPay.md)
- [fcnApplyStaffBankAdjustments](fcnApplyStaffBankAdjustments.md)
- [fcnBuildUnutilizedReserveList](fcnBuildUnutilizedReserveList.md)
- [fcnCalculateDHR](fcnCalculateDHR.md)
- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnCalculateDutyPeriodRig](fcnCalculateDutyPeriodRig.md)
- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCalculateForcedPremiumTripsPayValue](fcnCalculateForcedPremiumTripsPayValue.md)
- [fcnCalculateReserveBlockCredit](fcnCalculateReserveBlockCredit.md)
- [fcnCalculateReserveSingleAndMultiDayGuarantee](fcnCalculateReserveSingleAndMultiDayGuarantee.md)
- [fcnCalculateThrAndAdgAndDhr](fcnCalculateThrAndAdgAndDhr.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)
- [fcnCalculateTripHourlyRatio](fcnCalculateTripHourlyRatio.md)
- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)
- [fcnDetermineMileage](fcnDetermineMileage.md)
- [fcnDetermineOverfly](fcnDetermineOverfly.md)
- [fcnDetermineOverschedule](fcnDetermineOverschedule.md)
- [fcnDistributeDutyHoursToPayBucket](fcnDistributeDutyHoursToPayBucket.md)
- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)
- [fcnDistributeRemainingReserveGuarantee](fcnDistributeRemainingReserveGuarantee.md)
- [fcnDistributeToFP5Bucket](fcnDistributeToFP5Bucket.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnGetHoursInDecimalFormatFromHoursAndMinutes](fcnGetHoursInDecimalFormatFromHoursAndMinutes.md)
- [fcnGetLegGroundTimePay](fcnGetLegGroundTimePay.md)
- [fcnGetNonRONpremium](fcnGetNonRONpremium.md)
- [fcnGetSumLegBasePayForTrip](fcnGetSumLegBasePayForTrip.md)
- [fcnGetSumOfCharterLegPay](fcnGetSumOfCharterLegPay.md)
- [fcnGetSumOfDutyBasePay](fcnGetSumOfDutyBasePay.md)
- [fcnGetSumOfDutyCreditValues](fcnGetSumOfDutyCreditValues.md)
- [fcnGetSumOfLegBaseCreditValues](fcnGetSumOfLegBaseCreditValues.md)
- [fcnGetSumOfLegBasePayForTrip](fcnGetSumOfLegBasePayForTrip.md)
- [fcnGetSumOfLegCreditValues](fcnGetSumOfLegCreditValues.md)
- [fcnGetSumOfLegPay](fcnGetSumOfLegPay.md)
- [fcnGetSumOfLegPayForTrip](fcnGetSumOfLegPayForTrip.md)
- [fcnGetSumOfLegPremiumAboveDT](fcnGetSumOfLegPremiumAboveDT.md)
- [fcnGetSumOfLegPremiumAboveOT](fcnGetSumOfLegPremiumAboveOT.md)
- [fcnGetThisMonthDutyPeriodPay](fcnGetThisMonthDutyPeriodPay.md)
- [fcnGetTripExcess](fcnGetTripExcess.md)
- [fcnInitializeNonflyPayDays](fcnInitializeNonflyPayDays.md)
- [fcnModifyDutyAndTripValuesForSplitGuaranty](fcnModifyDutyAndTripValuesForSplitGuaranty.md)
- [fcnRoundCrewPayValues](fcnRoundCrewPayValues.md)
- [fcnRoundTripPayValues](fcnRoundTripPayValues.md)
- [fcnSetHighestRigAmounts](fcnSetHighestRigAmounts.md)
- [fcnSetLegPremiumThisMonth](fcnSetLegPremiumThisMonth.md)
- [fcnSetNonRonLegPremium](fcnSetNonRonLegPremium.md)
- [fcnShowPlnLegPaySummary](fcnShowPlnLegPaySummary.md)
- [fcnShowPlnTripPaySummary](fcnShowPlnTripPaySummary.md)
- [fcnShowSchedulePeriodSummary](fcnShowSchedulePeriodSummary.md)
- [fcnShowTripPaySummary](fcnShowTripPaySummary.md)

## Historial de cambios

```
Ben Lang - DE6259 - This function rounds 2 decimal places. Up at .005 and down at .004.
```

