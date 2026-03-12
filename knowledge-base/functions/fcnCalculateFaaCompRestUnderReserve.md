# fcnCalculateFaaCompRestUnderReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnCalculateFaaCompRestUnderReserve`

## Propósito
9/4/2015 - Melissa S - DE7351 - New function

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theRestValues | RestValues | |
| theReportDateTime | DateTime | |

## Lógica de negocio

```blaze
latestRelease is some DateTime.if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is unknown) then {return 10080.} else if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is not unknown) then {latestRelease = theRestValues.priorDutyRelease.} else if (theRestValues.lastReserveRelease is not unknown and theRestValues.priorDutyRelease is unknown) then {latestRelease = theRestValues.lastReserveRelease.} else {// DE7351 - We only want to go back the the prior duty if it was under a Reserve Block.  If not, we will follow the standard logic to take the later of PDR/LRR.if (theRestValues.priorDutyReleaseUnderReserve <> null and theRestValues.priorDutyReleaseUnderReserve <> unknown) then {latestRelease =  theRestValues.priorDutyRelease.} else {if (theRestValues.lastReserveRelease.isAfter(theRestValues.priorDutyRelease)) then {latestRelease =  theRestValues.lastReserveRelease.} else {latestRelease =  theRestValues.priorDutyRelease.}}}return fcnGetTimeDiffInMinutes(latestRelease, theReportDateTime).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
9/4/2015 - Melissa S - DE7351 - New function
9/24/2015 - DE7351 - Melissa S - Added logic to only go back to the prior duty if it was under a reserve block (using new priorDutyReleaseUnderReserve property.
If priorDutyReleaseUnderReserve is not set, comp rest will folow the standard logic of taking the later of the PDR or LRR
```

