# fcnCalculatePremiumOverBasePay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnCalculatePremiumOverBasePay`

## Propósito
Ben Lang - DE6144 - 03/24/2015 - Initial development

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |

## Lógica de negocio

```blaze
premiumOverBasePay is a real initially 0.dutyPeriodPay is some DutyPeriodPay.if (theTrip.dutyPeriodList <> null and theTrip.dutyPeriodList.size() > 0) thenfor each PayDutyPeriod in theTrip.dutyPeriodList as an array of PayDutyPeriod such that it.dutyPeriodPay <> null do {dutyPeriodPay = it.dutyPeriodPay.//----------------------DE6417 -Removing thsi check -> if (dutyPeriodPay.sumLegPremiumCredits <> 0.0) then {premiumOverBasePay += dutyPeriodPay.payValue - dutyPeriodPay.basePay.fcnShow("Found premium of " (dutyPeriodPay.payValue - dutyPeriodPay.basePay) " = " dutyPeriodPay.payValue " (payValue) - " dutyPeriodPay.basePay " (basePay) on duty period reporting on " it.reportDateTime).}return premiumOverBasePay.
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

## Historial de cambios

```
Ben Lang - DE6144 - 03/24/2015 - Initial development
Akshay Mishra - DE6417 - 04/28/2015 - Removed the check dutyPeriodPay.sumLegPremiumCredits &lt;&gt; 0.0 before setting the premiumOverBasePay, since the premium may be because the Duty Pay got set to DHR or DPM, even when the seum of leg premiums is 0.
```

