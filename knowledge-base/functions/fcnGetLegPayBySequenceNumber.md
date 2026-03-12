# fcnGetLegPayBySequenceNumber

## Metadata
- **Tipo**: SRL Function
- **Retorna**: LegPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLegPayBySequenceNumber`

## Propósito
US18085 - Melissa S - 7/29/2014 - Refactored for performance

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| seqNumber | integer | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aTripPay is not equal to null and    aTripPay.dutyPeriodPayList is not equal to null and    aTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do {if (it.legPayList is not equal to null and it.legPayList.size() > 0) then {for each LegPay in it.legPayList as an array of LegPay do {if (it.sequenceNumber is equal to seqNumber) then {return it.}}}}}return null.
```

## Historial de cambios

```
US18085 - Melissa S - 7/29/2014 - Refactored for performance
```

