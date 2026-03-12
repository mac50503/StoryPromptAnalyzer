# fcnIsFirstLegInDP

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsFirstLegInDP`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isFirstLegInDP is a boolean initially false.if(theDutyPeriod <> null and theDutyPeriod <> unknownand theDutyPeriod.firstLeg <> nulland theDutyPeriod.firstLeg <> unknownand thePayLeg <> nulland thePayLeg <> unknown) then {isFirstLegInDP = theDutyPeriod.firstLeg.equals(thePayLeg).}return isFirstLegInDP.
```

## Llamado por

- [fcnGetGTPDistributionBucketName](fcnGetGTPDistributionBucketName.md)
- [fcnGetPrevLegOfDP](fcnGetPrevLegOfDP.md)

