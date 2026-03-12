# fcnGetShortDateTimeString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetShortDateTimeString`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime | DateTime | |

## Lógica de negocio

```blaze
if (aDateTime <> unknown and aDateTime <> null) thenreturn DateTimeUtilities.getShortDateTimeString(aDateTime).elsereturn "".
```

## Llamado por

- [fcnAssignSchedulePeriodPayDaysOfService](fcnAssignSchedulePeriodPayDaysOfService.md)
- [fcnBuildUnutilizedReserveList](fcnBuildUnutilizedReserveList.md)
- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)
- [fcnGetDutyIdentificationString](fcnGetDutyIdentificationString.md)
- [fcnInitializeNonflyPayDays](fcnInitializeNonflyPayDays.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

