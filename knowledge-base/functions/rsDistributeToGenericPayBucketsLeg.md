# rsDistributeToGenericPayBucketsLeg

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDistributeToGenericPayBucketsLeg`

## Propósito
09/09/2014 Corey Gu - US16585 Initial development.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegPay | LegPay | |
| thePayLeg | PayLeg | |
| theDutyPeriod | PayDutyPeriod | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| thePayTrip | PayTrip | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |
| theGlobalDataCache | GlobalDataCache | |

## Historial de cambios

```
09/09/2014 Corey Gu - US16585 Initial development.
09/22/2014 Corey Gu - US16597 Created ruleRedEye.
09/23/2014 Corey Gu - US16591 Created rule300LoadBonus1 and rule300LoadBonus2.
09/25/2014 Corey Gu - US16593 Created ruleCharterWithFoodService
US18618:MP:10/10/2014:Moved REG/RGA rules from here.
10/16/2014 Corey Gu - US18705 Added pay rate to fcnAddToPayBucket.
11/05/2014 corey Gu US18991 - Use thePayLeg.legPay.positionA  to check position A in ruleSeniorInternational.
11/05/2014 Pedro L.  Update existing Pay Bucket logic to reference the new isPositionA boolean in the rule conditions US18920
11/11/2014 Akshay: Updated 300LoadBonus rules for deadhead legs (US18931)
12/10/2014 Ben L.  Updated regular and holiday bucket rules to use the legBeginInSchedulePeriod variable (DE5696)
12/16/2014 Corey Gu DE5643 - Modified ruleRedEye.
02/26/2014 TIm A. DE5963 - Added condition of not label "I" to 300 load bonus in ruleset rsCalculateGenericPayBucketsLeg
03/10/2045 Pedro L DE5881 - Added logic that adds bucket pay value to a transient field to keep track of what has been distributed already to other buckets besides RGA
6/16/2015 - Ben Lang - DE6669 - Added logic to use the first leg's scheduleDepartureDateTime for Inflight
3/9/2016 - Melissa S - CSCH-2434 - Added check for ruleLodo to also make sure the leg has a language code in order for the lodo pay rule to fire
11/62017 - Mark B - CREW-3740 - Add lodo bonus pay via legPayInflightAnalytics.
06/06/2024 - Sabyasachi - Added Leg Ground Time Pay Logic
```

