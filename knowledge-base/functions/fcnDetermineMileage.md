# fcnDetermineMileage

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnDetermineMileage`

## Propósito
02/28/2014 Tim Albright - US16955

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| forceDistance | boolean | |
| theStandardTripMileage | real | |
| theNonStandardTripMileage | real | |
| theStandardTripCredit | real | |
| theNonStandardTripMultiplier | real | |

## Lógica de negocio

```blaze
fcnShow("===>>> in function fcnDetermineMileage for flight leg " fcnGetFlightLegDisplayString(thePayLeg) " with args:  forceDistance = " forceDistance ", theStandardTripMileage = " theStandardTripMileage ", theNonStandardTripMileage = " theNonStandardTripMileage ", theStandardTripCredit = " theStandardTripCredit ", theNonStandardTripMultiplier = " theNonStandardTripMultiplier).retVal is a real initially 0.0.if (forceDistance) then  // THIS IS USED FOR DETERMINING FORCED MILEAGE CALCULATION FOR MILEPAY REQUESTS...{retVal = (theStandardTripCredit + math().round((thePayLeg.distance - theStandardTripMileage) / 40) * theNonStandardTripMultiplier).fcnShow("===>>> theStandardTripCredit + (theDistance - theStandardTripMileage) / 40 * theNonStandardTripMultiplier = " theStandardTripCredit " + ( " thePayLeg.distance " - " theStandardTripMileage ") / 40) * " theNonStandardTripMultiplier " = " retVal).}else if (thePayLeg.distance <= theStandardTripMileage) thenretVal = (theStandardTripCredit).else retVal = (theStandardTripCredit + math().round((thePayLeg.distance - theStandardTripMileage) / 40) * theNonStandardTripMultiplier).fcnShow("===>>> returning mileage-based TFP of " retVal " for flight leg " fcnGetFlightLegDisplayString(thePayLeg)).retVal = fcnRoundUpAt2DecimalPlaces(retVal).legMileageTfp_var = retVal.return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetFlightLegDisplayString](fcnGetFlightLegDisplayString.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`

## Historial de cambios

```
02/28/2014 Tim Albright - US16955
09/20/2017 Tim A. - added IF analytics data population code
01/09/2018 Tim A. - added FO analytics data population code
```

