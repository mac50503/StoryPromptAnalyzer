# fcnXrefPayLegToPayDutyPeriod

## Metadata
- **Tipo**: SRL Function
- **Retorna**: void
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnXrefPayLegToPayDutyPeriod`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayLeg | PayLeg | |
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (aPayLeg <> null and aPayDutyPeriod <> null) thenaPayLeg.payDutyPeriod = aPayDutyPeriod.
```

## Llamado por

- [fcnCreateTripPay](fcnCreateTripPay.md)

