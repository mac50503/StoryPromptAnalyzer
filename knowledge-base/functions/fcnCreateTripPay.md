# fcnCreateTripPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCreateTripPay`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance and common use between CrewPay and TripPay functions

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| includeInflight | boolean | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
aTripPay is some TripPay initially a TripPay.aPayDutyPeriod is some PayDutyPeriod initially null.aDutyPeriodPay is some DutyPeriodPay initially null.aLegPay is some LegPay initially null.tafb is an integer initially 0.dpIndex is an integer initially 0.legIndex is an integer initially 0.if (aPayTrip <> null) then {// US16985 06/26/2014 CG - aTripPay.tripPayInflight is used in rsCalculateRIGsif (includeInflight) then  aTripPay.tripPayInflight = a TripPayInflight.fcnXrefPayTripToTripPay(aPayTrip, aTripPay).if (aPayTrip.tripStartSchedulePeriod <> null) then aTripPay.startSchedulePeriodPay = aPayTrip.tripStartSchedulePeriod.schedulePeriodPay. if (aPayTrip.tripEndSchedulePeriod <> null) then aTripPay.endSchedulePeriodPay = aPayTrip.tripEndSchedulePeriod.schedulePeriodPay.// Initialize DutyPeriodPay and LegPay output objectsif (aPayTrip.dutyPeriodList is not equal to null and aPayTrip.dutyPeriodList.size() > 0) then {while (dpIndex < aPayTrip.dutyPeriodList.size()) do {aPayDutyPeriod = aPayTrip.dutyPeriodList.get(dpIndex).aDutyPeriodPay = a DutyPeriodPay.fcnXrefPayDutyPeriodToDutyPeriodPay(aPayDutyPeriod, aDutyPeriodPay).fcnXrefPayDutyPeriodToPayTrip(aPayDutyPeriod, aPayTrip).fcnXrefDutyPeriodPayToTripPay(aDutyPeriodPay, aTripPay).if (aPayDutyPeriod.payTrip.tripType = "R") then {aPayDutyPeriod.basePay = 6.0.aDutyPeriodPay.basePay = 6.0.}if (aPayDutyPeriod.legList is not equal to null and aPayDutyPeriod.legList.size() > 0) then {legIndex = 0.while (legIndex < aPayDutyPeriod.legList.size()) do {aLegPay = a LegPay.fcnXrefPayLegToLegPay(aPayDutyPeriod.legList.get(legIndex), aLegPay).fcnXrefPayLegToPayDutyPeriod(aPayDutyPeriod.legList.get(legIndex), aPayDutyPeriod).fcnXrefLegPayToDutyPeriodPay(aLegPay, aDutyPeriodPay).aDutyPeriodPay.legPayList.add(aLegPay).legIndex += 1.}}aTripPay.dutyPeriodPayList.add(aDutyPeriodPay).if (includeInflight = true and aGlobalDataCache <> null) then {if(fcnIsConfigCollectionToggleON("IF_VARIABLE_REPORT_TIME_NEW_TABLE_INFO")) then {aPayDutyPeriod.variableReportMinutes = aPayDutyPeriod.dpVarRptMinutes.} else {aGlobalDataCache.calculatePayVariableReportTime(aPayDutyPeriod).}aGlobalDataCache.calculatePayVariableReleaseTime(aPayDutyPeriod).}dpIndex += 1.}}// DE3683 05/16/2014 MP - use calculated TAFBaTripPay.timeAwayFromBase = aPayTrip.timeAwayFromBase.if (aPayTrip.firstDutyPeriod <> null and aPayTrip.lastDutyPeriod <> null) then {tafb = Duration.newInstance(aPayTrip.firstDutyPeriod.reportDateTime, aPayTrip.lastDutyPeriod.releaseDateTime).standardMinutes.if (aPayTrip.timeAwayFromBase <> tafb) thenaTripPay.timeAwayFromBase = tafb.}}return aTripPay.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsConfigCollectionToggleON](fcnIsConfigCollectionToggleON.md)
- [fcnXrefDutyPeriodPayToTripPay](fcnXrefDutyPeriodPayToTripPay.md)
- [fcnXrefLegPayToDutyPeriodPay](fcnXrefLegPayToDutyPeriodPay.md)
- [fcnXrefPayDutyPeriodToDutyPeriodPay](fcnXrefPayDutyPeriodToDutyPeriodPay.md)
- [fcnXrefPayDutyPeriodToPayTrip](fcnXrefPayDutyPeriodToPayTrip.md)
- [fcnXrefPayLegToLegPay](fcnXrefPayLegToLegPay.md)
- [fcnXrefPayLegToPayDutyPeriod](fcnXrefPayLegToPayDutyPeriod.md)
- [fcnXrefPayTripToTripPay](fcnXrefPayTripToTripPay.md)

## Llamado por

- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)
- [fcnCreateSchedulePeriodPayInflightAnalytics](fcnCreateSchedulePeriodPayInflightAnalytics.md)
- [fcnCreateTripPayInflightAnalytics](fcnCreateTripPayInflightAnalytics.md)
- [fcnCreateTripPayResponse](fcnCreateTripPayResponse.md)

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance and common use between CrewPay and TripPay functions
DE5879 - Akshay M  -  3/7/2015 - Implementing PerDiemTimeAwayFromBase for RS deadheads
DE7347 - Tim A. - 9/24/2015 - added calculation of variable report and variable release times
4/5/2016 - CSCH-2723 - Melissa S - Refactored for performance to use while loops and indexes instead of casting to Blaze arrays
```

