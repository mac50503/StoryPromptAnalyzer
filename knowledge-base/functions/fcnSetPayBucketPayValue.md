# fcnSetPayBucketPayValue

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnSetPayBucketPayValue`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theBucketName | string | |
| theValue | real | |

## Lógica de negocio

```blaze
if( theSchedulePeriodPay.getPayBucket(theBucketName) <> null) then {theSchedulePeriodPay.getPayBucket(theBucketName).payValue = theValue;}
```

