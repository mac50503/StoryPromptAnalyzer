# fcnGetLastDutyPeriodPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLastDutyPeriodPay`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay.dutyPeriodPayList is not equal to null and aTripPay.dutyPeriodPayList.size() > 0) then {return aTripPay.dutyPeriodPayList.get(aTripPay.dutyPeriodPayList.size() - 1).} else {return null.}
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

