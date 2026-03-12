# fcnGetLegCrewPosition

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetLegCrewPosition`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
legCrewPosition is a string initially null.if(thePayLeg <> nulland thePayLeg <> unknown) then {legCrewPosition = thePayLeg.legCrewPosition.if(legCrewPosition = null and thePayLeg.payLegInflight <> null and thePayLeg.payLegInflight <> unknown) then {legCrewPosition = thePayLeg.payLegInflight.crewPosition.}}return legCrewPosition.
```

## Llamado por

- [fcnGetGTPDistributionBucketName](fcnGetGTPDistributionBucketName.md)
- [fcnIsABucketApplicable](fcnIsABucketApplicable.md)

