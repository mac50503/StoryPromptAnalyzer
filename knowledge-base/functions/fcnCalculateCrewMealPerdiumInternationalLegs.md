# fcnCalculateCrewMealPerdiumInternationalLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateCrewMealPerdiumInternationalLegs`

## Propósito
5/06/2024 - Namratha- APIC-1102- Function for Crew meal Perdiem International Legs

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLegCurrentDP | PayLeg | |
| aPayLegPreviousDP | PayLeg | |
| aGlobalDataCache | GlobalDataCache | |
| qualifiedLegSequenceNumberList | List<String> | |
| aCrewPerdiemMeal | CrewPerDiemMeal | |
| aSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING function fcnCalculateCrewMealPerdiumInternationalLegs with trip ").mealsPayInternationalCount is an integer initially 0;ascheduledBlockTimeInHours is a real initially aCrewPerdiemMeal.scheduledBlockTimeInHours * 60.isCurrentLegInReportPeriod  is a boolean initially false.isPrevLegInReportPeriod  is a boolean initially false.isCurrentLegInSchedPeriod  is a boolean initially false.isPrevLegInSchedPeriod  is a boolean initially false.if(fcnDoesPayLegBeginInSchedulePeriodPay(aPayLegCurrentDP,aSchedulePeriodPay)) then{isCurrentLegInSchedPeriod = true.} if(fcnDoesPayLegBeginInSchedulePeriodPay(aPayLegPreviousDP,aSchedulePeriodPay)) then{isPrevLegInSchedPeriod = true.} if(fcnIsDateTimeWithinReportFilterRange(aPayLegCurrentDP.scheduledDepartureDateTime,reportFilterStart,reportFilterEnd) )then{isCurrentLegInReportPeriod= true.}if(fcnIsDateTimeWithinReportFilterRange(aPayLegPreviousDP.scheduledDepartureDateTime,reportFilterStart,reportFilterEnd) )then{isPrevLegInReportPeriod= true.}if (fcnIsPayLegDepartureStationInternational(aPayLegCurrentDP,aGlobalDataCache) and fcnIsPayLegArrrivalStationInternational(aPayLegPreviousDP,aGlobalDataCache)) then {if((fcnGetTimeDiffInMinutes(aPayLegCurrentDP.scheduledDepartureDateTime, aPayLegCurrentDP.scheduledArrivalDateTime) >= ascheduledBlockTimeInHours) and isCurrentLegInSchedPeriod)then{if(isCurrentLegInReportPeriod) then {mealsPayInternationalCount += 1.}                                                       qualifiedLegSequenceNumberList.add(aPayLegCurrentDP.sequenceNumber as a string).}if((fcnGetTimeDiffInMinutes(aPayLegPreviousDP.scheduledDepartureDateTime, aPayLegPreviousDP.scheduledArrivalDateTime) >= ascheduledBlockTimeInHours) and isPrevLegInSchedPeriod)then{if(isPrevLegInReportPeriod) then{mealsPayInternationalCount += 1.}                                           qualifiedLegSequenceNumberList.add(aPayLegPreviousDP.sequenceNumber as a string).}}return mealsPayInternationalCount.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)
- [fcnDoesPayLegBeginInSchedulePeriodPay](fcnDoesPayLegBeginInSchedulePeriodPay.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnIsPayLegArrrivalStationInternational](fcnIsPayLegArrrivalStationInternational.md)
- [fcnIsPayLegDepartureStationInternational](fcnIsPayLegDepartureStationInternational.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateCrewMealPerdiumInternational](fcnCalculateCrewMealPerdiumInternational.md)

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102- Function for Crew meal Perdiem International Legs
```

