# fcnCalculateEDDBucketName

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateEDDBucketName`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
isFAAPosition is a boolean initially thePayLeg.legPay.positionA;bucketNameForEDD is a string initially thePayLeg.legPay.premiumPayCode.if(isFAAPosition) then {if(theTrip.assignmentLabel = "J" and thePayLeg.legPay.premiumPayCode <> ("DT" and "DH" and "TT" and  "TH")) then {bucketNameForEDD = "JAA".} if(thePayLeg.legPay.premiumPayCode = "DT") then {if(thePayLeg.legWorkCodeList.contains("CT") and not thePayLeg.isDeadhead) then {bucketNameForEDD = "CTA".} else {bucketNameForEDD = "A"bucketNameForEDD.}}if(thePayLeg.legPay.premiumPayCode = ("DH" or "TH")) then {bucketNameForEDD = "A"bucketNameForEDD.} if(thePayLeg.legPay.premiumPayCode = "TT") then {bucketNameForEDD = "TTA".}if(thePayLeg.legPay.premiumPayCode = ("VJ" or  "JA")) then {if(theTrip.assignmentLabel = "E") then {bucketNameForEDD = "ADT".} else if((theTrip.assignmentLabel <> ("J" and "E") or thePayLeg.isDeadhead)) then {bucketNameForEDD = "AOT".}}} else {if(theTrip.assignmentLabel = "J" and thePayLeg.legPay.premiumPayCode <> ("DT" and "DH" and "TT" and  "TH")) then {bucketNameForEDD = "JAF".}if( thePayLeg.legPay.premiumPayCode = "DT" and thePayLeg.legWorkCodeList.contains("CT") and not thePayLeg.isDeadhead) then {bucketNameForEDD = "CT".}if(thePayLeg.legPay.premiumPayCode = ("VJ" or  "JA")) then {if(theTrip.assignmentLabel = "E") then {bucketNameForEDD = "DT".} else if((theTrip.assignmentLabel <> ("J" and "E") or thePayLeg.isDeadhead)) then {bucketNameForEDD = "OT".}}}bucketNameForEDD = bucketNameForEDD"BUCKET".fcnShow("Inside fcnCalculateEDDBucketName isFAAPosition ==>>"isFAAPosition"   anyPayLeg.sequenceNumber ==>>"thePayLeg.sequenceNumber"   bucketNameForEDD ==>>"bucketNameForEDD).return bucketNameForEDD.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

