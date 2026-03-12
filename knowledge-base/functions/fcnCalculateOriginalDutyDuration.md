# fcnCalculateOriginalDutyDuration

## Metadata
- **Tipo**: SRL Function
- **Retorna**: duration
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateOriginalDutyDuration`

## Propósito
US18932 11/18/2014 Mitesh P: This function is used to determine a duty period’s duration based on the scheduled datetimes only

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |
| isCharter | boolean | |

## Lógica de negocio

```blaze
reportDateTime is some DateTime initially a DateTime.releaseDateTime is some DateTime initially a DateTime.if (isCharter and thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime <> null) then {reportDateTime = thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReportDateTime.} else reportDateTime = thePayDutyPeriod.scheduledReportDateTime.if (isCharter) then {if (thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReleaseDateTime <> null) thenreleaseDateTime = thePayDutyPeriod.payDutyPeriodInflight.originalScheduledReleaseDateTime.elsereleaseDateTime = thePayDutyPeriod.scheduledReleaseDateTime.} else {if (thePayDutyPeriod.payTrip.lastDutyPeriod = thePayDutyPeriod) thenreleaseDateTime = thePayDutyPeriod.scheduledReleaseDateTime.elsereleaseDateTime = thePayDutyPeriod.lastLeg.scheduledArrivalDateTime.}return (Duration.newInstance(reportDateTime, releaseDateTime).standardMinutes " minutes") as a duration.
```

## Historial de cambios

```
US18932 11/18/2014 Mitesh P: This function is used to determine a duty period’s duration based on the scheduled datetimes only
Ben Lang 07/30/2015 - Added code to use original schedule times for charters
8/19/2105 - Melissa S - DE7244 - Changed original duty for charters to always use original scheduled release, regardless of if it's the last duty period or not
```

