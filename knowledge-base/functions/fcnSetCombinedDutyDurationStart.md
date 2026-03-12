# fcnSetCombinedDutyDurationStart

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetCombinedDutyDurationStart`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
rest is an integer initially 0.if (aDutyPeriod <> null) then{fcnShow("===>>> ENTERING fcnSetCombinedDutyDurationStart for DP " aDutyPeriod.sequenceNumber).isRonDuty is a boolean initially false.if (aDutyPeriod.dutyType = (ignoring case)"RON") thenisRonDuty = true.////     SET DEFAULT FOR combinedDurationBeginDateTimeaDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime = aDutyPeriod.reportDateTime.rest = fcnGetTimeDiffInMinutes(aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime, aDutyPeriod.reportDateTime).fcnShow("===>>> setting DP " aDutyPeriod.sequenceNumber "'s DEFAULT combinedDurationBeginDateTime to its report of " aDutyPeriod.reportDateTime).////     HANDLE ADJUSTING THE FIRST DUTY PERIOD DURATION WHEN TRIP IS ASSOCIATED WITH AN AIRPORT STANDBYanAirportStanby is some PayTrip initially aDutyPeriod.payTrip.associatedAirportStandby.if (anAirportStanby <> null and                   aDutyPeriod = aDutyPeriod.payTrip.firstDutyPeriod and                   anAirportStanby.beginDateTime.isBefore(aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime)) then{aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime = anAirportStanby.beginDateTime.rest = fcnGetTimeDiffInMinutes(aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime, aDutyPeriod.reportDateTime).fcnShow("===>>> setting DP " aDutyPeriod.sequenceNumber "'s combinedDurationBeginDateTime to its airport standby begin time of  " anAirportStanby.beginDateTime " ...rest = " rest).}////     HANDLE ADJUSTING THE DUTY PERIOD DURATIONS WHEN THE DUTY PERIODS IN THE SAME TRIP HAVE LESS THAN 8 HOURS REST BETWEEN THEMaReserveBlockDutyPeriod is some PayDutyPeriod initially null.if (isRonDuty = false and                                                                   //// DO NOT COMBINE DUTY DURATIONS FOR RON DUTY PERIODS...      aDutyPeriod <> aDutyPeriod.payTrip.firstDutyPeriod) then{index is an integer initially aDutyPeriod.payTrip.dutyPeriodList.indexOf(aDutyPeriod).fcnShow("===>>>in code block for non-first DP... index = " index " ...total duties in trip = " aDutyPeriod.payTrip.dutyPeriodList.size()).prevDutyPeriod is some PayDutyPeriod initially null.continue is a boolean initially true.while continue = true do {prevDutyPeriod = null.index -= 1.fcnShow("===>>> index now = " index).if (index >= 0 and index <= aDutyPeriod.payTrip.dutyPeriodList.size() - 1) then{prevDutyPeriod = aDutyPeriod.payTrip.dutyPeriodList.get(index).rest = fcnGetTimeDiffInMinutes(prevDutyPeriod.releaseDateTime, aDutyPeriod.reportDateTime).fcnShow("===>>> found previous duty period " prevDutyPeriod.sequenceNumber " ...rest = " rest).if (continue and                                                                prevDutyPeriod <> null and                                                 fcnDutyContainsAllNonPaidLimos(prevDutyPeriod) = false and     prevDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime.isBefore(aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime) and                   rest < 480) then{aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime = prevDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime.fcnShow("===>>> setting DP " aDutyPeriod.sequenceNumber "'s combinedDurationBeginDateTime to its prev duty period combinedDurationBeginDateTime of  " prevDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime " ...rest = " rest).}if (rest >= 480) thencontinue = false.}elsecontinue = false.}}////     HANDLE ADJUSTING THE DUTY PERIOD DURATION WHEN THE DUTY PERIOD IS THE FIRST DUTY IN THE TRIP AND////     THE FIRST LEG IN THE DUTY IS AN RS DEADHEADif (aDutyPeriod.payTrip.firstDutyPeriod = aDutyPeriod and //// THIS DP IS THE FIRST DP IN THE TRIP        aDutyPeriod.firstLeg <> null and              aDutyPeriod.firstLeg.isDeadhead = true and          aDutyPeriod.firstLeg.legWorkCodeList.contains("RS")) then{aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime  = aDutyPeriod.firstLeg.scheduledDepartureDateTime.minusMinutes(aDutyPeriod.variableReportMinutes).fcnShow("===>>> fcnSetCombinedDutyDurationStart ...trip " aDutyPeriod.payTrip.tripNameAndDate " ...DP " aDutyPeriod.sequenceNumber " start time of combined duty duration = first leg skd dep of " aDutyPeriod.firstLeg.scheduledDepartureDateTime " - variable report minutes of " aDutyPeriod.variableReportMinutes " = " aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime).}}fcnShow("===>>> EXITING fcnSetCombinedDutyDurationStart with combinedDurationBeginDateTime for DP " aDutyPeriod.sequenceNumber " = " aDutyPeriod.payDutyPeriodInflight.combinedDurationBeginDateTime).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDutyContainsAllNonPaidLimos](fcnDutyContainsAllNonPaidLimos.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

