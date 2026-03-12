# fcnShowPlnTripPaySummary

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnShowPlnTripPaySummary`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnTripPay | PlnTripPay | |

## Lógica de negocio

```blaze
if (debugMode) then {aPlnPayTrip is some PlnPayTrip initially aPlnTripPay.plnPayTrip.fcnShow("==> entering fcnShowPlnTripPaySummary with aPlnTripPay =  " aPlnTripPay.tripNameAndDate " ...aPlnPayTrip = " aPlnTripPay.plnPayTrip).tripStr is a string initially "Planning Trip".fcnShow("==>" tripStr ": " aPlnTripPay.tripNameAndDate " start = " DateTimeUtilities.getShortDateTimeString(aPlnPayTrip.beginDateTime)  " end = " DateTimeUtilities.getShortDateTimeString(aPlnPayTrip.endDateTime)).fcnShow(".........TAFB = " aPlnTripPay.timeAwayFromBase " ...ADG RIG = " aPlnTripPay.adgRig " ...ADG = " aPlnTripPay.averageDailyGuarantee " ...THR RIG = " aPlnTripPay.thrRig " ...THR = " aPlnTripPay.tripHourRatio " ...trip pay = " fcnRoundUpAt2DecimalPlaces(aPlnTripPay.payValue) " ...credit type = " aPlnTripPay.creditType).if (aPlnTripPay.plnDutyPeriodPayList <> null and aPlnTripPay.plnDutyPeriodPayList.size() > 0) then{aPayDutyPeriod is some PayDutyPeriod initially null.for each PlnDutyPeriodPay in aPlnTripPay.plnDutyPeriodPayList as an array of PlnDutyPeriodPay do{aPayDutyPeriod = it.payDutyPeriod.fcnShow(".........Planning Duty Period: " it.sequenceNumber " " aPayDutyPeriod.beginLocation "-" aPayDutyPeriod.endLocation " ...skd report = " DateTimeUtilities.getShortDateTimeString(it.scheduledReportDateTime) " ...skd release = "  DateTimeUtilities.getShortDateTimeString(it.scheduledReleaseDateTime)).fcnShow("............duty period pay = " fcnRoundUpAt2DecimalPlaces(it.payValue) " ...credit type = " it.creditType).fcnShow("............dpm = " it.dutyPeriodMinimum " ...dhr = " it.dutyHourRatio " ...sumLegTotalCredits = " fcnRoundUpAt2DecimalPlaces(it.sumLegTotalCredits)).if (it.plnLegPayList <> null and it.plnLegPayList.size() > 0) then{for each PlnLegPay in it.plnLegPayList as an array of PlnLegPay do{fcnShowPlnLegPaySummary(it).}}}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [fcnShowPlnLegPaySummary](fcnShowPlnLegPaySummary.md)

