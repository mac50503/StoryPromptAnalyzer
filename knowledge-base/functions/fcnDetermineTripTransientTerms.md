# fcnDetermineTripTransientTerms

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineTripTransientTerms`

## Propósito
11/27/2014 - US18673 - Mitesh P - This function should determine the different values pertaining to a Nonfly Trip that will be reused throughout the rules.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | LegalityTrip | |

## Lógica de negocio

```blaze
theTrip.isNonFly = false.theTrip.isDutyNonFly = false.if(theTrip.languageMap = null) then{theTrip.languageMap= a LinkedHashMap;}// US20562 - Reserve trips have "/" in the name but we want to remove this for IFif (theTrip.tripName is not null and theTrip.tripName.indexOf("/") >= 0) then {theTrip.tripName = theTrip.tripName.substring(0, theTrip.tripName.indexOf("/")).}// Calculate trip's duration report to releasetheTrip.durationBeginToEnd = Duration.newInstance(theTrip.beginDateTime, theTrip.endDateTime).toStandardMinutes().minutes.// Determine the SWA Day/Time for the trip's begin and each duty period in the trip's reportif (theTrip.beginDateTime <> null) then {theTrip.beginDateTimeSwaDay = fcnGetSWADayStart(theTrip.beginDateTime).}if (theTrip.dutyPeriodList <> null) then {for each LegalityDutyPeriod in theTrip.dutyPeriodList as an array of LegalityDutyPeriod do {it.legalityTrip = theTrip.it.reportDateTimeSwaDay = fcnGetSWADayStart(it.reportDateTime).// Determine languages on a Tripif (it.legList <> null ) then {for each LegalityLeg in it.legList as an array of LegalityLeg do {if(it.isDeadhead = false and it.languageCode <> null and theTrip.languageMap.containsKey(it.languageCode) = false) then{ //Only consider languages on active legs that have not already been put in the trip's language maptheTrip.languageMap.put(it.languageCode, it);}}}}}if (theTrip.nonFlyCode <> null and theTrip.nonFlyCode <> unknown and theTrip.nonFlyCode <> "") then {theTrip.isNonFly = true.// US20257 - Save Nonfly Types on the Trip so that the decision table doesn’t have to be called over and over, and so that this check can be done in rule conditions theTrip.isMiscNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Misc).theTrip.isTrainingNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Training).theTrip.isMiscTrainingNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Misc_Training).theTrip.isMiscWorkingNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Misc_Working).theTrip.isConflictNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Conflict).theTrip.isContractualConflictNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Contractual_Conflict).theTrip.isSickNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Sick).theTrip.isAirportStandbyNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Airport_Standby).theTrip.isTrainingQualNonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.Training_Qualification).theTrip.isETONonFly = fcnNonflyIsNonflyType(theTrip.nonFlyCode, NonflyCodeType.ETO).if (fcnNonflyIsForFaaDuty(theTrip)) then {theTrip.isDutyNonFly = true.// FAA Duty (Nonfly trips)theTrip.faaDutyStartDateTime = theTrip.beginDateTime.theTrip.faaDutyEndDateTime = theTrip.endDateTime.theTrip.faaDutyDuration =  fcnGetTimeDiffInMinutes(theTrip.faaDutyStartDateTime, theTrip.faaDutyEndDateTime).// Contract Duty (Nonfly trips)if (theTrip.tripClass <> ("C" and "L")) then {theTrip.contDutyStartDateTime = theTrip.beginDateTime.theTrip.contDutyEndDateTime = theTrip.endDateTime.theTrip.contDutyDuration =  fcnGetTimeDiffInMinutes(theTrip.contDutyStartDateTime, theTrip.contDutyEndDateTime).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSWADayStart](fcnGetSWADayStart.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [fcnNonflyIsForFaaDuty](fcnNonflyIsForFaaDuty.md)
- [fcnNonflyIsNonflyType](fcnNonflyIsNonflyType.md)

## Historial de cambios

```
11/27/2014 - US18673 - Mitesh P - This function should determine the different values pertaining to a Nonfly Trip that will be reused throughout the rules.
12/12/2015 - US19048 - Mitesh P - Added condition for Contract Duty.
03/12/2015 - US20192 - Melissa S - Switched logic for looking up the nonfly code to use new function/new decision table
03/19/2015 - US20257 - Melissa S - Added setting of nonfly types on the trip
03/25/2015 - US16631 - Melissa S - Modified to set durationBeginToEnd
04/01/2015 - US20434 - Melissa S - Modified Airport Standby list to come from the Nonfly decision table based on Nonfly type Airport_Standby
04/08/2015 - US20485- Melissa S - Added setting isTrainingQualNonFly
04/14/2015 - US20562 - Melissa S - Added logic to remove "/#" from the trip name
10/9/2015 - Performance - Melissa S - Added setting Trip's beginDateTimeSwaDay and Duty Period's reportDateTimeSwaDay and legalityTrip
```

