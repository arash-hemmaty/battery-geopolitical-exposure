import sys
from pathlib import Path
import pandas as pd
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))
from src.db import get_engine

def run_event_analysis():
    print("🚀 Starting Event Analysis (BQ2) - Before vs After Dec 2023...\n")
    engine = get_engine()
    query = "SELECT * FROM geo.v_event_analysis"
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        
    for (importer, hs_code), group in df.groupby(['importer', 'hs_code']):
        print(f"🔹 {importer} | HS Code: {hs_code}")
        for _, row in group.iterrows():
            marker = " ⬅️ (Policy Started)" if row['year'] == 2023 else ""
            print(f"   {int(row['year'])}: {row['qty_from_china_t']:,.2f} t{marker}")
        print("-" * 50)

if __name__ == "__main__":
    run_event_analysis()