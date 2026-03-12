# fcnDoesPayTripEndInSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDoesPayTripEndInSchedulePeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if(aPayTrip <> null and aSchedulePeriodPay <> null) then {if2025NewDomicileDayPayEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayTrip.beginDateTime, "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME").if(if2025NewDomicileDayPayEffectiveDateActiveFlag) then {if (aPayTrip.endDateTime.toLocalDateTime().isBefore(aSchedulePeriodPay.schedulePeriodStart.toLocalDateTime()) is equal to false and aPayTrip.endDateTime.toLocalDateTime().isAfter(aSchedulePeriodPay.schedulePeriodEnd.toLocalDateTime()) is equal to false) thenreturn true.elsereturn false.}else  {if (aPayTrip.endDateTime.isBefore(aSchedulePeriodPay.schedulePeriodStart) is equal to false and aPayTrip.endDateTime.isAfter(aSchedulePeriodPay.schedulePeriodEnd) is equal to false) thenreturn true.elsereturn false.}}else{return false.}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)

## Llamado por

- [fcnDetermineCarryOverTripCredits](fcnDetermineCarryOverTripCredits.md)

