# fcnIsCharter

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnIsCharter`

## Propósito
APIC-1501 -07/11/2025 - Santosh Kudumu - New function to check for charter on trip class and leg workcode list.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING fcnIsCharterLeg with Leg =>..." aPayTrip.tripName);retVal is a boolean initially false.if (aPayTrip <> null and aPayTrip.tripClass= ("C" or "L")) then {retVal = true.}else { if(aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do {if (it.legList.size() > 0 and at least 1 PayLeg in it.legList as an array of PayLeg satisfies it.legWorkCodeList.contains("CT") )then {retVal=true;}}}}return retVal.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Llamado por

- [fcnCalculateThrAndAdgAndDhr](fcnCalculateThrAndAdgAndDhr.md)

## Historial de cambios

```
APIC-1501 -07/11/2025 - Santosh Kudumu - New function to check for charter on trip class and leg workcode list.
```

