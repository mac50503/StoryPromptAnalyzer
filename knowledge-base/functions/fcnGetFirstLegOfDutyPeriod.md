# fcnGetFirstLegOfDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetFirstLegOfDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
retVal is some PayLeg initially null.if (aPayDutyPeriod <> null and aPayDutyPeriod.legList <> null and aPayDutyPeriod.legList.size() > 0) then{retVal = aPayDutyPeriod.legList.get(0).}return retVal.
```

## Llamado por

- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnDistributeToLateReturnBuckets](fcnDistributeToLateReturnBuckets.md)
- [fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay](fcnDoesFirstLegOfDutyPeriodInSchedulePeriodPay.md)

