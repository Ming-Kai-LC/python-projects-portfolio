# n8n Workflow Templates

This directory contains example workflow JSON files that you can import into n8n.

## Available Workflows

### 01_hello_world.json
**Description:** Simple workflow demonstrating basic structure
**Nodes:** Manual Trigger → Set
**Purpose:** Learn workflow basics and JSON structure
**Use Case:** Testing and learning

### 02_webhook_test.json
**Description:** Webhook endpoint with response
**Nodes:** Webhook → Process Data → Respond
**Purpose:** Learn webhook triggers and responses
**Use Case:** API endpoints, form submissions

### 03_data_validation.json
**Description:** Multi-step data validation
**Nodes:** Manual Trigger → Set → IF nodes (nested)
**Purpose:** Learn conditional logic and branching
**Use Case:** User registration, data quality checks

## How to Import Workflows

### Method 1: Via n8n UI

1. Open n8n at http://localhost:5678
2. Click **Workflows** in the left sidebar
3. Click **Import from File** button
4. Select the JSON file
5. Click **Import**
6. The workflow will appear in your workflow list

### Method 2: Via Python Client

```python
from scripts.n8n_client import N8nClient

client = N8nClient(
    base_url="http://localhost:5678",
    username="admin",
    password="changeme123"
)

# Import workflow
workflow = client.import_workflow('workflows/01_hello_world.json')
print(f"Imported: {workflow['name']}")
```

### Method 3: Bulk Import

```python
import os
from scripts.n8n_client import N8nClient

client = N8nClient(...)

# Import all workflows
for filename in os.listdir('workflows'):
    if filename.endswith('.json'):
        filepath = os.path.join('workflows', filename)
        try:
            wf = client.import_workflow(filepath)
            print(f"✅ Imported: {wf['name']}")
        except Exception as e:
            print(f"❌ Failed: {filename} - {e}")
```

## Creating Your Own Templates

When you create a workflow you want to save:

1. **Export from n8n:**
   - Open the workflow
   - Click the **⋮** menu (three dots)
   - Select **Download**
   - Save to this `workflows/` directory

2. **Name the file:**
   - Use descriptive names: `project_name.json`
   - Use underscores for spaces
   - Keep names lowercase

3. **Document it:**
   - Add entry to this README
   - Describe purpose and use case
   - List key nodes used

## Workflow Naming Convention

**Format:** `NN_descriptive_name.json`

Examples:
- `01_hello_world.json` - Simple introduction
- `02_webhook_test.json` - Webhook example
- `03_data_validation.json` - Conditional logic
- `04_api_integration.json` - External API calls
- `05_database_operations.json` - CRUD operations

## Tips for Using Templates

1. **Always test imported workflows** before activating
2. **Update credentials** if the workflow requires them
3. **Modify webhook paths** to avoid conflicts
4. **Check node compatibility** with your n8n version
5. **Export backups** before making major changes

## Modifying Templates

After importing:

1. **Rename the workflow** to something meaningful for your use case
2. **Update node parameters** to match your requirements
3. **Add your credentials** in Settings → Credentials
4. **Test with manual trigger** before activating
5. **Export your modified version** for backup

## Version Control

These JSON files are plain text and work great with Git:

```bash
# Track changes
git add workflows/
git commit -m "Add new workflow template"

# See differences
git diff workflows/01_hello_world.json
```

## Contributing Templates

Have a useful workflow to share?

1. Export your workflow
2. Remove sensitive information (credentials, personal data)
3. Add it to this directory
4. Update this README
5. Consider sharing with the n8n community

## Additional Resources

- [n8n Workflow Templates](https://n8n.io/workflows/)
- [n8n Documentation](https://docs.n8n.io/)
- [Community Forum](https://community.n8n.io/)

---

**Note:** These templates are for learning purposes. Always review and test before using in production.
