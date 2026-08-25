import os
import shutil
import argparse
import sys
import json
from pathlib import Path

from .graph_linter import validate
from .vram_calc import evaluate_model_vram

def create_dirs(base_path: Path, dirs: list):
    for d in dirs:
        (base_path / d).mkdir(parents=True, exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Bootstrap Knowledge Base architecture (OKF + QMD)")
    parser.add_argument("--target", default=".", help="Target directory for initialization (default: current directory)")
    parser.add_argument("--type", choices=["single", "umbrella"], default="single", help="Project architecture type")
    subparsers = parser.add_subparsers(dest="command")
    
    validate_parser = subparsers.add_parser("validate", help="Validate Markdown links in a knowledge base")
    validate_parser.add_argument("--dir", default="docs", help="Base directory to scan")
    
    calc_parser = subparsers.add_parser("calc-vram", help="Calculate VRAM and KV cache memory requirements")
    calc_parser.add_argument("--params", type=float, required=True, help="Total parameters in billions (e.g. 32.5 or 30.5)")
    calc_parser.add_argument("--active-params", type=float, default=None, help="Active parameters in billions for MoE (e.g. 3.3)")
    calc_parser.add_argument("--layers", type=int, required=True, help="Number of model layers (e.g. 64 or 48)")
    calc_parser.add_argument("--kv-heads", type=int, required=True, help="Number of KV heads (e.g. 8 or 4)")
    calc_parser.add_argument("--head-dim", type=int, default=128, help="Head dimension (default: 128)")
    calc_parser.add_argument("--quant", default="Q4_K_S", help="Weight quantization (default: Q4_K_S)")
    calc_parser.add_argument("--kv-quant", default="q8_0", help="KV cache quantization (default: q8_0)")
    calc_parser.add_argument("--arch", choices=["dense", "moe", "mamba_hybrid"], default="dense", help="Architecture type")
    calc_parser.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    if args.command == "validate":
        report, is_valid = validate(args.dir)
        print(report)
        return 0 if is_valid else 1

    if args.command == "calc-vram":
        total_params_val = args.params * 1e9
        active_params_val = (args.active_params * 1e9) if args.active_params else total_params_val
        res = evaluate_model_vram(
            total_params=total_params_val,
            active_params=active_params_val,
            num_layers=args.layers,
            num_kv_heads=args.kv_heads,
            head_dim=args.head_dim,
            quant=args.quant,
            kv_quant=args.kv_quant,
            architecture_type=args.arch,
        )
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print("=== VRAM & KV Cache Estimation ===")
            print(f"Architecture: {args.arch} | Params: {args.params}B (Active: {args.active_params or args.params}B)")
            print(f"Layers: {args.layers} | KV Heads: {args.kv_heads} | Head Dim: {args.head_dim}")
            print(f"Weights ({args.quant}): {res['weights_gib']} GiB | Overhead: {res['activation_overhead_gib']} GiB")
            print("\nContext Scaling Matrix:")
            for ctx in res["context_evaluation"]:
                fits_str = "YES (FITS)" if ctx["fits_24gb"] else "NO (OOM)"
                print(f"  Context {ctx['context_length']:>6} tokens: KV = {ctx['kv_cache_gib']:>6.2f} GiB | Peak VRAM = {ctx['peak_vram_gib']:>6.2f} GiB | 24GB GPU: {fits_str} (Placement: {ctx['placements']['24GB']})")
        return 0

    target = Path(args.target).resolve()
    pkg_dir = Path(__file__).parent.resolve()

    print(f"Initializing {args.type} Knowledge Base in {target}...")
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
