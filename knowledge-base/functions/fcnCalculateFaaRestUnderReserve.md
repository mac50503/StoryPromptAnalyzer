# fcnCalculateFaaRestUnderReserve

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnCalculateFaaRestUnderReserve`

## Propósito
2/16/2015 US18869 Mitesh P - This function calculates FAA Rest for a nonfly trip or duty period that is under a reserve block.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theReportDateTime | DateTime | |
| theAssociatedReserveBlockDutyPeriod | LegalityDutyPeriod | |
| theRestValues | RestValues | |

## Lógica de negocio

```blaze
if (theAssociatedReserveBlockDutyPeriod.legalityTrip <> null) then {// If the first reserve trip is before the first reserve block, rest starts at the prior duty releaseif( theAssociatedReserveBlockDutyPeriod.reportDateTime <> null and  theRestValues.priorDutyRelease is known and     theReportDateTime.isBefore(theAssociatedReserveBlockDutyPeriod.reportDateTime)) then {return fcnGetTimeDiffInMinutes(theRestValues.priorDutyRelease, theReportDateTime).}breakLoop is a boolean initially false.reserveBlock is some LegalityTrip initially theAssociatedReserveBlockDutyPeriod.legalityTrip.firstReserveReport is some DateTime.firstReserveRelease is some DateTime.tenHourRestEffectiveDate is some DateTime initially DateTime.newInstance(2022,7,1,0,0,0).// US20507 - Calculate firstReserveReport by finding the first Reserve Block in a series of consecutive SWA dayswhile (reserveBlock <> null and breakLoop = false) do {if (reserveBlock.priorDayReserveBlock = false) then {firstReserveReport = reserveBlock.firstDutyPeriod.reportDateTime.breakLoop = true.} else {reserveBlock = reserveBlock.priorConsecutiveReserveBlock.}} adjustedReport is some DateTime.if (theRestValues.priorDutyRelease is unknown or                    (theRestValues.priorDutyRelease is not unknown and theRestValues.priorDutyRelease.isBefore(firstReserveReport))) then {// For the first reserve trip under a reserve block and the previous day does NOT have a reserve block -// Always set enough rest so that legalities don't fire for the reserve trip and the reserve blockfrrToReportTimeInMinutes is an integer initially fcnGetTimeDiffInMinutes(firstReserveReport, theReportDateTime).if(theReportDateTime.isAfter(tenHourRestEffectiveDate)) then {if(frrToReportTimeInMinutes < 660) then {if(theRestValues.priorDutyRelease is not unknown) then {return fcnGetTimeDiffInMinutes(theRestValues.priorDutyRelease, theReportDateTime);} else {adjustedReport = theReportDateTime.minusHours(11);return fcnGetTimeDiffInMinutes(adjustedReport, theReportDateTime);}} else {return frrToReportTimeInMinutes;}} else if (frrToReportTimeInMinutes >= 540) then {return frrToReportTimeInMinutes.} else  {// < 9 hours if (theRestValues.previousReducedRestStart)  thenadjustedReport = theReportDateTime.minusHours(10).else // No Previous Reduced RestadjustedReport = theReportDateTime.minusHours(9).return fcnGetTimeDiffInMinutes(adjustedReport, theReportDateTime);} // theRestValues.priorDutyRelease is equal to or after firstDutyReport} else {// If the lastReserveReport is before the report, it was most likely adjusted for a REST nonflyif (theRestValues.lastReserveRelease is not unknown and theRestValues.lastReserveRelease.isBefore(theReportDateTime)) then {if (theRestValues.lastReserveRelease.isAfter(theRestValues.priorDutyRelease)) thenreturn fcnGetTimeDiffInMinutes( theRestValues.lastReserveRelease, theReportDateTime).else if(theRestValues.priorDutyRelease is not unknown) thenreturn fcnGetTimeDiffInMinutes( theRestValues.priorDutyRelease, theReportDateTime).// If the lastReserveRelease is after the Report, we need to look for the previous duty or reserve trip that ended before the Report.  No comparison with lastReserveReport here} else if (theRestValues.priorDutyRelease is not unknown) then {return fcnGetTimeDiffInMinutes(theRestValues.priorDutyRelease, theReportDateTime).}}}return -1.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)

## Historial de cambios

```
2/16/2015 US18869 Mitesh P - This function calculates FAA Rest for a nonfly trip or duty period that is under a reserve block.
4/9/2015 - US20507 - Melissa S - Updated logic for first thing under a reserve block - if previous day is also a reserve block
4/15/2015 - US20507 Melissa S - Updated rest under reserve calculations to go back to the first day of a consecutive group of reserve blocks, regardless of if they are linked
5/11/2015 - US20172 Mitesh P - Moved the entire logic to theAssociatedReserveBlockDutyPeriod.legalityTrip &lt;&gt; null block as legalityTrip will always be associated with duty Period.
```

