import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.db import get_engine

def run_alternative_analysis():
    print("🚀 Starting Alternative Suppliers Analysis (BQ4)...\n")
    engine = get_engine()
    query = "SELECT * FROM geo.v_alternative_suppliers"
    
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    for (importer, hs_code), group in df.groupby(['importer', 'hs_code']):
        print(f"🔹 {importer} | HS Code: {hs_code}")
        # فقط ۳ گزینه اول را نشان می‌دهیم
        top_alternatives = group.head(3)
        for i, row in enumerate(top_alternatives.itertuples(), 1):
            print(f"   {i}. {row.alternative_supplier}: {row.total_qty_t:,.2f} t (Active in {row.years_active} years)")
        print("-" * 50)

if __name__ == "__main__":
    run_alternative_analysis()