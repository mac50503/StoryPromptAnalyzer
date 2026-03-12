# fcnGetSumOfLegCreditValues

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetSumOfLegCreditValues`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
sumOfLegCredits is a real initially 0.for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay do{sumOfLegCredits = sumOfLegCredits + it.payValue.}return fcnRoundUpAt2DecimalPlaces(sumOfLegCredits).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

