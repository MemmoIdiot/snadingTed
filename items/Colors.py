from typing import Dict


class Colors:
    COLORS_SELECTOR: Dict[str, str] = {
        colore: f'//*[@id="color-{i}"]'
        for i, colore in enumerate((
            "nero", "marrone", "grigio", "beige", "rosa", "viola", "rosso",
            "giallo", "blu", "verde", "arancio", "bianco", "argento", "oro",
            "multi", "cachi", "turchese", "panna", "albicocca", "corallo",
            "borgogna", "rosa (carne)", "lilla", "azzurro", "blu marino",
            "verde scuro", "senape", "menta"), 1)
    }
