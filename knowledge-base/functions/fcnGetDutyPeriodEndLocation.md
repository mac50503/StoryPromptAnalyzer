# fcnGetDutyPeriodEndLocation

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\CommonPay\Functions\fcnGetDutyPeriodEndLocation`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aPayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
if (aPayDutyPeriod <> null and aPayDutyPeriod.lastLeg <> null) thenreturn aPayDutyPeriod.lastLeg.arrivalLocation.elsereturn "".
```

