# fcnGetPreviousPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetPreviousPayLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
previousPayLeg is some PayLeg initially null.for each PayLeg in thePayLeg.payDutyPeriod.legList as an array of PayLeg do{if(thePayLeg <> it) then{previousPayLeg = it;}else{return previousPayLeg;}}return previousPayLeg;
```

## Llamado por

- [fcnCalculateLegDutyHours](fcnCalculateLegDutyHours.md)

