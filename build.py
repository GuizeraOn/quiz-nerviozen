import re
import os

filepath = 'd:/Downloads/neuropatia/neuropathy-quiz-funnel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

css_to_add = """
  /* Demographics Grid */
  .grid-2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .grid-2x2 .opt-btn { flex-direction: column; padding: 12px; font-size: 0.9rem; text-align: center; justify-content: flex-start; }
  .demo-photo { font-size: 2.5rem; text-align: center; margin-bottom: 8px; }
  
  /* Checkboxes */
  .check-opt { text-align: left; padding: 16px 14px; justify-content: flex-start; }
  .check-opt input { margin-right: 12px; width: 18px; height: 18px; accent-color: var(--accent); }

  /* Doctor Audio Block */
  .audio-alert { background: #FEF2F2; border: 1px dashed #F87171; border-radius: 12px; padding: 16px; margin-top: 24px; text-align: center; }
  .dr-profile { display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 12px; text-align: left; background: #FFF; padding: 12px; border-radius: 8px; border: 1px solid #FECACA; }
  .dr-profile img { width: 55px; height: 55px; border-radius: 50%; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
  .dr-quote { font-style: italic; color: #475569; font-size: 0.9rem; margin-bottom: 16px; }
</style>"""
content = content.replace('</style>', css_to_add)

quiz_start = content.find('  <!-- ── STEP 1 ── -->')
quiz_end = content.find('  <!-- ── FAKE LOADER ── -->')

new_quiz_html = """  <!-- ── STEP 1 (Fricción Cero) ── -->
  <div class="screen active" id="step1">
    <p class="question">Cuando sientes <strong>hormigueo</strong> o dolor, ¿tu primer instinto es <strong>masajearte con alguna loción o pomada</strong>?</p>
    <div class="options">
      <button class="opt-btn" onclick="goStep(2)"><span class="icon">✅</span> <span>Sí, lo hago casi siempre.</span></button>
      <button class="opt-btn" onclick="goStep(2)"><span class="icon">❌</span> <span>No, rara vez lo hago.</span></button>
    </div>
  </div>

  <!-- ── STEP 2 (Mapeo de Síntomas) ── -->
  <div class="screen" id="step2">
    <p class="question">¿Cómo describirías exactamente la molestia más insoportable que sientes en tus extremidades?</p>
    <div class="options">
      <button class="opt-btn" onclick="goStep(3)"><span class="icon">⚡</span> <span>Punzadas eléctricas repentinas.</span></button>
      <button class="opt-btn" onclick="goStep(3)"><span class="icon">🔥</span> <span>Un ardor constante (como fuego o quemazón).</span></button>
      <button class="opt-btn" onclick="goStep(3)"><span class="icon">🧊</span> <span>Entumecimiento, frío y pérdida de sensibilidad.</span></button>
      <button class="opt-btn" onclick="goStep(3)"><span class="icon">📌</span> <span>Sensación de caminar sobre agujas o cristales.</span></button>
    </div>
  </div>

  <!-- ── STEP 3 (Duración) ── -->
  <div class="screen" id="step3">
    <p class="question">¿Hace cuánto tiempo comenzó este calvario en tus manos o pies?</p>
    <div class="options">
      <button class="opt-btn" onclick="goStep(4)"><span class="icon">⏱️</span> <span>Menos de 6 meses.</span></button>
      <button class="opt-btn" onclick="goStep(4)"><span class="icon">⏳</span> <span>Entre 1 y 3 años.</span></button>
      <button class="opt-btn" onclick="goStep(4)"><span class="icon">📅</span> <span>Entre 3 y 5 años.</span></button>
      <button class="opt-btn" onclick="goStep(4)"><span class="icon">🕰️</span> <span>Más de 5 años (he probado de todo).</span></button>
    </div>
  </div>

  <!-- ── STEP 4 (BREAK INFORMATIVO 1) ── -->
  <div class="screen" id="step4">
    <div class="correction-box" style="display:block; border-color: #F87171;">
      <span class="label" style="background:#FEF2F2; color:#DC2626;">⚠️ ALERTA NEUROLÓGICA</span>
      <p style="margin-bottom: 14px;">La industria médica tradicional te dirá que "aprendas a vivir con el dolor". Te recetarán pastillas como la Gabapentina que te dejan somnoliento, o cremas que solo adormecen la piel temporalmente.</p>
      <p>Pero la neurociencia moderna acaba de revelar algo inquietante: <strong>El daño en tus nervios NO es causado por una simple mala circulación ni por el desgaste de la edad.</strong></p>
      <button class="opt-btn" onclick="goStep(5)" style="margin-top: 20px; border-color: var(--accent); background: #F0FDF4; width: 100%; justify-content: center; font-weight: 800;">
        <span>Continuar con mi evaluación ➔</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 5 (La Trampa) ── -->
  <div class="screen" id="step5">
    <p class="question" id="step5Question">¿Cuál crees que es la verdadera razón por la que sientes ese insoportable dolor y ardor?</p>
    <div class="options" id="step5Options">
      <button class="opt-btn" onclick="step5Select()"><span class="icon">🩸</span> <span>Mala circulación sanguínea.</span></button>
      <button class="opt-btn" onclick="step5Select()"><span class="icon">🍬</span> <span>Niveles altos de azúcar.</span></button>
      <button class="opt-btn" onclick="step5Select()"><span class="icon">👴</span> <span>Desgaste natural por la edad.</span></button>
      <button class="opt-btn" onclick="step5Select()"><span class="icon">🧬</span> <span>La destrucción de tus Células de Schwann.</span></button>
    </div>
    
    <div class="spinner-wrap" id="step5Spinner" style="display:none;">
      <div class="spinner"></div><div class="spinner-text">Analizando tu respuesta...</div>
    </div>
    <div class="correction-box" id="step5Correction" style="display:none;">
      <span class="label">⚠️ INCORRECTO</span>
      <p style="margin-bottom: 12px;">La mayoría elige la circulación o el azúcar. Pero la verdadera raíz del dolor es la <strong>destrucción de tus Células de Schwann</strong> (el escudo protector de tus nervios). Sigamos...</p>
      <button class="opt-btn" onclick="goStep(6)" style="border-color: var(--accent); background: #F0FDF4; width: 100%; justify-content: center; font-weight: 800;">
        <span>CONTINUAR ➔</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 6 (Demografía Visual) ── -->
  <div class="screen" id="step6">
    <p class="question">Para que nuestro sistema calibre tu protocolo clínico, ¿en qué rango de edad te encuentras?</p>
    <div class="options grid-2x2">
      <button class="opt-btn" onclick="goStep(7)">
        <div class="demo-photo">🙎‍♀️</div>
        <span>40 a 49 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(7)">
        <div class="demo-photo">🧓</div>
        <span>50 a 59 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(7)">
        <div class="demo-photo">👵</div>
        <span>60 a 69 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(7)">
        <div class="demo-photo">👴</div>
        <span>70 años o más</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 7 (Impacto - Checkboxes) ── -->
  <div class="screen" id="step7">
    <p class="question">¿De qué manera este daño nervioso está destruyendo tu vida diaria? <em>(Selecciona todas las que apliquen)</em></p>
    <div class="options">
      <label class="opt-btn check-opt"><input type="checkbox"> <span>El dolor me despierta y no puedo dormir bien.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me cuesta caminar, estar de pie o hacer tareas simples.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me siento irritable, frustrado o ansioso constantemente.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me aísla de mi familia y ya no disfruto jugar.</span></label>
      
      <button class="cta-btn" onclick="goStep(8)" style="margin-top:20px;">Confirmar síntomas ➔</button>
    </div>
  </div>

  <!-- ── STEP 8 (BREAK INFORMATIVO 2) ── -->
  <div class="screen" id="step8">
    <div class="correction-box" style="display:block; border-color: #10B981; background: #FFF;">
      <span class="label" style="background:#F0FDF4; color:#059669;">🧬 EL ENEMIGO INVISIBLE</span>
      <p style="margin-bottom: 14px;">La razón por la que tus <strong>Células de Schwann</strong> están muriendo es por la presencia de "neurotóxicos" ocultos en tu propia casa.</p>
      
      <img src="toxic_nerve.png" style="width: 100%; border-radius: 8px; margin: 12px 0; border: 1px solid #E2E8F0;" alt="Daño por Neurotóxicos">

      <p style="margin-bottom: 14px;">Sin este escudo protector, los neurotóxicos arrasan tu red de nervios como ratas royendo cables eléctricos. Por eso sientes esos choques y ardores.</p>
      <p>Las siguientes respuestas nos dirán qué protocolo de reparación es exacto para tu nivel de toxicidad.</p>

      <button class="opt-btn" onclick="startFakeLoader()" style="margin-top: 20px; border-color: var(--accent); background: #10B981; color: white; width: 100%; justify-content: center; font-weight: 800;">
        <span style="color:white;">Ver mis resultados ➔</span>
      </button>
    </div>
  </div>

"""
content = content[:quiz_start] + new_quiz_html + content[quiz_end:]

bridge_cta_start = content.find('  <p style="text-align:center;font-weight:700;')
bridge_cta_parent_end = content.find('  <p class="urgency-note">', bridge_cta_start)

audio_masterstroke = """  <div class="audio-alert">
    <div class="audio-header">⚠️ ALERTA MÉDICA URGENTE:</div>
    <p style="font-size: 0.9rem; margin-bottom: 16px; color: #7F1D1D;">Según tu perfil, el daño en tu escudo nervioso está en <strong>Fase Crítica</strong>. Tienes un mensaje de voz y video urgente del especialista Carlos Mendoza explicando tu diagnóstico.</p>
    
    <div class="dr-profile">
      <img src="dr_mendoza.png" alt="Dr. Mendoza">
      <div class="dr-info">
        <strong style="color: #0F172A; font-weight: 800; display:block;">Dr. Carlos Mendoza</strong>
        <span style="color: #64748B; font-size: 0.8rem;">Investigador Clínico</span>
      </div>
    </div>
    
    <p class="dr-quote">"Por favor, escucha esto de inmediato antes de que el daño sea irreversible..."</p>
    
    <p style="font-weight:800; font-size:0.9rem; color:#0F172A; margin-bottom:12px;">👇 HAZ CLIC ABAJO PARA ESCUCHAR TU DIAGNÓSTICO 👇</p>
    
    <a class="cta-btn" href="vsl.html" target="_self" id="ctaBtn" style="padding: 16px 12px; font-size: 1rem; margin-bottom: 6px;">
      <span class="play-icon">▶️</span> ESCUCHAR EL MENSAJE AHORA
    </a>
  </div>
"""

content = content[:bridge_cta_start] + audio_masterstroke + content[bridge_cta_parent_end:]

js_updates = {
    'const progressMap = { 1: 10, 2: 35, 3: 60, 4: 85 };': 'const progressMap = { 1: 10, 2: 20, 3: 35, 4: 45, 5: 55, 6: 65, 7: 80, 8: 90 };',
    'function step2Select() {': 'function step5Select() {',
    "document.querySelectorAll('#step2Options .opt-btn').forEach(b => b.disabled = true);": "document.querySelectorAll('#step5Options .opt-btn').forEach(b => b.disabled = true);",
    "document.getElementById('step2Question').style.opacity = '0.3';": "document.getElementById('step5Question').style.opacity = '0.3';",
    "document.getElementById('step2Options').style.display = 'none';": "document.getElementById('step5Options').style.display = 'none';",
    "const spinner = document.getElementById('step2Spinner');": "const spinner = document.getElementById('step5Spinner');",
    "const box = document.getElementById('correctionBox');": "const box = document.getElementById('step5Correction');",
    "const question = document.getElementById('step2Question');": "const question = document.getElementById('step5Question');"
}

for old, new in js_updates.items():
    content = content.replace(old, new)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
