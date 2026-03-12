# fcnGetDHRStartDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetDHRStartDateTime`

## Propósito
10/6/2015 - DE7555 - Melissa S - New function for DHR start logic - moved from multiple other locations

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
dhrStartDateTime is some DateTime initially thePayDutyPeriod.reportDateTime.if (thePayDutyPeriod.firstLeg <> null) then {if (thePayDutyPeriod.firstLeg.legWorkCodeList.contains("RS")) then {dhrStartDateTime = thePayDutyPeriod.firstLeg.scheduledDepartureDateTime.minusMinutes(thePayDutyPeriod.variableReportMinutes).fcnShow("===>>> First leg of duty period " thePayDutyPeriod.sequenceNumber   " is an RS deadhead so setting dhrStartDateTime to leg skd dep - variable report minutes = "     thePayDutyPeriod.firstLeg.scheduledDepartureDateTime " - " thePayDutyPeriod.variableReportMinutes "  = " dhrStartDateTime).}}return dhrStartDateTime.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateDHR](fcnCalculateDHR.md)

## Historial de cambios

```
10/6/2015 - DE7555 - Melissa S - New function for DHR start logic - moved from multiple other locations
```

