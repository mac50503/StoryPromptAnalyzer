# fcnAllLabelsInWindow

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnAllLabelsInWindow`

## Propósito
04/23/2015 Corey Gu US16626 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| windowStartDateTime | DateTime | |
| windowEndDateTime | DateTime | |
| tripList | List<LegalityTrip> | |
| tripIndex | integer | |

## Lógica de negocio

```blaze
prvDutyIndex is a integer initially 0.prvTripIndex is a integer initially tripIndex.aTrip is some LegalityTrip.aDutyPeriod is some LegalityDutyPeriod. // Loop backwards through the tripList starting with the tripIndexwhile (prvTripIndex >= 0) do {aTrip = tripList.get(prvTripIndex).// Ghosted trips should be skipped completely as if they weren't on the board - they should have no effect on this logicif (aTrip.ghostedFlag = false) then {if (aTrip.isNonFly = false) then {// if the trip is not a Nonfly – check for the necessary label, and check each duty period to see if it is in the windowprvDutyIndex = aTrip.dutyPeriodList.size() - 1.while (prvDutyIndex >= 0) do {aDutyPeriod = aTrip.dutyPeriodList.get(prvDutyIndex).if (aDutyPeriod.reportDateTime.isEqual(windowStartDateTime) or aDutyPeriod.reportDateTime.isAfter(windowStartDateTime)) then { if (aDutyPeriod.legalityTrip <> null and  ((aDutyPeriod.legalityTrip.assignmentLabel = (ignoring case) ("O" or "J" or "K") ) or     (aDutyPeriod.legalityTrip.assignmentLabel = (ignoring case) ("R" or "S") and // Reserve Trip starts under a K label Reserve Block(aDutyPeriod.legalityTrip.associatedReserveBlockDutyPeriod <> null and aDutyPeriod.legalityTrip.associatedReserveBlockDutyPeriod.legalityTrip <> null and aDutyPeriod.legalityTrip.associatedReserveBlockDutyPeriod.legalityTrip.assignmentLabel = (ignoring case) "K") and// Duty Period is either not under a reserve block, or it is also under a K label reserve block (DE6832)(aDutyPeriod.associatedReserveBlockDutyPeriod = null or  (aDutyPeriod.associatedReserveBlockDutyPeriod <> null and aDutyPeriod.associatedReserveBlockDutyPeriod.legalityTrip <> null and aDutyPeriod.associatedReserveBlockDutyPeriod.legalityTrip.assignmentLabel = (ignoring case) "K"))   )) ) then {prvDutyIndex = prvDutyIndex -1.} else {return false.}} else { // Since the trips/duty periods are received in DateTime order, once we find one trip/duty period that starts outside the window, // all previous ones will also start outside the window. So we can stop looking.prvDutyIndex = -1.prvTripIndex = -1.}}}}prvTripIndex = prvTripIndex - 1.}// If no conditions have caused a false to be returned, then all labels are ok, and true should be returnedreturn true.
```

## Historial de cambios

```
04/23/2015 Corey Gu US16626 - Initial development
05/12/2015 Corey Gu - US20484 - Added (aTrip.ghostedFlag = false) condition.
5/22/2015 - DE6701 - Melissa S - Added check for nonfly trips against the window to avoid returning flase for a nonfly that isn't even in the window
6/17/2015 - DE6832 - Melissa S - Modified to also look at the DutyPeriods in the R label trip.  They either have to be under a K label, or not under a Reserve Block (carry out)
8/4/2015 - DE7164 - Modified to not look at nonflies in the window - they should be ignored
```

