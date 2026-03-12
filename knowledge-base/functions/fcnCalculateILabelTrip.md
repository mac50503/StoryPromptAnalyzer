# fcnCalculateILabelTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculateILabelTrip`

## Propósito
12/10/2014 Corey Gu DE5683 - Added code to assign 0 to dutyPeriodPay's payValue and legPay's payValue.

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Lógica de negocio

```blaze
fcnShow("===>>> IN FUNCTION fcnCalculateILabelTrip WITH TRIP " theTrip.tripName " ...LABEL = " theTrip.assignmentLabel).if (theTrip.tripPay <> null and theTrip.tripPay<>unknown) then  {theTrip.tripPay.payValue = 0.0.for each DutyPeriodPay in theTrip.tripPay.dutyPeriodPayList  as an array of DutyPeriodPay do{it.payValue = 0.0.for each LegPay in it.legPayList as an array of LegPay doit.payValue = 0.0.}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
12/10/2014 Corey Gu DE5683 - Added code to assign 0 to dutyPeriodPay's payValue and legPay's payValue.
```

