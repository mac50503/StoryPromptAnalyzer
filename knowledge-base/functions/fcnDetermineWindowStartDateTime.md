# fcnDetermineWindowStartDateTime

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnDetermineWindowStartDateTime`

## Propósito
03/16/2015 Corey Gu US16625/US16626

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| windowEndDateTime | DateTime | |
| daysInWindow | integer | |

## Lógica de negocio

```blaze
windowStartDateTime is some DateTime.// Window ends on the Previous SWA day – need to go back an extra calendar day for the window startif (windowEndDateTime.toLocalDateTime().hourOfDay < 3) then {windowStartDateTime = windowEndDateTime.minusDays(1).windowStartDateTime = windowStartDateTime.withTime(3,0,0,0).minusDays(daysInWindow-1).} else // Window ends on the current SWA daywindowStartDateTime = windowEndDateTime.withTime(3,0,0,0).minusDays(daysInWindow-1).return windowStartDateTime.
```

## Historial de cambios

```
03/16/2015 Corey Gu US16625/US16626
```

