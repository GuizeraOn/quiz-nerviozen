import re

filepath = 'd:/Downloads/neuropatia/neuropathy-quiz-funnel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_to_add = """
  /* WhatsApp Fake Audio CTA */
  .fake-audio-cta {
    background-color: #F0F2F5;
    border-radius: 12px;
    padding: 10px 12px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    text-decoration: none;
    color: inherit;
    width: 100%;
    transition: transform 0.1s ease;
    margin-bottom: 20px;
  }
  .fake-audio-cta:active {
    transform: scale(0.98);
  }
  .avatar-container {
    position: relative;
  }
  .avatar-img {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    object-fit: cover;
  }
  .mic-icon-badge {
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 20px;
    height: 20px;
    background: #34B7F1;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    color: white;
    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  }
  .player-body {
    flex-grow: 1;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .play-button {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    color: #8696A0;
    animation: mild-pulse 2s infinite;
  }
  @keyframes mild-pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1); }
  }
  .waveform-container {
    flex-grow: 1;
    height: 30px;
    position: relative;
    display: flex;
    align-items: center;
    overflow: hidden;
  }
  .waveform-img {
    width: 100%;
    height: 28px;
    opacity: 0.6;
    object-fit: cover;
    filter: invert(1);
  }
  .progress-dot {
    position: absolute;
    left: 2px;
    width: 14px;
    height: 14px;
    background: #25D366;
    border-radius: 50%;
    box-shadow: 0 0 2px rgba(0,0,0,0.2);
  }
  .audio-meta {
    font-size: 11px;
    color: #8696A0;
    white-space: nowrap;
  }
</style>"""
content = content.replace('</style>', css_to_add)

# 2. Replace Bridge Page bloat with lean WhatsApp strategy
start_str = '  <div class="alert-box info">'
end_str = '  <hr class="report-divider">'

start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx)

replacement_html = """
  <div class="data-profile-box" style="margin-top: 24px; margin-bottom:24px; font-size:1rem;">
    <strong style="color:#0F172A; display:block; margin-bottom:16px; font-size:1.1rem;">📋 Tu Perfil Neuropático</strong>
    <ul style="list-style:none; padding:0; margin:0; line-height:1.4;">
      <li><strong style="color: #DC2626;">🔴 Origen probable:</strong><br>Apoptosis celular inducida por neurotóxicos</li>
      <li style="margin-top: 14px;"><strong style="color: #D97706;">⚠️ Factor agravante:</strong><br>Uso crónico de cremas o analgésicos</li>
      <li style="margin-top: 14px;"><strong>📊 Nivel de daño:</strong><br>Alto (Fase Crítica)</li>
      <li style="margin-top: 14px;"><strong style="color: #059669;">✅ Pronóstico:</strong><br>Reversible</li>
    </ul>
  </div>

  <div style="background:#FEF2F2; padding: 12px; border-radius: 4px; border-left: 4px solid #EF4444; margin-bottom: 20px; font-size: 0.9rem; color: #7F1D1D; font-weight: 600;">
    ⚠️ ALERTA: Tienes un mensaje de voz urgente del experto Carlos Mendoza sobre tus resultados. ESCUCHA EL AUDIO ANTES DE CONTINUAR.
  </div>

  <!-- FAKE WHATSAPP PLAYER CTA -->
  <a href="vsl.html" class="fake-audio-cta" target="_self">
    <div class="avatar-container">
      <img src="dr_mendoza.png" alt="Dr. Carlos Mendoza" class="avatar-img">
      <div class="mic-icon-badge">🎤</div>
    </div>
    <div class="player-body">
      <div class="play-button">▶️</div>
      <div class="waveform-container">
        <img src="waveform.png" class="waveform-img" alt="Audio">
        <div class="progress-dot"></div>
      </div>
    </div>
    <div class="audio-meta">0:00 / 2:15</div>
  </a>

  <div style="text-align:center; margin-top:24px; margin-bottom: 16px;">
    <a href="vsl.html" target="_self" style="color:#2563EB; font-weight:700; text-decoration:underline; font-size:0.95rem;">Descubrir el Protocolo NervioZen para mi perfil ➔</a>
    <p style="color:#64748B; font-size:0.8rem; margin-top:16px;">Más de 87,000 personas ya recuperaron su vida con este método 100% natural.</p>
  </div>

"""

new_content = content[:start_idx] + replacement_html + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("done!")
