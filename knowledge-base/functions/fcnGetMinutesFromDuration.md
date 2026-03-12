# fcnGetMinutesFromDuration

## Metadata
- **Tipo**: SRL Function
- **Retorna**: integer
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Common\Functions\DateTime\fcnGetMinutesFromDuration`

## Propósito
US14133 - 9/27/2013 - Melissa - Changed to used milliseconds instead of parsing string

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| tmpDuration | duration | |

## Lógica de negocio

```blaze
if (tmpDuration <> unknown) then {return (round(tmpDuration.milliseconds / 1000 / 60)).} else {return 0.}
```

## Historial de cambios

```
US14133 - 9/27/2013 - Melissa - Changed to used milliseconds instead of parsing string
tmpHours is an integer initially 0.
tmpMinutes is an integer initially 0.
if (tmpDuration &gt;= 1 minute and tmpDuration &lt; 1 hour) then {
tmpMinutes = portable().subString(tmpDuration.toString(), 0,  (portable().findString(tmpDuration.toString(), " minute"))-1) as an integer.
} else if (tmpDuration &gt; 1 hour and portable().findString(tmpDuration.toString(), "minute") &gt; 0) then {
tmpHours = portable().subString(tmpDuration.toString(), 0,  (portable().findString(tmpDuration.toString(), " hour"))-1) as an integer.
if (tmpHours &gt;=1 and tmpHours &lt; 2) then {
tmpMinutes = portable().subString(tmpDuration.toString(), (portable().findString(tmpDuration.toString(), "hour "))+5,  (portable().findString(tmpDuration.toString(), " minute"))-1) as an integer.
} else {
tmpMinutes = portable().subString(tmpDuration.toString(), (portable().findString(tmpDuration.toString(), "hours "))+6,  (portable().findString(tmpDuration.toString(), " minute"))-1) as an integer.
}
} else if (tmpDuration &gt;= 1 hour and portable().findString(tmpDuration.toString(), "minute") = 0) then {
tmpHours = portable().subString(tmpDuration.toString(), 0,  (portable().findString(tmpDuration.toString(), " hour"))-1) as an integer.
}
return (tmpHours * 60 + tmpMinutes).
```

