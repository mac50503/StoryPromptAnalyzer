# fcnCreatePlnTripPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnTripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnCreatePlnTripPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPlnPayTrip | PlnPayTrip | |

## Lógica de negocio

```blaze
aPlnTripPay is some PlnTripPay initially null.if (aPlnPayTrip <> null) then {aPlnTripPay = a PlnTripPay.aPayDutyPeriod is some PayDutyPeriod initially null.aPlnDutyPeriodPay is some PlnDutyPeriodPay initially null.aPayLeg is some PayLeg initially null.aPlnLegPay is some PlnLegPay initially null.//////// XREF REQUEST TRIP TO RESPONSE TRIP...//// XREF RESPONSE TRIP TO REQUEST TRIP...////aPlnPayTrip.plnTripPay = aPlnTripPay. aPlnTripPay.plnPayTrip = aPlnPayTrip. aPlnPayTrip.tripNameAndDate = aPlnPayTrip.tripName "/" aPlnPayTrip.beginDateTime.dayOfMonth.aPlnTripPay.tripNameAndDate = aPlnPayTrip.tripNameAndDate.// Initialize PlnDutyPeriodPay and PlnLegPay output objectsif (aPlnPayTrip.payDutyPeriodList is not equal to null and aPlnPayTrip.payDutyPeriodList.size() > 0) then     {for each PayDutyPeriod in aPlnPayTrip.payDutyPeriodList as an array of PayDutyPeriod do      {         aPayDutyPeriod = it.//////// XFREF REQUEST DUTY PERIOD TO REQUEST TRIP...////aPayDutyPeriod.plnPayTrip = aPlnPayTrip.//////// XREF REQUEST DUTY PERIOD TO RESPONSE DUTY PERIOD...//// XREF RESPONSE DUTY PERIOD TO REQUEST DUTY PERIOD...//// XREF RESPONSE DUTY PERIOD TO RESPONSE TRIP...////aPlnDutyPeriodPay = a PlnDutyPeriodPay.aPayDutyPeriod.plnDutyPeriodPay = aPlnDutyPeriodPay. aPlnDutyPeriodPay.payDutyPeriod = aPayDutyPeriod.  aPlnDutyPeriodPay.plnTripPay = aPlnTripPay.  aPlnDutyPeriodPay.sequenceNumber = aPayDutyPeriod.sequenceNumber.  aPlnDutyPeriodPay.scheduledReportDateTime = aPayDutyPeriod.reportDateTime.  aPlnDutyPeriodPay.scheduledReleaseDateTime = aPayDutyPeriod.releaseDateTime.  //////// ADD NEW REPONSE DUTY PERIOD TO RESONSE TRIP DUTY PERIOD LIST...////aPlnTripPay.plnDutyPeriodPayList.add(aPlnDutyPeriodPay).//////// CREATE RESONSE LEG OBJECTS AND XREF TO REQUEST LEG OBJECTS...////if (aPayDutyPeriod.legList is not equal to null and aPayDutyPeriod.legList.size() > 0) then {    aPayDutyPeriod = it.for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do     {        aPayLeg = it.//////// CREATE RESPONSE LEG OBJECT AND ADD TO RESPONSE DUTY PERIOD PLNLEGLIST...////aPlnLegPay = a PlnLegPay.aPlnLegPay.plnDutyPeriodPay = aPlnDutyPeriodPay.aPlnDutyPeriodPay.plnLegPayList.add(aPlnLegPay).//////// CREATE RESPONSE LEG OBJECT AND XREF REQUEST LEG TO RESPONSE LEG...//////aPlnLegPay = a PlnLegPay.aPayLeg.plnLegPay = aPlnLegPay.aPlnLegPay.payLeg = aPayLeg.aPlnLegPay.sequenceNumber = aPayLeg.sequenceNumber.aPlnLegPay.basePay = aPayLeg.basePay.aPlnLegPay.creditType = aPayLeg.creditType.       }aPlnDutyPeriodPay.firstLeg = aPlnDutyPeriodPay.plnLegPayList.get(0).aPlnDutyPeriodPay.lastLeg = aPlnDutyPeriodPay.plnLegPayList.get(aPlnDutyPeriodPay.plnLegPayList.size() - 1).}}}if (aPlnTripPay.plnDutyPeriodPayList.size() > 0) then{aPlnTripPay.firstDutyPeriod = aPlnTripPay.plnDutyPeriodPayList.get(0).aPlnTripPay.lastDutyPeriod = aPlnTripPay.plnDutyPeriodPayList.get(aPlnTripPay.plnDutyPeriodPayList.size() - 1).}}return aPlnTripPay.
```

## Llamado por

- [fcnCreatePlnLinePayResponse](fcnCreatePlnLinePayResponse.md)
- [fcnCreatePlnTripPayResponse](fcnCreatePlnTripPayResponse.md)

