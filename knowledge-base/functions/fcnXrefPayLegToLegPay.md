# fcnXrefPayLegToLegPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayLegToLegPay`

## Propósito
06/27/2017 - Tim A. - CREW-65 - added initialization of LegPay.payValueNoPremium

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aLegPay | LegPay | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and aLegPay <> null) then{aPayLeg.legPay = aLegPay.aLegPay.payLeg = aPayLeg.aLegPay.sequenceNumber = aPayLeg.sequenceNumber.aLegPay.creditType = aPayLeg.creditType.aLegPay.basePay = aPayLeg.basePay.aLegPay.payValueNoPremium = aPayLeg.basePay.}
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)

## Historial de cambios

```
06/27/2017 - Tim A. - CREW-65 - added initialization of LegPay.payValueNoPremium
```

