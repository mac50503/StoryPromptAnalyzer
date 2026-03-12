# fcnCalculateFaaRestForWindowUnderReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnCalculateFaaRestForWindowUnderReserve`

## Propósito
5/6/2015 - DE6514 -Melissa S - New function for calculating rest under reserves for the 24/7 and 48/7 "window" rules.  These rules will have a different rest value used than the faaRest value

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReportDateTime | DateTime | |
| theAssociatedReserveBlockDutyPeriod | LegalityDutyPeriod | |
| theRestValues | RestValues | |

## Lógica de negocio

```blaze
// If the first reserve trip is before the first reserve block, rest starts at the prior duty releaseif (theAssociatedReserveBlockDutyPeriod.legalityTrip = null and    theAssociatedReserveBlockDutyPeriod.reportDateTime <> null and     theReportDateTime.isBefore(theAssociatedReserveBlockDutyPeriod.reportDateTime)) then {return fcnCalculateFaaRest(theRestValues, theReportDateTime).}// If the lastReserveReport is before the report, it was most likely adjusted for a REST nonflyif (theRestValues.lastReserveRelease is not unknown and theRestValues.lastReserveRelease.isBefore(theReportDateTime)) then {return fcnCalculateFaaRest(theRestValues, theReportDateTime).// If the lastReserveRelease is after the Report, we need to look for the duty in the Reserve Block that ended before the Report to use as the lastReserveRelease instead} else if (theRestValues.priorDutyRelease is not unknown) then {previousReserveBlock is some LegalityDutyPeriod initially theAssociatedReserveBlockDutyPeriod.legalityTrip.getPreviousDutyPeriod(theAssociatedReserveBlockDutyPeriod).if (previousReserveBlock is not null) then {if (previousReserveBlock.releaseDateTime.isAfter(theRestValues.priorDutyRelease)) then {return fcnGetTimeDiffInMinutes(previousReserveBlock.releaseDateTime, theReportDateTime).} else {return fcnGetTimeDiffInMinutes(theRestValues.priorDutyRelease, theReportDateTime).}} else {return fcnCalculateFaaRestPreferLRR(theRestValues, theReportDateTime).}}return -1.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCalculateFaaRest](fcnCalculateFaaRest.md)
- [fcnCalculateFaaRestPreferLRR](fcnCalculateFaaRestPreferLRR.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
5/6/2015 - DE6514 -Melissa S - New function for calculating rest under reserves for the 24/7 and 48/7 "window" rules.  These rules will have a different rest value used than the faaRest value
```

