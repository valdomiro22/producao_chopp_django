
from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured


# ==================================================
# DIRETÓRIOS E VARIÁVEIS DE AMBIENTE
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# ==================================================
# SEGURANÇA
# ==================================================

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "DJANGO_ALLOWED_HOSTS",
        "localhost,127.0.0.1"
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "DJANGO_CSRF_TRUSTED_ORIGINS", ""
    ).split(",")
    if origin.strip()
]

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https"
)


# ==================================================
# APLICAÇÕES
# ==================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Bibliotecas
    "django_bootstrap5",
    "stdimage",

    # Aplicações do projeto
    "home",
    "barril",
    "produto",
    "grade",
    "producao",
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS E TEMPLATES
# ==================================================

ROOT_URLCONF = "producao_chopp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "producao_chopp.wsgi.application"


# ==================================================
# BANCO DE DADOS
# ==================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:

    # PostgreSQL Neon (Vercel)
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=0,
            ssl_require=True
        )
    }

elif os.getenv("VERCEL"):

    raise ImproperlyConfigured(
        "DATABASE_URL não configurada na Vercel."
    )

else:

    # PostgreSQL local (Windows)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv(
                "DB_NAME", "producao_chopp"
            ),
            "USER": os.getenv(
                "DB_USER", "postgres"
            ),
            "PASSWORD": os.environ["DB_PASSWORD"],
            "HOST": os.getenv(
                "DB_HOST", "localhost"
            ),
            "PORT": os.getenv(
                "DB_PORT", "5432"
            ),
        }
    }


# ==================================================
# VALIDAÇÃO DE SENHAS
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ==================================================
# IDIOMA E FUSO HORÁRIO
# ==================================================

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# ==================================================
# ARQUIVOS ESTÁTICOS
# ==================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ==================================================
# E-MAIL
# ==================================================

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
}


# ==================================================
# CONFIGURAÇÕES ADICIONAIS
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
