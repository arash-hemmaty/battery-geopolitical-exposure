"""
Exposure Engine - KPI 1 Calculation
Reads from the geo.v_kpi1_exposure view and prints a summary.
"""
import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.db import get_engine

def run_exposure_engine():
    print("🚀 Starting Exposure Engine (KPI 1)...\n")
    
    engine = get_engine()
    
    query = """
        SELECT 
            year, 
            importer_name, 
            hs_code, 
            exposed_qty_t, 
            total_qty_t, 
            potential_exposure_pct
        FROM geo.v_kpi1_exposure
        WHERE year = (SELECT MAX(year) FROM geo.v_kpi1_exposure)
        ORDER BY potential_exposure_pct DESC
    """
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
            
        if df.empty:
            print("⚠️ No data found. Check if policies and trade dates overlap.")
            return

        print(f"📊 Results for the latest available year ({df['year'].iloc[0]}):\n")
        print(f"{'Importer':<15} | {'HS Code':<10} | {'Policy Type':<20} | {'Potential Exposure %':<20} | {'Exposed Qty (t)':<15}")
        print("-" * 90)
        
        for _, row in df.head(10).iterrows():
            print(f"{row['importer_name']:<15} | {row['hs_code']:<10} | {'Export Licensing':<20} | {row['potential_exposure_pct']:>18.2f}% | {row['exposed_qty_t']:>15,.2f}")

        print("\n✅ Exposure analysis completed successfully.")
        
    except Exception as e:
        print(f"❌ Error executing query: {e}")

if __name__ == "__main__":
    run_exposure_engine()