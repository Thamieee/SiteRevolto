from services.user_service import register_logic, profile_logic, confirm_email_logic, login_logic, logout_logic

def register():
    return register_logic()

def profile(username: str):
    return profile_logic(username=username)

def confirm_email(token):
    return confirm_email_logic(token=token)

def login():
    return login_logic()

def logout():
    return logout_logic()