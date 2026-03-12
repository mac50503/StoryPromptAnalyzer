# fcnCalculateDHR

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateDHR`

## Propósito
10/6/2015 - DE7555 - Melissa S - Moved DHR calculation to a function to keep it logically separate from other calculations

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
dhrStartDateTime is some DateTime initially fcnGetDHRStartDateTime(aPayDutyPeriod).dhrEndDateTime is some DateTime initially fcnGetDHREndDateTime(aPayDutyPeriod).aPayDutyPeriod.dutyPeriodPay.dutyHourRatio = (fcnGetTimeDiffInMinutes(dhrStartDateTime, dhrEndDateTime) / 60) * 0.74.aPayDutyPeriod.dutyPeriodPay.dutyHourRatio = fcnRoundUpAt2DecimalPlaces(aPayDutyPeriod.dutyPeriodPay.dutyHourRatio).fcnShow("===>>>Calculating DHR for DP = " aPayDutyPeriod.sequenceNumber " from DHR start (" dhrStartDateTime ") to DHR end (" dhrEndDateTime ") * 0.74 = " aPayDutyPeriod.dutyPeriodPay.dutyHourRatio).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetDHREndDateTime](fcnGetDHREndDateTime.md)
- [fcnGetDHRStartDateTime](fcnGetDHRStartDateTime.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateThrAndAdgAndDhr](fcnCalculateThrAndAdgAndDhr.md)

## Historial de cambios

```
10/6/2015 - DE7555 - Melissa S - Moved DHR calculation to a function to keep it logically separate from other calculations
```

