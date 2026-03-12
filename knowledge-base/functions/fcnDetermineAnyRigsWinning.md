# fcnDetermineAnyRigsWinning

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDetermineRigsWinning`

## Propósito
APIC-1435 Function used in rsDistributeToPremiumPayBuckets - ruleEDDPayAssignment

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isTripRigsGreaterThanPremium is a boolean initially thePayLeg.legPay.dutyPeriodPay.tripPay.tripPayInflight.rigsGreaterThanPremium.isDutyPeriodRigsGreaterThanPremium is a boolean initially thePayLeg.legPay.dutyPeriodPay.rigsGreaterThanPremium.isAnyRigsWinning is a boolean initially  (isTripRigsGreaterThanPremium or isDutyPeriodRigsGreaterThanPremium).fcnShow("Inside fcnDetermineRigsWinning."" ...isTripRigsGreaterThanPremium = " isTripRigsGreaterThanPremium" ...isDutyPeriodRigsGreaterThanPremium = " isDutyPeriodRigsGreaterThanPremium" ... thePayLeg.legPay.sequenceNumber = "thePayLeg.legPay.sequenceNumber" .. isAnyRigsWinning = "isAnyRigsWinning).return isAnyRigsWinning;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnIsPremiumCodeChangeNeeded](fcnIsPremiumCodeChangeNeeded.md)

## Historial de cambios

```
APIC-1435 Function used in rsDistributeToPremiumPayBuckets - ruleEDDPayAssignment
```

