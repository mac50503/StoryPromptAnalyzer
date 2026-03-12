# fcnSetPayBucketRate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetPayBucketRate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theCrewPayRequest | CrewPayRequest | |
| theSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
aPayBucket is some PayBucket initially null.if (theCrewPayRequest.payBucketList <> null and theCrewPayRequest.payBucketList.size()>0 ) then{for each PayBucket in theCrewPayRequest.payBucketList as an array of PayBucket do {// 08/28/2014, Corey Gu - Per Tim, all paybuckets are passed in as a single list, but we need different instances of the entrire list for each schedule period pay.// Otherwise, Feb processing would override the Jan processing of the same bucket name. That's why we use clone() here.aPayBucket = it.clone() as a PayBucket.dtInflightSetPayBucketRate_Instance(aPayBucket, theSchedulePeriodPay.schedulePeriodStart).theSchedulePeriodPay.addPayBucket(aPayBucket).}}
```

