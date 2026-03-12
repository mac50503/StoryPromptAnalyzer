# rsDeriveRONPremiumPayCode

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDeriveRONPremiumPayCode`

## Propósito
06/27/2014 Ben Lang US16814

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLeg | PayLeg | |
| thePreviousDutyPeriod | PayDutyPeriod | |
| theDutyPeriodDuration | duration | |

## Historial de cambios

```
06/27/2014 Ben Lang US16814
08/19/2014 Corey Gu US18258 - Modified DetermineArrivalDateTime() to use determineBestArrivalDateTimeNoEstimated() in ruleCalculateReducedRestFlag.
10/22/2014 Corey Gu US18781- See comments in rules.
8/19/2015 - Melissa S - DE7254 - Changed the all deadheads condition to be all (deadheads OR LIMO) for rulePriorDayReserveYNumber01, rulePriorDayReserveYNumber02, and rulePriorDayReserveNNumber01
10/11/2021 - Alex F -  APIC-257 - Updated ruleset to support overriding premium pay code when a work code is set
```

