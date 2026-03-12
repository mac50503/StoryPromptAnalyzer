# fcnGetDutyPeriodPayBySequenceNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DutyPeriodPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyPeriodPayBySequenceNumber`

## Propósito
Ben Lang - 1/30/14 - US15654 - Modified function to use theSequenceNumber instead of sequenceNumber as an input parameter to solve the for each loop ambiguity

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aSequenceNumber | integer | |
| dutyPeriodPayList | List<DutyPeriodPay> | |

## Lógica de negocio

```blaze
returnVal is some DutyPeriodPay initially null.if (dutyPeriodPayList is not equal to null) then {for each DutyPeriodPay in dutyPeriodPayList as an array of DutyPeriodPay do {if (it.sequenceNumber is equal to aSequenceNumber) then {return it.}}}return null.
```

## Historial de cambios

```
Ben Lang - 1/30/14 - US15654 - Modified function to use theSequenceNumber instead of sequenceNumber as an input parameter to solve the for each loop ambiguity
7/24/2014 - Melissa S - Refactored to not initialize a temp return variable.
```

