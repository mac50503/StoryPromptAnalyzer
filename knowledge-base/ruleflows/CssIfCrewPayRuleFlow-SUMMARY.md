# CssIfCrewPayRuleFlow - Resumen

## Metadata
- **Tipo**: Ruleflow
- **Propósito**: Orquesta el flujo completo de cálculo de pago para tripulación CSS Inflight
- **Ubicación**: `CrewRulesRepository/DecisionServices/CSS/Inflight/PayRuleFlows/CssCrewPayRuleFlow`
- **Fecha inicial**: 8/23/2013 US13673

## ¿Qué es un Ruleflow?

Un Ruleflow es el "director de orquesta" que coordina la ejecución de múltiples funciones y rulesets en un orden específico. Es como un diagrama de flujo ejecutable.

## Variables principales

```
- theCrewPayRequest: CrewPayRequest
- thePayCrewMemberLine: PayCrewMemberLine  
- theCrewPayResponse: CrewPayResponse
- theTripList: List<PayTrip>
- theTripPayList: List<TripPay>
- theSchedulePeriodPayList: List<SchedulePeriodPay>
- theGlobalDataCache: GlobalDataCache
- theSwaHolidayList: List<SwaHoliday>
```

## Flujo principal

### 1. Inicialización
- Recibe `BlazePayRequest` como entrada
- Extrae todas las variables necesarias del request
- Calcula días Conus/Oconus con `fcnSetTripSetConusAndOconusDays`

### 2. Loop por Schedule Period
Para cada período de programación:

#### 2.1 Preparación
- Obtiene el SchedulePeriodPay actual
- Crea objetos de analytics si está habilitado
- Resetea límites Conus/Oconus
- Establece rates de PayBuckets
- Calcula años de experiencia

#### 2.2 Loop por Trip
Para cada viaje en el período:

**Pasos:**
1. Determina términos transitorios del trip (`fcnDetermineTripTransientTerms`)
2. Cross-reference trip con tripPay
3. Establece posición A
4. Calcula THR, ADG y DHR
5. Establece montos de RIG más altos

#### 2.3 Loop por Duty Period
Para cada período de servicio en el trip:

**Pasos:**
1. Cross-reference duty period con dutyPeriodPay
2. Establece términos transitorios
3. Calcula duración y descanso (`rsCalculateDutyPeriodDurationAndRest`)
4. Calcula duración real del duty

#### 2.4 Loop por Leg
Para cada tramo en el duty period:

**Pasos clave:**
1. **Conversión de zona horaria** (si aplica APIC-1585):
   - Convierte legs a zona horaria del domicilio del trip
   - Solo para legs que no son primero ni último

2. Cross-reference leg con legPay
3. Establece posición A
4. **Calcula créditos base** (`rsCalculateLegBaseCredits`)
5. **Deriva código de premium** (`rsDeriveRegularPremiumPayCode`)
6. **Calcula créditos totales** (`rsCalculateLegTotalCredits`)

#### 2.5 Después del loop de legs
1. **Calcula créditos de duty period** (`rsCalculateDutyPeriodCredits`)
2. **Calcula RIGs de duty period** (`rsCalculateDutyPeriodRIGS`)

#### 2.6 Después del loop de duty periods
1. Asocia duty periods con bloques de reserva
2. Calcula contribución de productividad
3. **Distribuye a buckets de pago** (`rsDistributeTripPayToBuckets`)
4. Calcula pago de holiday
5. Calcula pago de experiencia
6. Calcula pago de longevidad

### 3. Después del loop de trips
1. Calcula garantía de reserva
2. Calcula pago Conus/Oconus
3. Distribuye garantía restante
4. Aplica ajustes de staff bank
5. Redondea valores de pago

### 4. Finalización
- Retorna el `BlazePayRequest` actualizado con todos los cálculos

## Rulesets principales llamados

| Ruleset | Propósito |
|---------|-----------|
| `rsCalculateDutyPeriodDurationAndRest` | Calcula duración y descanso del duty period |
| `rsCalculateLegBaseCredits` | Calcula créditos base del leg |
| `rsDeriveRegularPremiumPayCode` | Determina código de premium |
| `rsCalculateLegTotalCredits` | Calcula créditos totales del leg |
| `rsCalculateDutyPeriodCredits` | Calcula créditos del duty period |
| `rsCalculateDutyPeriodRIGS` | Calcula RIGs del duty period |
| `rsDistributeTripPayToBuckets` | Distribuye pago a buckets |
| `rsCalculateHolidayPayBucket` | Calcula pago de holidays |

## Funciones principales llamadas

| Función | Propósito |
|---------|-----------|
| `fcnSetTripSetConusAndOconusDays` | Establece días Conus/Oconus |
| `fcnDetermineTripTransientTerms` | Determina términos transitorios del trip |
| `fcnCalculateThrAndAdgAndDhr` | Calcula THR, ADG y DHR |
| `fcnSetHighestRigAmounts` | Establece montos de RIG más altos |
| `fcnConvertLegToTripDomicileTimeZone` | Convierte leg a zona horaria del domicilio (APIC-1585) |
| `fcnCalculateActualDutyDuration` | Calcula duración real del duty |
| `fcnCalculateTripContributionForProductivityPay` | Calcula contribución de productividad |
| `fcnCalculateExperiencePayBucket` | Calcula pago de experiencia |
| `fcnCalculateLongevityBucket` | Calcula pago de longevidad |

## Características especiales

### Toggle de Domicile Day (APIC-1585)
```blaze
if fcnIsDateTimeOnOrAfterConfigCollectionEffectiveDateTime(
    theTrip.beginDateTime, 
    "IF_2025_NEW_DOMICILE_DAY_PAY_BLAZE_EFFECTIVE_DATETIME"
) then
    // Convierte legs a zona horaria del domicilio
    fcnConvertLegToTripDomicileTimeZone(theLeg, theTrip.tripDomicileTimeZone)
```

### Data Analytics
Si `includeDataAnalytics = true`, crea objetos de analytics para cada schedule period.

### Splits condicionales
- Verifica si hay trips en el schedule period
- Verifica tipo de trip (no "I" ni "R")
- Verifica credit types específicos
- Verifica si duty contiene solo limos de duración cero

## Orden de ejecución

```
1. Schedule Period Loop
   └─> 2. Trip Loop
       └─> 3. Duty Period Loop
           └─> 4. Leg Loop
               ├─> Calcula base credits
               ├─> Deriva premium code
               └─> Calcula total credits
           ├─> Calcula duty period credits
           └─> Calcula duty period RIGs
       ├─> Distribuye a buckets
       ├─> Calcula holidays
       ├─> Calcula experiencia
       └─> Calcula longevidad
   ├─> Calcula garantía de reserva
   ├─> Calcula Conus/Oconus
   └─> Redondea valores
```

## Cómo usar esta información

### Para entender el flujo completo:
1. Empieza por el Schedule Period Loop
2. Sigue el flujo Trip → Duty Period → Leg
3. Nota que cada nivel tiene su propio procesamiento

### Para debugging:
1. Identifica en qué loop estás (Schedule Period, Trip, Duty Period, o Leg)
2. Verifica qué ruleset/función se está ejecutando
3. Revisa las variables de ese nivel

### Para modificaciones:
1. Identifica dónde en el flujo necesitas hacer el cambio
2. Verifica si afecta a otros niveles
3. Considera el orden de ejecución

## Notas importantes

- Este ruleflow es el "cerebro" del sistema de pago
- Coordina más de 50 funciones y rulesets diferentes
- El orden de ejecución es crítico
- Los loops están anidados: SP → Trip → DP → Leg
- Cada nivel tiene su propio conjunto de cálculos

## Historial de cambios clave

- 8/23/2013 US13673: Setup inicial
- 7/30/2015 DE7024: Modificación de credit type P bajo reserva
- 7/29/2015 DE7134: Eliminación de lógica para credit type F
- APIC-1585: Cambios de Domicile Day (conversión de zona horaria)
