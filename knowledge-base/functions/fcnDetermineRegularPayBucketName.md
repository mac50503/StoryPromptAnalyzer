# fcnDetermineRegularPayBucketName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDetermineRegularPayBucketName`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| isDPRigsGreaterThanPremium | boolean | |
| isPositionA | boolean | |

## Lógica de negocio

```blaze
bucketName is a string initially "".tripAssignmentLabel is a string initially thePayTrip.assignmentLabel.if(tripAssignmentLabel = (ignoring case) ("J" or "V" or "U" or "E" or "S")) then {if(isPositionA) then {if(isDPRigsGreaterThanPremium) then {bucketName = "RGABUCKET".} else if (tripAssignmentLabel = (ignoring case) ("J")) then {bucketName = "JAABUCKET".} else if (tripAssignmentLabel = (ignoring case) ("E")) then {bucketName = "ADTBUCKET".} else {bucketName = "AOTBUCKET".}} else {if(isDPRigsGreaterThanPremium) then {bucketName = "REGBUCKET".} else if (tripAssignmentLabel = (ignoring case) ("J")) then {bucketName = "JAFBUCKET".} else if (tripAssignmentLabel = (ignoring case) ("E")) then {bucketName = "DTBUCKET".} else {bucketName = "OTBUCKET".}}} else {if(isPositionA) then {bucketName = "RGABUCKET".} else {bucketName = "REGBUCKET".}}return bucketName.
```

