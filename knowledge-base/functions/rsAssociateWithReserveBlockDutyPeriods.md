# rsAssociateWithReserveBlockDutyPeriods

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Rulesets\rsAssociateWithReserveBlockDutyPeriods`

## Propósito
02/16/2015 - US18869 - Mitesh P - This ruleset  is used to make an association between a nonfly trip and a Reserve Block’s Duty Period, or a flying Trip and a Reserve Block Duty Period

## Historial de cambios

```
02/16/2015 - US18869 - Mitesh P - This ruleset  is used to make an association between a nonfly trip and a Reserve Block’s Duty Period, or a flying Trip and a Reserve Block Duty Period
03/09/2015 - US20136 - Melissa S - Updates for anyReserveTrip to not look for assignmentLabel=R.  Any flying trip that starts the same SWA day and has an overlap should be considered for a reserve trip
03/12/2015 - US20192 - Melissa S - Updated to use a common function for determining if a nonfly code is an airport standby
03/19/2015 - US20257 - Melissa S - Modified to use nonfly types save on the trip
04/09/2015 - US20507 - Melissa S - Moved logic for setting priorDayReserveBlock from the function fcnDetermineTripAdditionalTransientTerms
05/04/2015 - US20172 - Mitesh P - Add all the reserve Block duty periods to ReserveBlockDutyPeriodList
05/12/2013 - US20484 Corey Gu - Added it.ghostedFlag=false condition to anyReserveBlockTrip and anyTrip patterns.
6/17/2015 - DE6832 - Melissa S -Added associateReserveTripDutyPeriodToReserveBlock - for the 48 in 7 rule, we also need to know what Reserve Block a duty period in a Reserve Trip is associated with.
8/4/2015 - DE7155 - Melissa S - Added setting associatedReserveTripDutyEndDateTime
10/9/2015 - Performance - Melissa S - Moved logic for the rule addToReserveBlockDutyPeriodList from here to rsBuildReserveLists, so that theReserveBlockDutyPeriods list can be used in the rules here
10/9/2015 - Performance - Melissa S - Refactored rules to fire using the theReserveBlockDutyPeriods list, and the new properties reportDateTimeSwaDay and beginDateTimeSwaDay
```

