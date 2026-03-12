# fcnGetDHREndDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetDHREndDateTime`

## Propósito
10/6/2015 - DE7555 - Melissa S - Renamed function to match DHR start naming

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is some DateTime initially aPayDutyPeriod.releaseDateTime.aPayLeg is some PayLeg initially null.if (aPayDutyPeriod <> null) then{//// DEFAULT END DATE TIEM IS THE DUTY PERIOD RELEASE...retVal = aPayDutyPeriod.releaseDateTime.    //// HANDLE CONDITION OF LAST LEG IS A SAME STATION LIMO WITH ZERO DURATION...if (aPayDutyPeriod.lastLeg <> null and     aPayDutyPeriod.lastLeg.limoFlag = true and            aPayDutyPeriod.lastLeg.departureLocation = aPayDutyPeriod.lastLeg.arrivalLocation and     fcnGetTimeDiffInMinutes(aPayDutyPeriod.lastLeg.determineBestDepartureDateTimeNoEstimated(), aPayDutyPeriod.lastLeg.determineBestArrivalDateTimeNoEstimated()) = 0 andaPayDutyPeriod.legList.size() > 1) then{fcnShow("===>>> last leg is a same-station LIMO with zero duration for DP " aPayDutyPeriod.sequenceNumber).for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{legDuration is an integer initially fcnGetTimeDiffInMinutes(it.determineBestDepartureDateTimeNoEstimated(), it.determineBestArrivalDateTimeNoEstimated()).if (it.limoFlag = false or (it.limoFlag = true and legDuration > 0)) then{retVal = it.determineBestArrivalDateTimeNoEstimated().if (it.limoFlag = false) then{retVal = retVal.plusMinutes(aPayDutyPeriod.variableReleaseMinutes).fcnShow("===>>> setting DP " aPayDutyPeriod.sequenceNumber "'s DHR end date time to its best avail arr time of " it.determineBestArrivalDateTimeNoEstimated() " plus its variable release time of " aPayDutyPeriod.variableReleaseMinutes).}}}}else if (aPayDutyPeriod.lastLeg <> null and  aPayDutyPeriod.lastLeg.limoFlag = true and aPayDutyPeriod.lastLeg.departureLocation = aPayDutyPeriod.lastLeg.arrivalLocation and fcnGetTimeDiffInMinutes(aPayDutyPeriod.lastLeg.determineBestDepartureDateTimeNoEstimated(), aPayDutyPeriod.lastLeg.determineBestArrivalDateTimeNoEstimated()) = 0 and aPayDutyPeriod.legList.size() = 1) then{retVal = aPayDutyPeriod.reportDateTime.}else    //// LAST LEG OF DUTY IS NOT A SAME STATION LIMO OF ZERO DURATION...{// CREWT-905 - if DP's last leg is RS (waved) and there are non-RS legs in DP as well then calculate end time using its arrival time + 30 minuteslastNonRSLeg is some PayLeg initially fcnGetLastNonRSLegInDuty(aPayDutyPeriod).lastLeg is some PayLeg initially aPayDutyPeriod.lastLeg.if(lastLeg <> null and lastLeg.legWorkCodeList <> null and lastLeg.legWorkCodeList.contains("RS") = true and lastNonRSLeg <> null) then {legBestArr is some DateTime initially lastLeg.determineBestArrivalDateTimeNoEstimated().if(legBestArr <> null) then {retVal = legBestArr.plusMinutes(30).fcnShow("===>>> fcnGetDHREndDateTime adding 30 minutes to leg's arrival time " legBestArr " result " retVal).}}//// ADJUST FOR SCHEDULED RELEASE AFTER ACTAUL RELEASE...else if (aPayDutyPeriod.scheduledReleaseDateTime <> null and aPayDutyPeriod.releaseDateTime <> null and                        aPayDutyPeriod.scheduledReleaseDateTime > aPayDutyPeriod.releaseDateTime) then {retVal = aPayDutyPeriod.scheduledReleaseDateTime.}}}fcnShow("===>>> fcnGetDHREndDateTime returning " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetLastNonRSLegInDuty](fcnGetLastNonRSLegInDuty.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateDHR](fcnCalculateDHR.md)

## Historial de cambios

```
10/6/2015 - DE7555 - Melissa S - Renamed function to match DHR start naming
```

