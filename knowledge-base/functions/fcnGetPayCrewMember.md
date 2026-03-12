# fcnGetPayCrewMember

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayCrewMember
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayCrewMember`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayCrewMemberLine | PayCrewMemberLine | |
| theSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
if (theSchedulePeriodPay is not equal to null and    thePayCrewMemberLine is not equal to null and     thePayCrewMemberLine.crewMemberList is not equal to null and     thePayCrewMemberLine.crewMemberList.size() > 0) then{for each PayCrewMember in thePayCrewMemberLine.crewMemberList as an array of PayCrewMember do {if (it.schedulePeriodName is equal to theSchedulePeriodPay.schedulePeriodName) thenreturn it.}}return null.
```

## Llamado por

- [fcnCalculateLongevityBucket](fcnCalculateLongevityBucket.md)
- [fcnCreateCrewPayResponse](fcnCreateCrewPayResponse.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

