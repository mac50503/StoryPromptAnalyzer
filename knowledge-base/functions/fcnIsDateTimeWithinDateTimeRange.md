# fcnIsDateTimeWithinDateTimeRange

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnIsDateTimeWithinDateTimeRange`

## Propósito
21 Jan 2015 Tim A. - utility fucntion to test if a date lies within a specified date range.  Default is true.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| dateToTest | DateTime | |
| dateRangeBegin | DateTime | |
| dateRangeEnd | DateTime | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.if (dateToTest <> null and dateRangeBegin <> null and dateRangeEnd <> null) then{//fcnShow("===>>> ENTERING fcnIsDateTimeWithinDateTimeRange with date to test =  " dateToTest ", start = " dateRangeBegin ", end = " dateRangeEnd).priorToStart is a boolean initially dateToTest.isBefore(dateRangeBegin).afterEnd is a boolean initially dateToTest.isAfter(dateRangeEnd).if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(dateToTest, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {priorToStart = dateToTest.toLocalDateTime().isBefore(dateRangeBegin.toLocalDateTime()).afterEnd = dateToTest.toLocalDateTime().isAfter(dateRangeEnd.toLocalDateTime()).}if (priorToStart or afterEnd) thenretVal = false.}//if (retVal is equal to false) then//fcnShow("===>>> EVENT NOT WITHIN DATE RANGE FILTER ... event date = " dateToTest " ...date range start = " dateRangeBegin " ...date range end = " dateRangeEnd).//fcnShow("===>>> EXITING fcnIsDateTimeWithinDateTimeRange with retVal =  " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnDoAllDutyPeriodsInSpHaveRapAssociations](fcnDoAllDutyPeriodsInSpHaveRapAssociations.md)
- [fcnFindSchedulePeriodName](fcnFindSchedulePeriodName.md)
- [fcnGetCpCodePayRateForLeg](fcnGetCpCodePayRateForLeg.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnSetPreviousDayReserve](fcnSetPreviousDayReserve.md)

## Historial de cambios

```
21 Jan 2015 Tim A. - utility fucntion to test if a date lies within a specified date range.  Default is true.
```

