# fcnCalculateDutyPeriodContributionForProductivityPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateDutyPeriodContributionForProductivityPay`

## Propósito
Mar 12 2015 Tim A. - helper function to assist with productivity pay calculation

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| reportDateRangeFilterStart | DateTime | |
| reportDateRangeFilterEnd | DateTime | |
| useReserveMethodology | boolean | |

## Lógica de negocio

```blaze
aTripPay is some TripPay initially aDutyPeriodPay.tripPay.retVal is a real initially 0.0.hasRapAssociation is a boolean initially false.if (aDutyPeriodPay.payDutyPeriod.payDutyPeriodInflight.rapAssociationList.size() > 0) thenhasRapAssociation = true.skipThisDutyPeriod is a boolean initially false.if (useReserveMethodology and hasRapAssociation) then{skipThisDutyPeriod = true.fcnShow("===>>> trip = " aTripPay.tripNameAndDate " ...skipping DP " aDutyPeriodPay.sequenceNumber " because it is assocated with a reserve block duty...").}if (skipThisDutyPeriod = false and    fcnIsDateTimeWithinDateTimeRange(aDutyPeriodPay.reportDateTime, theSchedulePeriodPay.schedulePeriodStart, theSchedulePeriodPay.schedulePeriodEnd) and    fcnIsDateTimeWithinReportFilterRange(aDutyPeriodPay.reportDateTime, reportDateRangeFilterStart, reportDateRangeFilterEnd)) then{if (useReserveMethodology and fcnIsReserveTrip(aDutyPeriodPay.tripPay.payTrip) and hasRapAssociation = false) then{fcnShow("===>>> reserve trip "  aTripPay.tripNameAndDate " has DP " aDutyPeriodPay.sequenceNumber " with no associated reserve block duty...").}if (aTripPay.creditType  = "G" and    aTripPay.basePay > fcnGetSumOfLegPayForTrip(aTripPay) and    aTripPay.basePay > aTripPay.tripPayInflight.dutyPeriodSum) then{retVal = aTripPay.payTrip.basePay.}//// TEST FOR CT=G and PREMIUM > RIG....else if (aTripPay.creditType  = "G" and             aTripPay.tripPayInflight.rigsGreaterThanPremium = false and             aDutyPeriodPay.rigsGreaterThanPremium = false) then{retVal = aDutyPeriodPay.sumLegBaseCredits.}else if (aDutyPeriodPay.sumLegTotalCredits > aDutyPeriodPay.payDutyPeriod.basePay and             aDutyPeriodPay.sumLegTotalCredits > aDutyPeriodPay.dutyHourRatio) then{retVal = aDutyPeriodPay.sumLegBaseCredits.}else if (aDutyPeriodPay.payDutyPeriod.creditType = ("E" or "P")) then{if (aDutyPeriodPay.payDutyPeriod.basePay > aDutyPeriodPay.sumLegBaseCredits) thenretVal = aDutyPeriodPay.payDutyPeriod.basePay. elseretVal = aDutyPeriodPay.sumLegBaseCredits + aDutyPeriodPay.dutyPeriodRig  +  aDutyPeriodPay.tripExcess. //// DE7314 added duty rig,  DE7515 added tripExcess}else {if (aDutyPeriodPay.tripPay.assignmentLabel = ("J" or "U" or "V")) then{if(aDutyPeriodPay.rigsGreaterThanPremium) then{retVal = aDutyPeriodPay.basePay.}else{retVal = aDutyPeriodPay.sumLegBaseCredits.if (aDutyPeriodPay.tripPay.assignmentLabel = ("J" or "U" or "V" or "D")) thenretVal += aDutyPeriodPay.dutyPeriodRig.}}else if (aDutyPeriodPay.creditType = "D") then{retVal = math().max(aDutyPeriodPay.dutyHourRatio, aDutyPeriodPay.sumLegTotalCredits).if (aDutyPeriodPay.payValue > aDutyPeriodPay.basePay and                                                 aDutyPeriodPay.payValue > aDutyPeriodPay.highestDutyPeriodRig) thenretVal -= aDutyPeriodPay.dutyPeriodRig.}else if (aDutyPeriodPay.sumLegTotalCredits > aDutyPeriodPay.sumLegBaseCredits and                            aDutyPeriodPay.thisMonthPay = aDutyPeriodPay.sumLegTotalCredits) then{retVal = aDutyPeriodPay.sumLegBaseCredits.}else if (aDutyPeriodPay.thisMonthPay >= aDutyPeriodPay.sumLegBaseCredits and                                          aDutyPeriodPay.thisMonthPay >= aDutyPeriodPay.dutyPeriodMinimum) then{retVal = aDutyPeriodPay.thisMonthPay - aDutyPeriodPay.sumLegPremiumCredits.}else if (aDutyPeriodPay.sumLegBaseCredits >= aDutyPeriodPay.dutyHourRatio and                                          aDutyPeriodPay.sumLegBaseCredits >= aDutyPeriodPay.dutyPeriodMinimum) then{retVal = aDutyPeriodPay.sumLegBaseCredits.}else{retVal = aDutyPeriodPay.thisMonthPay.}if (aTripPay.payTrip.creditType <> (ignoring case) "F") then{if (aDutyPeriodPay.tripExcess > 0.0) then{retVal += aDutyPeriodPay.tripExcess.}}}//fcnShow("===>>> Exiting fcnCalculateDutyPeriodContributionForProductivityPay... Trip = " aDutyPeriodPay.tripPay.tripNameAndDate " ...DP = " aDutyPeriodPay.sequenceNumber " ...returning: " retVal).}return fcnRoundUpAt2DecimalPlaces(retVal).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfLegPay](fcnGetSumOfLegPay.md)
- [fcnGetSumOfLegPayForTrip](fcnGetSumOfLegPayForTrip.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnIsReserveTrip](fcnIsReserveTrip.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [ping](ping.md)

## Historial de cambios

```
Mar 12 2015 Tim A. - helper function to assist with productivity pay calculation
May 19 2015 Tim A. - added report date range filter parameters
```

