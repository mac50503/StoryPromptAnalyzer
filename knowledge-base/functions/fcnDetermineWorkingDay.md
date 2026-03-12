# fcnDetermineWorkingDay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineWorkingDay`

## Propósito
07/15/2015 - DE7031 - Melissa S - Moved working days logic from fcnDetermineTripAdditionalTransientTerms.  Updated "R" label from the working days logic.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
// Check to see if the trip or any of its duty periods should count towards working daysdutyIndex is an integer initially 0.dutyPeriod is some LegalityDutyPeriod.lastReserveBlockLabel is a string initially "".if (workingDaysBlockArray <> null and theTrip.isNonFly = false) then {// All days in O and K label trips will count towards working daysif (theTrip.assignmentLabel = (ignoring case) ("O" or "K")) then {fcnAddToWorkingDaysBlockArray(theTrip.beginDateTime, theTrip.endDateTime, workingDaysBlockArray);}// R label trips only count as working days if under a K label Reserve Block.  Since K labels have already been counted, we only need to // check duty periods in an R label trip that extend past the end of the reserve block to see if any additional working days need to be addedif (theTrip.assignmentLabel = (ignoring case) ("R" or "S")) then {if (theTrip.dutyPeriodList <> null) then {dutyIndex = theTrip.dutyPeriodList.size() - 1.// Check to see if the last duty period extends past the end of the reserve blockif (theTrip.dutyPeriodList.get(dutyIndex).associatedReserveBlockDutyPeriod = null) then {// Find the label for the last associated reserve blockwhile (dutyIndex >=0) do {dutyPeriod = theTrip.dutyPeriodList.get(dutyIndex).if (dutyPeriod.associatedReserveBlockDutyPeriod = null) then {// Keep looking until a duty period with an associated reserve block is founddutyIndex = dutyIndex - 1.} else {lastReserveBlockLabel = dutyPeriod.associatedReserveBlockDutyPeriod.legalityTrip.assignmentLabel.// Exit loop once a duty period is found with an associated reserve blockdutyIndex = -1.}}// If the last associated reserve block label is K, add every duty period in the R label trip that extends past the end of the reserve block to the working days listif (lastReserveBlockLabel = (ignoring case) ("K")) then {dutyIndex = theTrip.dutyPeriodList.size() - 1.while (dutyIndex >=0) do {dutyPeriod = theTrip.dutyPeriodList.get(dutyIndex).if (dutyPeriod.associatedReserveBlockDutyPeriod = null) then {fcnAddToWorkingDaysBlockArray(dutyPeriod.reportDateTime, dutyPeriod.releaseDateTime, workingDaysBlockArray);// Keep looking until a duty period with an associated reserve block is founddutyIndex = dutyIndex - 1.} else {// Exit loop once a duty period is found with an associated reserve blockdutyIndex = -1.}}}}}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddToWorkingDaysBlockArray](fcnAddToWorkingDaysBlockArray.md)

## Historial de cambios

```
07/15/2015 - DE7031 - Melissa S - Moved working days logic from fcnDetermineTripAdditionalTransientTerms.  Updated "R" label from the working days logic.
```

