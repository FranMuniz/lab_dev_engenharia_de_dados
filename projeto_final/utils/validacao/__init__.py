from sqlalchemy import text

def validar_consistencia(engine, schema):
    print("\n[VALIDAÇÃO] Iniciando validação de consistência...")

    query_gold = f"SELECT COUNT(*) FROM {schema}.br_alphavantage_s0_daily_refined"
    query_silver = f"SELECT COUNT(DISTINCT data_ref) FROM {schema}.br_alphavantage_s0_daily_live"

    with engine.connect() as conn:
        gold_count = conn.execute(text(query_gold)).scalar()
        silver_count = conn.execute(text(query_silver)).scalar()

    print(f"Registros Silver: {silver_count}, Registros Gold: {gold_count}")

    if gold_count == silver_count:
        print("[VALIDAÇÃO] Consistência OK: Gold cobre todas as datas da Silver.")
    else:
        print("[VALIDAÇÃO] Inconsistência detectada: Gold != Silver.")
