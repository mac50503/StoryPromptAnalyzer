# fcnXrefPayDutyPeriodToPayTrip

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayDutyPeriodToPayTrip`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |
| aPayTrip | PayTrip | |

## Lógica de negocio

```blaze
if (aPayDutyPeriod <> null and aPayTrip <> null) thenaPayDutyPeriod.payTrip = aPayTrip.
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)

