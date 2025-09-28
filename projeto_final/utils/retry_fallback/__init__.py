import os
import shutil
import pandas as pd
import time

def executar_com_retry(func, max_tentativas=3, espera=5, fallback_func=None, *args, **kwargs):
    for tentativa in range(1, max_tentativas + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERRO] Tentativa {tentativa}/{max_tentativas} falhou: {e}")
            if tentativa < max_tentativas:
                time.sleep(espera)
            else:
                print("[FALHA DEFINITIVA] Todas tentativas falharam.")
                if fallback_func:
                    print("[FALLBACK] Executando fallback...")
                    return fallback_func(*args, **kwargs)
                else:
                    raise e

def fallback_api(symbol, api_key):
    print(f"[FALLBACK API] Gerando DataFrame vazio para {symbol}.")
    return pd.DataFrame()

def fallback_upload(arquivo_local, bucket, destino):
    print(f"[FALLBACK UPLOAD] Salvando localmente: {arquivo_local} -> fallback_files/")
    os.makedirs("fallback_files", exist_ok=True)
    destino_local = os.path.join("fallback_files", os.path.basename(destino))
    shutil.copy(arquivo_local, destino_local)
    return destino_local

def fallback_db(*args, **kwargs):
    print("[FALLBACK DB] Salvando em fallback_db.csv")
    df = args[0]
    os.makedirs("fallback_files", exist_ok=True)
    df.to_csv("fallback_files/fallback_db.csv", mode="a", index=False)
    return True
