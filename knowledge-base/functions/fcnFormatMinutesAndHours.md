# fcnFormatMinutesAndHours

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnFormatMinutesAndHours`

## Propósito
US14133 - 9/27/2013 - Melissa - Changed to use string formatter

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| minutes | integer | |

## Lógica de negocio

```blaze
if (minutes >=0) then {if ((minutes div 60) = 0) then {return(""String.format("%02d:%02d", a fixed array of 2 Object initially {it[0]=(minutes div 60) as an Object, it[1]=(minutes mod 60) as an Object})).} else {return(""String.format("%01d:%02d", a fixed array of 2 Object initially {it[0]=(minutes div 60) as an Object, it[1]=(minutes mod 60) as an Object})).}} else {if ((minutes div 60) = 0) then {return(""String.format("-%02d:%02d", a fixed array of 2 Object initially {it[0]=(math().abs(minutes) div 60) as an Object, it[1]=(math().abs(minutes) mod 60) as an Object})).} else {return(""String.format("-%01d:%02d", a fixed array of 2 Object initially {it[0]=(math().abs(minutes) div 60) as an Object, it[1]=(math().abs(minutes) mod 60) as an Object})).}}
```

## Historial de cambios

```
US14133 - 9/27/2013 - Melissa - Changed to use string formatter
```

