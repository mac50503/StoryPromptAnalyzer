# fcnCalculateTotalPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateTotalPayBucket`

## Propósito
US16650:MP:09/26/2014 - This function adds up all the TFP buckets and assigns the value to the totalPayBucket.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |

## Lógica de negocio

```blaze
//Loop through each TFP based Pay Buckets and store into TOTBUCKETfcnShow("===>>> ENTERING fcnCalculateTotalPayBucket ...SP = " theSchedulePeriodPay.schedulePeriodName " ...pay bucket counnt = " theSchedulePeriodPay.payBucketList.size()).if (theSchedulePeriodPay.payBucketList <>null and theSchedulePeriodPay.payBucketList.size() > 0) then{for each PayBucket in theSchedulePeriodPay.payBucketList as an array of PayBucket      such that (it.payValue >0 and it.bucketMetric = PayMetric.TFP and it.bucketName<>"TOTBUCKET") do {theSchedulePeriodPay.addToBucketPayValue("TOTBUCKET", it.payValue).fcnShow("===>>> adding bucket " it.bucketName "'s payValue of " it.payValue " to TOTBUCKET ... value now =  " theSchedulePeriodPay.getPayBucket("TOTBUCKET").payValue).}//Set Projected Credit, it is same as Bucket total.theSchedulePeriodPay.projectedCredit = theSchedulePeriodPay.getPayBucket("TOTBUCKET").payValue.}fcnShow("===>>> EXITING fcnCalculateTotalPayBucket  ...SP = " theSchedulePeriodPay.schedulePeriodName " ...TOTBUCKET = " theSchedulePeriodPay.projectedCredit).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
US16650:MP:09/26/2014 - This function adds up all the TFP buckets and assigns the value to the totalPayBucket.
US16564:MP:09/26/2014 - Also sets the projected credit.
```

