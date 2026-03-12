# fcnGetCpCodePayRateForLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetCpCodePayRateForLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (aPayLeg <> null and     aGlobalDataCache <> null and     aGlobalDataCache.cpCodeList <> null and          aGlobalDataCache.cpCodeList.size() > 0) then{aCpCode is some CpCode initially null.legEventDate is some DateTime initially aPayLeg.scheduledDepartureDateTime.effectiveDate is some DateTime initially null.discontinueDate is some DateTime initially null.for each CpCode in aGlobalDataCache.cpCodeList as an array of CpCode do{aCpCode = it.if (aCpCode.code = aPayLeg.cpCode) then{effectiveDate = aCpCode.effectiveDate.discontinueDate = fcnGetCpCodeDiscontinueDate(aCpCode, aGlobalDataCache).if (fcnIsDateTimeWithinDateTimeRange(legEventDate, effectiveDate, discontinueDate)) thenreturn aCpCode.rate.}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetCpCodeDiscontinueDate](fcnGetCpCodeDiscontinueDate.md)
- [fcnIsDateTimeWithinDateTimeRange](fcnIsDateTimeWithinDateTimeRange.md)

## Llamado por

- [fcnCalculateTripCpCodePay](fcnCalculateTripCpCodePay.md)

