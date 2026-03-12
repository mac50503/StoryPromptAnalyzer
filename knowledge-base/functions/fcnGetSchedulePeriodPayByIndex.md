# fcnGetSchedulePeriodPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodPayByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPayList | List<SchedulePeriodPay> | |
| index | integer | |

## Lógica de negocio

```blaze
if (theSchedulePeriodPayList is not equal to null) then {if (theSchedulePeriodPayList.size() is greater than or equal to (index +1)) then return theSchedulePeriodPayList.get(index).}return null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

