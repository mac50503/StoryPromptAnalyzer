# fcnGetNextPayLeg

## Metadata
- **Tipo**: SRL Function
- **Retorna**: PayLeg
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetNextPayLeg`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
theLegFound is a boolean initially false;nextPayLeg is some PayLeg initially null.for each PayLeg in thePayLeg.payDutyPeriod.legList as an array of PayLeg do{if(theLegFound) then{nextPayLeg = it;return nextPayLeg;}else if(thePayLeg = it) then{theLegFound = true;}}return nextPayLeg;
```

## Llamado por

- [fcnCalculateLegDutyHours](fcnCalculateLegDutyHours.md)

