# fcnGetTripPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetTripPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Lógica de negocio

```blaze
if (theTrip.dutyPeriodList.get(0).creditType = "P") thenreturn math().max(theTrip.basePay, theTrip.tripPay.tripPayInflight.baseDutyPeriodSum).elsereturn fcnMaxOf4Numbers(theTrip.basePay, theTrip.tripPay.tripPayInflight.baseDutyPeriodSum, theTrip.tripPay.tripPayInflight.adgValue, theTrip.dutyPeriodList.get(0).dutyPeriodPay.dutyHourRatio).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnMaxOf4Numbers](fcnMaxOf4Numbers.md)

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)
- [fcnDistributeToPerDiemBuckets](fcnDistributeToPerDiemBuckets.md)
- [fcnGetTripPayForDutyPeriodUnderReserve](fcnGetTripPayForDutyPeriodUnderReserve.md)

