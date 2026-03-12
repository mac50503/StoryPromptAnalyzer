# fcnGetLegIdentificationString

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLegIdentificationString`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is a string.if (aPayLeg <> null) then{retVal = "pay leg: " aPayLeg.flightNumber " " aPayLeg.departureLocation "-" aPayLeg.arrivalLocation " from trip: ".if (aPayLeg.payDutyPeriod <> null and aPayLeg.payDutyPeriod.payTrip <> null) thenretVal = retVal "" aPayLeg.payDutyPeriod.payTrip.tripNameAndDate.}return retVal.
```

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)
- [fcnGetSchedulePeriodPayForLegPay](fcnGetSchedulePeriodPayForLegPay.md)

