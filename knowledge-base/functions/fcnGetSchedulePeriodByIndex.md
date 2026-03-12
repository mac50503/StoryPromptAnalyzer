# fcnGetSchedulePeriodByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\fcnGetSchedulePeriodByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodList | List<SchedulePeriod> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theSchedulePeriodList is not equal to null and theSchedulePeriodList.size() > 0) then {if (theSchedulePeriodList.size() is greater than or equal to (index +1)) then return theSchedulePeriodList.get(index).}return null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

