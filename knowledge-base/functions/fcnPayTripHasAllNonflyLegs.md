# fcnPayTripHasAllNonflyLegs

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnPayTripHasAllNonflyLegs`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aTrip is not equal to null and    aTrip.dutyPeriodList is not equal to null and    aTrip.dutyPeriodList.size() > 0) then{for each PayDutyPeriod in aTrip.dutyPeriodList as an array of PayDutyPeriod do {if (it.legList is not equal to null and it.legList.size() > 0) then {for each PayLeg in it.legList as an array of PayLeg do {if (it.nonFlyCode = "" or it.nonFlyCode =null or it.nonFlyCode =unknown) then {return false.}}}}}return true.
```

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)

