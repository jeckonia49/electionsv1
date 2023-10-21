from .base import *


# APPLICATIONS

LOCAL_APPS = ["accounts", "apis"]
FRAMEWORK_APPS = [
    "corsheaders",
    "rest_framework",
]

INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += FRAMEWORK_APPS

# CORS POLICY
CORS_ALLOWED_ORIGINS = [
"http://localhost:5173"
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    
    "DEFAULT_AUTHENTICATION_CLASSES" : [
        'rest_framework.authentication.SessionAuthentication',
    ]
}