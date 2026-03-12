# fcnSetPayDutyPeriodTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetPayDutyPeriodTransientTerms`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |
| theGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
thePayDutyPeriod.startOfRest = fcnCalculateStartOfRestForPay(thePayDutyPeriod.payTrip, thePayDutyPeriod).thePayDutyPeriod.amountOfRest = fcnGetTimeDiffInMinutes(thePayDutyPeriod.startOfRest, thePayDutyPeriod.reportDateTime).if  theGlobalDataCache is not null then {releaseStation is some Station initially  theGlobalDataCache.stationMap.get(thePayDutyPeriod.endLocation).if releaseStation is not null then {thePayDutyPeriod.releaseDateTimeInLocalTimezone = DateTimeUtilities.convertDateTimeToTimezone(thePayDutyPeriod.releaseDateTime, releaseStation.timezone).}}fcnShow("===>>> Exiting fcnSetPayDutyPeriodTransientTerms  ...trip = " thePayDutyPeriod.payTrip.tripName  " ...DP = " thePayDutyPeriod.sequenceNumber    " ...startOfRest = " thePayDutyPeriod.startOfRest  " ...amountOfRest = " thePayDutyPeriod.amountOfRest).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateStartOfRestForPay](fcnCalculateStartOfRestForPay.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

