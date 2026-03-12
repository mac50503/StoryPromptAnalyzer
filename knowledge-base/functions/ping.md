# ping

## Metadata
- **Tipo**: SRL Function
- **Retorna**: RuleResult
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\ping`

## Propósito
*(Sin descripción)*

## Lógica de negocio

```blaze
theRuleResult is some RuleResult initially a RuleResult.theMessage is some RuleMessage initially a RuleMessage.theMessage.messageText = "Ping successful...".theRuleResult.ruleMessageList.add(theMessage).return(theRuleResult).
```

## Llamado por

- [fcnCalculateDutyPeriodContributionForProductivityPay](fcnCalculateDutyPeriodContributionForProductivityPay.md)
- [fcnCalculateTripContributionForProductivityPay](fcnCalculateTripContributionForProductivityPay.md)
- [fcnCreateInflightTripSets](fcnCreateInflightTripSets.md)
- [fcnDetermineDutyPeriodTransientTerms](fcnDetermineDutyPeriodTransientTerms.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnGetOverlappingTrips](fcnGetOverlappingTrips.md)

