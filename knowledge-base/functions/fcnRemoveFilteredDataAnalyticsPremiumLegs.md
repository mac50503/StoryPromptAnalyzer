# fcnRemoveFilteredDataAnalyticsPremiumLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnRemoveFilteredDataAnalyticsPremiumLegs`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
//Removes premium pay values from the filtered data analytics payComponentList.fcnShow("===>>> IN FUNCTION fcnRemoveFilteredDataAnalyticsPremiumLegs").premiumTypesToRemove is a ArrayList.for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay do{ dutyPeriodPay is some DutyPeriodPay initially it.if ( it.dutyPeriodPayInflightAnalytics <> null and it.dutyPeriodPayInflightAnalytics.filteredDataAnalytics <> null and it.dutyPeriodPayInflightAnalytics.filteredDataAnalytics.payComponentList <> null ) then {for each string in it.dutyPeriodPayInflightAnalytics.filteredDataAnalytics.payComponentList as an array of string do  { value is a string initially it.for each LegPremiumType in LegPremiumType.values() as a fixed array of LegPremiumType do  {if (value.contains(it.toString() as a CharSequence)) then {premiumTypesToRemove.add(value).}}}//Now safely remove the Premium types from the dutyfor each string in premiumTypesToRemove as an array of string do  {fcnShow("fcnRemoveFilteredDataAnalyticsPremiumLegs: Removing premium value: " it).dutyPeriodPay.dutyPeriodPayInflightAnalytics.filteredDataAnalytics.payComponentList.remove(it).}}}
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

