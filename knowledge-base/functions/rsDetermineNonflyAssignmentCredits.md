# rsDetermineNonflyAssignmentCredits

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsDetermineNonflyAssignmentCredits`

## Propósito
US16560 - MP - 07/17/2014 - This ruleset determines the pay credit values for nonfly assignments.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayTrip | PayTrip | |
| theTripPay | TripPay | |
| theTripPayList | List<TripPay> | |
| tripIndex | integer | |
| theGlobalDataCache | GlobalDataCache | |
| thePayTripList | List<PayTrip> | |

## Llamado por

- [fcnCalculateTripDutyHours](fcnCalculateTripDutyHours.md)

## Historial de cambios

```
US16560 - MP - 07/17/2014 - This ruleset determines the pay credit values for nonfly assignments.
DE4890 - AM - 09/09/2014 - modified ruleHomeStudyNonflyCredits rule to fix trip referencing error.
DE5077 - TA - removed credit tyoe condition from rules ruleAirportStandbyNonflyCredits1 and ruleAirportStandbyNonflyCredits2
DE5077 - removed action theTripPay.payValue = math().min(tempCredit, 5) from rules  ruleAirportStandbyNonflyCredits1 and ruleAirportStandbyNonflyCredits2
10/31/2014 Corey gu US18818 - modified ruleAirportStandbyNonflyCredits2 by adding condition hePayTrip.endDateTime.isAfter(thePayTrip.associatedReserveTrip.beginDateTime)
and created ruleAirportStandbyNonflyCredits3.
02/06/2015 Tim A. - DE5942 - modified rule ruleDefaultPaidNonflyCredits to call function fcnGetNonflyDefaultCredits to obtain nonfly default credits
02/06/2015 Tim A. - DE5942 - added rule ruleNonflyWithoutDefaultCredits
03/24/2015 Ben Lang - DE6115 - Added rule ruleDefaultPaidNonflyCredits2. Changed ruleDefaultPaidNonflyCredits to ruleDefaultPaidNonflyCredits1.
1/13/2017 Rachel Starfield - CREW-733 - Changed hardcoding of HS pay to call fcnGetNonflyDefaultCredits("HS").
1/16/2017 Rachel Starfield - CREW-147 - Added new Default Paid Nonfly Credits rules.
1/27/2017 Rachel Starfield - CREW-147 - Updated to make U behave like V.
06/11/2017 - Tim A. - CREW-63 - added rule ruleHomeStudyNonflyCreditsFromGlobalDataCache
6/23/2017 - Rachel Starfield - CREW-2195 - Fixed forced premium pay
6/29/2017 Rachel Starfield - CREW-2195 - Only 1.5 pay for U label for MM and MMA
03/05/2025 Palak Gupta -APIC-1477- added a check for credit Type &lt;&gt; F in ruleAirportStandbyNonflyCredits1, ruleAirportStandbyNonflyCredits2 and ruleAirportStandbyNonflyCredits3 with effective dates.
```

