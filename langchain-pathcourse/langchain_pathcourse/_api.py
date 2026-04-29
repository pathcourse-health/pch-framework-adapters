"""Shared API helpers and error mapping for langchain-pathcourse."""

PCH_GATEWAY = "https://gateway.pathcoursehealth.com/v1"


class PathCourseError(Exception):
    """Base exception for PathCourse adapter errors."""


class InsufficientBalanceError(PathCourseError):
    """Raised when the agent's USDC balance is too low to make a request."""


class TierError(PathCourseError):
    """Raised when the requested model is above the agent's certification tier."""


def map_status_to_error(status_code: int, body: dict) -> Exception:
    """Map gateway HTTP status + body to a typed exception."""
    err_type = (body or {}).get("error", {}).get("type") if isinstance(body, dict) else None
    message = (body or {}).get("error", {}).get("message", "PathCourse gateway error")
    if status_code == 402 or err_type == "insufficient_balance":
        return InsufficientBalanceError(message)
    if status_code == 403 and err_type in ("tier_too_low", "model_not_in_tier"):
        return TierError(message)
    return PathCourseError(f"{status_code}: {message}")
