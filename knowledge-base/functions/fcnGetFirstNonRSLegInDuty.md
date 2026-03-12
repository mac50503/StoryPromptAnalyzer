# fcnGetFirstNonRSLegInDuty

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetFirstNonRSLegInDuty`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if(thePayDutyPeriod <> null and thePayDutyPeriod.legList <> null) then{index is an integer initially 0;thePayLeg is some PayLeg initially null;while(index < thePayDutyPeriod.legList.size()) do{thePayLeg = thePayDutyPeriod.legList.get(index);if(thePayLeg <> null and (thePayLeg.legWorkCodeList = null  or (thePayLeg.legWorkCodeList <> null and thePayLeg.legWorkCodeList.contains("RS") = false))) then{return thePayLeg;}index = index + 1;}}return null;
```

## Llamado por

- [fcnCalculateLegDutyHours](fcnCalculateLegDutyHours.md)

