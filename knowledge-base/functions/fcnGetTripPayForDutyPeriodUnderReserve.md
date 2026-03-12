# fcnGetTripPayForDutyPeriodUnderReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: TripPay
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetTripPayForDutyPeriodUnderReserve`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| originalTripPay | TripPay | |

## Lógica de negocio

```blaze
aTripPayUnderReserve is some TripPay initially originalTripPay.if (aPayDutyPeriod.payDutyPeriodInflight <> null and    aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList <> null and   aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size() > 0) then {count is an integer initially 0.associationCount is an integer initially aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.size().while count < associationCount do {aTripPayUnderReserve = aPayDutyPeriod.payDutyPeriodInflight.rapAssociationList.get(count).payTrip.tripPay.count +=1.}} else if (aPayDutyPeriod.rapAssociation <> null) then {aTripPayUnderReserve = aPayDutyPeriod.rapAssociation.payTrip.tripPay.}if(originalTripPay <> null and originalTripPay <> unknown) then {if(aTripPayUnderReserve.tripNameAndDate <> originalTripPay.tripNameAndDate) then {fcnShow(" RETURNING fcnGetTripPayForDutyPeriodUnderReserve "" ...TRIP ==>>"aTripPayUnderReserve.tripNameAndDate" ... ***DP IS UNDER RESERVE*** "" ...aPayDutyPeriod.sequenceNumber ==>> "aPayDutyPeriod.sequenceNumber" .. INSIDE ORIGINAL  TRIP ==>>"originalTripPay.tripNameAndDate" ...aPayDutyPeriod.reportDateTime ==>>"aPayDutyPeriod.reportDateTime" ...aPayDutyPeriod beginLocation ==>>"aPayDutyPeriod.beginLocation" ...aPayDutyPeriod endLocation ==>>"aPayDutyPeriod.endLocation).} else {fcnShow(" RETURNING fcnGetTripPayForDutyPeriodUnderReserve "" ...aPayDutyPeriod.sequenceNumber ==>> "aPayDutyPeriod.sequenceNumber" ... ***DP IS NOT UNDER RESERVE*** "" .. INSIDE ORIGINAL  TRIP ==>>"originalTripPay.tripNameAndDate" ...aPayDutyPeriod.reportDateTime ==>>"aPayDutyPeriod.reportDateTime" ...aPayDutyPeriod beginLocation ==>>"aPayDutyPeriod.beginLocation" ...aPayDutyPeriod endLocation ==>>"aPayDutyPeriod.endLocation).}}return aTripPayUnderReserve.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTripPay](fcnGetTripPay.md)
- `fcnShow()`

