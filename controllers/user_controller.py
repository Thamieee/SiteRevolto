from services.user_service import register_logic, profile_logic, email_verification_logic

def register():
    return register_logic()

def profile(username: str):
    return profile_logic(username=username)

def email_verification(token):
    return email_verification_logic(token=token)