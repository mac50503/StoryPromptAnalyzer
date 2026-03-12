# fcnGetPlnDutyPeriodPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PlnDutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\PlanningPay\Functions\fcnGetPlnDutyPeriodPayByIndex`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPayList | List<PlnDutyPeriodPay> | |
| index | integer | |

## Lógica de negocio

```blaze
retVal is some PlnDutyPeriodPay initially null.if (aDutyPeriodPayList is not equal to null and aDutyPeriodPayList.size() is greater than or equal to (index +1)) then retVal = aDutyPeriodPayList.get(index).return retVal.
```

