# fcnGetPayBucketForMealPerdiemPayRateCode

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayBucket
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayBucketForMealPerdiemPayRateCode`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| apayRateCode | string | |

## Lógica de negocio

```blaze
if(theSchedulePeriodPay <> null) then {for each PayBucket in theSchedulePeriodPay.payBucketList  as an array of PayBucket do{if(it.payWageCode = portable().toInteger(apayRateCode)) then {return it.}}}return null;
```

