# fcnCalculateCrewMealPerdiumDomesticLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnCalculateCrewMealPerdiumDomesticLegs`

## Propósito
5/06/2024 - Namratha - APIC-1102- Function for Crew meal Perdiem Domestic Legs

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| aGlobalDataCache | GlobalDataCache | |
| qualifiedLegSequenceNumberList | List<String> | |
| aCrewPerdiemMeal | CrewPerDiemMeal | |
| aSchedulePeriodPay | SchedulePeriodPay | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING function fcnCalculateCrewMealPerdiumDomesticLegs with trip " ).mealsPayDomesticCount is an integer initially 0;legCounter is an integer initially 0;aPayLegCurrentDP is some PayLeg initially null.ascheduledBlockTimeInHours is a real initially aCrewPerdiemMeal.scheduledBlockTimeInHours * 60.fcnShow("ScheduledBlockTimeInHours considered for Crew Meal Perdiem Calculation " ascheduledBlockTimeInHours).isAdditionalUseCaseApplicableEffectiveDate is a boolean initially fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(aPayDutyPeriod.reportDateTime, "IF_2025_ADDITIONAL_CREW_MEALS_BLAZE_EFFECTIVE_DATETIME").if(aPayDutyPeriod <> null and aPayDutyPeriod.legList<>null and aPayDutyPeriod.legList.size()>0)then{while(legCounter < aPayDutyPeriod.legList.size()) do{if((aPayDutyPeriod.legList.get(legCounter).nonFlyCode = null as a string oraPayDutyPeriod.legList.get(legCounter).nonFlyCode = "" or aPayDutyPeriod.legList.get(legCounter).nonFlyCode is unknown)) then {if ((fcnIsPayLegDepartureStationInternational(aPayDutyPeriod.legList.get(legCounter) ,aGlobalDataCache) = false ) and (fcnIsPayLegArrrivalStationInternational(aPayDutyPeriod.legList.get(legCounter),aGlobalDataCache) = false)) then {aPayLegCurrentDP = aPayDutyPeriod.legList.get(legCounter). if((fcnGetTimeDiffInMinutes(aPayLegCurrentDP.scheduledDepartureDateTime,aPayLegCurrentDP.scheduledArrivalDateTime ) >= ascheduledBlockTimeInHours) ) then {                                         if (fcnDoesPayLegBeginInSchedulePeriodPay(aPayLegCurrentDP,aSchedulePeriodPay) ) then{if(isAdditionalUseCaseApplicableEffectiveDate and  fcnIsLegWorkCodeInCrewMealExclusionary(aPayLegCurrentDP) = false) then{if( fcnIsDateTimeWithinReportFilterRange(aPayLegCurrentDP.scheduledDepartureDateTime,reportFilterStart,reportFilterEnd)) then {mealsPayDomesticCount+=1.}qualifiedLegSequenceNumberList.add(aPayLegCurrentDP.sequenceNumber as a string).}else if (isAdditionalUseCaseApplicableEffectiveDate = false) then {if( fcnIsDateTimeWithinReportFilterRange(aPayLegCurrentDP.scheduledDepartureDateTime,reportFilterStart,reportFilterEnd)) then {mealsPayDomesticCount+=1.}qualifiedLegSequenceNumberList.add(aPayLegCurrentDP.sequenceNumber as a string).}} }}}legCounter+=1;}}return mealsPayDomesticCount.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnDoesPayLegBeginInSchedulePeriodPay](fcnDoesPayLegBeginInSchedulePeriodPay.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime](fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnIsLegWorkCodeInCrewMealExclusionary](fcnIsLegWorkCodeInCrewMealExclusionary.md)
- [fcnIsPayLegArrrivalStationInternational](fcnIsPayLegArrrivalStationInternational.md)
- [fcnIsPayLegDepartureStationInternational](fcnIsPayLegDepartureStationInternational.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)

## Historial de cambios

```
5/06/2024 - Namratha - APIC-1102- Function for Crew meal Perdiem Domestic Legs
11/11/2024 Namratha-BLAZER-185 -Added Additional Condition Post Effective date for Crew Meal Perdiem Exclusionary Conditions
```

