# fcnIsDateTimeWithinReportFilterRange

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnIsDateTimeWithinReportFilterRange`

## Propósito
22 Jul 2015 Ben Lang DE7067 - Utility fucntion to test if a date lies within a specified date range excluding the dateRangeEnd.  Default is true.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateToTest | DateTime | |
| dateRangeBegin | DateTime | |
| dateRangeEnd | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.priorToStart is a boolean initially true.afterEnd is a boolean initially true.if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(dateToTest, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if (dateToTest <> null and dateRangeBegin <> null and dateRangeEnd <> null) then{//fcnShow("===>>> ENTERING fcnIsDateTimeWithinReportFilterRange with date to test =  " dateToTest ", start = " dateRangeBegin ", end = " dateRangeEnd).if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {priorToStart = dateToTest.toLocalDateTime().isBefore(dateRangeBegin.toLocalDateTime()).afterEnd = (dateToTest.toLocalDateTime().isEqual(dateRangeEnd.toLocalDateTime()) or dateToTest.toLocalDateTime().isAfter(dateRangeEnd.toLocalDateTime())).}else {priorToStart = dateToTest.isBefore(dateRangeBegin).afterEnd = (dateToTest.isEqual(dateRangeEnd) or dateToTest.isAfter(dateRangeEnd)).}if (priorToStart or afterEnd)  thenretVal = false.}//if (retVal is equal to false) then//fcnShow("===>>> EVENT NOT WITHIN DATE RANGE FILTER ... event date = " dateToTest " ...date range start = " dateRangeBegin " ...date range end = " dateRangeEnd).//fcnShow("===>>> EXITING fcnIsDateTimeWithinDateTimeRange with retVal =  " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)
- `fcnShow()`

## Llamado por

- [fcnAddToBaseOfPayBucket](fcnAddToBaseOfPayBucket.md)
- [fcnAddToPayValueOfPayBucket](fcnAddToPayValueOfPayBucket.md)
- [fcnApplyStaffBankAdjustments](fcnApplyStaffBankAdjustments.md)
- [fcnAreAllDutyPeriodsWithinReportDateRange](fcnAreAllDutyPeriodsWithinReportDateRange.md)
- [fcnCalculateCrewMealPerdiumDomesticLegs](fcnCalculateCrewMealPerdiumDomesticLegs.md)
- [fcnCalculateCrewMealPerdiumInternationalLegs](fcnCalculateCrewMealPerdiumInternationalLegs.md)
- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnCalculateExperiencePayBucket](fcnCalculateExperiencePayBucket.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnDistributeDutyHoursToPayBucket](fcnDistributeDutyHoursToPayBucket.md)
- [fcnDistributeToFP5Bucket](fcnDistributeToFP5Bucket.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)
- [fcnGetEventDateForExperiencePay](fcnGetEventDateForExperiencePay.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)

## Historial de cambios

```
22 Jul 2015 Ben Lang DE7067 - Utility fucntion to test if a date lies within a specified date range excluding the dateRangeEnd.  Default is true.
```

