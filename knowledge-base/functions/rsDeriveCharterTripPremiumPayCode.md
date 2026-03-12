# rsDeriveCharterTripPremiumPayCode

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDeriveCharterTripPremiumPayCode`

## Propósito
08/19/2014 Corey Gu US18258 - Modified theDutyAmountAtBlockIn() to use  determineBestArrivalDateTimeNoEstimated() in ruleCalculateReducedRestFlag.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | PayLeg | |
| thePreviousDutyPeriod | PayDutyPeriod | |

## Historial de cambios

```
08/19/2014 Corey Gu US18258 - Modified theDutyAmountAtBlockIn() to use  determineBestArrivalDateTimeNoEstimated() in ruleCalculateReducedRestFlag.
8/19/2015 - Melissa S - DE7244 - Added hoursLate property, and changed rules to use hoursLate instead of the originalDutyDay + 1 hour for rules that check if the actual duty is an hou late
8/28/2015 - DE7331 - Melissa S - Added new property previousDutyCountsAsRest and new rule ruleSetExemptFromReducedRestFlag2 to make sure the reduced rest isn't used when the previous duty period is a LIMO that should be counted as REST
2/7/2017 - CREW-1001 - Rachel Starfield - Added E Label to reducedRest and TripLabelUVJ rules
2/7/2017 - CREW-1018 - Mark Bevington - E Label changes renamed rules to include E
2/27/2017 - CREW-1118 - Rachel Starfield - Separated out E in rules that paid VJ so that E would pay DT.
```

