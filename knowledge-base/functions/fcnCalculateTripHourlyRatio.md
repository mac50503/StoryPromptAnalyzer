# fcnCalculateTripHourlyRatio

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateTripHourlyRatio`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| thrDivisor | real | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aPayTrip <> null and thrDivisor > 0.0) then{retVal = fcnRoundUpAt2DecimalPlaces(aPayTrip.timeAwayFromBase / (thrDivisor * 60)).dpCount is an integer initially aPayTrip.dutyPeriodList.size().lastDutyPeriod is some PayDutyPeriod initially aPayTrip.lastDutyPeriod.if (dpCount > 1) thenlastDutyPeriod = aPayTrip.dutyPeriodList.get(dpCount -1).lastLeg is some PayLeg initially null.if (lastDutyPeriod <> null) thenlastLeg = lastDutyPeriod.lastLeg. //fcnShow("===> entering function fcnCalculateTripHourlyRatio with trip " aPayTrip.tripName " .... time away from base = " aPayTrip.timeAwayFromBase " ... thrDivisor = " thrDivisor " ...DP count = " dpCount).//fcnShow("===> default THR = TAFB(" aPayTrip.timeAwayFromBase " / (thrDivisor(" thrDivisor ") * 60) = " retVal). lastLegIsNonfly is a boolean initially fcnIsNonFlyLeg(lastLeg).if (lastDutyPeriod <> null and     lastLeg <> null and                    (lastLegIsNonfly is equal to false or     (lastLegIsNonfly is equal to true and aPayTrip.lastDutyPeriod.lastLeg.nonFlyCode = (ignoring case) ("FDP" or "RFDP")))) then{minutes is a real initially 0.0.if (aPayTrip.firstDutyPeriod <> null and     aPayTrip.lastDutyPeriod <> null and    aPayTrip.lastDutyPeriod.lastLeg <> null and    (aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime = null or aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime is unknown)) then{//fcnShow("===>>> using last leg SCHEDULED arrival time to calculate THR").minutes = fcnGetTimeDiffInMinutes(aPayTrip.firstDutyPeriod.reportDateTime, lastLeg.scheduledArrivalDateTime).}else if (aPayTrip.firstDutyPeriod <> null and          aPayTrip.lastDutyPeriod <> null and         aPayTrip.lastDutyPeriod.lastLeg <> null and         aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime <> null) then{if (aPayTrip.lastDutyPeriod.lastLeg.actualInDateTime.isAfter(aPayTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime) = true) then{//fcnShow("===>>> using last leg ACTUAL arrival time to calculate THR").minutes = fcnGetTimeDiffInMinutes(aPayTrip.firstDutyPeriod.reportDateTime, lastLeg.actualInDateTime).}else{//fcnShow("===>>> using last leg SCHEDULED arrival time to calculate THR").minutes = fcnGetTimeDiffInMinutes(aPayTrip.firstDutyPeriod.reportDateTime, lastLeg.scheduledArrivalDateTime).}}retVal = ((minutes + 30) / (thrDivisor * 60)).retVal = fcnRoundUpAt2DecimalPlaces(retVal).//fcnShow("===> ADJUSTED THR = (minutes(" minutes ") + 30) / (thrDivisor(" thrDivisor ") * 60) = " retVal).//fcnShow("===> first duty(" aPayTrip.firstDutyPeriod.sequenceNumber ") report = " DateTimeUtilities.getShortDateTimeString(aPayTrip.firstDutyPeriod.reportDateTime) " ...last leg(" lastLeg.sequenceNumber ") skd arr time = " lastLeg.scheduledArrivalDateTime  " act arr time = " lastLeg.actualInDateTime).//fcnShow("===> thrDivisor = " thrDivisor " ...minutes between first duty report and last leg arrival = " minutes " ...in hours = " minutes / 60 " ...in days = " minutes / 60 / 24).}}//fcnShow("===> leaving function fcnCalculateTripHourlyRatio.... returning: " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnIsNonFlyLeg](fcnIsNonFlyLeg.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

