"""
Módulo de gerenciamento de sessões dos usuários no WhatsApp.
"""

user_sessions = {}

def start_session(user_id, data={}):
    """Inicia uma sessão para o usuário."""
    user_sessions[user_id] = data

def update_session(user_id, key, value):
    """Atualiza dados dentro da sessão do usuário."""
    if user_id in user_sessions:
        user_sessions[user_id][key] = value

def get_session(user_id):
    """Retorna a sessão atual do usuário."""
    return user_sessions.get(user_id, {})

def remove_session(user_id):
    """Remove a sessão do usuário."""
    user_sessions.pop(user_id, None)
