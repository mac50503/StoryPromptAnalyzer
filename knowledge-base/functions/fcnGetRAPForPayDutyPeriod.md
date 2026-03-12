# fcnGetRAPForPayDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayDutyPeriod
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetRAPForPayDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReserveBlock | PayTrip | |
| theDutyPeriod | PayDutyPeriod | |
| comparedTime | integer | |

## Lógica de negocio

```blaze
//// comparedTime value:// 1: compare theDutyPeriod.reportDateTime is within the RAP// 2: compare theDutyPeriod.releaseDateTime is within the RAP// 3. compare theDutyPeriod.reportDateTimea before the RAP reportDateTime, and theDutyPeriod.releaseDateTime is after the RAP's releaseDateTime.//RAPListLength is an integer initially 0.aRAP is some PayDutyPeriod.index is an integer initially 0.aRAPFound is a boolean initially false.RAPListLength = theReserveBlock.dutyPeriodList.size().index = 0.select comparedTimecase 1: {while (index < RAPListLength and aRAPFound = false) do {aRAP = theReserveBlock.dutyPeriodList.get(index).if ((theDutyPeriod.reportDateTime.isEqual(aRAP.reportDateTime) or     theDutyPeriod.reportDateTime.isAfter(aRAP.reportDateTime)) and       theDutyPeriod.reportDateTime.isBefore(aRAP.releaseDateTime)) then {aRAPFound = true.} else {index = index + 1.}}}case 2: {while (index < RAPListLength and aRAPFound = false) do {aRAP = theReserveBlock.dutyPeriodList.get(index).if ((theDutyPeriod.releaseDateTime.isBefore(aRAP.releaseDateTime) or     theDutyPeriod.releaseDateTime.isEqual(aRAP.releaseDateTime)) and       theDutyPeriod.releaseDateTime.isAfter(aRAP.reportDateTime)) then {aRAPFound = true.} else {index = index + 1.}}}case 3: {while (index < RAPListLength and aRAPFound = false) do {aRAP = theReserveBlock.dutyPeriodList.get(index).if (aRAP.reportDateTime.isAfter(theDutyPeriod.reportDateTime) and       aRAP.releaseDateTime.isBefore(theDutyPeriod.releaseDateTime)) then {aRAPFound = true.} else {index = index + 1.}}}if (aRAPFound = true) then {return aRAP.} else {return null.}
```

