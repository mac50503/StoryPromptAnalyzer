# fcnDetermineCombinedDutyDurationForTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineCombinedDutyDurationForTrip`

## Propósito
12/2/2014 US19124/US19129 Mitesh P - This function determines the different values pertaining to a trip and update the corresponding transient fields in LegalityTrip both for FAA and Contract

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripList | List<LegalityTrip> | |
| tripCounter | integer | |

## Lógica de negocio

```blaze
combinedFAADutyStart is some DateTime.combinedContractDutyStart is some DateTime.theTrip is some LegalityTrip initially theTripList.get(tripCounter).if (theTrip.ghostedFlag = false) then {//FAA Duty Combined - Nonfly / Duty Assignments  if (theTrip.faaDutyStartDateTime <> null and theTrip.restForDuty < 480) then {// Call the fcnFindPreviousTripToCombineForFAADuty using theTripCounter-1 // since we want to start looking for the duty to combine with the PREVIOUS trip, not the one we are calculating duty forcombinedFAADutyStart = fcnFindPreviousTripToCombineForFAADuty(theTripList, tripCounter-1).if combinedFAADutyStart <> null then {theTrip.faaDutyStartDateTime = combinedFAADutyStart.theTrip.faaDutyDuration = fcnGetTimeDiffInMinutes(theTrip.faaDutyStartDateTime, theTrip.faaDutyEndDateTime).}}//Contract Duty Combined    if (theTrip.contDutyStartDateTime <> null and theTrip.restForDuty < 480) then {// Call the fcnFindPreviousTripToCombineForContractDuty using theTripCounter-1 // since we want to start looking for the duty to combine with the PREVIOUS trip, not the one we are calculating duty forcombineForDuty is some CombineForDuty initially a CombineForDuty.apply fcnFindPreviousTripToCombineForContractDuty(theTripList, tripCounter-1, combineForDuty).if combineForDuty.dutyStartDateTime <>  null then {theTrip.contDutyStartDateTime = combineForDuty.dutyStartDateTime.theTrip.contDutyDuration = fcnGetTimeDiffInMinutes(theTrip.contDutyStartDateTime, theTrip.contDutyEndDateTime).theTrip.addContractDutyLabels(combineForDuty.dutyLabels).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnFindPreviousTripToCombineForContractDuty](fcnFindPreviousTripToCombineForContractDuty.md)
- [fcnFindPreviousTripToCombineForFAADuty](fcnFindPreviousTripToCombineForFAADuty.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
12/2/2014 US19124/US19129 Mitesh P - This function determines the different values pertaining to a trip and update the corresponding transient fields in LegalityTrip both for FAA and Contract
12/26/2014 US19126 Mitesh P - Reworked FAA Duty Combined to look further back than just the previous trip
05/12/2015 US20484 Corey Gu - Added if (theTrip.ghostedFlag = false) then statement
1/5/2015 US19132 Mitesh P - Updated for Contract duty
1/28/2015 US19445 Mitesh P - Updated to use class CombineForDuty instead
6/22/2015 - DE6890 - Melissa S - Updated to add the combined trips labels to contractDutyLabels when a combine is done for contract duty
```

