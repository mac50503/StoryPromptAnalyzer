# fcnGetSumOfLegPremiumForTripAboveOT

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfLegPremiumForTripAboveOT`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aTripPay <> null and aTripPay.tripPayInflight <> null) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do retVal += fcnGetSumOfLegPremiumAboveOT(it).}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetSumOfLegPremium](fcnGetSumOfLegPremium.md)
- [fcnGetSumOfLegPremiumAboveOT](fcnGetSumOfLegPremiumAboveOT.md)

