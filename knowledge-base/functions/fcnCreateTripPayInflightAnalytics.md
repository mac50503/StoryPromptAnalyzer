# fcnCreateTripPayInflightAnalytics

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCreateTripPayInflightAnalytics`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTripPay | TripPay | |

## Lógica de negocio

```blaze
fcnShow("===>>> ENTERING function fcnCreateTripPayInflightAnalytics...").if (aTripPay <> null) then{aTripPay.tripPayInflightAnalytics = a TripPayInflightAnalytics.if (aTripPay.dutyPeriodPayList.size() > 0) then{aDutyPeriodPay is some DutyPeriodPay initially null.aLegPay is some LegPay initially null.for each DutyPeriodPay in aTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{aDutyPeriodPay = it.aDutyPeriodPay.dutyPeriodPayInflightAnalytics = a DutyPeriodPayInflightAnalytics.if (aDutyPeriodPay.legPayList.size() > 0) then{for each LegPay in aDutyPeriodPay.legPayList as an array of LegPay do{aLegPay = it.aLegPay.legPayInflightAnalytics = a LegPayInflightAnalytics.aLegPay.legPayInflightAnalytics.legIsDeadhead = fcnIsInflightDeadhead(aLegPay.payLeg).aLegPay.legPayInflightAnalytics.tripLabel = aTripPay.payTrip.assignmentLabel.}}}}//fcnShow("===>>> created TripPayInflightAnalytics object for " aTripPay.tripNameAndDate).}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- [fcnCreateTripPay](fcnCreateTripPay.md)
- [fcnIsInflightDeadhead](fcnIsInflightDeadhead.md)
- `fcnShow()`

## Llamado por

- [fcnCreateSchedulePeriodPayInflightAnalytics](fcnCreateSchedulePeriodPayInflightAnalytics.md)

