# fcnDutyPeriodHasLegWithoutWorkCode

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDutyPeriodHasLegWithoutWorkCode`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| workCode | string | |

## Lógica de negocio

```blaze
retVal is a boolean initially false;if (aPayDutyPeriod <> null and aPayDutyPeriod.legList.size() > 0) then{for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{if (it.legWorkCodeList = null or it.legWorkCodeList.size() = 0 or it.legWorkCodeList.contains(workCode) = false) then{retVal = true;}}}return retVal;
```

