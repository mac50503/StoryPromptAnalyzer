# fcnXrefPayTripToTripPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayTripToTripPay`

## Propósito
Ben Lang 3/26/2014 US16544 - Test that the fcnXrefPayLegToLegPay passes the thePayLeg data to the theLegPay object.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aTripPay <> null) then{aPayTrip.setTripNameAndDate().aTripPay.payTrip = aPayTrip.aPayTrip.tripPay = aTripPay.aTripPay.sequenceNumber = aPayTrip.sequenceNumber.aTripPay.tripName = aPayTrip.tripName.aTripPay.creditType = aPayTrip.creditType.aTripPay.tripClass = aPayTrip.tripClass.aTripPay.tripType = aPayTrip.tripType.aTripPay.tripType = aPayTrip.tripType.aTripPay.multiDutyPeriodTrip = aPayTrip.multiDutyPeriodTrip.aTripPay.beginDateTime = aPayTrip.beginDateTime.aTripPay.endDateTime = aPayTrip.endDateTime.aTripPay.startsInSchedulePeriod = aPayTrip.startsInSchedulePeriod.aTripPay.endsInSchedulePeriod= aPayTrip.endsInSchedulePeriod.aTripPay.assignmentLabel = aPayTrip.assignmentLabel.aTripPay.nonFlyCode = aPayTrip.nonFlyCode.aTripPay.basePay = aPayTrip.basePay.if (aTripPay.tripPayInflight <> null and aPayTrip.payTripInflight <> null) then{aTripPay.tripPayInflight.paidNonFly = aPayTrip.payTripInflight.paidNonFly.aTripPay.tripPayInflight.isReserveTrip = aPayTrip.payTripInflight.isReserveTrip.}}
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)

## Historial de cambios

```
Ben Lang 3/26/2014 US16544 - Test that the fcnXrefPayLegToLegPay passes the thePayLeg data to the theLegPay object.
Tim Albright 10/21/2014 - Added xref to property isReserveTrip
```

