# fcnCalculateTripCpCodePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateTripCpCodePay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aPayTrip <> null) then{aPayDutyPeriod is some PayDutyPeriod initially null.aPayLeg is some PayLeg initially null.aLegPay is some LegPay initially null.aTripPay is some TripPay initially null.aSchedulePeriodPay is some SchedulePeriodPay initially null.aPayRate is a real initially 0.0.if (aPayTrip.dutyPeriodList.size() > 0) then{for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do{aPayDutyPeriod = it.if (aPayDutyPeriod.legList.size() > 0) then{for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{aPayLeg = it.aLegPay = aPayLeg.legPay.if (fcnGetCpCodeAssociatedBucket(aPayLeg.cpCode) <> null) then{aTripPay = fcnGetTripPayFromPayLeg(aPayLeg).aSchedulePeriodPay = fcnGetSchedulePeriodPayForLegPay(aPayLeg.legPay).if (aTripPay <> null and aSchedulePeriodPay <> null) then{aPayRate = fcnGetCpCodePayRateForLeg(aPayLeg, aGlobalDataCache).legCpCodePay is a real initially 0.0.legCpCodePay = fcnRoundUpAt2DecimalPlaces(aLegPay.payValueNoPremium * aPayRate).//fcnShow("===>>> pay no premium for " fcnGetLegIdentificationString(aPayLeg) " = " aLegPay.payValueNoPremium).//fcnShow("===>>> calculating CpCode Pay for " fcnGetLegIdentificationString(aPayLeg)).//fcnShow("===>>> pay no premium of leg * CpCode rate = " aLegPay.payValueNoPremium " * " aPayRate " = " legCpCodePay).fcnDistributeToPayBucket (aSchedulePeriodPay, fcnGetCpCodeAssociatedBucket(aPayLeg.cpCode), legCpCodePay, aPayRate,aPayLeg.scheduledDepartureDateTime, reportFilterStart, reportFilterEnd, aTripPay).if(aLegPay <> null and aLegPay.legPayInflightAnalytics <> null and aLegPay.dutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{  theDutyPeriodPayInflightAnalytics is some DutyPeriodPayInflightAnalytics initially aLegPay.dutyPeriodPay.dutyPeriodPayInflightAnalytics;if(fcnGetCpCodeAssociatedBucket(aPayLeg.cpCode) = "SAFBUCKET") then{if( aLegPay.legPayInflightAnalytics.legIsDeadhead = false) then{aLegPay.legPayInflightAnalytics.legBonusPayMap.put("South American", legCpCodePay);if(theDutyPeriodPayInflightAnalytics.sumOfLegBonusPayMap.containsKey("South American")) then{theDutyPeriodPayInflightAnalytics.sumOfLegBonusPayMap.put("South American",fcnRoundUpAt2DecimalPlaces(theDutyPeriodPayInflightAnalytics.sumOfLegBonusPayMap.get("South American") + aLegPay.legPayInflightAnalytics.legBonusPayMap.get("South American")));}else{theDutyPeriodPayInflightAnalytics.sumOfLegBonusPayMap.put("South American",fcnRoundUpAt2DecimalPlaces(aLegPay.legPayInflightAnalytics.legBonusPayMap.get("South American")));}}else{aLegPay.legPayInflightAnalytics.legDeadheadBonusPayMap.put("South American", legCpCodePay);if(theDutyPeriodPayInflightAnalytics.sumOfDeadheadLegBonusPayMap.containsKey("South American")) then{theDutyPeriodPayInflightAnalytics.sumOfDeadheadLegBonusPayMap.put("South American",fcnRoundUpAt2DecimalPlaces(theDutyPeriodPayInflightAnalytics.sumOfDeadheadLegBonusPayMap.get("South American") + aLegPay.legPayInflightAnalytics.legDeadheadBonusPayMap.get("South American")));}else{theDutyPeriodPayInflightAnalytics.sumOfDeadheadLegBonusPayMap.put("South American",fcnRoundUpAt2DecimalPlaces(aLegPay.legPayInflightAnalytics.legDeadheadBonusPayMap.get("South American")));}}}}}}}}}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)
- [fcnGetCpCodeAssociatedBucket](fcnGetCpCodeAssociatedBucket.md)
- [fcnGetCpCodePayRateForLeg](fcnGetCpCodePayRateForLeg.md)
- [fcnGetLegIdentificationString](fcnGetLegIdentificationString.md)
- [fcnGetSchedulePeriodPayForLegPay](fcnGetSchedulePeriodPayForLegPay.md)
- [fcnGetTripPay](fcnGetTripPay.md)
- [fcnGetTripPayFromPayLeg](fcnGetTripPayFromPayLeg.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

