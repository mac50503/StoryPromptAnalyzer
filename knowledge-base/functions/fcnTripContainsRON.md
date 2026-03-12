# fcnTripContainsRON

## Metadata
- **Tipo**: SRL Function
- **Retorna**: boolean
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnTripContainsRON`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayTrip <> null and aPayTrip.dutyPeriodList <> null and aPayTrip.dutyPeriodList.size() > 0) then {for each PayDutyPeriod in aPayTrip.dutyPeriodList as an array of PayDutyPeriod do {if (it.dutyType <> unknown and it.dutyType =(ignoring case)"RON") thenreturn true.}}return false.
```

## Llamado por

- [fcnSetPayTripTransientTerms](fcnSetPayTripTransientTerms.md)

