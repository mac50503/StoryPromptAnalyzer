# fcnSetHighestRigAmounts

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetHighestRigAmounts`

## Propósito
7/24/2015 - DE7092 - Melissa S - Added condition at the trip level from RON - trips with a RON duty period should not consider THR

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if2025RepReserveEffectiveDateActiveFlag is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aTripPay.beginDateTime, "IF_2025_REP_BLAZE_RESERVE_EFFECTIVE_DATE").if (aTripPay <> null and aTripPay.tripPayInflight <> null and aTripPay.dutyPeriodPayList <> null and aTripPay.dutyPeriodPayList.size() > 0) then{lastLeg is some PayLeg.lastLegLateAmount is a duration initially 0 hours.// Determine how late the last leg of the trip isif (aTripPay.payTrip.lastDutyPeriod <> null and aTripPay.payTrip.lastDutyPeriod.lastLeg <> null and     aTripPay.payTrip.lastDutyPeriod.lastLeg.scheduledArrivalDateTime <> null and                     aTripPay.payTrip.lastDutyPeriod.lastLeg.actualInDateTime <> null) then {lastLeg = aTripPay.payTrip.lastDutyPeriod.lastLeg.lastLegLateAmount = ((Duration.newInstance(lastLeg.scheduledArrivalDateTime, lastLeg.actualInDateTime).standardMinutes " minutes") as a duration).}// ==================== Determine highest trip RIG ====================// A trip with a RON duty period will always use zero for the highest RIG //// DE7121if (aTripPay.payTrip.containsRON = true) then {aTripPay.tripPayInflight.highestTripRig = 0.0.  // F Credit type - not J,U,V label and under a reserve trip will pick the higher of Base Pay or THR, everything else will use base pay} else if (aTripPay.payTrip.creditType = "F") then {aTripPay.tripPayInflight.highestTripRig = 0.0.//aTripPay.tripPayInflight.highestTripRig = aTripPay.basePay.//if (aTripPay.assignmentLabel <> (ignoring case) ("J" and "V" and "U") and aTripPay.tripPayInflight.isReserveTrip = true) then //{//aTripPay.tripPayInflight.highestTripRig = math().max(aTripPay.basePay, aTripPay.tripPayInflight.thrValue).//}// P credit type not under a reserve, and <= 3 hours late will use Base Pay as the highest RIG} else if (aTripPay.payTrip.creditType = ("P") and aTripPay.tripPayInflight.isReserveTrip = false and lastLegLateAmount <= 3 hours) then aTripPay.tripPayInflight.highestTripRig = aTripPay.basePay.// P credit type under a reserve or > 3 hours late, and Credit types U, and Q will use the higher of Base Pay or THR as the highest RIGelse if (aTripPay.payTrip.creditType = ("P" or "Q" or "U" or "G")) thenaTripPay.tripPayInflight.highestTripRig = math().max(aTripPay.basePay, aTripPay.tripPayInflight.thrValue).// All other credit types wil use the highest of ADG or THR as the highest RIGelse aTripPay.tripPayInflight.highestTripRig = math().max(aTripPay.tripPayInflight.adgValue, aTripPay.tripPayInflight.thrValue).// ====================Determine highest Duty RIG ====================for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do {lastLegLateAmount = 0 hours.// Determine how late the last leg of the duty period isif (it.payDutyPeriod.lastLeg <> null and     it.payDutyPeriod.lastLeg.scheduledArrivalDateTime <> null and                    it.payDutyPeriod.lastLeg.actualInDateTime <> null) then {lastLeg = it.payDutyPeriod.lastLeg.lastLegLateAmount = ((Duration.newInstance(lastLeg.scheduledArrivalDateTime, lastLeg.actualInDateTime).standardMinutes " minutes") as a duration).}// Default is to use highest of DHR and DPM for highest RIGit.highestDutyPeriodRig = math().max(it.dutyHourRatio, it.dutyPeriodMinimum).// RON default is always 0.0if (it.payDutyPeriod.dutyType = "RON") then it.highestDutyPeriodRig = 0.0.else if (it.payDutyPeriod.dutyType <> "RON") then {// P credit type not under a reserve, and <= 3 hours late will use Base Pay as the highest RIGif (it.payDutyPeriod.creditType = ("P") and it.rapAssociation = null and lastLegLateAmount <= 3 hours) thenit.highestDutyPeriodRig = it.payDutyPeriod.basePay.// P credit type under a reserve or > 3 hours late, and Credit types E, Q will use the higher of Base Pay or DHR as the highest RIGelse if (it.payDutyPeriod.creditType = ("P" or "E" or "Q")) thenit.highestDutyPeriodRig = math().max(it.dutyHourRatio, it.payDutyPeriod.basePay).// F credit type won't use RIGs - using zero here since there are no RIGs in this scenarioelse if (it.payDutyPeriod.creditType = ("F")) thenit.highestDutyPeriodRig = 0.0.// D credit type will only use DHRelse if (it.payDutyPeriod.creditType = ("D")) then{it.highestDutyPeriodRig = it.dutyHourRatio.}// M credit type will only use DPMelse if (it.payDutyPeriod.creditType = ("M")) then {it.highestDutyPeriodRig = it.dutyPeriodMinimum.if (if2025RepReserveEffectiveDateActiveFlag) then {it.highestDutyPeriodRig = 4.0.}}// G credit type will use the higher of Base Pay, DHR, or DPM as the highest RIGelse if (it.payDutyPeriod.creditType = ("G")) thenit.highestDutyPeriodRig = fcnMaxOf3Numbers(it.dutyHourRatio, it.dutyPeriodMinimum, it.payDutyPeriod.basePay).}if (aTripPay.payTrip.containsRON = false) then {aTripPay.tripPayInflight.highestDutyRigSum += it.highestDutyPeriodRig.aTripPay.tripPayInflight.highestDutyRigSum = fcnRoundUpAt2DecimalPlaces(aTripPay.tripPayInflight.highestDutyRigSum).}}fcnShow("===>>> EXITING fcnSetHighestDutyRigSum for " aTripPay.tripNameAndDate " ...highestTripRig = " aTripPay.tripPayInflight.highestTripRig " ...highestDutyRigSum = " aTripPay.tripPayInflight.highestDutyRigSum).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnMaxOf3Numbers](fcnMaxOf3Numbers.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
7/24/2015 - DE7092 - Melissa S - Added condition at the trip level from RON - trips with a RON duty period should not consider THR
7/24/2015 - DE7099 - Melissa S - Added condition at the trip level for P &lt;= 3 hours (blocks THR)
7/24/2015 - DE6967 - Melissa S - Added condition at the duty period level for P &lt;= 3 hours (blocks DHR), removed condition at the duty level for trip credit type &lt;&gt; P or E
7/29/2015 - DE7134 - Melissa S - Updated logic for setting highestDutyPeriodRig to include what should be done for credit types M, F, G, Q, D, and P under a reserve block
(this defect only addressed F credit type specifically, but the logic for the other credit types was missing per the CT Locations and RIGS tabs in the workbook)
7/30/2015 - DE7144 - Melissa S - Modified D credit type at the duty level to only use DHR, and not to compare the passed in value (base pay)
7/30/2105 - N/A - Melissa S - Refactor of highest trip rig logic for credit types F and G
7/31/2015 - DE7071 - Melissa S - Set highest duty RIG for a RON duty to 0 instead of 4
```

