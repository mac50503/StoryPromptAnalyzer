# fcnRONValueToDeductForPremiumLabelTrips

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnRONValueToDeductForPremiumLabelTrips`

## Propósito
APIC-1491 This function is to fix the issue that was raised in the ticket listed.   This applies to Premium and RON  Assignment Label's J, U, V, E, S

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Lógica de negocio

```blaze
valueToAdjust is a real initially 0.0;if ((theTrip.tripPay is not null) and (theTrip.assignmentLabel is equal to ("J" or "U" or "V" or "E" or "S"))) then {for each DutyPeriodPay in theTrip.tripPay.dutyPeriodPayList as an array of DutyPeriodPay such that (it.rigsGreaterThanPremium = true) do {if(theTrip.assignmentLabel is not equal to "E") then {valueToAdjust +=  it.basePay * 0.5;} else {valueToAdjust +=  it.basePay;}}}fcnShow("Inside fcnRONValueToDeductForPremiumLabelTrips."" ...trip = " theTrip.tripNameAndDate" ... theTrip.sequenceNumber = " theTrip.sequenceNumber" .. valueToAdjust = " valueToAdjust).return valueToAdjust;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
APIC-1491 This function is to fix the issue that was raised in the ticket listed.   This applies to Premium and RON  Assignment Label's J, U, V, E, S
```

