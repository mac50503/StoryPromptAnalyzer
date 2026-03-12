# fcnGetRegularPayForLegInForcedDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetRegularPayForLegInForcedDutyPeriod`

## Propósito
Ben Lang - DE7501 - Returns the amount to distribute to the regular buckets for forced duty periods

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegPay | LegPay | |

## Lógica de negocio

```blaze
//fcnShow("===>>> entering fcnGetRegularPayForLegInForcedDutyPeriod for leg " fcnGetFlightLegDisplayString(theLegPay.payLeg)).retVal is a real initially 0.0.fcnShow("Entering fcnGetRegularPayForLegInForcedDutyPeriod "" ...theLegPay.sequenceNumber = "theLegPay.sequenceNumber" ...theLegPay.payValue = "theLegPay.payValue" ...  theLegPay.dutyPeriodPay.distributedPay = " theLegPay.dutyPeriodPay.distributedPay" ... theLegPay.dutyPeriodPay.payValue = "theLegPay.dutyPeriodPay.payValue" ...theLegPay.dutyPeriodPay.tripPay.distributedPay = "theLegPay.dutyPeriodPay.tripPay.distributedPay" ... theLegPay.dutyPeriodPay.tripPay.thisMonthPay = "theLegPay.dutyPeriodPay.tripPay.thisMonthPay).if (((theLegPay.payValue + theLegPay.dutyPeriodPay.distributedPay) <= theLegPay.dutyPeriodPay.payValue) and ((theLegPay.payValue + theLegPay.dutyPeriodPay.tripPay.distributedPay) <= theLegPay.dutyPeriodPay.tripPay.thisMonthPay)) then {retVal = theLegPay.payValue.fcnShow("Inside IF retVal = "retVal).} else {retVal = math().min((theLegPay.dutyPeriodPay.payValue - theLegPay.dutyPeriodPay.distributedPay),                      (theLegPay.dutyPeriodPay.tripPay.thisMonthPay - theLegPay.dutyPeriodPay.tripPay.distributedPay)).fcnShow("Inside ELSE retVal = "retVal).}//fcnShow("===>>> exiting fcnGetRegularPayForLegInForcedDutyPeriod for leg " fcnGetFlightLegDisplayString(theLegPay.payLeg) " ... returning " retVal).return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFlightLegDisplayString](fcnGetFlightLegDisplayString.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang - DE7501 - Returns the amount to distribute to the regular buckets for forced duty periods
```

