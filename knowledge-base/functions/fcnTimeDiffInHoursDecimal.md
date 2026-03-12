# fcnTimeDiffInHoursDecimal

## Metadata
- **Tipo**: SRL Function
- **Retorna**: real
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnTimeDiffInHoursDecimal`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| aDateTime1 | DateTime | |
| aDateTime2 | DateTime | |

## Lógica de negocio

```blaze
diff is a real initially aDateTime2.millis - aDateTime1.millis.//diffMinutes is a real  initially diff / (60 * 1000).diffHours is an real  initially  diff / (60 * 60 * 1000).return diffHours.
```

## Llamado por

- [fcnCalculateConusAndOconusPay](fcnCalculateConusAndOconusPay.md)
- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)

