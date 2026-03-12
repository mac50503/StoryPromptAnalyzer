# fcnDetermineDaysOffForSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineDaysOffForSchedulePeriod`

## Propósito
4/10/2015 - Melissa S - Fixed issue where this was failing when a schedule period didn't start on the 1st of the month

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriod | LegalitySchedulePeriod | |

## Lógica de negocio

```blaze
daysInSchedulePeriod is an integer initially 0.daysOff is an integer initially 0.dayCount is an integer initially 0.dayFound is a boolean.aDay is some DateTime.if (theSchedulePeriod <> null and theSchedulePeriod.schedulePeriodStart <> null and theSchedulePeriod.schedulePeriodEnd <> null and    theSchedulePeriod <> unknown and theSchedulePeriod.schedulePeriodStart <> unknown and theSchedulePeriod.schedulePeriodEnd <> unknown) then {daysInSchedulePeriod = Days.daysBetween(theSchedulePeriod.schedulePeriodStart, theSchedulePeriod.schedulePeriodEnd.plusDays(1)).days.}daysOff = daysInSchedulePeriod.while (dayCount < daysInSchedulePeriod) do {aDay = theSchedulePeriod.schedulePeriodStart.plusDays(dayCount).dayFound = false.for each WorkingDaysBlock in workingDaysBlockArray such that (dayFound = false) do {// Check for isBefore the end because we are using 0300 for the end instead of 0259 due to the DST gap in the spring where 0259 doesn't exist// APIC-1589 add to localDateTime to compare dates with diferent time zoneif2025NewDomicileDayLegalityEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(it.startDateTime, "IF_2025_NEW_DOMICILE_DAY_LEGALITY_BLAZE_EFFECTIVE_DATETIME").if (if2025NewDomicileDayLegalityEffectiveDateActiveFlag and aDay.toLocalDateTime().isBefore(it.startDateTime.toLocalDateTime()) = false and aDay.toLocalDateTime().isBefore(it.endDateTime.toLocalDateTime())) then {daysOff -= 1.dayFound = true.}else if (if2025NewDomicileDayLegalityEffectiveDateActiveFlag = false and aDay.isBefore(it.startDateTime) = false and aDay.isBefore(it.endDateTime)) then {daysOff -= 1.dayFound = true.}}dayCount += 1.}return daysOff.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Historial de cambios

```
4/10/2015 - Melissa S - Fixed issue where this was failing when a schedule period didn't start on the 1st of the month
```

