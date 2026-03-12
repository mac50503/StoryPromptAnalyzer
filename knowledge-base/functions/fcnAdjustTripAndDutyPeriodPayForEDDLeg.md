# fcnAdjustTripAndDutyPeriodPayForEDDLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAdjustTripAndDutyPeriodPayForEDDLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| modifiedEDDLegPayValue | real | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| theReportDateTime | DateTime | |
| isLegInSchedulePeriod | boolean | |

## Lógica de negocio

```blaze
fcnShow("Entering fcnAdjustTripAndDutyPeriodPayForEDDLeg").fcnAdjustPremiumTripAndDutyPeriodPay(thePayLeg, modifiedEDDLegPayValue, theSchedulePeriodPay, theReportDateTime,isLegInSchedulePeriod);fcnShow("Exiting fcnAdjustTripAndDutyPeriodPayForEDDLeg").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAdjustPremiumTripAndDutyPeriodPay](fcnAdjustPremiumTripAndDutyPeriodPay.md)
- `fcnShow()`

