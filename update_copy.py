import re

filepath = 'd:/Downloads/neuropatia/neuropathy-quiz-funnel.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    # Step 1
    "fricción cero": "Fricción Cero", # Just in case
    "¿tu primer instinto es <strong>masajearte con alguna loción o pomada</strong>?": "¿tu primer instinto es <strong>frotarte con alguna crema o pomada</strong>?",
    
    # Step 2
    "¿Cómo describirías exactamente la molestia más insoportable que sientes en tus extremidades?": "¿Cómo describirías la molestia más difícil de soportar que sientes en tus manos o pies?",
    "Punzadas eléctricas repentinas.": "Punzadas eléctricas que llegan de repente.",
    "Un ardor constante (como fuego o quemazón).": "Un ardor constante, como si te quemaras por dentro.",
    "Entumecimiento, frío y pérdida de sensibilidad.": "Adormecimiento, frío y pérdida de sensibilidad.",
    "Sensación de caminar sobre agujas o cristales.": "Sensación de caminar sobre agujas o vidrios rotos.",

    # Step 3
    "¿Hace cuánto tiempo comenzó este calvario en tus manos o pies?": "¿Hace cuánto tiempo empezó este sufrimiento en tus manos o pies?",
    "Más de 5 años (he probado de todo).": "Más de 5 años (ya probé de todo).",

    # Step 4
    "¿Cuál crees que es la verdadera razón por la que sientes ese insoportable dolor y ardor?": "¿Cuál crees que es la verdadera razón por la que sientes ese dolor y ardor insoportables?",
    "La mayoría elige la circulación o el azúcar. Pero la verdadera raíz del dolor es la <strong>destrucción de tus Células de Schwann</strong> (el escudo protector de tus nervios). Sigamos...": "La mayoría escoge la circulación o el azúcar. Pero la verdadera raíz del dolor es la <strong>destrucción de tus Células de Schwann</strong> — el escudo protector de tus nervios. Continuemos...",

    # Step 5
    'que "aprendas a vivir con el dolor". Te recetarán pastillas como la Gabapentina que te dejan somnoliento.': 'que "aprendas a vivir con el dolor". Te recetarán pastillas como la Gabapentina que te dejan atontado, sin energía y sin poder pensar con claridad.',
    
    # Step 6
    "Para calibrar tu protocolo metabólico: ¿Eres Hombre o Mujer?": "Para personalizar tu protocolo: ¿Eres Hombre o Mujer?",

    # Step 7
    "Para que nuestro sistema calibre tu protocolo clínico, ¿en qué rango de edad te encuentras?": "Para que nuestro sistema ajuste tu protocolo clínico, ¿en qué rango de edad estás?",

    # Step 8
    "¿De qué manera este daño nervioso está destruyendo tu vida diaria?": "¿De qué forma este daño nervioso está afectando tu vida diaria?",
    "El dolor me despierta y no puedo dormir bien.": "El dolor me despierta en la noche y no puedo descansar bien.",
    "Me cuesta caminar, estar de pie o hacer tareas simples.": "Me cuesta caminar, permanecer de pie o hacer cosas sencillas.",
    "Me siento irritable, frustrado o ansioso constantemente.": "Me siento irritable, agotado o con angustia todo el tiempo.",
    "Me aísla de mi familia y ya no disfruto jugar.": "Me aleja de mi familia y ya no puedo disfrutar momentos con mis seres queridos.",

    # Step 9
    "La razón por la que tus <strong>Células de Schwann</strong> mueren está en tu propia casa.": "La razón por la que tus <strong>Células de Schwann</strong> están muriendo se encuentra en tu propio hogar.",
    "Neurotóxicos ocultos en jabones y alimentos arrasan tus nervios como ratas royendo cables eléctricos. Por eso sientes ardor.": "Hay neurotóxicos escondidos en jabones y alimentos que destruyen tus nervios como si fueran cables pelados siendo roídos por dentro. Por eso sientes ese ardor que no te da tregua.",

    # Step 10 (Loader setup)
    "Escaneando marcadores de daño nervioso...": "Escaneando marcadores neurológicos...",
    "Cruzando con base de datos...": "Cruzando datos con base clínica...",
    "Verificando protocolos de recuperación...": "Finalizando recomendaciones personalizadas...",

    # Step 11
    "Uso crónico de cremas o analgésicos": "Uso prolongado de cremas o analgésicos",
    "urgente del experto Carlos Mendoza sobre tus resultados.": "urgente del especialista Carlos Mendoza con los resultados de tu evaluación.",
    "ya recuperaron su vida con este método": "ya recuperaron su calidad de vida con este método"
}

for old, new in replacements.items():
    if old in html:
        html = html.replace(old, new)
    else:
        print(f"NOT FOUND: {old}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("done!")
