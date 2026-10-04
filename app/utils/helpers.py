from typing import Any, Dict


def to_dict(obj: Any) -> Dict[str, Any]:
    if hasattr(obj, "dict"):
        return obj.dict()
    if hasattr(obj, "__dict__"):
        return vars(obj)
    return {"value": str(obj)}


def build_response(message: str, data: Any = None) -> Dict[str, Any]:
    result = {"message": message}
    if data is not None:
        result["data"] = data
    return result




# helper functions, to_dict, build_response, format_date, parse_date, validate_email, validate_password, generate_token, verify_token, hash_password, verify_password, send_email, send_sms, log_event, handle_error 