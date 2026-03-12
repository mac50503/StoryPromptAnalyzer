# fcnAssociateInflightPayDutyPeriodsToRaps

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAssociateInflightPayDutyPeriodsToRaps`

## Propósito
Ben Lang - 8/4/14 - US18071 - This function determines the association between duty periods and RAPs. If the duty period's report dateTime is on or after

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTripList | List<PayTrip> | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnAssociateInflightPayDutyPeriodsToRaps...").aDutyPeriodList is some List<PayDutyPeriod> initially an ArrayList.aRAPList is some List<PayDutyPeriod> initially an ArrayList.aDutyPeriod is some PayDutyPeriod initially null.aDutyPeriodInflight is some PayDutyPeriodInflight initially null.aRAP is some PayDutyPeriod initially null.aRAPInflight is some PayDutyPeriodInflight initially null.aPayTrip is some PayTrip initially null.aPayDutyPeriod is some PayDutyPeriod initially null.tripIndex is an integer initially 0.dutyPeriodIndex is an integer initially 0.rapIndex is an integer initially 0.// Create duty period and RAP array and add PaydutyPeriodInflight objectswhile tripIndex < thePayTripList.size() do {dutyPeriodIndex = 0.while dutyPeriodIndex < thePayTripList.get(tripIndex).dutyPeriodList.size() do {if (thePayTripList.get(tripIndex).dutyPeriodList.get(dutyPeriodIndex).payDutyPeriodInflight = null) then thePayTripList.get(tripIndex).dutyPeriodList.get(dutyPeriodIndex).payDutyPeriodInflight = a PayDutyPeriodInflight.// if (thePayTripList.get(tripIndex).tripType = "R" or thePayTripList.get(tripIndex).assignmentLabel = ("K" or "T" or "B")) then //// US18772 - no londer use labels for deternining if a trip is a reserve blockif (thePayTripList.get(tripIndex).tripType = "R") thenaRAPList.add(thePayTripList.get(tripIndex).dutyPeriodList.get(dutyPeriodIndex)).// WE DON'T YET KNOW WHICH TRIPS ARE RESERVE TRIPS SO WE NEED TO ADD ALL THE NON-RESERVE BLOCK // DUTY PERIODS SO THEY CAN BE TESTED FOR INTERSECTION WITH A RAP...else aDutyPeriodList.add(thePayTripList.get(tripIndex).dutyPeriodList.get(dutyPeriodIndex)).dutyPeriodIndex += 1.}tripIndex += 1.}fcnShow("===>>. RAP count = " aRAPList.size() " ... Reserve trip DP count = " aDutyPeriodList.size()).dutyPeriodIndex = 0.// Create the duty periods' RAP associations...while dutyPeriodIndex < aDutyPeriodList.size() do {aDutyPeriod = aDutyPeriodList.get(dutyPeriodIndex).aDutyPeriodInflight = aDutyPeriod.payDutyPeriodInflight. rapIndex = 0.while rapIndex < aRAPList.size() do {aRAP = aRAPList.get(rapIndex).aRAPInflight = aRAP.payDutyPeriodInflight. if (fcnIsSameSwaDay(fcnGetFirstFlyingLegScheduledDepartureDateTime(aDutyPeriod), aRAP.reportDateTime) and    aDutyPeriodInflight is not null and    aRAPInflight is not null) then {aDutyPeriodInflight.rapAssociationList.add(aRAP).aRAPInflight.rapAssociationList.add(aDutyPeriod).fcnShow("===>>>DP " aDutyPeriod.sequenceNumber   " reporting at " aDutyPeriod.reportDateTime.toString()   " is associated with RAP " aRAP.sequenceNumber   " reporting at " aRAP.reportDateTime.toString()).fcnShow("===>>>RAP " aRAP.sequenceNumber   " reporting at " aRAP.reportDateTime.toString()   " is associated with DP " aDutyPeriod.sequenceNumber  " ... size of list = " aRAPInflight.rapAssociationList.size()).}rapIndex += 1.}dutyPeriodIndex += 1.}rapAssociationStr is a string initially "none".tripIndex = 0.while tripIndex < thePayTripList.size() do {aPayTrip = thePayTripList.get(tripIndex).if (aPayTrip.tripType <> "R" and aPayTrip.dutyPeriodList.size() > 0) then {dutyPeriodIndex = 0.while dutyPeriodIndex < aPayTrip.dutyPeriodList.size() do {aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dutyPeriodIndex).//// SET THE TRIP LEVEL PROPERTY isReserveTrip... //// ALL NON-RESERVEBLOCK TRIPS WITH AT LEAST ONE DUTY PERIOD WITH RAP ASSOCIATIONS ARE RESERVE TRIPS...if (aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size() > 0) then {aPayTrip.payTripInflight.isReserveTrip = true.aPayTrip.tripPay.tripPayInflight.isReserveTrip = true.}dutyPeriodIndex += 1.}}// US18772 - no londer use labels for deternining if a trip is a reserve blockelse if (aPayTrip.tripType = "R") then {dutyPeriodIndex = 0.while dutyPeriodIndex < aPayTrip.dutyPeriodList.size() do {aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dutyPeriodIndex).fcnShow("===>>> Inlight Reserve Block Day " aPayDutyPeriod.sequenceNumber " reporting at " aPayDutyPeriod.reportDateTime.toString()    " ... size of RAP association list = " aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size()).dutyPeriodIndex += 1.}}tripIndex += 1. }fcnShow("===>>> EXITING fcnAssociateInflightPayDutyPeriodsToRaps...").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnGetFirstFlyingLegScheduledDepartureDateTime](fcnGetFirstFlyingLegScheduledDepartureDateTime.md)
- [fcnIsSameSwaDay](fcnIsSameSwaDay.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang - 8/4/14 - US18071 - This function determines the association between duty periods and RAPs. If the duty period's report dateTime is on or after
a RAP's report dateTime and before the end of a RAPS's release dateTime, then the duty period is associated with that RAP.
7/1/2015 - Melissa S - DE6910 - Only creating a new PayDutyPeriodInflight if the value is null.  Otherwise the values passed in were being overwritten.
4/5/2016 - CSCH-2723 - Melissa S - Refactored for performance to use while loops and indexes instead of casting to Blaze arrays
```

