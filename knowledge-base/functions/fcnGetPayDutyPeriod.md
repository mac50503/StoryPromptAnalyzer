# fcnGetPayDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayDutyPeriod`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriodList | List<PayDutyPeriod> | |
| aDutyPeriodCounter | integer | |

## Lógica de negocio

```blaze
if (aPayDutyPeriodList is not equal to null and aPayDutyPeriodList.size() > 0 and aPayDutyPeriodList.size() - 1 >= aDutyPeriodCounter) thenreturn aPayDutyPeriodList.get(aDutyPeriodCounter).elsereturn null.
```

## Llamado por

- [fcnGetPayDutyPeriodByIndex](fcnGetPayDutyPeriodByIndex.md)

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

