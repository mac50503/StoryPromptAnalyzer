# fcnAdjustTripAndDutyPeriodPayForLDLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAdjustTripAndDutyPeriodPayForLDLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| modifiedLDLegPayValue | real | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| theReportDateTime | DateTime | |
| isLegInSchedulePeriod | boolean | |

## Lógica de negocio

```blaze
fcnShow("Entering fcnAdjustTripAndDutyPeriodPayForLDLeg").fcnAdjustPremiumTripAndDutyPeriodPay(thePayLeg, modifiedLDLegPayValue, theSchedulePeriodPay, theReportDateTime,isLegInSchedulePeriod);fcnShow("Exiting fcnAdjustTripAndDutyPeriodPayForLDLeg").
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAdjustPremiumTripAndDutyPeriodPay](fcnAdjustPremiumTripAndDutyPeriodPay.md)
- `fcnShow()`

