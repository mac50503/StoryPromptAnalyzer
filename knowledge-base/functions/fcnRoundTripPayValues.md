# fcnRoundTripPayValues

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnRoundTripPayValues`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if aTripPay is not equal to null then{aTripPay.payValue = fcnRoundUpAt2DecimalPlaces(aTripPay.payValue).aTripPay.mdhPayValue = fcnRoundUpAt2DecimalPlaces(aTripPay.mdhPayValue).aTripPay.premiumPayValue = fcnRoundUpAt2DecimalPlaces(aTripPay.premiumPayValue).aTripPay.thisMonthPay = fcnRoundUpAt2DecimalPlaces(aTripPay.thisMonthPay).aTripPay.lastMonthPay = fcnRoundUpAt2DecimalPlaces(aTripPay.lastMonthPay).aTripPay.nextMonthPay = fcnRoundUpAt2DecimalPlaces(aTripPay.nextMonthPay).if (aTripPay.dutyPeriodPayList is not equal to null and aTripPay.dutyPeriodPayList.size() > 0) then{for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{it.payValue = fcnRoundUpAt2DecimalPlaces(it.payValue).it.mdhPayValue = fcnRoundUpAt2DecimalPlaces(it.mdhPayValue).it.premiumPayValue = fcnRoundUpAt2DecimalPlaces(it.premiumPayValue).it.tripExcess = fcnRoundUpAt2DecimalPlaces(it.tripExcess).if (it.legPayList is not equal to null and it.legPayList.size() > 0) then{for each LegPay in it.legPayList as an array of LegPay do{it.payValue = fcnRoundUpAt2DecimalPlaces(it.payValue).}} }} }
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)

