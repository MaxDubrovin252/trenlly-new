__all__=(
    "router",
    "user_verify_by_token",
)

from .views import router
from .dependencies import user_verify_by_token