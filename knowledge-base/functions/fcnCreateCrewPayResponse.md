# fcnCreateCrewPayResponse

## Metadata
- **Tipo**: SRL Function
- **Retorna**: CrewPayResponse
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateCrewPayResponse`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aCrewPayRequest | CrewPayRequest | |
| includeInflight | boolean | |

## Lógica de negocio

```blaze
aCrewPayResponse is a CrewPayResponse.aCrewPayResponse.crewId = fcnGetCrewId(aCrewPayRequest).aPayTrip is some PayTrip initially null.aTripPay is some TripPay initially null.aPayCrewMember is some PayCrewMember initially null.if (aCrewPayRequest.crewLine is not equal to null and    aCrewPayRequest.crewLine.schedulePeriodList is not equal to null and     aCrewPayRequest.crewLine.schedulePeriodList.size() > 0) then{// Create the list of SchedulePeriodPay objects and add to the responseaSchedulePeriodPay is some SchedulePeriodPay initially null.for each SchedulePeriod in aCrewPayRequest.crewLine.schedulePeriodList as an array of SchedulePeriod do {aSchedulePeriodPay = a SchedulePeriodPay.if (includeInflight) then {aSchedulePeriodPay.schedulePeriodPayInflight = a SchedulePeriodPayInflight. aSchedulePeriodPay.schedulePeriodPayInflight.schedulePeriodPay = aSchedulePeriodPay.}aCrewPayResponse.addSchedulePeriodPay(aSchedulePeriodPay).fcnXrefSchedulePeriodToSchedulePeriodPay(it, aSchedulePeriodPay).}// Set the reportsOnHoliday field for all PayDutyPeriodsfor each PayTrip in aCrewPayRequest.crewLine.tripList as an array of PayTrip do {fcnAssignDutyPeriodReportsOnHoliday(it, aCrewPayRequest.swaHolidayList);}// Loop through all SchedulePeriods and create/add the TripPay response objects to the appropriate SchedulePeriodPay objectsfor each SchedulePeriod in aCrewPayRequest.crewLine.schedulePeriodList as an array of SchedulePeriod do {aSchedulePeriodPay = it.schedulePeriodPay.// Find the crew member asociated with the SchedulePeriodaPayCrewMember = fcnGetPayCrewMemberBySchedulePeriodName(aCrewPayRequest.crewLine.crewMemberList, aSchedulePeriodPay.schedulePeriodName).if (aPayCrewMember <> null) then aSchedulePeriodPay.crewPosition = aPayCrewMember.crewPosition.if (aCrewPayRequest.crewLine is not equal to null and     aCrewPayRequest.crewLine.tripList is not equal to null and     aCrewPayRequest.crewLine.tripList.size() > 0) then {for each PayTrip in aCrewPayRequest.crewLine.tripList as an array of PayTrip do {aPayTrip = it.// Initialize the startSchedulePeriodPay field for TripPay, and add the TripPay object to TripPayList for the SchedulePeriodPayif (aSchedulePeriodPay.schedulePeriodName.equalsIgnoreCase(aPayTrip.startsInSchedulePeriod)) then {aTripPay = fcnCreateTripPay(aPayTrip, includeInflight, aCrewPayRequest.globalDataCache).aTripPay.startSchedulePeriodPay = aSchedulePeriodPay.if (aSchedulePeriodPay.tripPayList.contains(aTripPay) is equal to false) thenaSchedulePeriodPay.addTripPay(aTripPay).}// Initialize the endSchedulePeriodPay field for TripPay, and add the TripPay object to TripPayList for the SchedulePeriodPayif (aPayTrip.endsInSchedulePeriod <> aPayTrip.startsInSchedulePeriod and     aSchedulePeriodPay.schedulePeriodName.equalsIgnoreCase(aPayTrip.endsInSchedulePeriod)) then {aTripPay = fcnCreateTripPay(aPayTrip, includeInflight, aCrewPayRequest.globalDataCache).aTripPay.endSchedulePeriodPay = aSchedulePeriodPay.if (aSchedulePeriodPay.tripPayList.contains(aTripPay) is equal to false) then aSchedulePeriodPay.addTripPay(aTripPay).if (aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then{for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{if (it.payDutyPeriodInflight <> null) thenit.payDutyPeriodInflight.payCrewMember = aPayCrewMember.}}}}}// Create the list of PayBuckets in the responseif (aCrewPayRequest.payAdjustmentList <> null and aCrewPayRequest.payAdjustmentList.size() > 0) then {//aPayAdjustment is some PayAdjustment initially a PayAdjustment.for each PayAdjustment in aCrewPayRequest.payAdjustmentList as an array of PayAdjustment do {if (fcnDoesPayAdjustmentBeginInSchedulePeriod(it, aSchedulePeriodPay)) then it.xrefSchedulePeriodPay(aSchedulePeriodPay).}} }}return aCrewPayResponse.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAssignDutyPeriodReportsOnHoliday](fcnAssignDutyPeriodReportsOnHoliday.md)
- [fcnCreateTripPay](fcnCreateTripPay.md)
- [fcnDoesPayAdjustmentBeginInSchedulePeriod](fcnDoesPayAdjustmentBeginInSchedulePeriod.md)
- [fcnGetCrewId](fcnGetCrewId.md)
- [fcnGetPayCrewMember](fcnGetPayCrewMember.md)
- [fcnGetPayCrewMemberBySchedulePeriodName](fcnGetPayCrewMemberBySchedulePeriodName.md)
- [fcnXrefSchedulePeriodToSchedulePeriodPay](fcnXrefSchedulePeriodToSchedulePeriodPay.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance
CREW-4750 - 4/23/2018 - Updated call to fcnAssignDutyPeriodReportsOnHoliday
```

