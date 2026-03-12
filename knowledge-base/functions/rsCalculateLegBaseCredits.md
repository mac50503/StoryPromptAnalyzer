# rsCalculateLegBaseCredits

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateLegBaseCredits`

## Propósito
06/12/2014 Corey Gu US16556 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayLeg | PayLeg | |
| theLegPay | LegPay | |

## Historial de cambios

```
06/12/2014 Corey Gu US16556 - Initial development
10/10/2014 Tim A DE5173 - new actions for ruleCalculateLegBaseCreditsForWorkCodeEqualToGR
10/10/2014 Tim A DE5173 - new rules ruleSetGateReturnFlightBlockTimeUsingScehduledTimes, ruleSetGateReturnFlightBlockTimeUsingActualDepartureTime, ruleSetGateReturnFlightBlockTimeUsingActualArrivalTime
12/22/2014 Corey Gu US19294 - Modified ruleCalculateLegBaseCreditsForWorkCodeNotEqualToGR
06/03/2015 Tim A. DE6412 - added rule ruleForcedLegTripLabelJvu
02/06/2017 Rachel Starfield CREW-1001 - added rule ruleForcedLegTripLabelE
10/04/2024 - Changed the rule ruleForcedLegTripLabelJvu to ruleForcedLegTripLabelJVUS, also added S label check in the rule
```

