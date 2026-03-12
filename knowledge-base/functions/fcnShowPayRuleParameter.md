# fcnShowPayRuleParameter

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnShowPayRuleParameter`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| thePayRuleParameter | PayRuleParameter | |

## Lógica de negocio

```blaze
fcnShow("===>>>   StandardTripMileage  = " thePayRuleParameter.standardTripMileage).fcnShow("===>>>   NonStandardTripMileage  = " thePayRuleParameter.nonStandardTripMileage).fcnShow("===>>>   StandardTripCredit  = " thePayRuleParameter.standardTripCredit).fcnShow("===>>>   NonStandardTripMultiplier  = " thePayRuleParameter.nonStandardTripMultiplier).fcnShow("===>>>   OverscheduleStandardMinutes  = " thePayRuleParameter.overscheduleStandardMinutes).fcnShow("===>>>   OverscheduleStandardAdder  = " thePayRuleParameter.overscheduleStandardAdder).fcnShow("===>>>   OverscheduleOverrideDivisor  = " thePayRuleParameter.overscheduleOverrideDivisor).fcnShow("===>>>   OverflyStandardMinutes  = " thePayRuleParameter.overscheduleOverrideMultiplier).fcnShow("===>>>   NonStandardTripMileage  = " thePayRuleParameter.overflyStandardMinutes).fcnShow("===>>>   OverflyStandardMultiplier  = " thePayRuleParameter.overflyStandardMultiplier).
```

## Dependencias

Esta function llama a:

- [fcn](fcn.md)
- `fcnShow()`

