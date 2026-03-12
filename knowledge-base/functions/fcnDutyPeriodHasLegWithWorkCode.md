# fcnDutyPeriodHasLegWithWorkCode

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDutyPeriodHasLegWithWorkCode`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| workCodes | string | |

## Lógica de negocio

```blaze
retVal is a boolean initially false.if (aPayDutyPeriod <> null and aPayDutyPeriod.legList.size() > 0) then{for each PayLeg in aPayDutyPeriod.legList as an array of PayLeg do{if (retVal = false and it.legWorkCodeList <> null and it.legWorkCodeList.size() > 0) then{for each string in it.legWorkCodeList as an array of string do{if (retVal = false and workCodes.contains(it as a CharSequence)) thenretVal = true.}}}}return retVal.
```

