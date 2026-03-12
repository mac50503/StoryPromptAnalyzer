# fcnShowLegPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnShowLegPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
if (debugMode) then{fcnShow("===>>>INSIDE fncShowLegPay... DP count = "  theTripPay.dutyPeriodPayList.size() "   Leg count = "  theTripPay.dutyPeriodPayList.get(0).legPayList.size()).for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{    for each LegPay in it.legPayList as an array of LegPay do    fcnShow("===>>> LegPay " it.sequenceNumber" Base Pay = " it.basePay "   Pay Value = " it.payValue "  Credit Type = " it.creditType " ...Premium Pay Code = " it.premiumPayCode).}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

