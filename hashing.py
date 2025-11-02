import hashlib

def calculando_file_hash(caminho_arquivo):
        hasher = hashlib.sha256()
        with open(caminho_arquivo, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()