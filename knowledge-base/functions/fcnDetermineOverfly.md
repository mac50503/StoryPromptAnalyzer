# fcnDetermineOverfly

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnDetermineOverfly`

## Propósito
06/12/2014 Corey Gu US16556 Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| theOverflyStandardMinutes | real | |
| theOverflyStandardMultiplier | real | |

## Lógica de negocio

```blaze
retVal is a real initially 0.0.if (thePayLeg.actualInDateTime <> null and thePayLeg.actualInDateTime <> unknown and thePayLeg.actualOutDateTime <> null and thePayLeg.actualOutDateTime <> unknown) then {theActualBlockTime is an integer initially Duration.newInstance(thePayLeg.actualOutDateTime, thePayLeg.actualInDateTime).standardMinutes.theScheduledBlockTime is an integer initially Duration.newInstance(thePayLeg.scheduledDepartureDateTime, thePayLeg.scheduledArrivalDateTime).standardMinutes.if (theActualBlockTime > theScheduledBlockTime) then {retVal = (((theActualBlockTime - theScheduledBlockTime)/theOverflyStandardMinutes) * theOverflyStandardMultiplier).fcnShow("===>>> in fcnDetermineOverfly for leg " fcnGetFlightLegDisplayString(thePayLeg) " ... sched block minutes =  " theScheduledBlockTime " ... actual block minutes =  " theActualBlockTime).fcnShow("===>>> in fcnDetermineOverfly for leg " fcnGetFlightLegDisplayString(thePayLeg) " ... overfly interim value = " retVal).retVal = math().truncate(retVal, -1).//// CHANGED TO TRUNCATE FROM ROUND WITH DEFECT 4981...fcnShow("===>>> in fcnDetermineOverfly for leg " fcnGetFlightLegDisplayString(thePayLeg) " ... overfly after truncate = " retVal).}} //// ANALYTICSif (thePayLeg.legPay <> null and thePayLeg.legPay.legPayInflightAnalytics <> null) then{thePayLeg.legPay.legPayInflightAnalytics.overflyPremiumTfp = retVal.thePayLeg.legPay.legPayInflightAnalytics.overflyPremiumTfp = fcnRoundUpAt2DecimalPlaces(thePayLeg.legPay.legPayInflightAnalytics.overflyPremiumTfp).}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFlightLegDisplayString](fcnGetFlightLegDisplayString.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
06/12/2014 Corey Gu US16556 Initial development
09/15/2014 Tim A. changed round in formula to truncate
09/20/2017 Tim A. - added analytics data population code
```

