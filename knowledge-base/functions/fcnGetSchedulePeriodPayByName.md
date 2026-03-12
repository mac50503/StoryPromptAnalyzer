# fcnGetSchedulePeriodPayByName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: SchedulePeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSchedulePeriodPayByName`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSchedulePeriodPayList | List<SchedulePeriodPay> | |
| name | string | |

## Lógica de negocio

```blaze
//fcnShow("===>>>ENTERING function fcnGetSchedulePeriodPayByName ... searching for name: " name).if (aSchedulePeriodPayList is not equal to null and aSchedulePeriodPayList.size() > 0) then{for each SchedulePeriodPay in aSchedulePeriodPayList  as an array of SchedulePeriodPay do {    if (it.schedulePeriodName = (ignoring case) name) then        return it.}}return null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

