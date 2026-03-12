# fcnCalculateTripDutyHours

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateTripDutyHours`

## Propósito
01/12/2025 APIC-1686 Use baseNonFlyGenericCode for all Nonfly Base

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
theDutyHours is a real initially 0.0;nonflysWithDutyHours is a string initially ";AS1;ASB1;ASB2;ASB3;ASB4;BO;BUS;CC;HTAS;WTL;IDL;NCOI;PMA;PPL;CCP;CISM;CN;FDAP;HOTL;IN;LINK;MM;MMA;MTG;PT;RNU;RTS;SPP;STQ;TA;TR;";//Note: HS accrues duty hours but this calculation is done in rsDetermineNonflyAssignmentCreditsif(theTripPay.dutyPeriodPayList <> null and (theTripPay.nonFlyCode = null or theTripPay.nonFlyCode = "")) then {for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do {        theDutyHours += fcnGetTimeDiffInMinutes(it.reportDateTime, it.releaseDateTime);    }theTripPay.dutyHours = theDutyHours;}else if(fcnGetBaseNonFlyGenericCode(theTripPay.nonFlyCode) <> null ornonflysWithDutyHours.replaceAll("\\s","") contains match (ignoring case)";"theTripPay.nonFlyCode";") then{theTripPay.dutyHours = fcnGetTimeDiffInMinutes(theTripPay.beginDateTime, theTripPay.endDateTime);}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnGetBaseNonFlyGenericCode](fcnGetBaseNonFlyGenericCode.md)
- [fcnGetTimeDiffInMinutes](fcnGetTimeDiffInMinutes.md)
- [rsDetermineNonflyAssignmentCredits](rsDetermineNonflyAssignmentCredits.md)

## Historial de cambios

```
APIC-480 - Alex Frank - 06/08/2022 - Added FADAP
APIC-737 - Team APIC- 07/12/2023- Added LINK
APIC-1219 - Pradip C - 08/06/2024 - 08/06/2024 - Added PMA to nonflysWithDutyHours
APIC-1303 - Palak Gupta - 07/07/2024 -- Added PPL to nonflysWithDutyHours
APIC-1377 - Palak Gupta - 11/13/2024 -- Added NCOI to nonflysWithDutyHours
APIC-1420 -Sudha Chaturvedi - 12/17/2024 -- Added HTAS to nonflysWithDutyHours
APIC-1424 -Sudha Chaturvedi - 12/24/2024 -- Added WTL to nonflysWithDutyHours
APIC-1430 -Palak Gupta - 01/16/2025 -- Added IDL to nonflysWithDutyHours
01/12/2025 APIC-1686 Use baseNonFlyGenericCode for all Nonfly Base
```

