# fcnGetPayDutyPeriodByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayDutyPeriodByIndex`

## Propósito
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriodList | List<PayDutyPeriod> | |
| index | integer | |

## Lógica de negocio

```blaze
retVal is some PayDutyPeriod initially null.if (aPayDutyPeriodList is not equal to null and aPayDutyPeriodList.size() is greater than or equal to (index +1)) then retVal =  aPayDutyPeriodList.get(index).//fcnShow(".....returning from fcnGetPayDutyPeriodByIndex with list = " aPayDutyPeriodList " of size " aPayDutyPeriodList.size() " and index = " index " with PDP = " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetPayDutyPeriod](fcnGetPayDutyPeriod.md)
- `fcnShow()`

## Historial de cambios

```
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

