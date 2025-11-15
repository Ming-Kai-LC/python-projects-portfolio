"""
Notebook Validation Script
===========================

Tests all notebooks to ensure they can run smoothly.
"""

import json
import os
import sys
from pathlib import Path

def validate_notebook(notebook_path):
    """
    Validate a Jupyter notebook file.

    Returns:
        tuple: (is_valid, issues_list)
    """
    issues = []

    try:
        # 1. Check file exists
        if not os.path.exists(notebook_path):
            issues.append(f"File not found: {notebook_path}")
            return False, issues

        # 2. Check valid JSON
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
        except json.JSONDecodeError as e:
            issues.append(f"Invalid JSON: {e}")
            return False, issues
        except UnicodeDecodeError as e:
            issues.append(f"Encoding error: {e}")
            return False, issues

        # 3. Check required notebook structure
        if 'cells' not in nb:
            issues.append("Missing 'cells' key")
            return False, issues

        if 'metadata' not in nb:
            issues.append("Missing 'metadata' key")

        if 'nbformat' not in nb:
            issues.append("Missing 'nbformat' key")

        # 4. Check cells
        for i, cell in enumerate(nb['cells']):
            if 'cell_type' not in cell:
                issues.append(f"Cell {i}: Missing 'cell_type'")

            if 'source' not in cell:
                issues.append(f"Cell {i}: Missing 'source'")

            # Check code cells for basic syntax (Python)
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))

                # Skip empty cells
                if not source.strip():
                    continue

                # Skip cells with Jupyter magic commands or bash commands
                lines = source.splitlines()
                has_magic_or_bash = any(
                    line.strip().startswith(('!', '%', '%%'))
                    for line in lines
                    if line.strip() and not line.strip().startswith('#')
                )
                if has_magic_or_bash:
                    continue

                # Skip cells with only comments
                if all(line.strip().startswith('#') or not line.strip()
                       for line in lines):
                    continue

                # Try to compile the code
                try:
                    compile(source, f'<cell_{i}>', 'exec')
                except SyntaxError as e:
                    issues.append(f"Cell {i}: Syntax error - {e}")

        # 5. Report
        if issues:
            return False, issues
        else:
            return True, []

    except Exception as e:
        issues.append(f"Unexpected error: {e}")
        return False, issues


def validate_all_notebooks(notebooks_dir):
    """
    Validate all notebooks in a directory.
    """
    notebooks_path = Path(notebooks_dir)
    notebooks = sorted(notebooks_path.glob('*.ipynb'))

    if not notebooks:
        print(f"No notebooks found in {notebooks_dir}")
        return

    print(f"Validating {len(notebooks)} notebooks...\n")
    print("=" * 70)

    all_valid = True
    results = []

    for nb_path in notebooks:
        is_valid, issues = validate_notebook(nb_path)
        results.append((nb_path.name, is_valid, issues))

        if is_valid:
            # Get cell count
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            cell_count = len(nb['cells'])

            print(f"[OK] {nb_path.name}")
            print(f"     Cells: {cell_count}")
        else:
            all_valid = False
            print(f"[FAIL] {nb_path.name}")
            for issue in issues:
                print(f"       - {issue}")

        print()

    print("=" * 70)

    if all_valid:
        print("\n[SUCCESS] All notebooks are valid!")
    else:
        print(f"\n[ERROR] Found issues in {sum(1 for _, v, _ in results if not v)} notebook(s)")
        print("\nFailed notebooks:")
        for name, valid, issues in results:
            if not valid:
                print(f"  - {name}: {len(issues)} issue(s)")

    return all_valid


def validate_workflows(workflows_dir):
    """
    Validate workflow JSON files.
    """
    workflows_path = Path(workflows_dir)
    workflows = sorted(workflows_path.glob('*.json'))

    if not workflows:
        print(f"No workflows found in {workflows_dir}")
        return

    print(f"\nValidating {len(workflows)} workflow files...\n")
    print("=" * 70)

    all_valid = True

    for wf_path in workflows:
        try:
            with open(wf_path, 'r', encoding='utf-8') as f:
                wf = json.load(f)

            name = wf.get('name', 'UNNAMED')
            nodes = len(wf.get('nodes', []))

            print(f"[OK] {wf_path.name}")
            print(f"     Name: {name}")
            print(f"     Nodes: {nodes}")
            print()

        except Exception as e:
            all_valid = False
            print(f"[FAIL] {wf_path.name}")
            print(f"       Error: {e}")
            print()

    print("=" * 70)

    if all_valid:
        print("\n[SUCCESS] All workflows are valid!")
    else:
        print("\n[ERROR] Some workflows have issues")

    return all_valid


if __name__ == "__main__":
    # Get project root
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    print("n8n Workflow Automation - Validation Script")
    print("=" * 70)
    print()

    # Validate notebooks
    notebooks_valid = validate_all_notebooks(project_dir / 'notebooks')

    # Validate workflows
    workflows_valid = validate_workflows(project_dir / 'workflows')

    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Notebooks: {'[PASSED]' if notebooks_valid else '[FAILED]'}")
    print(f"Workflows: {'[PASSED]' if workflows_valid else '[FAILED]'}")
    print()

    # Exit code
    sys.exit(0 if (notebooks_valid and workflows_valid) else 1)
