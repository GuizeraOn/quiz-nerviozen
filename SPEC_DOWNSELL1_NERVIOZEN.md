# ESPECIFICAÇÃO TÉCNICA COMPLETA
## Página: `/downsell1` — Activador de Absorción 10X
## Projeto: NervioZen Funnel — LATAM Español Neutro
## Versão: 1.0 — Documento para Desenvolvedor

---

## 1. CONTEXTO E PROPÓSITO DA PÁGINA

Esta página é exibida **exclusivamente quando o usuário recusa o Upsell 1** (Activador de Absorción 10X a $17). O objetivo é capturar compradores com intenção mas resistência ao preço, oferecendo o mesmo produto a 50% de desconto ($8.50).

**Fluxo de navegação:**
```
[Compra do produto principal $9.90]
    ↓
[Upsell 1 — $17] → [RECUSA] → [ESTA PÁGINA — Downsell 1 — $8.50]
    ↓ (aceita ou recusa)
[Upsell 2 — $27]
```

**Regra crítica:** O botão de aceite e recusa é 100% gerenciado pelo widget da Hotmart. Não construir botões customizados para ação de compra. O programador apenas estiliza o container ao redor do widget.

---

## 2. STACK TÉCNICA

- **HTML5 + CSS3 puro** (sem frameworks obrigatórios — vanilla JS para delay e animações)
- **Google Fonts** via CDN
- **Responsivo mobile-first** (breakpoint principal: 480px)
- **Sem integração VTurb ou player de vídeo**
- **Sem formulários** — toda ação de compra via widget Hotmart
- **Meta Pixel** no `<head>` (tag de ViewContent nesta página)
- **Microsoft Clarity** no `<head>`

---

## 3. PALETA DE CORES

```css
:root {
  /* Cores principais */
  --color-alert-bg:       #C0392B;      /* Vermelho alerta — header */
  --color-alert-text:     #FFFFFF;      /* Branco sobre alerta */
  --color-alert-pulse:    #E74C3C;      /* Variação pulsante */

  /* Fundo e superfície */
  --color-page-bg:        #0D0D0D;      /* Preto profundo — fundo geral */
  --color-card-bg:        #141414;      /* Cartão ligeiramente mais claro */
  --color-card-border:    #2A2A2A;      /* Borda sutil dos cartões */
  --color-section-divider:#1E1E1E;

  /* Textos */
  --color-text-primary:   #F5F5F5;      /* Texto principal */
  --color-text-secondary: #ABABAB;      /* Texto secundário / subtexto */
  --color-text-highlight: #FFFFFF;      /* Branco puro para ênfase máxima */

  /* Acentos */
  --color-price-old:      #888888;      /* Preço riscado */
  --color-price-new:      #27AE60;      /* Verde — preço novo */
  --color-gold:           #F0B429;      /* Dourado — selos / garantia */
  --color-accent-warn:    #E67E22;      /* Laranja — urgência secundária */

  /* Gradiente de urgência (uso no header) */
  --gradient-alert: linear-gradient(135deg, #B71C1C 0%, #C0392B 50%, #B71C1C 100%);
}
```

---

## 4. TIPOGRAFIA

```css
/* Importar via Google Fonts CDN no <head> */
/* Família principal: Montserrat (títulos, alertas, preços) */
/* Família corpo: Open Sans (parágrafos, copy) */

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Open+Sans:wght@400;600;700&display=swap');

:root {
  --font-display: 'Montserrat', sans-serif;
  --font-body:    'Open Sans', sans-serif;
}
```

**Hierarquia de tamanhos (mobile-first):**

| Elemento                        | Mobile       | Desktop (≥480px) | Peso     | Família      |
|---------------------------------|--------------|------------------|----------|--------------|
| Header alerta (linha 1)         | 13px         | 15px             | 700      | Montserrat   |
| Header alerta (linha 2 — título)| 22px         | 28px             | 900      | Montserrat   |
| H2 — títulos de seção           | 20px         | 24px             | 800      | Montserrat   |
| H3 — subtítulos                 | 16px         | 18px             | 700      | Montserrat   |
| Parágrafo principal             | 15px         | 16px             | 400      | Open Sans    |
| Parágrafo bold/ênfase           | 15px         | 16px             | 700      | Open Sans    |
| Preço riscado                   | 18px         | 20px             | 600      | Montserrat   |
| Preço novo                      | 32px         | 38px             | 900      | Montserrat   |
| Label "APENAS HOJE"             | 11px         | 12px             | 700      | Montserrat   |
| Garantia / rodapé               | 12px         | 13px             | 400      | Open Sans    |
| Botão recusa (texto link)       | 12px         | 13px             | 400      | Open Sans    |

---

## 5. ESTRUTURA GERAL DA PÁGINA (WIREFRAME VERTICAL)

```
┌─────────────────────────────────────────┐
│  [BLOCO A] HEADER DE ALERTA PULSANTE    │  ← vermelho, full-width, animado
├─────────────────────────────────────────┤
│  [BLOCO B] MENSAGEM DE RECONHECIMENTO   │  ← dark card, copy curta
├─────────────────────────────────────────┤
│  [BLOCO C] REAPRESENTAÇÃO DO PROBLEMA   │  ← 2 parágrafos, dark bg
├─────────────────────────────────────────┤
│  [BLOCO D] OFERTA 50% OFF               │  ← destaque visual, preços
├─────────────────────────────────────────┤
│  [BLOCO E] O QUE ESTÁ INCLUÍDO          │  ← lista concisa, ícones ✅
├─────────────────────────────────────────┤
│  [BLOCO F] GARANTIA                     │  ← ícone escudo dourado
├─────────────────────────────────────────┤
│  [BLOCO G] WIDGET HOTMART               │  ← container centralizado, delay
├─────────────────────────────────────────┤
│  [BLOCO H] BOTÃO DE RECUSA (link texto) │  ← abaixo do widget, discreto
└─────────────────────────────────────────┘
```

**Layout geral:**
- `max-width`: 600px
- Centralizado com `margin: 0 auto`
- Padding lateral: 16px (mobile) / 24px (desktop)
- Background page: `var(--color-page-bg)`
- Sem sidebar, sem menu, sem header de navegação
- Sem footer com links externos

---

## 6. ESPECIFICAÇÃO BLOCO A — HEADER DE ALERTA PULSANTE

**Objetivo:** Interromper o scroll e criar urgência imediata antes de qualquer leitura.

```
┌─────────────────────────────────────────┐
│  ⚠️ ESPERA — ANTES DE IRTE            │  ← linha 1
│  TENEMOS ALGO ESPECIAL PARA TI        │  ← linha 2 (grande)
└─────────────────────────────────────────┘
```

**Especificações:**
- `background`: `var(--gradient-alert)` com `background-size: 200%` animado (shimmer lento)
- `width`: 100vw com `margin-left: calc(-50vw + 50%)` para sair do container e ir full-width
- `padding`: 18px 20px (mobile) / 22px 32px (desktop)
- `text-align`: center
- Borda inferior: `4px solid #FF6B6B` (linha de destaque clara)
- Box-shadow: `0 4px 20px rgba(192, 57, 43, 0.5)` — brilho vermelho para baixo

**Linha 1 — Supertítulo:**
- Texto: `⚠️ ESPERA — ANTES DE IRTE`
- Font: Montserrat 700, 13px mobile / 15px desktop
- Color: `rgba(255,255,255,0.85)`
- `letter-spacing: 2px`
- `text-transform: uppercase`
- `margin-bottom: 6px`

**Linha 2 — Título principal do header:**
- Texto: `TENEMOS ALGO ESPECIAL PARA TI`
- Font: Montserrat 900, 22px mobile / 28px desktop
- Color: `#FFFFFF`
- `letter-spacing: 0.5px`
- `text-shadow: 0 2px 8px rgba(0,0,0,0.4)`

**Animação CSS obrigatória (keyframe):**
```css
@keyframes shimmer {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.alert-header {
  animation: shimmer 3s ease infinite;
  background-size: 200%;
}
```

**Animação de pulso no ícone ⚠️:**
```css
@keyframes pulse-icon {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.15); }
}
.alert-icon {
  display: inline-block;
  animation: pulse-icon 1.4s ease-in-out infinite;
}
```

---

## 7. ESPECIFICAÇÃO BLOCO B — MENSAGEM DE RECONHECIMENTO

**Objetivo:** Validar a decisão do usuário sem atacar, criar ponte emocional antes da oferta.

**Container:**
- Background: `var(--color-card-bg)`
- Border-left: `4px solid var(--color-accent-warn)`
- `border-radius: 8px`
- `padding: 20px 22px`
- `margin: 24px 0 0`

**Copy exata (espanhol neutro LATAM):**

```
Entendemos perfectamente que $17 puede no ser el momento ideal.

Pero sabemos que recuperar tu movilidad, tu sueño y tu calidad de vida SÍ es 
una prioridad para ti. Por eso, antes de que te vayas, tenemos una última 
oportunidad que solo aparece una vez y que no vamos a poder ofrecerte después.
```

**Formatação:**
- Parágrafo 1: Open Sans 400, 15px/16px, color `var(--color-text-primary)`, `line-height: 1.7`
- Parágrafo 2: Open Sans 400, 15px/16px, color `var(--color-text-primary)`, `line-height: 1.7`
- `"SÍ es una prioridad"` → `<strong>` + color `var(--color-alert-pulse)` (vermelho)
- `margin-bottom: 0` no último parágrafo
- Separação entre parágrafos: `margin-bottom: 12px`

---

## 8. ESPECIFICAÇÃO BLOCO C — REAPRESENTAÇÃO DO PROBLEMA

**Objetivo:** Reativar a dor e o problema central de forma concisa (máx. 3 parágrafos).

**Container:**
- Background: `var(--color-page-bg)`
- `padding: 28px 0`
- Sem card — texto solto sobre o fundo escuro

**Copy exata:**

```
¿Recuerdas por qué llegaste hasta aquí?

Porque el entumecimiento, el hormigueo y ese ardor que no te da tregua en manos 
y pies siguen robándote el sueño, la energía y los momentos que más importan 
con tu familia.

El problema no es solo el dolor. El problema es que tu hígado está tan saturado 
de químicos acumulados que ningún nutriente llega donde debe llegar: directamente 
a tus células de Schwann para reparar la vaina de mielina dañada.

Sin el Activador de Absorción 10X, incluso el protocolo NervioZen que ya 
adquiriste puede no darte los resultados que esperas, porque los nutrientes 
simplemente no llegarán a tus nervios.
```

**Formatação:**
- Linha 1 `¿Recuerdas...?`: Montserrat 800, 20px/24px, color `#FFFFFF`, `margin-bottom: 16px`
- Parágrafos seguintes: Open Sans 400, 15px/16px, color `var(--color-text-primary)`, `line-height: 1.75`
- `"entumecimiento, el hormigueo y ese ardor"` → `<strong>` color `#FFFFFF`
- `"células de Schwann"` e `"vaina de mielina"` → `<em>` color `var(--color-gold)` (dourado)
- `"Activador de Absorción 10X"` → `<strong>` color `#FFFFFF`
- Separação entre parágrafos: `margin-bottom: 14px`

---

## 9. ESPECIFICAÇÃO BLOCO D — OFERTA 50% OFF

**Objetivo:** Apresentar o desconto com máximo impacto visual e clareza de valor.

**Container externo:**
- Background: `linear-gradient(135deg, #0F2010 0%, #1A2F1B 100%)` — verde escuro
- `border: 2px solid var(--color-price-new)`
- `border-radius: 12px`
- `padding: 24px 20px`
- `margin: 8px 0 0`
- `text-align: center`
- Box-shadow: `0 0 30px rgba(39, 174, 96, 0.2)`

**Linha de etiqueta (topo do card):**
- Texto: `🔥 ÚLTIMA OPORTUNIDAD — SOLO PARA TI`
- Font: Montserrat 700, 11px/12px
- Color: `var(--color-price-new)`
- `letter-spacing: 2px`
- `text-transform: uppercase`
- `margin-bottom: 16px`

**Nome do produto:**
- Texto: `Activador de Absorción 10X`
- Font: Montserrat 900, 22px/26px
- Color: `#FFFFFF`
- `margin-bottom: 6px`

**Subtítulo do produto:**
- Texto: `El protocolo de 3 días que activa la absorción total de NervioZen`
- Font: Open Sans 400, 13px/14px
- Color: `var(--color-text-secondary)`
- `margin-bottom: 20px`

**Bloco de preços:**

```
┌─────────────────────────────────────┐
│  Valor normal:  ~~$17.00~~          │
│  HOY PAGAS SOLO:                    │
│         $8.50                       │
│    PAGO ÚNICO — SIN MENSUALIDADES  │
└─────────────────────────────────────┘
```

- "Valor normal:" → Open Sans 600, 14px, color `var(--color-text-secondary)`
- "~~$17.00~~" → Montserrat 600, 18px/20px, color `var(--color-price-old)`, `text-decoration: line-through`
- "HOY PAGAS SOLO:" → Montserrat 700, 13px, color `var(--color-text-secondary)`, `letter-spacing: 1px`, `text-transform: uppercase`, `margin-top: 10px`
- "$8.50" → Montserrat 900, 44px mobile / 52px desktop, color `var(--color-price-new)`, `line-height: 1`, `display: block`, `margin: 4px 0 8px`
- "PAGO ÚNICO — SIN MENSUALIDADES" → Montserrat 700, 11px, color `rgba(39,174,96,0.75)`, `letter-spacing: 1.5px`, `text-transform: uppercase`

**Badge de desconto (posicionamento absoluto sobre o card):**
- Conteúdo: `50% OFF`
- Posição: `position: absolute; top: -14px; right: 20px`
- Background: `var(--color-alert-bg)`
- Color: `#FFFFFF`
- Font: Montserrat 800, 13px
- `padding: 4px 12px`
- `border-radius: 20px`
- `letter-spacing: 1px`
- O container pai deve ter `position: relative; overflow: visible`

---

## 10. ESPECIFICAÇÃO BLOCO E — O QUE ESTÁ INCLUÍDO

**Objetivo:** Reforçar o valor percebido com lista objetiva do que o usuário receberá.

**Título da seção:**
- Texto: `¿Qué recibirás exactamente?`
- Font: Montserrat 800, 18px/20px
- Color: `#FFFFFF`
- `margin-bottom: 16px`
- `margin-top: 28px`

**Lista de itens** (estrutura `<ul>` estilizada — sem bullets padrão):

```
✅  El Activador de Absorción 10X COMPLETO
    Protocolo de 72 horas para resetear tu filtro hepático y garantizar 
    que los nutrientes lleguen directo a tus nervios.

✅  El Elixir del Amanecer
    La bebida natural de cada mañana para despertar tu sistema digestivo 
    y maximizar la absorción desde el primer minuto del día.

✅  El Método del Enjuague Profundo
    Paso a paso de 72 horas para barrer los residuos de medicamentos 
    acumulados en tu hígado.

✅  El Protocolo de Reparación Nocturna
    Rutina de pocos segundos que tu cuerpo ejecuta mientras duermes 
    para regenerar tus células al máximo.

✅  Guía de Energía Celular (BONO)
    Elimina el cansancio crónico y recupera la vitalidad de tus mejores años.

✅  Bono de Visualización Sanadora (BONO)
    Frecuencias sonoras para calmar tu sistema nervioso central de inmediato.

✅  Bono Sorpresa Exclusivo (BONO)
    Solo lo descubrirás al entrar a tu área de miembros. Te dejará sin palabras.
```

**Formatação por item:**
- Container do item: `display: flex; gap: 12px; margin-bottom: 16px; align-items: flex-start`
- Ícone ✅: `font-size: 18px; flex-shrink: 0; margin-top: 1px`
- Texto do título do item: Open Sans **700**, 15px/16px, color `#FFFFFF`, `display: block; margin-bottom: 3px`
- Texto descritivo: Open Sans 400, 13px/14px, color `var(--color-text-secondary)`, `line-height: 1.6`
- Itens marcados como `(BONO)`: o label `(BONO)` recebe `color: var(--color-gold)` com font Montserrat 700, 11px, `letter-spacing: 1px`
- Container lista: `background: var(--color-card-bg); border: 1px solid var(--color-card-border); border-radius: 10px; padding: 20px 18px; margin-top: 4px`

---

## 11. ESPECIFICAÇÃO BLOCO F — GARANTIA

**Objetivo:** Eliminar 100% do risco percebido antes do widget.

**Container:**
- `display: flex`
- `gap: 16px`
- `align-items: center`
- Background: `rgba(240, 180, 41, 0.05)`
- `border: 1px solid rgba(240,180,41,0.2)`
- `border-radius: 10px`
- `padding: 18px 16px`
- `margin: 24px 0`

**Ícone escudo:**
- Usar emoji `🛡️` ou SVG de escudo
- `font-size: 42px` (mobile) / `48px` (desktop)
- `flex-shrink: 0`

**Bloco de texto:**
- Título: `Garantía Total de 30 Días`
  - Font: Montserrat 800, 16px/18px, color `var(--color-gold)`
  - `margin-bottom: 6px`
- Copy:
  ```
  Si por cualquier razón sientes que el Activador de Absorción 10X no era 
  lo que buscabas, escríbenos por WhatsApp y te devolvemos cada centavo 
  de tus $8.50 de inmediato, sin preguntas. Y podrás quedarte con todo 
  el programa como nuestro regalo.
  ```
  - Font: Open Sans 400, 13px/14px, color `var(--color-text-secondary)`, `line-height: 1.65`

---

## 12. ESPECIFICAÇÃO BLOCO G — WIDGET HOTMART + DELAY

### 12.1 Delay de exibição

**O widget Hotmart NÃO aparece imediatamente ao carregar a página.**

Implementar via JavaScript puro:

```javascript
// Delay: 8 segundos após DOMContentLoaded
document.addEventListener('DOMContentLoaded', function () {
  const widgetContainer = document.getElementById('hotmart-widget-container');
  const widgetOverlay   = document.getElementById('widget-loading-overlay');

  // Container começa oculto
  widgetContainer.style.opacity = '0';
  widgetContainer.style.visibility = 'hidden';
  widgetContainer.style.transition = 'opacity 0.6s ease, visibility 0.6s ease';

  // Overlay de loading visível durante o delay
  widgetOverlay.style.display = 'flex';

  setTimeout(function () {
    widgetOverlay.style.display = 'none';
    widgetContainer.style.opacity = '1';
    widgetContainer.style.visibility = 'visible';
  }, 8000); // 8.000ms = 8 segundos
});
```

**Razão do delay:** Forçar leitura mínima da copy de urgência antes de oferecer a ação.

**O valor do delay pode ser ajustado** — variável `const WIDGET_DELAY_MS = 8000` no topo do script para facilitar.

### 12.2 Overlay de loading (exibido durante o delay)

```
┌──────────────────────────────────────┐
│                                      │
│   ⏳  Preparando tu oferta...        │
│       Por favor espera un momento    │
│                                      │
└──────────────────────────────────────┘
```

**Specs do overlay:**
- `position: relative` (dentro do flow normal, não fixed)
- `display: flex; flex-direction: column; align-items: center; justify-content: center`
- `min-height: 120px`
- Background: `var(--color-card-bg)`
- `border: 1px dashed var(--color-card-border)`
- `border-radius: 10px`
- `padding: 28px 20px`
- Ícone ⏳: `font-size: 28px; margin-bottom: 10px`
- Texto "Preparando tu oferta...": Montserrat 700, 15px, color `#FFFFFF`
- Subtexto "Por favor espera un momento": Open Sans 400, 13px, color `var(--color-text-secondary)`

**Animação de loading:**
```css
@keyframes pulse-loading {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.5; }
}
.widget-loading-text {
  animation: pulse-loading 1.5s ease-in-out infinite;
}
```

### 12.3 Container do widget Hotmart

```html
<div id="hotmart-widget-container">
  <!-- 
    INSTRUÇÃO AO DESENVOLVEDOR:
    Inserir aqui o widget da Hotmart gerado no painel do produto.
    O widget já contém os botões de aceite e recusa nativos da plataforma.
    Não adicionar nenhum botão customizado dentro deste container.
    O container apenas fornece o wrapper de espaçamento e alinhamento.
  -->
  <div class="hotmart-widget-wrapper">
    [WIDGET HOTMART AQUI]
  </div>
</div>
```

**CSS do container:**
```css
#hotmart-widget-container {
  margin: 0 auto;
  max-width: 480px;
  padding: 0 8px;
}

.hotmart-widget-wrapper {
  background: var(--color-card-bg);
  border: 1px solid var(--color-card-border);
  border-radius: 12px;
  padding: 20px 16px;
  overflow: hidden;
}
```

**Texto acima do widget (header do bloco G):**
- Texto: `Activa tu descuento de 50% ahora`
- Font: Montserrat 800, 18px/20px, color `#FFFFFF`
- `text-align: center`
- `margin-bottom: 6px`
- `margin-top: 28px`

**Subtexto acima do widget:**
- Texto: `Recuerda: este precio especial desaparece cuando salgas de esta página`
- Font: Open Sans 400, 13px, color `var(--color-alert-pulse)` (vermelho suave)
- `text-align: center`
- `margin-bottom: 16px`

---

## 13. ESPECIFICAÇÃO BLOCO H — BOTÃO DE RECUSA

**Objetivo:** Dar saída ao usuário de forma discreta, sem chamar atenção.

**Este link só aparece APÓS o widget Hotmart ser exibido (mesmo delay de 8s).**

```html
<div class="refuse-container">
  <a href="[URL_UPSELL2_OU_PROXIMA_ETAPA]" class="refuse-link">
    No, gracias. No necesito asegurar que NervioZen funcione en mi caso.
    Prefiero arriesgarme sin el Activador de Absorción.
  </a>
</div>
```

**CSS:**
```css
.refuse-container {
  text-align: center;
  margin: 20px auto 40px;
  max-width: 400px;
  padding: 0 16px;
}

.refuse-link {
  font-family: var(--font-body);
  font-size: 12px;        /* mobile */
  font-weight: 400;
  color: var(--color-text-secondary);
  text-decoration: none;
  line-height: 1.5;
  display: inline-block;
  opacity: 0.65;
  transition: opacity 0.2s ease;
  border-bottom: 1px solid transparent;
}

.refuse-link:hover {
  opacity: 1;
  color: var(--color-text-primary);
  border-bottom: 1px solid var(--color-text-secondary);
}

@media (min-width: 480px) {
  .refuse-link {
    font-size: 13px;
  }
}
```

**Behavior JavaScript — o link de recusa aparece com o widget:**
```javascript
// Dentro do mesmo setTimeout do widget
setTimeout(function () {
  document.getElementById('refuse-link-container').style.display = 'block';
}, 8000);
```

**O link de recusa redireciona para:** a próxima etapa do funil (Upsell 2 / `/upsell2`). **Não redireciona para fora do funil.** O programador deve configurar o href correto conforme o fluxo Hotmart.

---

## 14. RESPONSIVIDADE MOBILE (regra única de breakpoint)

```css
/* BASE: mobile-first — estilos padrão para ≤ 479px */

@media (min-width: 480px) {
  /* Ajustes para telas maiores — tablets e desktop */
  
  body {
    padding: 0 20px;
  }

  /* Alert header — aumentar tamanho de fonte */
  .alert-header-line2 {
    font-size: 28px;
  }

  /* Card de oferta — mais espaçamento interno */
  .offer-card {
    padding: 32px 28px;
  }

  /* Preço $8.50 — maior em desktop */
  .price-new {
    font-size: 52px;
  }

  /* Lista de itens — padding lateral maior */
  .items-list-container {
    padding: 24px 24px;
  }
}

/* NENHUM elemento deve ter overflow horizontal */
* {
  box-sizing: border-box;
  max-width: 100%;
}

img {
  max-width: 100%;
  height: auto;
}
```

**Regras mobile obrigatórias:**
- Nenhum elemento deve causar scroll horizontal
- `font-size` mínimo em qualquer elemento visível: **12px**
- `min-height` para botões/links clicáveis: **44px** (padrão de toque iOS/Android)
- Sem `hover` states que sejam a única forma de revelar conteúdo
- O widget Hotmart deve respeitar a largura do container (checar se o widget tem `max-width: 100%` ativo)

---

## 15. `<HEAD>` — META TAGS E SCRIPTS OBRIGATÓRIOS

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO: página de conversão — não indexar -->
  <meta name="robots" content="noindex, nofollow">
  
  <title>NervioZen — Tu Oferta Especial de Bienvenida</title>
  <meta name="description" content="Activa el Activador de Absorción 10X con 50% de descuento exclusivo.">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">

  <!-- Favicon: logo NervioZen -->
  <link rel="icon" type="image/png" href="/assets/logo_nerviozen.png">

  <!-- Meta Pixel (ViewContent) -->
  <!-- [INSERIR PIXEL META AQUI] -->

  <!-- Microsoft Clarity -->
  <!-- [INSERIR CLARITY AQUI] -->
</head>
```

---

## 16. ANIMAÇÕES E UX GLOBAL

**Entrada da página (page load):**
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Aplicar stagger nos blocos principais */
.block-b { animation: fadeInUp 0.5s ease 0.1s both; }
.block-c { animation: fadeInUp 0.5s ease 0.2s both; }
.block-d { animation: fadeInUp 0.5s ease 0.3s both; }
.block-e { animation: fadeInUp 0.5s ease 0.4s both; }
.block-f { animation: fadeInUp 0.5s ease 0.5s both; }
```

**Badge 50% OFF — microanimação:**
```css
@keyframes badge-bounce {
  0%, 100% { transform: scale(1) rotate(-2deg); }
  50%       { transform: scale(1.08) rotate(-2deg); }
}
.discount-badge {
  animation: badge-bounce 2s ease-in-out infinite;
}
```

**Card de oferta — brilho sutil (border glow pulsante):**
```css
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(39, 174, 96, 0.15); }
  50%       { box-shadow: 0 0 40px rgba(39, 174, 96, 0.35); }
}
.offer-card {
  animation: glow-pulse 3s ease-in-out infinite;
}
```

**Scroll behavior:**
```css
html {
  scroll-behavior: smooth;
}
```

---

## 17. ACESSIBILIDADE BÁSICA

- Todos os links devem ter `aria-label` descritivo
- O link de recusa deve ter `role="button"` e ser focável via teclado
- Contraste mínimo de texto sobre fundo: **4.5:1** (verificar com ferramenta)
- Nunca usar cor como único indicador de estado
- `alt=""` em imagens decorativas; `alt="[descrição]"` em imagens informativas

---

## 18. PERFORMANCE

- Nenhuma imagem pesada nesta página (página é 100% CSS/texto)
- Google Fonts com `display=swap` para evitar FOIT
- Scripts não-críticos com `defer`
- Widget Hotmart com `loading="lazy"` se suportado
- CSS minificado em produção

---

## 19. CHECKLIST FINAL DO DESENVOLVEDOR

Antes de marcar como pronto, verificar:

- [ ] Header alerta renderiza full-width em mobile sem overflow
- [ ] Animação shimmer no header funcionando suavemente
- [ ] Badge "50% OFF" posicionado corretamente (absolute) sem clipar em mobile
- [ ] Preço $8.50 em destaque máximo, legível em qualquer tela
- [ ] Widget Hotmart oculto nos primeiros 8 segundos
- [ ] Overlay de loading visível e animado nos primeiros 8 segundos
- [ ] Widget e link de recusa aparecem simultaneamente após 8s
- [ ] Link de recusa **não** é um botão de compra — aponta para próxima etapa do funil
- [ ] Nenhum scroll horizontal em iPhone SE (320px largura)
- [ ] Sem links de saída do funil (menu, rodapé, redes sociais)
- [ ] Meta robots `noindex` no `<head>`
- [ ] Pixel Meta e Clarity instalados
- [ ] Favicon ativo

---

## 20. COPY COMPLETA — ORDEM EXATA NA PÁGINA

Para referência do desenvolvedor, abaixo toda a copy na sequência de renderização:

---

**[HEADER A]**
```
⚠️ ESPERA — ANTES DE IRTE
TENEMOS ALGO ESPECIAL PARA TI
```

---

**[BLOCO B]**
```
Entendemos perfectamente que $17 puede no ser el momento ideal.

Pero sabemos que recuperar tu movilidad, tu sueño y tu calidad de vida SÍ es 
una prioridad para ti. Por eso, antes de que te vayas, tenemos una última 
oportunidad que solo aparece una vez y que no vamos a poder ofrecerte después.
```

---

**[BLOCO C]**
```
¿Recuerdas por qué llegaste hasta aquí?

Porque el entumecimiento, el hormigueo y ese ardor que no te da tregua en manos 
y pies siguen robándote el sueño, la energía y los momentos que más importan 
con tu familia.

El problema no es solo el dolor. El problema es que tu hígado está tan saturado 
de químicos acumulados que ningún nutriente llega donde debe llegar: directamente 
a tus células de Schwann para reparar la vaina de mielina dañada.

Sin el Activador de Absorción 10X, incluso el protocolo NervioZen que ya 
adquiriste puede no darte los resultados que esperas, porque los nutrientes 
simplemente no llegarán a tus nervios.
```

---

**[BLOCO D — OFFER CARD]**
```
🔥 ÚLTIMA OPORTUNIDAD — SOLO PARA TI

Activador de Absorción 10X
El protocolo de 3 días que activa la absorción total de NervioZen

Valor normal: ~~$17.00~~
HOY PAGAS SOLO:
          $8.50
PAGO ÚNICO — SIN MENSUALIDADES
```

---

**[BLOCO E — LISTA]**
```
¿Qué recibirás exactamente?

✅  El Activador de Absorción 10X COMPLETO
    Protocolo de 72 horas para resetear tu filtro hepático y garantizar 
    que los nutrientes lleguen directo a tus nervios.

✅  El Elixir del Amanecer
    La bebida natural de cada mañana para despertar tu sistema digestivo 
    y maximizar la absorción desde el primer minuto del día.

✅  El Método del Enjuague Profundo
    Paso a paso de 72 horas para barrer los residuos de medicamentos 
    acumulados en tu hígado.

✅  El Protocolo de Reparación Nocturna
    Rutina de pocos segundos que tu cuerpo ejecuta mientras duermes 
    para regenerar tus células al máximo.

✅  Guía de Energía Celular   (BONO)
    Elimina el cansancio crónico y recupera la vitalidad de tus mejores años.

✅  Bono de Visualización Sanadora   (BONO)
    Frecuencias sonoras para calmar tu sistema nervioso central de inmediato.

✅  Bono Sorpresa Exclusivo   (BONO)
    Solo lo descubrirás al entrar a tu área de miembros. Te dejará sin palabras.
```

---

**[BLOCO F — GARANTIA]**
```
🛡️  Garantía Total de 30 Días

Si por cualquier razón sientes que el Activador de Absorción 10X no era 
lo que buscabas, escríbenos por WhatsApp y te devolvemos cada centavo 
de tus $8.50 de inmediato, sin preguntas. Y podrás quedarte con todo 
el programa como nuestro regalo.
```

---

**[BLOCO G — PRÉ-WIDGET]**
```
Activa tu descuento de 50% ahora

Recuerda: este precio especial desaparece cuando salgas de esta página

[OVERLAY DE LOADING — 8 segundos]
    ⏳  Preparando tu oferta...
        Por favor espera un momento

[WIDGET HOTMART após 8s]
```

---

**[BLOCO H — RECUSA]**
```
No, gracias. No necesito asegurar que NervioZen funcione en mi caso.
Prefiero arriesgarme sin el Activador de Absorción.
```

---

*Fim do documento de especificação técnica.*
*Versão 1.0 — NervioZen Downsell 1 — Para uso exclusivo da equipe de desenvolvimento.*
