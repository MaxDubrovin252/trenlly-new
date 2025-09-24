import bcrypt

def hash_password(password:str)->bytes:
    pass_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password=pass_bytes,salt=bcrypt.gensalt())

def verify_password(password:str, hash_pass:bytes)->bool:
    return bcrypt.checkpw(password=password.encode(),hashed_password=hash_pass)