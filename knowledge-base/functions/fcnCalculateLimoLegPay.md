# fcnCalculateLimoLegPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateLimoLegPay`

## Propósito
US20939 -

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.block is an integer initially 0.adjustedBlock is an integer initially 0.if (aLegPay <> null and     aLegPay.payLeg <> null) then{block = fcnGetTimeDiffInMinutes(aLegPay.payLeg.determineBestDepartureDateTimeNoEstimated(), aLegPay.payLeg.determineBestArrivalDateTimeNoEstimated()).if (block > 0) then{retVal = 1.0.adjustedBlock = block - 120.if (adjustedBlock >= 6) thenretVal += (0.1 * math().truncate(adjustedBlock  /  6)).}}//fcnShow("===>>> in fcnCalculateLimoLegPay with leg " aLegPay.sequenceNumber " ...block = " block " ...dep station = " aLegPay.payLeg.departureLocation " ...arr station = " aLegPay.payLeg.arrivalLocation " ...returning " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- `fcnShow()`

## Historial de cambios

```
US20939 -
If my Leg's isLIMO Flag = TRUE and
my Leg's Arrival Station &lt;&gt;  my Leg's Departure Station  then
return 1. 0 TFP for first 2 hours plus 0.1 TFP for each incremental 6 minutes
6/1/2015 - US20939 - Melissa S - Changed to use best available times instead of actual only
```

