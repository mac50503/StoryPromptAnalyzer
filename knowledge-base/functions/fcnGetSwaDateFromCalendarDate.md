# fcnGetSwaDateFromCalendarDate

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetSwaDateFromCalendarDate`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| sourceDate | DateTime | |
| startOfDay | boolean | |

## Lógica de negocio

```blaze
retVal is some DateTime initially sourceDate.if (sourceDate <> null) then{if (startOfDay = true) thenretVal = DateTime.newInstance(sourceDate.year, sourceDate.monthOfYear, sourceDate.dayOfMonth, 3, 0).  // same day as source set time to 3 AMelse{nextDay is some DateTime initially sourceDate.plusDays(1)./// next day as source set time to 3 am; Making this 3 am because Joda will crash if a date is created between 2 and 3 am on a day light saving dayretVal = DateTime.newInstance(nextDay.year, nextDay.monthOfYear, nextDay.dayOfMonth, 3, 00).  }}return retVal.
```

## Llamado por

- [fcnDistributePerdiemPayToDutyPeriods](fcnDistributePerdiemPayToDutyPeriods.md)

