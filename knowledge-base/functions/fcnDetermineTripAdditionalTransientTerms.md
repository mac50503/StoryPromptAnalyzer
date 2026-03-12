# fcnDetermineTripAdditionalTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineTripAdditionalTransientTerms`

## Propósito
02/23/2015 - US16635 - Mitesh P - Added logic to set firstAfterReserveBlock.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |
| thePreviousTrip | LegalityTrip | |
| theTripIndex | integer | |
| theTripList | List<LegalityTrip> | |

## Lógica de negocio

```blaze
if (theTrip.tripType = (ignoring case) "R") then {tripIndex is an integer initially theTripIndex+1.breakLoop is a boolean initially false.firstTripAfterReserve is some LegalityTrip.while (breakLoop is false and tripIndex < theTripList.size()) do {firstTripAfterReserve = theTripList.get(tripIndex).if (firstTripAfterReserve.ghostedFlag = false) then {if (firstTripAfterReserve.isNonFly = false or (firstTripAfterReserve.isNonFly = true and fcnNonflyIsForFaaRest(firstTripAfterReserve) = true)) then {if (firstTripAfterReserve.associatedReserveBlockDutyPeriod = null and firstTripAfterReserve.beginDateTime.isAfter(theTrip.endDateTime)) then {firstTripAfterReserve.firstAfterReserveBlock = true.breakLoop = true.} else if (firstTripAfterReserve.associatedReserveBlockDutyPeriod <> null and firstTripAfterReserve.endDateTime.isAfter(theTrip.endDateTime)) then {// DE7266 - For trips after the reserve block that extend past the reserve block, we stop the loop (most likely a reserve trip carrying out - we don't want// the firstTripAfterReserve to be set in this case)// DE7558 - Updated to make sure this only happens when the trip extending past the reserve block is associated with the reserve blockbreakLoop = true.}}}tripIndex+=1.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnNonflyIsForFaaRest](fcnNonflyIsForFaaRest.md)

## Historial de cambios

```
02/23/2015 - US16635 - Mitesh P - Added logic to set firstAfterReserveBlock.
03/08/2015 - US20136 - Melissa S - Removed code for AirportStandby/ReserveBlock association.  The rule associateAirportStandbyToReserveBlock should be used instead
03/08/2015 - US20136 - Melissa S - Removed check for assignmentLabel=R from the logic for next trip following reserve block and switched to check associatedReserveBlockDutyPeriod
03/12/2015 - US20192 - Melissa S - Switched Airport Standby logic to call a common function
03/19/2015 - US20257 - Melissa S - Modified to use nonfly types saved on the trip instead of calling to the decision table again
04/06/2015 - US20466 - Melissa S - Removed Airport Standby from working days array (Minimum Days Off Rule)
04/09/2015 - US20507 - Melissa S - Moved logic for setting priorDayReserveBlock to the ruleset rsAssociateWithReserveBlockDutyPeriods
05/12/2015 - US28484 - Corey Gu - Added firstTripAfterReserve.ghostedFlag = false condition to the if statement.
07/15/2015 - DE7031 - Melissa S - Moved working days logic to fcnDetermineWorkingDay.
8/20/2015 - DE7266 - Melissa S - Added condition when setting firstAfterReserveBlock for reserve trips extending past reserve blocks
10/5/2015 - DE7558 - Melissa S - Updated condition when setting firstAfterReserveBlock for reserve trips extending past reserve blocks to make sure it is only applied when the trip extending past the reserve block is associated with the reserve block
10/21/2015 - DE7558 - Melissa S - Updated condition to make sure that when the next trip after a Reserve Block is a nonfly that is not used for FAA Rest, it gets skipped and we keep checking trips
```

