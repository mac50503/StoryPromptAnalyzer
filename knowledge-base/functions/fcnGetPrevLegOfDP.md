# fcnGetPrevLegOfDP

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetPrevLegOfDP`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDutyPeriod | PayDutyPeriod | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
previousLeg is some PayLeg initially null.if(theDutyPeriod <> nulland theDutyPeriod <> unknownand theDutyPeriod.legList <> nulland theDutyPeriod.legList <> unknownand theDutyPeriod.legList.size() > 0and not fcnIsFirstLegInDP(theDutyPeriod, thePayLeg)) then {previousLeg = theDutyPeriod.legList.get(theDutyPeriod.legList.indexOf(thePayLeg) - 1).}return previousLeg.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnIsFirstLegInDP](fcnIsFirstLegInDP.md)

## Llamado por

- [fcnGetGTPDistributionBucketName](fcnGetGTPDistributionBucketName.md)

