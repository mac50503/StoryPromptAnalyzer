# fcnAddTripPayBuckets

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAddTripPayBuckets`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| bucketCode | string | |
| amount | real | |
| rate | real | |
| aTripPay | TripPay | |
| isBaseValue | boolean | |

## Lógica de negocio

```blaze
if(bucketCode <> null and amount > 0 and rate > 0 and aTripPay <> null and aTripPay <> unknown) then {bucketBasePay is a real initially fcnRoundUpAt2DecimalPlaces(amount).if(isBaseValue is false) then { bucketBasePay = fcnRoundUpAt2DecimalPlaces(amount / rate).}aTripPay.addTripPayBuckets(bucketCode, bucketBasePay, rate).fcnShow("... fcnAddTripPayBuckets Adding Trip Pay Bucket ""...Trip ==>>"aTripPay.tripNameAndDate"...bucketCode ==>>"bucketCode"...bucketBasePay==>>"amount"...bucket rate==>>"rate).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Llamado por

- [fcnAddToBaseOfPayBucket](fcnAddToBaseOfPayBucket.md)
- [fcnDistributeToPayBucket](fcnDistributeToPayBucket.md)

