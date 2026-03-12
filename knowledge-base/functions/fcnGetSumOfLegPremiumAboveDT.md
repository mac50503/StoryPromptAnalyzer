# fcnGetSumOfLegPremiumAboveDT

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfLegPremiumAboveDT`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aDutyPeriodPay <> null and     aDutyPeriodPay.legPayList <> null and     aDutyPeriodPay.legPayList.size() > 0) then{for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay doretVal += math().max(0, it.payValue - fcnRoundUpAt2DecimalPlaces(it.basePay * 2.0)).}retVal = fcnRoundUpAt2DecimalPlaces(retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

## Llamado por

- [fcnGetSumOfLegPremiumForTripAboveDT](fcnGetSumOfLegPremiumForTripAboveDT.md)

