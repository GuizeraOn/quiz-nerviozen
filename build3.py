import re

filepath = 'd:/Downloads/neuropatia/neuropathy-quiz-funnel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the progress map
content = re.sub(
    r'const progressMap = \{.*?\};',
    'const progressMap = { 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 85, 9: 95 };',
    content
)

# 2. Add the aggressive pulse CSS
css_to_add = """
  @keyframes pulse-aggressive {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
    70% { transform: scale(1.03); box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
  }
  .pulse-aggressive {
    animation: pulse-aggressive 1.2s infinite !important;
  }
</style>
"""
content = content.replace('</style>', css_to_add)

# 3. Add ID to the main CTA button
content = content.replace(
    '<a href="vsl.html" target="_self" class="opt-btn" style="border-color: #059669; background: #25D366;',
    '<a href="vsl.html" id="mainVslCta" target="_self" class="opt-btn" style="border-color: #059669; background: #25D366;'
)

# 4. Add pulse toggles to JS
pulse_logic = """
    doCarlosAudio.addEventListener('play', () => {
      const cta = document.getElementById('mainVslCta');
      if(cta) cta.classList.add('pulse-aggressive');
    });
    doCarlosAudio.addEventListener('pause', () => {
      const cta = document.getElementById('mainVslCta');
      if(cta) cta.classList.remove('pulse-aggressive');
    });

    // Animate UI elements while audio plays
"""
content = content.replace('    // Animate UI elements while audio plays', pulse_logic)

# 5. Fix JS step5Select -> step4Select
js_replace = """
// ── Step 4 transition (La Trampa) ──
function step4Select() {
  document.querySelectorAll('#step4Options .opt-btn').forEach(b => b.disabled = true);
  document.getElementById('step4Question').style.opacity = '0.3';
  document.getElementById('step4Options').style.display = 'none';

  const spinner = document.getElementById('step4Spinner');
  spinner.style.display = 'flex';

  setTimeout(() => {
    spinner.style.display = 'none';
    const box = document.getElementById('step4Correction');
    const question = document.getElementById('step4Question');
    if (question) question.style.display = 'none';
    box.style.display = 'block';
  }, 1500);
}
"""
content = re.sub(
    r'// ── Step 2 transition ──\s*function step5Select\(\) \{[\s\S]*?\}, 1500\);\s*\}',
    js_replace.strip(),
    content
)


# 6. Replace the entire HTML Steps block
start_tag = '<!-- ── STEP 4 (BREAK INFORMATIVO 1) ── -->'
end_tag = '<!-- ── FAKE LOADER ── -->'
start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

new_steps_html = """<!-- ── STEP 4 (La Trampa) ── -->
  <div class="screen" id="step4">
    <p class="question" id="step4Question">¿Cuál crees que es la verdadera razón por la que sientes ese insoportable dolor y ardor?</p>
    <div class="options" id="step4Options">
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🩸</span> <span>Mala circulación sanguínea.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🍬</span> <span>Niveles altos de azúcar.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">👴</span> <span>Desgaste natural por la edad.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🧬</span> <span>La destrucción de tus Células de Schwann.</span></button>
    </div>
    
    <div class="spinner-wrap" id="step4Spinner" style="display:none;">
      <div class="spinner"></div><div class="spinner-text">Analizando tu respuesta...</div>
    </div>
    <div class="correction-box" id="step4Correction" style="display:none;">
      <span class="label">⚠️ INCORRECTO</span>
      <p style="margin-bottom: 12px;">La mayoría elige la circulación o el azúcar. Pero la verdadera raíz del dolor es la <strong>destrucción de tus Células de Schwann</strong> (el escudo protector de tus nervios). Sigamos...</p>
      <button class="opt-btn" onclick="goStep(5)" style="border-color: var(--accent); background: #F0FDF4; width: 100%; justify-content: center; font-weight: 800;">
        <span>CONTINUAR ➔</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 5 (BREAK INFORMATIVO 1) ── -->
  <div class="screen" id="step5">
    <div class="correction-box" style="display:block; border-color: #F87171;">
      <span class="label" style="background:#FEF2F2; color:#DC2626;">⚠️ ALERTA NEUROLÓGICA</span>
      <p style="margin-bottom: 14px;">La industria médica tradicional te dirá que "aprendas a vivir con el dolor". Te recetarán pastillas como la Gabapentina que te dejan somnoliento.</p>
      <p>Pero la neurociencia comprobó que <strong>el daño nervioso NO es causado por mala circulación ni por el desgaste de la edad.</strong></p>
      <button class="opt-btn" onclick="goStep(6)" style="margin-top: 20px; border-color: var(--accent); background: #F0FDF4; width: 100%; justify-content: center; font-weight: 800;">
        <span>Continuar con mi evaluación ➔</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 6 (Género - Micro-compromiso) ── -->
  <div class="screen" id="step6">
    <p class="question">Para calibrar tu protocolo metabólico: ¿Eres Hombre o Mujer?</p>
    <div class="options">
      <button class="opt-btn" onclick="goStep(7)"><span class="icon">👨</span> <span>Hombre</span></button>
      <button class="opt-btn" onclick="goStep(7)"><span class="icon">👩</span> <span>Mujer</span></button>
    </div>
  </div>

  <!-- ── STEP 7 (Demografía Visual) ── -->
  <div class="screen" id="step7">
    <p class="question">Para que nuestro sistema calibre tu protocolo clínico, ¿en qué rango de edad te encuentras?</p>
    <div class="options grid-2x2">
      <button class="opt-btn" onclick="goStep(8)">
        <div class="demo-photo">🙎‍♀️</div>
        <span>40 a 49 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(8)">
        <div class="demo-photo">🧓</div>
        <span>50 a 59 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(8)">
        <div class="demo-photo">👵</div>
        <span>60 a 69 años</span>
      </button>
      <button class="opt-btn" onclick="goStep(8)">
        <div class="demo-photo">👴</div>
        <span>70 años o más</span>
      </button>
    </div>
  </div>

  <!-- ── STEP 8 (Impacto - Checkboxes) ── -->
  <div class="screen" id="step8">
    <p class="question">¿De qué manera este daño nervioso está destruyendo tu vida diaria? <em>(Selecciona todas las que apliquen)</em></p>
    <div class="options">
      <label class="opt-btn check-opt"><input type="checkbox"> <span>El dolor me despierta y no puedo dormir bien.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me cuesta caminar, estar de pie o hacer tareas simples.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me siento irritable, frustrado o ansioso constantemente.</span></label>
      <label class="opt-btn check-opt"><input type="checkbox"> <span>Me aísla de mi familia y ya no disfruto jugar.</span></label>
      
      <button class="cta-btn" onclick="goStep(9)" style="margin-top:20px;">Confirmar síntomas ➔</button>
    </div>
  </div>

  <!-- ── STEP 9 (BREAK INFORMATIVO 2) ── -->
  <div class="screen" id="step9">
    <div class="correction-box" style="display:block; border-color: #10B981; background: #FFF;">
      <span class="label" style="background:#F0FDF4; color:#059669;">🧬 EL ENEMIGO INVISIBLE</span>
      <p style="margin-bottom: 14px;">La razón por la que tus <strong>Células de Schwann</strong> mueren está en tu propia casa.</p>
      
      <img src="toxic_nerve.png" style="width: 100%; border-radius: 8px; margin: 12px 0; border: 1px solid #E2E8F0;" alt="Daño por Neurotóxicos">

      <p style="margin-bottom: 14px;">Neurotóxicos ocultos en jabones y alimentos arrasan tus nervios como ratas royendo cables eléctricos. Por eso sientes ardor.</p>
      
      <button class="opt-btn" onclick="startFakeLoader()" style="margin-top: 20px; border-color: var(--accent); background: #10B981; color: white; width: 100%; justify-content: center; font-weight: 800;">
        <span style="color:white;">Ver mis resultados ➔</span>
      </button>
    </div>
  </div>

  """

content = content[:start_idx] + new_steps_html + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("done!")
