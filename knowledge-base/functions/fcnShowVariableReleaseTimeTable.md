# fcnShowVariableReleaseTimeTable

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\Logging\fcnShowVariableReleaseTimeTable`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aGlobalDataCache | GlobalDataCache | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnShowVariableReleaseTimeTable with arg aGlobalDataCache = " aGlobalDataCache).if (aGlobalDataCache = null) thenfcnShow("===>>> aGlobalDataCache is NULL").else if (aGlobalDataCache.variableReleaseTimesTable = null) thenfcnShow("===>>> aGlobalDataCache.variableReleaseTimesTable = is NULL").else{count is an integer initially 0.entryCount is an integer initially aGlobalDataCache.variableReleaseTimesTable.size().fcnShow("===>>> variable release times table contains " entryCount  " entries").if (entryCount > 0) then{for each VariableReleaseTimes in aGlobalDataCache.variableReleaseTimesTable as an array of VariableReleaseTimes do  {count += 1.fcnShow("===>>> entry " count " ...postClearance = " it.postClearance).fcnShow("===>>> entry " count " ...lastDutyPeriod = " lastDutyPeriod).fcnShow("===>>> entry " count " ...contractualReleaseTime = " contractualReleaseTime).fcnShow("===>>> entry " count " ...farReleaseTime = " farReleaseTime).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

