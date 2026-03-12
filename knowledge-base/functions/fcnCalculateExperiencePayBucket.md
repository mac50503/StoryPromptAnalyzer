# fcnCalculateExperiencePayBucket

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateExperiencePayBucket`

## Propósito
DE5694 - Ben Lang - 12/11/2014 - Add basePay of a DutyPeriod to the EXP bucket if it is greater than the sumLegTotalCredits

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayCrewMember | PayCrewMember | |
| theSchedulePeriodPay | SchedulePeriodPay | |
| theTripPayList | List<TripPay> | |
| reportFilterStart | DateTime | |
| reportFilterEnd | DateTime | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnCalculateExperiencePayBucket ... SP = " theSchedulePeriodPay.schedulePeriodName " ...yearsOfExperience = " thePayCrewMember.payCrewMemberInflight.yearsOfExperience " ...count of trips = " theTripPayList.size()).if (thePayCrewMember.payCrewMemberInflight.yearsOfExperience >= 25) then {reserveGuarantyAdded is a real initially 0.0.reserveGuarantyDiff is a real initially 0.0.legsCreditWithCT is an real initially 0.0. //Keep track of the leg's credit with legWorkCode of CT for a given Duty PeriodbaseCreditToAdd is a real initially 0.0. //Variable to calculate the credit to be added to the EXPBUCKETlegPremium is a real initially 0.0.aTripPay is some TripPay initially a TripPay.tripName is a string initially "".experiencePayEvenDateTime is some DateTime initially null.noflyCodesToExclude is a string initially ";BO;BUS;CC;HTAS;WTL;IDL;NCOI;PMA;PPL;CCP;CCS;CCR;CISM;CN;EFL;EFLV;FDAP;FI1;FI2;FI3;FI4;FI5;FP1;FP2;FP3;FP4;FP5;FTC;FTS;HOTL;HS;".noflyCodesToExclude = noflyCodesToExclude "IL;IN;IP;JD;JRY;LINK;LMA;LME;PLNS;LVP;MTG;MV;MVVA;PT;RETR;RTS;".noflyCodesToExclude = noflyCodesToExclude "SCK;SKA;SL1;SLP;PFS;SPP;STQ;TR;VA;VAPO;WCI;WCN;WCP;WCS;MM;MMA;TA;EXT2;EXT4;ETO2;ETO4;".for each TripPay in theTripPayList as an array of TripPay such that (((fcnIsNonFlyTrip(it.payTrip) and it.tripPayInflight.paidNonFly = "Y") or fcnIsNonFlyTrip(it.payTrip) = false) and it.tripClass <> "C" and it.tripClass <> "L"  and it.assignmentLabel <> "I"  and(fcnGetBaseNonFlyGenericCode(it.nonFlyCode) = null andnoflyCodesToExclude.replaceAll("\\s","") contains match (ignoring case)";"it.nonFlyCode"." is equal to false)) do {aTripPay = it.//NonFly trips                       if (fcnIsNonFlyTrip(it.payTrip)) then                       {                        fcnShow("Trip " tripName " nonflyCode " aTripPay.nonFlyCode " and beginDateTime " aTripPay.beginDateTime " sumDutyCredits " aTripPay.sumDutyPeriodCredits).                                  if (nonFlyCode = ("AS1" or "ASB1" or "ASB2" or "ASB3" or "ASB4")) then                                  {                                          fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 1... fcnCalculateExperiencePayBuckets .standby nonfly trip.. SP = " theSchedulePeriodPay.schedulePeriodName " ...adding trip " tripName "'s this payValue " aTripPay.payValue " to base value of EXPBUCKET...").                                                                                                                                         fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", aTripPay.payValue, 1.5, aTripPay.beginDateTime, reportFilterStart, reportFilterEnd,aTripPay).                                  }                                  else                                  {                                            fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 2... fcnCalculateExperiencePayBuckets .standby nonfly trip.. SP = " theSchedulePeriodPay.schedulePeriodName " ...adding trip " tripName "'s this payValue " aTripPay.payValue " to base value of EXPBUCKET...").                                                                                                                                     fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", aTripPay.basePay, 1.5, aTripPay.beginDateTime, reportFilterStart, reportFilterEnd,aTripPay).                                  }                       }fcnShow("===>>> Trip " tripName "... SP = " theSchedulePeriodPay.schedulePeriodName "...is nonfly? = " fcnIsNonFlyTrip(it.payTrip)).//Not nonfly tripsif (fcnIsNonFlyTrip(it.payTrip) = false) then{experiencePayEvenDateTime = fcnGetEventDateForExperiencePay(aTripPay, reportFilterStart, reportFilterEnd).fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 3... fcnCalculateExperiencePayBuckets  in Trip " tripName "... SP = " theSchedulePeriodPay.schedulePeriodName "...reportFilterStart = " reportFilterStart "...reportFilterEnd = " reportFilterEnd).// If a forced split trip                                            if (aTripPay.basePay > aTripPay.tripPayInflight.baseDutyPeriodSum and aTripPay.lastMonthPay > 0 and aTripPay.creditType = "F") then                                            {baseCreditToAdd = aTripPay.basePay.                                                           for each DutyPeriodPay in it.dutyPeriodPayList as an array of DutyPeriodPay                                                                                such that ((fcnDoesDutyPeriodPayBeginInSchedulePeriodPay(it, theSchedulePeriodPay) and                           fcnIsDateTimeWithinReportFilterRange(it.reportDateTime, reportFilterStart, reportFilterEnd)) = false)     do    {         baseCreditToAdd -= it.basePay.         fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 4... fcnCalculateExperiencePayBuckets ... subtract duty period " it.sequenceNumber "'s base pay of " it.basePay " from baseCreditToAdd ...value now = " baseCreditToAdd).                                                             }                                             fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 5... fcnCalculateExperiencePayBuckets ... SP = " theSchedulePeriodPay.schedulePeriodName " ...Trip " tripName "...credit type = " aTripPay.creditType "...basePay to add " baseCreditToAdd "...beginDateTime " aTripPay.beginDateTime "...reportFilterStart " reportFilterStart "...reportFilterEnd " reportFilterEnd).                                                        fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", baseCreditToAdd, 1.5, experiencePayEvenDateTime, reportFilterStart, reportFilterEnd,aTripPay).                                             }                                             //No split and forced trip                                             else if (aTripPay.creditType = "F" and aTripPay.nextMonthPay = 0.0 and aTripPay.lastMonthPay = 0.0 and aTripPay.basePay <> aTripPay.tripPayInflight.baseDutyPeriodSum) then                                             {                                             fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 6...fcnCalculateExperiencePayBuckets ..forced trip no split. SP = " theSchedulePeriodPay.schedulePeriodName " ...Trip " tripName "...credit type" aTripPay.creditType "...basePay to add " aTripPay.basePay "...beginDateTime " aTripPay.beginDateTime "...reportFilterStart " reportFilterStart "...reportFilterEnd " reportFilterEnd).fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", aTripPay.basePay, 1.5, experiencePayEvenDateTime, reportFilterStart, reportFilterEnd, aTripPay).                                             }else{baseCreditToAdd =  fcnGetExperiencePayContribution(aTripPay, theSchedulePeriodPay, reportFilterStart, reportFilterEnd).fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", baseCreditToAdd, 1.5, experiencePayEvenDateTime, reportFilterStart, reportFilterEnd, aTripPay).                                                           fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 7 ...fcnCalculateExperiencePayBuckets ..non-forced trip ...SP = " theSchedulePeriodPay.schedulePeriodName " ...Trip " tripName "...credit type" aTripPay.creditType "...baseCreditToAdd = " baseCreditToAdd  " ...EXPBUCKET's baseValue = " theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue).}}//Add ON and ONA buckets to the EXPBUCKET (adding RON Rig to EXP).  This is only for the trips that have RON RIGsumRONRig is a real initially math().max(it.payTrip.onBucketAmount + it.payTrip.onaBucketAmount, 0).if (sumRONRig > 0.0) then{fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 8... fcnCalculateExperiencePayBuckets... SP = " theSchedulePeriodPay.schedulePeriodName " ...adding sum of ON and ONA buckets of " sumRONRig " to base value of EXPBUCKET...").fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", sumRONRig, 1.5, experiencePayEvenDateTime, reportFilterStart, reportFilterEnd,aTripPay).}}fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 9... fcnCalculateExperiencePayBuckets ..remainingReserveGuaranty = " theSchedulePeriodPay.remainingReserveGuaranty).//Add the remaining reserve guaranty to the EXPBUCKETif (theSchedulePeriodPay.remainingReserveGuaranty > 0.0) then{fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 10... fcnCalculateExperiencePayBuckets ...reserves SP = " theSchedulePeriodPay.schedulePeriodName " ...adding remaining reserve guaranty of  " theSchedulePeriodPay.remainingReserveGuaranty  " to base value of EXPBUCKET...").fcnAddToBaseOfPayBucket(theSchedulePeriodPay, "EXPBUCKET", theSchedulePeriodPay.remainingReserveGuaranty, 1.5, experiencePayEvenDateTime, reportFilterStart, reportFilterEnd, null).}// TUX ROUNDS UP EXP AT HALF SO WE ARE DOING THE SAME HERE...fcnShow("===>>> fcnCalculateExperiencePayBucket - CODE BLOCK 11... fcnCalculateExperiencePayBuckets ...just before rounding " theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue * 1.5 " to 2 decimal places, up at half..." ).theSchedulePeriodPay.getPayBucket("EXPBUCKET").payValue = fcnRoundUpAt2DecimalPlaces(theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue * 1.5).}fcnShow("===>>> EXITING fcnCalculateExperiencePayBucket ... SP = " theSchedulePeriodPay.schedulePeriodName " ...EXPBUCKET's baseValue = " theSchedulePeriodPay.getPayBucket("EXPBUCKET").baseValue ", payValue = " theSchedulePeriodPay.getPayBucket("EXPBUCKET").payValue ", payRate = " theSchedulePeriodPay.getPayBucket("EXPBUCKET").payRate).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnAddToBaseOfPayBucket](fcnAddToBaseOfPayBucket.md)
- [fcnDoesDutyPeriodPayBeginInSchedulePeriodPay](fcnDoesDutyPeriodPayBeginInSchedulePeriodPay.md)
- [fcnGetBaseNonFlyGenericCode](fcnGetBaseNonFlyGenericCode.md)
- [fcnGetEventDateForExperiencePay](fcnGetEventDateForExperiencePay.md)
- [fcnGetExperiencePayContribution](fcnGetExperiencePayContribution.md)
- [fcnIsDateTimeWithinReportFilterRange](fcnIsDateTimeWithinReportFilterRange.md)
- [fcnIsNonFlyTrip](fcnIsNonFlyTrip.md)
- [fcnRoundUpAt2DecimalPlaces](fcnRoundUpAt2DecimalPlaces.md)
- `fcnShow()`
- [main](main.md)

## Historial de cambios

```
DE5694 - Ben Lang - 12/11/2014 - Add basePay of a DutyPeriod to the EXP bucket if it is greater than the sumLegTotalCredits
DE5703 - Ben Lang - 12/18/2014 - Going back to original design. Add up buckets' bases to get the base Value of the EXPBUCKET.
DE5867 - Tim A. - 02/19/2015 - refactored function to add DP base pay, no charters plus any applicable trip rig
CSCH-2160 - Tim A. - 03/08/2018 - make sure that a crew working a trip for premium does not get LESS EXP pay than a crew working the same trip for straight time
CREW-62 - Rachel Starfield - 1/24/2017 - Added new nonfly codes MM, MMA, and TA
CREWT-5 - Rachel Starfield - 11/11/2020 - Added ETO2/ETO4/EXT2/EXT4
APIC-480 - Alex Frank - 06/08/2022 - Added FADAP
APIC-1219 - Pradip C - 08/06/2024 - Added PMA to noflyCodesToExclude
APIC-1303 - Palak Gupta - 07/07/2024 - Added PPL to noflyCodesToExclude
APIC-1305 - Palak Gupta - 11/12/2024 Added PLNS to noflyCodesToExclude
APIC-13077 - Palak Gupta - 11/20/2024 Added NCOI to noflyCodesToExclude
APIC-1448 - Palak Gupta - 12/19/2024 Added CCP to noflyCodesToExclude
APIC-1420 - Palak Gupta - 12/23/2024 Added HTAS to noflyCodesToExclude
APIC-1424 - Sudha Chaturvedi - 12/24/2024 Added WTL to noflyCodesToExclude
APIC-1430 - Palak Gupta - 01/16/2025 Added IDL to noflyCodesToExclude
APIC-1555 - Palak Gupta - 05/23/2025 Added FTS to noflyCodesToExclude
```

