# rsCalculateNonFlyPayBuckets

## Metadata
- **Tipo**: SRL Ruleset
- **Retorna**: N/A
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Rulesets\rsCalculateNonFlyPayBuckets`

## Propósito
MP:08/282014:This ruleset determines the nonfly pay bucket calculations: basePay, payValue, and payRate.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| theSwaHolidayList | List<SwaHoliday> | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Historial de cambios

```
MP:08/282014:This ruleset determines the nonfly pay bucket calculations: basePay, payValue, and payRate.
US16570, US16571, US16573, US16575, US16577, US16579, US16576, US16580, US16581, US16584, US16586, US16569, US16587, US16589, US16588, US16590, US18042
10/21/2014 Melissa S.  Refactored 4 similar functions into fcnDistributeToPayBucket (Removed fcnAddToPayBucket, fcnCalculateNonFlyPayBucket, fcnCalculatePremiumPayBucket)
14 Jan 2015 Tim A. DE5700 - modified rules ruleRegularBucket2 and ruleRegularBucket3 and added new rules ruleRegularBucket4 and ruleRegularBucket5
1/17/2017 Rachel Starfield  - CREW-147 - Updated Training rules with new V and E label logic.
1/19/2017 Rachel Starfield - CREW-62 - Updated Company Convenience rules with TA, MM, and MMA nonfly code rules.
1/31/2017 Rachel Starfield - CREW-62 - Adding MM and MMA to holiday bucket rules.
10/18/2017 Usha.D    -   Crew-3380-Adding SLR code to sick buckets
11/11/20 - Rachel Starfield - CREWT-5 - Adding ETO2/ETO4 to ETOBUCKET and EXT2/EXT4 to EETOBUCKET
06/08/22 - Alex Frank - APIC-480 - Added new rule for FADAP
APIC-784 - Utsav Malik, Henry Asare, and Alex Frank- 07/14/2023 - Added new nonfly code LINK to allowed nonflies
APIC-1219 - Pradip C - 08/06/2024 - Added ruleCompanyConvenienceBucket13 for PMA
APIC-1303 - Palak Gupta - 07/07/2024 Added ruleCompanyConvenienceBucket14 for PPL
APIC-1403 - Pradip Chatterjee - Removed Duty Hour calculation for PMA and PPL
APIC-1382 - Pradip Chatterjee - 11/04/2024 - Added new bucket PMA and PPL
APIC-1305 - Palak Gupta - 11/12/2024 Added rulesick9 rulesick10 for PLNS
APIC-1377 - Palak Gupta - 11/21/2024 Added PMA and PPL back to CNBUCKET along with new nonfly NCOI in ruleCNBucket
APIC-1420 -Sudha Chaturvedi - 12/17/2024 Added  HTAS rule CNBucket
APIC-1424 -Sudha Chaturvedi - 12/24/2024 Added  WTL rule CNBucket
APIC-1430 -Palak Gupta - 01/16/2025 Added  IDL rule CNBucket
APIC-1455 -Sudha Chaturvedi - 05/26/2025 Added  FTS to ruleCompanyConvenienceBucket1&amp; ruleCompanyConvenienceBucket2.
```

