# fcnGetLastNonRSLegInDuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetLastNonRSLegInDuty`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if(thePayDutyPeriod <> null and thePayDutyPeriod.legList <> null) then{index is an integer initially thePayDutyPeriod.legList.size() - 1;thePayLeg is some PayLeg initially null;while(index >= 0) do{thePayLeg = thePayDutyPeriod.legList.get(index);if(thePayLeg <> null and (thePayLeg.legWorkCodeList = null  or (thePayLeg.legWorkCodeList <> null and thePayLeg.legWorkCodeList.contains("RS") = false))) then{return thePayLeg;}index = index - 1;}}return null;
```

## Llamado por

- [fcnCalculate16HrsDutyDurationEDD](fcnCalculate16HrsDutyDurationEDD.md)
- [fcnCalculateActualDutyDuration](fcnCalculateActualDutyDuration.md)
- [fcnCalculateLegDutyHours](fcnCalculateLegDutyHours.md)
- [fcnGetDHREndDateTime](fcnGetDHREndDateTime.md)

