# rstQualificationTimes

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Qualifications\Rulesets\rstQualificationTimes`

## Propósito
11/4/2014 - MS - US18846 - Initial ruleset development, added HGST Qualification rule

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegalityLegs | List<LegalityLeg> | |
| theQualificationResult | QualificationResult | |
| theNinetyDayQualEffectiveDateTime | DateTime | |
| theTransactionDateTime | DateTime | |
| theCrewId | integer | |

## Historial de cambios

```
11/4/2014 - MS - US18846 - Initial ruleset development, added HGST Qualification rule
11/5/2014 - MS - US18847 - Added HGSL Qualification rule
11/5/2014 - MS - US18845 - Added PLT 737 rule
11/5/2014 - MS - US18929 - Added Special Station Qualification rule
04/27/2015 Corey Gu - Production issue. Need add the oldest flight of the consecutive 3 flights to theQualiicationResult.
6/15/2014 - DE6814 - Melissa S - Special Station Quals should include the effectiveDate as "Day 1", so we have to use expiresInDays-1 for the expiration date calculation.
7/20/2015 - Melissa S - US21136/US21146 - Effective dated existing PLT737 rule, and added new PLT737 rule that considers takeoffs/landings for the pilot only
10/3/2016 - RS - CSCH-3918 - Setting SecondOfMinute to 0 when checking against qualification effective datetime.
```

