# fcnFindSchedulePeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnFindSchedulePeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| spName | string | |
| spList | List<SchedulePeriod> | |

## Lógica de negocio

```blaze
if (spList is not equal to null and spList.size() > 0) then {for each SchedulePeriod in spList as an array of SchedulePeriod do { if (spName is equal to it.schedulePeriodName) then {return it.}}}return null.
```

## Llamado por

- [fcnInitializePayTripSchedulePeriods](fcnInitializePayTripSchedulePeriods.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

