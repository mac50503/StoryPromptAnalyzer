# fcnCalculateFaaRest

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnCalculateFaaRest`

## Propósito
2/16/2015 US18869 Mitesh P - This function calculates the FAA Rest value by taking the duration from the later of the Last Reserve Release or the Prior Duty Release to the report date time that is passed in.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theRestValues | RestValues | |
| theReportDateTime | DateTime | |

## Lógica de negocio

```blaze
latestRelease is some DateTime.if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is unknown) then {return 10080.} else if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is not unknown) then {latestRelease = theRestValues.priorDutyRelease.} else if (theRestValues.lastReserveRelease is not unknown and theRestValues.priorDutyRelease is unknown) then {latestRelease = theRestValues.lastReserveRelease.} else if (theRestValues.lastReserveRelease is not unknown and theRestValues.priorDutyRelease is not unknown) then {if (theRestValues.lastReserveRelease.isAfter(theRestValues.priorDutyRelease) and (theRestValues.lastReserveRelease.isBefore(theReportDateTime) or theRestValues.priorDutyReleaseUnderReserve = null)) then {latestRelease =  theRestValues.lastReserveRelease.} else {latestRelease =  theRestValues.priorDutyRelease.} }return fcnGetTimeDiffInMinutes(latestRelease, theReportDateTime).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Llamado por

- [fcnCalculateFaaRestForWindowUnderReserve](fcnCalculateFaaRestForWindowUnderReserve.md)

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This function calculates the FAA Rest value by taking the duration from the later of the Last Reserve Release or the Prior Duty Release to the report date time that is passed in.
```

