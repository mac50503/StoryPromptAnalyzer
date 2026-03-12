# fcnAddToDutyPeriodSumOfLegPremimum

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAddToDutyPeriodSumOfLegPremimum`

## Propósito
09/22/2017 - Tim A. - added analytics data

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
if (aLegPay <> null and     aLegPay.dutyPeriodPay <> null and    aLegPay.basePay < aLegPay.payValue) then{premAmt is a real initially (aLegPay.payValue - aLegPay.basePay).premAmt = fcnRoundUpAt2DecimalPlaces(premAmt).if (aLegPay.legPayInflightAnalytics <> null) thenaLegPay.legPayInflightAnalytics.premiumTfp = premAmt.aLegPay.dutyPeriodPay.sumLegPremiumCredits += premAmt.aLegPay.dutyPeriodPay.sumLegPremiumCredits = fcnRoundUpAt2DecimalPlaces(aLegPay.dutyPeriodPay.sumLegPremiumCredits).fcnShow("For duty period that reports on " aLegPay.dutyPeriodPay.reportDateTime "... Adding " (aLegPay.payValue - aLegPay.basePay) " to sumLegPremiumCredits which now equals " aLegPay.dutyPeriodPay.sumLegPremiumCredits).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
09/22/2017 - Tim A. - added analytics data
```

