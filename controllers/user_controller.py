from services.user_service import create_logic, profile_logic

def create():
    return create_logic()

def profile(username: str):
    return profile_logic(username=username)