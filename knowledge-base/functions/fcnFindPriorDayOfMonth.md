# fcnFindPriorDayOfMonth

## Metadata
- **Tipo**: SRL Function
- **Retorna**: DateTime
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Legality\InflightLegality\Functions\fcnFindPriorDayOfMonth`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theDate | DateTime | |
| theDayOfMonth | integer | |

## Lógica de negocio

```blaze
theNewDate is some DateTime initially theDate;while (theNewDate.dayOfMonth <> theDayOfMonth) do {theNewDate = theNewDate.minusDays(1);}return theNewDate;
```

