import os
import sys
import django
from django.conf import settings
from django.template.loader import render_to_string

# Basisverzeichnis hinzufügen
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'deintraumgarten'))

# Django-Einstellungen konfigurieren
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.staticfiles',  # Ermöglicht das Laden statischer Dateien
        'myapp',  # Name deiner Django-App
    ],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'deintraumgarten', 'myapp', 'templates')],
            'APP_DIRS': True,
        },
    ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[os.path.join(BASE_DIR, 'deintraumgarten', 'myapp', 'static')],
)

# Django initialisieren
django.setup()

# Templates rendern
def render_templates():
    # Das `index.html`-Template rendern und in den `public`-Ordner speichern
    output_path = os.path.join(BASE_DIR, 'public', 'index.html')
    rendered_content = render_to_string('index.html')

    # Sicherstellen, dass der Zielordner existiert
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Gerenderten Inhalt in die Datei schreiben
    with open(output_path, 'w') as f:
        f.write(rendered_content)

if __name__ == "__main__":
    render_templates()
