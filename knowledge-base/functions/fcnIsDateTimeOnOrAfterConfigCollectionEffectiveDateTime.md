# fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime`

## Propósito
03/31/2025 - APIC-1527 -Santosh K: new function to check if theCompareDateTime is on or after effectiveDateTimeKey's effective date time on config collection on the inFlightGlobalVar.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theCompareDateTime | DateTime | |
| theEffectiveDateTimeKey | string | |

## Lógica de negocio

```blaze
isDateTimeOnOrAfterEffectiveDateTime is a boolean initially false.effectiveDateTime is some DateTime.theConfigCollection is some ConfigCollection initially inFlightGlobalVar.configCollection.if(theConfigCollection <> null and theConfigCollection <> unknown and theConfigCollection.effectiveDateTimeMap <> null and theConfigCollection.effectiveDateTimeMap <> unknown and theConfigCollection.effectiveDateTimeMap.containsKey(theEffectiveDateTimeKey)) then {  effectiveDateTime  = theConfigCollection.effectiveDateTimeMap.get(theEffectiveDateTimeKey).dateTime;}if(effectiveDateTime <> null and effectiveDateTime <> unknown and theCompareDateTime <> null and theCompareDateTime <> unknown and effectiveDateTime.isAfter(theCompareDateTime) = false) then {  isDateTimeOnOrAfterEffectiveDateTime = true.}return isDateTimeOnOrAfterEffectiveDateTime.
```

## Llamado por

- [fcnAdjustPremiumTripAndDutyPeriodPay](fcnAdjustPremiumTripAndDutyPeriodPay.md)
- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)
- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)
- [fcnCalculateReserveSingleAndMultiDayGuarantee](fcnCalculateReserveSingleAndMultiDayGuarantee.md)
- [fcnCalculateThrAndAdgAndDhr](fcnCalculateThrAndAdgAndDhr.md)
- [fcnCreateTripPayResponse](fcnCreateTripPayResponse.md)
- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)
- [fcnDetermineConusPerDiemPayRate](fcnDetermineConusPerDiemPayRate.md)
- [fcnDetermineDaysOffForSchedulePeriod](fcnDetermineDaysOffForSchedulePeriod.md)
- [fcnDetermineDutyPeriodTransientTerms](fcnDetermineDutyPeriodTransientTerms.md)
- [fcnDetermineDutyTripExcess](fcnDetermineDutyTripExcess.md)
- [fcnDetermineOconusPerDiemPayRate](fcnDetermineOconusPerDiemPayRate.md)
- [fcnDistributeToLateReturnBuckets](fcnDistributeToLateReturnBuckets.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay](fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay.md)
- [fcnDoesLegPayBeginInSchedulePeriodPay](fcnDoesLegPayBeginInSchedulePeriodPay.md)
- [fcnDoesPayAdjustmentBeginInSchedulePeriod](fcnDoesPayAdjustmentBeginInSchedulePeriod.md)
- [fcnDoesPayLegBeginInSchedulePeriodPay](fcnDoesPayLegBeginInSchedulePeriodPay.md)
- [fcnDoesPayTripBeginInSchedulePeriod](fcnDoesPayTripBeginInSchedulePeriod.md)
- [fcnDoesPayTripEndInSchedulePeriod](fcnDoesPayTripEndInSchedulePeriod.md)
- [fcnGetFirstFlyingLegOfDutyPeriod](fcnGetFirstFlyingLegOfDutyPeriod.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)
- [fcnGetLegGroundTimePay](fcnGetLegGroundTimePay.md)
- [fcnGetSchedulePeriodNameForDateTime](fcnGetSchedulePeriodNameForDateTime.md)
- [fcnGetSchedulePeriodPayForDutyPeriodPay](fcnGetSchedulePeriodPayForDutyPeriodPay.md)
- [fcnInitializePayTripSchedulePeriods](fcnInitializePayTripSchedulePeriods.md)
- [fcnIsDPPayEndsInNextSPPay](fcnIsDPPayEndsInNextSPPay.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnIsDutyPeriodPayWithinSchedulePeriodPay](fcnIsDutyPeriodPayWithinSchedulePeriodPay.md)
- [fcnIsLegEligibleForEDDPay](fcnIsLegEligibleForEDDPay.md)
- [fcnIsLegEligibleForLDPay](fcnIsLegEligibleForLDPay.md)
- [fcnReportsOnHoliday](fcnReportsOnHoliday.md)
- [fcnSetHighestRigAmounts](fcnSetHighestRigAmounts.md)
- [fcnSetTripNonDeadheadBeginEndTime](fcnSetTripNonDeadheadBeginEndTime.md)

## Historial de cambios

```
03/31/2025 - APIC-1527 -Santosh K: new function to check if theCompareDateTime is on or after effectiveDateTimeKey's effective date time on config collection on the inFlightGlobalVar.
```

