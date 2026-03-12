# fcnSetLegPositionA

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnSetLegPositionA`

## Propósito
05/07/2015 Akshay M: DE6491 - Added Trip Class = P check.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theLegPay | LegPay | |

## Lógica de negocio

```blaze
// my Trip's Class = P or my Trip's Position = FAA or my Leg's Workcode includes "PA" or my Leg's Positon = FAAif (theLegPay.payLeg.payDutyPeriod.payTrip.tripClass = "P" or    //--------->Added as per DE6491     (theLegPay.payLeg.payLegInflight <> null and theLegPay.payLeg.payLegInflight.crewPosition = "FAA") or     theLegPay.payLeg.legWorkCodeList.contains("PA")) then{theLegPay.positionA = true.theLegPay.dutyPeriodPay.positionA = true;   //// IF ANY LEGS IN A DP ARE POSITION A THEN THE DP IS POSITION A...}elsetheLegPay.positionA = false.fcnShow("===>>> Exiting fcnSetLegPositionA ...positionA for Leg " theLegPay.sequenceNumber "  = " theLegPay.positionA).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
05/07/2015 Akshay M: DE6491 - Added Trip Class = P check.
```

