"""
run_pipeline.py
---------------
Master Execution Script — Bluestock MF Capstone
Runs all pipeline stages in sequence.

Author: Sakshi Kumari
Date: June 2025
"""

import subprocess
import sys
import time


def run_step(step_num, script_name, description):
    """Run a single pipeline step and handle errors."""
    print(f"\n{'='*55}")
    print(f"  STEP {step_num}: {description}")
    print(f"{'='*55}")
    start = time.time()
    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True, text=True
    )
    elapsed = round(time.time() - start, 2)
    if result.returncode == 0:
        print(result.stdout)
        print(f"  [OK] Completed in {elapsed}s")
    else:
        print(f"  [ERROR] {script_name} failed:")
        print(result.stderr)
        sys.exit(1)


def main():
    """Main function — runs all pipeline steps in order."""
    print("\n" + "="*55)
    print("  BLUESTOCK FINTECH — MF ANALYTICS PIPELINE")
    print("="*55)

    steps = [
        (1, "scripts/data_ingestion.py",                 "Data Ingestion"),
        (2, "scripts/live_nav_fetch.py",                 "Live NAV Fetch"),
        (3, "scripts/nav_history_cleaning.py",           "NAV History Cleaning"),
        (4, "scripts/investor_transactions_cleaning.py", "Investor Transactions Cleaning"),
        (5, "scripts/scheme_performance_cleaning.py",    "Scheme Performance Cleaning"),
        (6, "scripts/database_load.py",                  "Load to SQLite DB"),
        (7, "scripts/amfi_validation.py",                "AMFI Code Validation"),
        (8, "scripts/fund_master_analysis.py",           "Fund Master Analysis"),
        (9, "scripts/recommender.py",                    "Fund Recommender"),
    ]

    total_start = time.time()
    for step_num, script, desc in steps:
        run_step(step_num, script, desc)

    print(f"\n{'='*55}")
    print(f"  PIPELINE COMPLETE!")
    print(f"  Total time: {round(time.time()-total_start, 2)}s")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()