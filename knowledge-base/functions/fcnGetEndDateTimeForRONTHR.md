# fcnGetEndDateTimeForRONTHR

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetEndDateTimeForRONTHR`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
////    LOOKING BACKWARDS FROM THE START OF THE RON DUTY PERIOD FIND THE THE MOST RECNT FLYING LEG //    OR LIMO LEG THAT SATISFY THE FOLLOWING CONDITIONS://        LEG IS NOT IN A RON DUTY PERIOD//        IF LEG IS A SAME STATION LIMO IT IS IN A DUTY PERIOD CONTAINING ONLY LIMO LEGS//retVal is some DateTime initially null.lastLegSeqNum is an integer initially 0.dutyContainsAllLimos is a boolean initially false.sameStations is a boolean initially false.if (aPayDutyPeriod <> null and aPayDutyPeriod.payTrip <> null and aPayDutyPeriod.payTrip.dutyPeriodList.size() > 1) then{aPayLeg is some PayLeg initially null.dutyLastLegArrival is some DateTime initially aPayDutyPeriod.lastLeg.determineBestArrivalDateTimeNoEstimated().//fcnShow("===>>> dutyLastLegArrival = " dutyLastLegArrival).legBestArrival is some DateTime initially null.legList is some List<PayLeg> initially fcnGetTripLegList(aPayDutyPeriod.payTrip).if (legList <> null and legList.size() > 0) then{for each PayLeg in legList as an array of PayLeg do{aPayLeg  = it.if (aPayLeg.limoFlag = true and aPayLeg.departureLocation = aPayLeg.arrivalLocation) thensameStations = trueelsesameStations = false.//fcnShow("===>>> leg " aPayLeg.sequenceNumber " ...limoFlag = " aPayLeg.limoFlag " ...same stations = " sameStations).if (aPayLeg.payDutyPeriod.dutyType <> "RON" and aPayLeg.payDutyPeriod.sequenceNumber <> aPayDutyPeriod.sequenceNumber) then{legBestArrival = aPayLeg.determineBestArrivalDateTimeNoEstimated().if (dutyLastLegArrival <> null and dutyLastLegArrival.isAfter(legBestArrival)) then{lastLegSeqNum = aPayLeg.sequenceNumber.retVal = legBestArrival.}}}}}fcnShow("===>>> returning from fcnGetPreviousLegBestArrivalForRONTAFB with DP " aPayDutyPeriod.sequenceNumber " ... last leg for RONTAFB " lastLegSeqNum "'s best avail arrival = " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetPreviousLeg](fcnGetPreviousLeg.md)
- [fcnGetPreviousLegBestArrivalForRONTAFB](fcnGetPreviousLegBestArrivalForRONTAFB.md)
- [fcnGetTripLegList](fcnGetTripLegList.md)
- `fcnShow()`

