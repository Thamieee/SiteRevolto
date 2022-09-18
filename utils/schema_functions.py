def enforce_schema(schema: list, form: dict):
    for key in form:
        if not key in schema:
            form.pop(key)
    for value in schema:
        if not form[value]:
            form[value] = None
    return form

def get_users_schema() -> list:
    users_schema = (
        "id", "is_admin", "email", "username", "password", "role",
        "date_added"
    )
    return users_schema
