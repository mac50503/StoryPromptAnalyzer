# fcnCalculateDutyPeriodRig

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateDutyPeriodRig`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
dutyRig is a real initially 0.0.if (aDutyPeriodPay <> null and     aDutyPeriodPay.payValue - aDutyPeriodPay.sumLegTotalCredits > 0.0) then{dutyRig = aDutyPeriodPay.payValue - aDutyPeriodPay.sumLegTotalCredits.dutyRig = fcnRoundUpAt2DecimalPlaces(dutyRig).aDutyPeriodPay.dutyPeriodRig = dutyRig.fcnShow("===>>> setting DP " aDutyPeriodPay.sequenceNumber  "'s dutyPeriodRig to " dutyRig).if (aDutyPeriodPay.dutyPeriodPayInflightAnalytics <> null) then{aDutyPeriodPay.dutyPeriodPayInflightAnalytics.dutyRigTfp = aDutyPeriodPay.dutyPeriodRig.}}return dutyRig.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

