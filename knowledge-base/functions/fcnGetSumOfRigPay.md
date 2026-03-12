# fcnGetSumOfRigPay

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetSumOfRigPay`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTripPay | TripPay | |

## Lógica de negocio

```blaze
theSumOfTripRig is a real initially 0.0.for each DutyPeriodPay in theTripPay.dutyPeriodPayList as an array of DutyPeriodPay such that it.rigsGreaterThanPremium dotheSumOfTripRig += it.payValue.return theSumOfTripRig.
```

