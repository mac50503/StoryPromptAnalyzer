# fcnAddToPayValueOfPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnAddToPayValueOfPayBucket`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| theBucketCode | string | |
| thePayValue | real | |
| thePayRate | real | |
| eventDate | DateTime | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
if (fcnIsDateTimeWithinReportFilterRange(eventDate, reportFilterStart, reportFilterEnd)) then{bucketFoundTrue is a boolean initially false.if (theSchedulePeriodPay.getPayBucket(theBucketCode) <> null) thenbucketFoundTrue = true;thePayBucket is some PayBucket initially theSchedulePeriodPay.getPayBucket(theBucketCode).if (thePayBucket <> null) thenthePayBucket.payRate = thePayRate.theSchedulePeriodPay.addToBucketPayValue(theBucketCode, thePayValue).if (thePayBucket <> null) then{thePayBucket.baseValue = fcnRoundUpAt2DecimalPlaces(thePayBucket.baseValue).thePayBucket.payValue = fcnRoundUpAt2DecimalPlaces(thePayBucket.payValue).}fcnShow("===>>> EXITING fcnAddToPayValueOfPayBucket  ...SP = " theSchedulePeriodPay.schedulePeriodName "...pay bucket " theBucketCode " is found = " bucketFoundTrue "... value added = " thePayValue " ...new bucket base value = " theSchedulePeriodPay.getPayBucket(theBucketCode).baseValue " ...new bucket pay value = " theSchedulePeriodPay.getPayBucket(theBucketCode).payValue "... bucket payRate = " theSchedulePeriodPay.getPayBucket(theBucketCode).payRate).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

