import hashlib
import hmac
from dataclasses import dataclass

# Login simples com usuário local.
# Quando o banco de dados estiver pronto, basta trocar a busca em _USERS
# por uma consulta ao banco mantendo a função authenticate().
#
# Usuário de exemplo:  admin  /  admin123
# (a senha fica guardada apenas como hash PBKDF2, nunca em texto puro)

_ITERATIONS = 120_000


@dataclass(frozen=True)
class User:
    username: str
    name: str
    role: str


_USERS = {
    "admin": {
        "name": "Administrador",
        "role": "Conta local",
        "salt": bytes.fromhex("027ace11e7eb9be55de1e7f1ce4561a0"),
        "hash": bytes.fromhex("b53622bd28a36916ce4b1403be4a256cb9e5913ddf071631fa3797735d44edfb"),
    },
}

# usado quando o usuário não existe, para o tempo de resposta ser o mesmo
_DUMMY_SALT = bytes(16)
_DUMMY_HASH = bytes(32)


def _hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _ITERATIONS)


def authenticate(username, password):
    # retorna o User se as credenciais forem válidas, senão None
    record = _USERS.get(username.strip().lower())
    salt = record["salt"] if record else _DUMMY_SALT
    expected = record["hash"] if record else _DUMMY_HASH

    candidate = _hash_password(password, salt)
    if record is not None and hmac.compare_digest(candidate, expected):
        return User(username=username.strip().lower(), name=record["name"], role=record["role"])
    return None
