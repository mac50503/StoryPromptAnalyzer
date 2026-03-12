# fcnGetDutyPeriodPayByIndex

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyPeriodPayByIndex`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPayList | List<DutyPeriodPay> | |
| index | integer | |

## Lógica de negocio

```blaze
retVal is some DutyPeriodPay initially null.if (aDutyPeriodPayList is not equal to null and aDutyPeriodPayList.size() is greater than or equal to (index +1)) then retVal =  aDutyPeriodPayList.get(index).//fcnShow(".....returning from fcnGetDutyPeriodPayByIndex with list = " aDutyPeriodPayList " of size " aDutyPeriodPayList.size() "  and index = " index " with DPP = " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetDutyPeriodPay](fcnGetDutyPeriodPay.md)
- `fcnShow()`

