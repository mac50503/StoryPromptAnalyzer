# fcnGetCpCodeDiscontinueDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetCpCodeDiscontinueDate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aCpCode | CpCode | |
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
retVal is some DateTime initially null.if (aCpCode <> null and     aGlobalDataCache <> null and     aGlobalDataCache.cpCodeList <> null and          aGlobalDataCache.cpCodeList.size() > 0) then{count is an integer initially aGlobalDataCache.cpCodeList.size().index is an integer initially aGlobalDataCache.cpCodeList.indexOf(aCpCode).nextCpCode is some CpCode initially null.//// If the CpCode is the last one in the GDC, set the discontinue date to now + 100 yearsif ((index + 1) >= count) thenretVal = DateTime.now().plusYears(100).else{nextCpCode = aGlobalDataCache.cpCodeList.get(index + 1).if (nextCpCode <> null) thenretVal = nextCpCode.effectiveDate.minusMinutes(1). }  }return retVal.
```

## Llamado por

- [fcnGetCpCodePayRateForLeg](fcnGetCpCodePayRateForLeg.md)

