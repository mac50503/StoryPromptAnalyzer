# fcnDoesPayTripBeginInSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesPayTripBeginInSchedulePeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
//fcnShow("===>>> testing trip " aPayTrip.tripName " for membership in SP " aSchedulePeriodPay.schedulePeriodName).if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially false.if(aPayTrip <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag = fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").}if (aPayTrip <> null and aSchedulePeriodPay <> null and     if2025NewDomicileDayPayEffectiveDateActiveFlag and aSchedulePeriodPay.schedulePeriodStart <> null and aSchedulePeriodPay.schedulePeriodEnd <> null and     aPayTrip.beginDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and     aPayTrip.beginDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.if (aPayTrip <> null and aSchedulePeriodPay <> null and    if2025NewDomicileDayPayEffectiveDateActiveFlag = false and     aPayTrip.beginDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and     aPayTrip.beginDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- `fcnShow()`

## Llamado por

- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

