# fcnIsNonPaidLimoLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnIsNonPaidLimoLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is a boolean initially true.if (aPayLeg <> null) then{isLimo is a boolean initially aPayLeg.limoFlag.sameStations is a boolean initially aPayLeg.departureLocation = aPayLeg.arrivalLocation.limoDuration is an integer initially fcnGetTimeDiffInMinutes(aPayLeg.determineBestDepartureDateTimeNoEstimated(), aPayLeg.determineBestArrivalDateTimeNoEstimated()).if (isLimo = false or   (isLimo = true and sameStations = false and limoDuration > 0) or    (isLimo = true and aPayLeg.creditType = (ignoring case) "F" and aPayLeg.basePay <> 0.0)) thenretVal = false.}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Llamado por

- [fcnDutyContainsAllNonPaidLimos](fcnDutyContainsAllNonPaidLimos.md)
- [fcnIsRedEyePayEligible](fcnIsRedEyePayEligible.md)

