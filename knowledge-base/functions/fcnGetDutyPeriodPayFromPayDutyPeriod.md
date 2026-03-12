# fcnGetDutyPeriodPayFromPayDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyPeriodPayFromPayDutyPeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (aPayDutyPeriod <> null) thenreturn aPayDutyPeriod.dutyPeriodPay.elsereturn null.
```

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

