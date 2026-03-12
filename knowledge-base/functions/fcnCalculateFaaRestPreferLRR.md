# fcnCalculateFaaRestPreferLRR

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnCalculateFaaRestPreferLRR`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theRestValues | RestValues | |
| theReportDateTime | DateTime | |

## Lógica de negocio

```blaze
latestRelease is some DateTime.if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is unknown) then {return 10080.} else if (theRestValues.lastReserveRelease is unknown and theRestValues.priorDutyRelease is not unknown) then {latestRelease = theRestValues.priorDutyRelease.} else if (theRestValues.lastReserveRelease is not unknown) then {latestRelease = theRestValues.lastReserveRelease.}return fcnGetTimeDiffInMinutes(latestRelease, theReportDateTime).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Llamado por

- [fcnCalculateFaaRestForWindowUnderReserve](fcnCalculateFaaRestForWindowUnderReserve.md)

