# fcnFindSchedulePeriodName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnFindSchedulePeriodName`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTripBeginDateTime | DateTime | |
| spList | List<SchedulePeriod> | |

## Lógica de negocio

```blaze
if (spList is not equal to null and spList.size() > 0) then {for each SchedulePeriod in spList as an array of SchedulePeriod do { if (fcnIsDateTimeWithinDateTimeRange(aPayTripBeginDateTime,it.schedulePeriodStart,it.schedulePeriodEnd)) then {return it.schedulePeriodName.}}}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)

## Llamado por

- [fcnInitializePayTripSchedulePeriods](fcnInitializePayTripSchedulePeriods.md)

