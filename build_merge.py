import re

filepath = 'd:/Downloads/neuropatia/neuropathy-quiz-funnel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Step 4 and Step 5 HTML with merged Step 4
merged_step_4 = """<!-- ── STEP 4 (La Trampa + Break Fusionado) ── -->
  <div class="screen" id="step4">
    <p class="question" id="step4Question">¿Cuál crees que es la verdadera razón por la que sientes ese dolor y ardor insoportables?</p>
    <div class="options" id="step4Options">
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🩸</span> <span>Mala circulación sanguínea.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🍬</span> <span>Niveles altos de azúcar.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">👴</span> <span>Desgaste natural por la edad.</span></button>
      <button class="opt-btn" onclick="step4Select()"><span class="icon">🧬</span> <span>La destrucción de tus Células de Schwann.</span></button>
    </div>
    
    <div class="spinner-wrap" id="step4Spinner" style="display:none;">
      <div class="spinner"></div><div class="spinner-text">Analizando tu respuesta...</div>
    </div>
    <div class="correction-box" id="step4Correction" style="display:none; border-color: #F87171;">
      <span class="label" style="background:#FEF2F2; color:#DC2626;">⚠️ INCORRECTO</span>
      <p style="margin-bottom: 14px;">La industria médica te dirá que "aprendas a vivir con el dolor" o culpará a la mala circulación. Te recetarán pastillas que solo te dejan somnoliento.</p>
      
      <img src="schwann_cells.webp" style="width: 100%; border-radius: 8px; margin: 12px 0; border: 1px solid #E2E8F0;" alt="Daño Células de Schwann">

      <p style="margin-bottom: 14px;">Pero la neurociencia moderna acaba de revelar la verdad: La verdadera raíz del dolor es la <strong>destrucción de tus Células de Schwann</strong> (el escudo protector de tus nervios). Sigamos...</p>
      <button class="opt-btn" onclick="goStep(5)" style="margin-top: 20px; border-color: var(--accent); background: #F0FDF4; width: 100%; justify-content: center; font-weight: 800;">
        <span>Calibrar mi diagnóstico ➔</span>
      </button>
    </div>
  </div>"""

# Remove old step 4 and 5
start_tag = '<!-- ── STEP 4 (La Trampa) ── -->'
end_tag = '<!-- ── STEP 6 (Género - Micro-compromiso) ── -->'
start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

html = html[:start_idx] + merged_step_4 + '\n\n  ' + html[end_idx:]

# Rename ID step6 to step5
html = html.replace('id="step6"', 'id="step5"')
html = html.replace('<!-- ── STEP 6 (Género - Micro-compromiso) ── -->', '<!-- ── STEP 5 (Género - Micro-compromiso) ── -->')
html = html.replace("selectGender('m')", "selectGender('m')") # no change needed but wait, selectGender does goStep(7). Let's fix selectGender in JS.

# Rename ID step7 to step6
html = html.replace('id="step7"', 'id="step6"')
html = html.replace('<!-- ── STEP 7 (Demografía Visual) ── -->', '<!-- ── STEP 6 (Demografía Visual) ── -->')
html = html.replace('goStep(8)', 'goStep(7)')

# Rename ID step8 to step7
html = html.replace('id="step8"', 'id="step7"')
html = html.replace('<!-- ── STEP 8 (Impacto - Checkboxes) ── -->', '<!-- ── STEP 7 (Impacto - Checkboxes) ── -->')
html = html.replace('goStep(9)', 'goStep(8)')

# Rename ID step9 to step8
html = html.replace('id="step9"', 'id="step8"')
html = html.replace('<!-- ── STEP 9 (BREAK INFORMATIVO 2) ── -->', '<!-- ── STEP 8 (BREAK INFORMATIVO 2) ── -->')

# Update JS progress map
html = re.sub(
    r'const progressMap = \{.*?\};',
    'const progressMap = { 1: 10, 2: 20, 3: 35, 4: 50, 5: 65, 6: 75, 7: 85, 8: 95 };',
    html
)

# Update selectGender JS logic
html = html.replace('goStep(7);', 'goStep(6);')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("done!")
