# fcnCalculateConusAndOconusPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateConusAndOconusPay`

## Propósito
Ben Lang - US8942 - 03/10/14 - The fcnCalculateConusAndOcuonusPay function calculates the oconus and conus pay for a particular TripPay.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aTripPay | TripPay | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aTripPay <> null and (aPayTrip.payTripInflight = null or (aPayTrip.payTripInflight <> null and aPayTrip.tripSet <> null)) and fcnIsReserveBlock(aPayTrip) is equal to false and fcnIsNonFlyTrip(aPayTrip) is equal to false and fcnGetFirstFlyingLeg(aPayTrip) <> null)  then {fcnShow("===>>> ENTERING function fcnCalculateConusAndOconusPay with trip " aPayTrip.tripNameAndDate).conusPayRate is a real initially fcnDetermineConusPerDiemPayRate(aPayTrip.beginDateTime);oconusPayRate is a real initially fcnDetermineOconusPerDiemPayRate(aPayTrip.beginDateTime);perdiemTripStartDateTime is some DateTime initially aPayTrip.nonDeadheadBeginDateTime;perdiemTripEndDateTime is some DateTime initially aPayTrip.nonDeadheadEndDateTime;firstDutyPeriodWithOconusLeg is some PayDutyPeriod initially null.if (aGlobalDataCache <> null and aGlobalDataCache.stationMap <> null and fcnTripHasOconusLeg(aPayTrip, aGlobalDataCache) and fcnPayTripHasAllNonflyLegs(aPayTrip)=false) then {firstDutyPeriodWithOconusLeg = fcnGetFirstDutyPeriodWithOconusLeg(aPayTrip, aGlobalDataCache).fcnShow("===>>> in code block 1 with firstDutyPeriodWithOconusLeg = " firstDutyPeriodWithOconusLeg).// --------------------Adding RS deadhead logic as per DE6065 requirementif (aTripPay.tripPayInflight is not equal to null) then//// INFLIGHT SCOPE...{fcnShow("===>>> in code block 2 - INFLIGHT scope...").if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripStartDateTime <> null) thenperdiemTripStartDateTime = aPayTrip.payTripInflight.perdiemTripStartDateTime;if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripEndDateTime <> null) thenperdiemTripEndDateTime = aPayTrip.payTripInflight.perdiemTripEndDateTime;if (firstDutyPeriodWithOconusLeg <> null and firstDutyPeriodWithOconusLeg = aPayTrip.firstDutyPeriod) then{// To handle the case where the First DP has OCONUS leg, but all legs are RS deadheadsaTripPay.oconusPay = fcnTimeDiffInHoursDecimal(perdiemTripStartDateTime, perdiemTripEndDateTime) * oconusPayRate.}else if (firstDutyPeriodWithOconusLeg<>null and firstDutyPeriodWithOconusLeg.reportDateTime.isBefore(aPayTrip.nonDeadheadEndDateTime)) then{// To handle the case where the Last DP is the first duty period that has OCONUS leg, but all legs are RS deadheadsaTripPay.conusPay = fcnTimeDiffInHoursDecimal(perdiemTripStartDateTime, firstDutyPeriodWithOconusLeg.reportDateTime) * conusPayRate.aTripPay.oconusPay = fcnTimeDiffInHoursDecimal(firstDutyPeriodWithOconusLeg.reportDateTime, perdiemTripEndDateTime) * oconusPayRate.secondDuty is some PayDutyPeriod initially aPayTrip.dutyPeriodList.get(1).}else{aTripPay.conusPay = fcnTimeDiffInHoursDecimal(perdiemTripStartDateTime, perdiemTripEndDateTime) * conusPayRate.}}else    //// FLT OPS SCOPE...{perdiemTripStartDateTime = aPayTrip.beginDateTime.perdiemTripEndDateTime = aPayTrip.endDateTime.//(my trip's last duty period's release time - report time of the first duty period with an oconus leg)*oconusPayRate = add to oconusPayif (aPayTrip.lastDutyPeriod is not equal to null and firstDutyPeriodWithOconusLeg is not equal to null) then{aTripPay.oconusPay = fcnTimeDiffInHoursDecimal(firstDutyPeriodWithOconusLeg.reportDateTime, aPayTrip.lastDutyPeriod.releaseDateTime) * oconusPayRate.}//(report time of first duty period with oconus leg - report time of my trip's first duty period)*conusPayRate = add to conusPayif (aPayTrip.firstDutyPeriod is not equal to null and firstDutyPeriodWithOconusLeg is not equal to null) then{aTripPay.conusPay = fcnTimeDiffInHoursDecimal(aPayTrip.firstDutyPeriod.reportDateTime, firstDutyPeriodWithOconusLeg.reportDateTime) * conusPayRate.}fcnShow("===>>> in code block 3 - fltOps scope... OCONUS PAY NOW = " aTripPay.oconusPay).}} else {if (aTripPay.tripPayInflight is not equal to null) then{fcnShow("===>>> in code block 4 INFLIGHT CONUS scope... perdiemTimeAwayFromBase = " aTripPay.perdiemTimeAwayFromBase " ...conusPayRate = " conusPayRate).// DE5879 Replacing timeAwayFromBase field with perdiemTimeAwayFromBaseaTripPay.conusPay = aTripPay.perdiemTimeAwayFromBase * conusPayRate/60.fcnShow("===>>> fcnCalculateConusAndOconusPay - setting CONUS pay for trip " aPayTrip.tripNameAndDate).if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripStartDateTime <> null) thenperdiemTripStartDateTime = aPayTrip.payTripInflight.perdiemTripStartDateTime.if (aPayTrip.payTripInflight <> null and aPayTrip.payTripInflight.perdiemTripEndDateTime <> null) thenperdiemTripEndDateTime = aPayTrip.payTripInflight.perdiemTripEndDateTime.}else{fcnShow("===>>> in code block 5 FLTOPS CONUS scope... ").//DE3683 05/16/2014 MP - use calculated TAFB aTripPay.conusPay = aTripPay.timeAwayFromBase* conusPayRate/60. fcnShow("===>>> fcnCalculateConusAndOconusPay - setting CONUS pay for trip " aPayTrip.tripNameAndDate).}}if (aTripPay.tripPayInflightAnalytics <> null or aTripPay.tripPayFltOpsAnalytics <> null) thenfcnDistributePerdiemPayToDutyPeriods(aPayTrip, perdiemTripStartDateTime, perdiemTripEndDateTime, firstDutyPeriodWithOconusLeg, conusPayRate, oconusPayRate).}//////// FOR PERDIEM PROPERTIES, ROUND TO 3 DECIMAL PLACES OF ACCURACY THEN ROUND TO 2 DECIMAL PLACES OF ACCURACY...////if (aTripPay <> null)  then {aTripPay.perdiemPay = math().round(math().round(aTripPay.conusPay, -3), -2) + math().round(math().round(aTripPay.oconusPay, -3), -2).}fcnShow("===>>> EXITING fcnCalculateConusAndOconusPay - CONUS pay for trip " aTripPay.tripNameAndDate  " = " aTripPay.conusPay " ...OCONUS pay  = " aTripPay.oconusPay).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDetermineConusPerDiemPayRate](fcnDetermineConusPerDiemPayRate.md)
- [fcnDetermineOconusPerDiemPayRate](fcnDetermineOconusPerDiemPayRate.md)
- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)
- [fcnGetFirstDutyPeriodWithOconusLeg](fcnGetFirstDutyPeriodWithOconusLeg.md)
- [fcnGetFirstFlyingLeg](fcnGetFirstFlyingLeg.md)
- [fcnIsNonFlyTrip](fcnIsNonFlyTrip.md)
- [fcnIsReserveBlock](fcnIsReserveBlock.md)
- [fcnPayTripHasAllNonflyLegs](fcnPayTripHasAllNonflyLegs.md)
- `fcnShow()`
- [fcnTimeDiffInHoursDecimal](fcnTimeDiffInHoursDecimal.md)
- [fcnTripHasOconusLeg](fcnTripHasOconusLeg.md)

## Llamado por

- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)

## Historial de cambios

```
Ben Lang - US8942 - 03/10/14 - The fcnCalculateConusAndOcuonusPay function calculates the oconus and conus pay for a particular TripPay.
Mitesh P - DE3683 - 05/16/2014 - use calculated TAFB
Akshay - US17075 - 05/20/2014 - Return conusPay, oconusPay and total perdiemPay for each trip
Akshay - DE6065 - 03/30/2014 - Remove deadheads from OCONUS/CONUS perdiem calculations.
RS - CSCH-3895/CSCH-4055 - 10/27/2016 - Updated Per Diem Pay Rates
RS - CREW-3446 - 9/18/2017 - Allow overriding of Per Diem dates
```

