# fcnGetTripPayFromPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayFromPayLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |

## Lógica de negocio

```blaze
retVal is some TripPay initially null.if (aPayLeg <> null and aPayLeg.legPay <> null and aPayLeg.legPay.dutyPeriodPay <> null) then{retVal = aPayLeg.legPay.dutyPeriodPay.tripPay.}return retVal.
```

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)

