# fcnCalculatePremiumPayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculatePremiumPayBucket`

## Propósito
MP:09/15/2014: US18357:  This function populates the pay buckets with the pay rate and base value

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| thePayBucket | string | |
| thePayValue | real | |
| thePayRate | real | |

## Lógica de negocio

```blaze
aPayBucket is some PayBucket initially theSchedulePeriodPay.getPayBucket(thePayBucket).addWorked is a boolean initially theSchedulePeriodPay.addToBucketPayValue(thePayBucket, thePayValue).fcnShow("===>>> Adding " thePayValue " to pay bucket " thePayBucket " for SP " theSchedulePeriodPay.schedulePeriodName " was successful = " addWorked).if (aPayBucket <> null) then{aPayBucket.payRate = thePayRate.aPayBucket.baseValue = aPayBucket.payValue / thePayRate.fcnShow("===>>> Current values for pay bucket " thePayBucket " ...payValue  = " aPayBucket.payValue  " ...baseValue  = " aPayBucket.baseValue  " ...payRate  = " aPayBucket.payRate).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
MP:09/15/2014: US18357:  This function populates the pay buckets with the pay rate and base value
```

