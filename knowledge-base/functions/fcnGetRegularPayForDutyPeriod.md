# fcnGetRegularPayForDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetRegularPayForDutyPeriod`

## Propósito
Ben Lang - DE7435 - Returns the amount to distribute to the regular buckets for forced trips

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriodPay | DutyPeriodPay | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if ((theDutyPeriodPay.proratedPay - theDutyPeriodPay.distributedPay) <= (theDutyPeriodPay.tripPay.thisMonthPay - theDutyPeriodPay.tripPay.distributedPay)) then {fcnShow("===>>> in fcnGetRegularPayForDutyPeriod ... theDutyPeriodPay.proratedPay - theDutyPeriodPay.distributedPay = " theDutyPeriodPay.proratedPay " - " theDutyPeriodPay.distributedPay).retVal = theDutyPeriodPay.proratedPay - theDutyPeriodPay.distributedPay.}else{fcnShow("===>>> in fcnGetRegularPayForDutyPeriod ... theDutyPeriodPay.tripPay.thisMonthPay - theDutyPeriodPay.tripPay.distributedPay = " theDutyPeriodPay.tripPay.thisMonthPay " - " theDutyPeriodPay.tripPay.distributedPay).retVal = theDutyPeriodPay.tripPay.thisMonthPay - theDutyPeriodPay.tripPay.distributedPay.}retVal = math().max(0.0, retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang - DE7435 - Returns the amount to distribute to the regular buckets for forced trips
```

