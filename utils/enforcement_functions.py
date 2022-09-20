def check_user_form(data) -> bool:
    is_data_ok = True
    if not data["username"]:
        is_data_ok = False
    elif not data["email"]:
        is_data_ok = False
    elif not data["password"]:
        is_data_ok = False
    elif data["confirmPassword"] != data["password"]:
        is_data_ok = False
    return is_data_ok
