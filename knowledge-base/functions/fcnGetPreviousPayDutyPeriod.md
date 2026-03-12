# fcnGetPreviousPayDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPreviousPayDutyPeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodList | List<PayDutyPeriod> | |
| aDutyPeriodCounter | integer | |

## Lógica de negocio

```blaze
//fcnShow("===>>>ENTERING fcnGetPreviousPayDutyPeriod").if (aDutyPeriodCounter > 0 and aDutyPeriodList <> null and aDutyPeriodList.size() > 1) thenreturn aDutyPeriodList.get(aDutyPeriodCounter-1).elsereturn null.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateStartOfRestForPay](fcnCalculateStartOfRestForPay.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

