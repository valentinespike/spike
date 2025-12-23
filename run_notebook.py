\
import os
import argparse
import papermill as pm

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notebook", default="notebooks/Untitled12.ipynb")
    ap.add_argument("--output", default="outputs/executed.ipynb")
    ap.add_argument("--parameters_json", default="", help="Optional JSON string of parameters to inject")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    params = {}
    if args.parameters_json:
        import json
        params = json.loads(args.parameters_json)

    # Execute notebook
    pm.execute_notebook(
        input_path=args.notebook,
        output_path=args.output,
        parameters=params,
        log_output=True,
    )

if __name__ == "__main__":
    main()
