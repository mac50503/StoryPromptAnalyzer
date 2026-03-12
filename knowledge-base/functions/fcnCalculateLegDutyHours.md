# fcnCalculateLegDutyHours

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateLegDutyHours`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |

## Lógica de negocio

```blaze
theDutyHours is a real initially 0.0;if(thePayLeg.legWorkCodeList = null  or (thePayLeg.legWorkCodeList <> null and thePayLeg.legWorkCodeList.contains("RS") = false)) then{theDutyHours = fcnGetTimeDiffInMinutes(thePayLeg.determineDepartureDateTime(), thePayLeg.determineArrivalDateTime());if(thePayLeg = fcnGetFirstNonRSLegInDuty(thePayLeg.payDutyPeriod)) then{theDutyHours += fcnGetTimeDiffInMinutes(thePayLeg.payDutyPeriod.reportDateTime, thePayLeg.determineDepartureDateTime());}else{theDutyHours += fcnGetTimeDiffInMinutes(fcnGetPreviousPayLeg(thePayLeg).determineArrivalDateTime(),thePayLeg.determineDepartureDateTime())/2;}if (thePayLeg = fcnGetLastNonRSLegInDuty(thePayLeg.payDutyPeriod)) then{theDutyHours += fcnGetTimeDiffInMinutes(thePayLeg.determineArrivalDateTime(), thePayLeg.payDutyPeriod.releaseDateTime);}else{theDutyHours += fcnGetTimeDiffInMinutes(thePayLeg.determineArrivalDateTime(), fcnGetNextPayLeg(thePayLeg).determineDepartureDateTime())/2;}}thePayLeg.legPay.dutyHours = theDutyHours;
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFirstNonRSLegInDuty](fcnGetFirstNonRSLegInDuty.md)
- [fcnGetLastNonRSLegInDuty](fcnGetLastNonRSLegInDuty.md)
- [fcnGetNextPayLeg](fcnGetNextPayLeg.md)
- [fcnGetPreviousPayLeg](fcnGetPreviousPayLeg.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

