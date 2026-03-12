# fcnGetPayBucketPayValue

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetPayBucketPayValue`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theBucketName | string | |

## Lógica de negocio

```blaze
if( theSchedulePeriodPay.getPayBucket(theBucketName) <> null) then { return theSchedulePeriodPay.getPayBucket(theBucketName).payValue.}else{return 0.0;}
```

