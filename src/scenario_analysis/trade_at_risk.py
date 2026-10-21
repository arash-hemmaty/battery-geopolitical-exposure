"""
Scenario Engine - Trade-at-Risk (BQ3 / KPI 3)
Calculates the direct trade volume at risk under different export reduction scenarios.
"""
import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.db import get_engine

def run_scenario_analysis():
    print("🚀 Starting Scenario Engine (Trade-at-Risk)...\n")
    
    engine = get_engine()
    
    # ما سناریوها را روی سال 2025 (آخرین سال) اجرا می‌کنیم
    # و روی واردکنندگان بزرگی که در KPI 1 شناسایی کردیم تمرکز می‌کنیم
    query = """
        SELECT 
            year, 
            importer_name, 
            hs_code, 
            exposed_qty_t
        FROM geo.v_kpi1_exposure
        WHERE year = 2025 
          AND importer_name IN ('South Korea', 'Germany', 'Japan', 'United States')
          AND exposed_qty_t > 100 -- فقط مقادیر معنادار
    """
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
            
        if df.empty:
            print("⚠️ No data found for scenario analysis.")
            return

        print(f"📊 Trade-at-Risk Analysis for Year 2025 (Base Volume)\n")
        
        # تعریف سناریوها
        scenarios = [0.25, 0.50, 1.00]
        
        for _, row in df.iterrows():
            base_qty = row['exposed_qty_t']
            print(f"🔹 Importer: {row['importer_name']} | HS Code: {row['hs_code']} | Base Exposed Volume: {base_qty:,.2f} t")
            
            for shock in scenarios:
                at_risk = base_qty * shock
                print(f"   └─ {int(shock*100)}% Reduction Scenario: {at_risk:,.2f} t at risk")
            print("-" * 60)

        print("\n✅ Scenario analysis completed successfully.")
        
    except Exception as e:
        print(f"❌ Error executing query: {e}")

if __name__ == "__main__":
    run_scenario_analysis()