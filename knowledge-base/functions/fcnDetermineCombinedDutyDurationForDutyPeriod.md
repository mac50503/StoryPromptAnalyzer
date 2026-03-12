# fcnDetermineCombinedDutyDurationForDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineCombinedDutyDurationForDutyPeriod`

## Propósito
12/26/2014 US19126 Mitesh P - This function should determine the different values pertaining to a flight duty period and update the corresponding fields.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | LegalityDutyPeriod | |
| dutyPeriodCounter | integer | |
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
combinedFAADutyStart is some DateTime.combinedContractDutyStart is some DateTime.// FAA // 1st Duty Period In Trip and has FAA Duty and < 8 hours rest for dutyif (dutyPeriodCounter = 0 and theTripList <> unknown and theDutyPeriod.faaDutyStartDateTime <> unknown and theDutyPeriod.faaDutyStartDateTime <> null and theDutyPeriod.restForDuty < 480) then {// Call the fcnFindPreviousTripToCombineForFAADuty using theTripCounter-1 // since we want to start looking for the duty to combine with the PREVIOUS trip, not the one we are calculating duty forcombinedFAADutyStart = fcnFindPreviousTripToCombineForFAADuty(theTripList, tripCounter-1).if combinedFAADutyStart <> null then {theDutyPeriod.faaDutyStartDateTime = combinedFAADutyStart.theDutyPeriod.faaDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.faaDutyStartDateTime, theDutyPeriod.faaDutyEndDateTime).}}// Not 1st Duty Period in Trip and has FAA Duty and < 8 hours rest for dutyif (dutyPeriodCounter > 0 and theDutyPeriod.faaDutyStartDateTime <> unknown and theDutyPeriod.faaDutyStartDateTime <> null and theDutyPeriod.restForDuty < 480) then {// Call the function using theDutyPeriodCounter-1 since we want to start looking for the duty to combine with the PREVIOUS Duty Period, not the one  we are calculating duty forcombinedFAADutyStart = fcnFindPreviousDutyToCombineForFAADuty(theTripList, tripCounter, dutyPeriodCounter - 1).if combinedFAADutyStart <> null then {theDutyPeriod.faaDutyStartDateTime = combinedFAADutyStart.theDutyPeriod.faaDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.faaDutyStartDateTime, theDutyPeriod.faaDutyEndDateTime).}}//Contract // Initialize the Duty Period’s contractDutyLegs list with the legs in the existing DutyPeriod.theDutyPeriod.addContractDutyLegs(theDutyPeriod.legList).// 1st Duty Period In Trip and has Contract Duty and < 8 hours rest for dutyif (dutyPeriodCounter = 0 and theTripList <> unknown and theDutyPeriod.contDutyStartDateTime <> null and theDutyPeriod.restForDuty < 480) then {// Call the fcnFindPreviousTripToCombineForContractDuty using theTripCounter-1 // since we want to start looking for the duty to combine with the PREVIOUS trip, not the one we are calculating duty forcombineForDuty is some CombineForDuty initially a CombineForDuty.apply fcnFindPreviousTripToCombineForContractDuty(theTripList, tripCounter-1, combineForDuty).if (combineForDuty.dutyStartDateTime <> unknown and combineForDuty.dutyStartDateTime <> null) then {theDutyPeriod.addContractDutyLegs(combineForDuty.dutyLegs).theDutyPeriod.legalityTrip.addContractDutyLabels(combineForDuty.dutyLabels).theDutyPeriod.contDutyStartDateTime = combineForDuty.dutyStartDateTime.theDutyPeriod.contDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.contDutyStartDateTime, theDutyPeriod.contDutyEndDateTime).}}// Not 1st Duty Period in Trip and has Contract Duty and < 8 hours rest for dutyif (dutyPeriodCounter > 0 and theDutyPeriod.contDutyStartDateTime <> null and theDutyPeriod.restForDuty < 480) then {// Call the function using theDutyPeriodCounter-1 since we want to start looking for the duty to combine with the PREVIOUS Duty Period, not the one we are calculating duty forcombineForDuty is some CombineForDuty initially a CombineForDuty.apply fcnFindPreviousDutyToCombineForContractDuty(theTripList, tripCounter, dutyPeriodCounter - 1, combineForDuty).if (combineForDuty.dutyStartDateTime <> unknown and combineForDuty.dutyStartDateTime <> null) then {theDutyPeriod.addContractDutyLegs(combineForDuty.dutyLegs).theDutyPeriod.legalityTrip.addContractDutyLabels(combineForDuty.dutyLabels).theDutyPeriod.contDutyStartDateTime = combineForDuty.dutyStartDateTime.theDutyPeriod.contDutyDuration = fcnGetTimeDiffInMinutes(theDutyPeriod.contDutyStartDateTime, theDutyPeriod.contDutyEndDateTime).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousDutyToCombineForContractDuty](fcnFindPreviousDutyToCombineForContractDuty.md)
- [fcnFindPreviousDutyToCombineForFAADuty](fcnFindPreviousDutyToCombineForFAADuty.md)
- [fcnFindPreviousTripToCombineForContractDuty](fcnFindPreviousTripToCombineForContractDuty.md)
- [fcnFindPreviousTripToCombineForFAADuty](fcnFindPreviousTripToCombineForFAADuty.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
12/26/2014 US19126 Mitesh P - This function should determine the different values pertaining to a flight duty period and update the corresponding fields.
12.30.2104 Melissa S - Fixed errors caused by a null tripList (for the trip legality check)
1/5/2014 US19132 Mitesh P - Updated for Contract duty
1/28/2015 US19445 Mitesh P - Updated to use class CombineForDuty instead
6/22/2015 - DE6890 - Melissa S - Updated to add the combined trips labels to contractDutyLabels when a combine is done for contract duty
```

