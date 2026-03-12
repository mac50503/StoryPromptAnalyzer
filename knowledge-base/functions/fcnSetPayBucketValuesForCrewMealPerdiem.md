# fcnSetPayBucketValuesForCrewMealPerdiem

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnSetPayBucketValuesForCrewMealPerdiem`

## Propósito
5/06/2024 - Namratha- APIC-1102-Created Main Function for Crew meal Perdiem

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theSchedulePeriodPay | SchedulePeriodPay | |
| aPayRateCode | string | |
| thePayValue | real | |
| theBaseValue | real | |
| thePayRate | real | |

## Lógica de negocio

```blaze
if(theSchedulePeriodPay <> null) then {for each PayBucket in theSchedulePeriodPay.payBucketList  as an array of PayBucket do{if(it.payWageCode as a string is equal to aPayRateCode  and it.bucketName.equalsIgnoreCase("CMPBUCKET")) then {cmpdValue is a real initially it.payValue.cmpdValue += thePayValue.theLegCount is a real initially it.baseValue.theLegCount += theBaseValue.it.payValue = cmpdValue.it.baseValue = theLegCount.it.payRate = thePayRate.}}}
```

## Llamado por

- [fcnCalculateCrewMealPerdiem](fcnCalculateCrewMealPerdiem.md)

## Historial de cambios

```
5/06/2024 - Namratha- APIC-1102-Created Main Function for Crew meal Perdiem
```

