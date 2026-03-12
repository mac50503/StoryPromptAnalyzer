# fcnGetLastLegPremiumPayCodeFromLatestRRRDP

## Metadata
- **Tipo**: SRL Function
- **Retorna**: string
- **Ubicación**: `CrewRulesRepository\TechnicalLibrary\Pay\InflightPay\Functions\fcnGetLasLegPremiumPayCodeFromLatestRRRDP`

## Propósito
*(Sin descripción)*

## Parámetros

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| theTrip | PayTrip | |
| thePayDutyPeriod | PayDutyPeriod | |

## Lógica de negocio

```blaze
counter is an integer initially theTrip.dutyPeriodList.size() - 1.while counter > 0 do {theCurrentDutyPeriod is some PayDutyPeriod initially theTrip.dutyPeriodList.get(counter).indexOfPassedPayDutyPeriod is a real initially theTrip.dutyPeriodList.indexOf(thePayDutyPeriod) .if(((theCurrentDutyPeriod.amountOfRest -30)<600 or (theCurrentDutyPeriod.amountOfRest-30) >= 660)and indexOfPassedPayDutyPeriod >= counter) then {return "".} else if (theCurrentDutyPeriod.dutyType = "RRR" and (theCurrentDutyPeriod.amountOfRest -30)>=600 and (theCurrentDutyPeriod.amountOfRest-30) < 660and indexOfPassedPayDutyPeriod >= counter) then {return theCurrentDutyPeriod.lastLeg.legPay.premiumPayCode.}counter -= 1.}return "".
```

