# fcnReportsOnHoliday

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnReportsOnHoliday`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| reportDateTime | DateTime | |
| aSwaHolidayList | List<SwaHoliday> | |

## Lógica de negocio

```blaze
if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(reportDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if (reportDateTime <> null and     aSwaHolidayList <> null and     aSwaHolidayList.size() > 0) then{for each SwaHoliday in aSwaHolidayList as an array of SwaHoliday do {if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if (reportDateTime.toLocalDateTime().isBefore(it.startDateTime.toLocalDateTime()) = false and        reportDateTime.toLocalDateTime().isAfter(it.endDateTime.toLocalDateTime()) = false) thenreturn true.}else {if (reportDateTime.isBefore(it.startDateTime) = false and       reportDateTime.isAfter(it.endDateTime) = false) thenreturn true.}}}return false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)
- [fcnCalculateHolidayPayBucketFromReserve](fcnCalculateHolidayPayBucketFromReserve.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

