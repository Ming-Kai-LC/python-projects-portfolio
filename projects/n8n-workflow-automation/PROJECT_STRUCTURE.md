# Project Structure Documentation

This document provides detailed information about each directory and file in the n8n Workflow Automation learning project.

## Directory Overview

```
n8n-workflow-automation/
├── Root Configuration Files
├── notebooks/           # Interactive learning modules
├── workflows/          # n8n workflow JSON templates
├── scripts/            # Python utilities and tools
├── docs/               # Additional documentation
└── data/               # Working directory (gitignored)
```

---

## Root Directory Files

### `README.md`
**Purpose:** Main project documentation and entry point
**Contains:**
- Project overview and goals
- Installation instructions
- Learning path description
- Quick start guide
- Troubleshooting basics

**When to use:** First file to read when starting the project

---

### `PROJECT_STRUCTURE.md` (this file)
**Purpose:** Detailed explanation of project organization
**Contains:**
- Directory structure breakdown
- File descriptions
- Usage guidelines

**When to use:** Understanding where files belong and what they do

---

### `docker-compose.yml`
**Purpose:** Docker configuration for n8n instance
**Contains:**
- n8n service definition
- Port mappings (5678)
- Environment variables
- Volume mounts
- Optional PostgreSQL configuration

**How to use:**
```bash
# Start n8n
docker-compose up -d

# Stop n8n
docker-compose down

# View logs
docker logs n8n

# Restart
docker-compose restart
```

**Key Configuration:**
- Default credentials: admin / changeme123
- Port: 5678
- Data persistence: Docker volume `n8n_data`
- Timezone: Asia/Kuala_Lumpur

---

### `requirements.txt`
**Purpose:** Python package dependencies
**Contains:**
- Jupyter and notebook packages
- HTTP libraries (requests, httpx)
- Data processing (pandas, numpy)
- Visualization (plotly, matplotlib)
- Utilities (python-dotenv, rich)

**How to use:**
```bash
pip install -r requirements.txt
```

---

### `.env.example` (to be created)
**Purpose:** Template for environment variables
**Contains:**
- N8N_BASE_URL
- N8N_API_KEY
- N8N_USERNAME
- N8N_PASSWORD

**How to use:**
```bash
# Copy example to .env
cp .env.example .env

# Edit with your values
# Never commit .env to version control
```

---

### `.gitignore`
**Purpose:** Exclude files from version control
**Should include:**
```
# Environment
.env
venv/

# Data directory
data/

# Jupyter
.ipynb_checkpoints/
__pycache__/

# OS files
.DS_Store
Thumbs.db
```

---

## Notebooks Directory

**Location:** `notebooks/`
**Purpose:** Interactive Jupyter notebooks for learning

### File Naming Convention
- Two-digit prefix (00-09)
- Descriptive name with underscores
- `.ipynb` extension

Example: `00_setup_and_introduction.ipynb`

---

### Module 00: Setup and Introduction
**File:** `00_setup_and_introduction.ipynb`
**Duration:** 60-75 minutes
**Difficulty:** Beginner

**Topics:**
- What is n8n and workflow automation
- Comparison with other platforms
- Installation methods (Docker, npm, cloud)
- First workflow creation
- n8n UI tour

**Outputs:**
- Running n8n instance
- First executed workflow
- Exported workflow JSON

**Dependencies:** None (start here)

---

### Module 01: n8n Fundamentals
**File:** `01_n8n_fundamentals.ipynb`
**Duration:** 45-60 minutes
**Difficulty:** Beginner

**Topics:**
- Node types and categories
- Execution model
- Data structure (JSON)
- Connections and flow
- Debugging workflows

**Outputs:**
- 3 basic workflows
- Understanding of workflow JSON structure

**Prerequisites:** Module 00

---

### Module 02: Basic Workflows
**File:** `02_basic_workflows.ipynb`
**Duration:** 60-75 minutes
**Difficulty:** Beginner

**Topics:**
- HTTP Request node
- JSON data handling
- Filtering data
- Error handling
- Cron scheduling

**Projects:**
- Weather API integration
- Email notification system
- Scheduled daily tasks

**Prerequisites:** Module 01

---

### Module 03: Nodes and Connections
**File:** `03_nodes_and_connections.ipynb`
**Duration:** 60-75 minutes
**Difficulty:** Intermediate

**Topics:**
- Set node (data manipulation)
- IF node (conditional logic)
- Switch node (routing)
- Merge node (combining data)
- Expressions and variables

**Projects:**
- Data validation workflow
- Multi-path decision workflow
- Array processing with loops

**Prerequisites:** Module 02

---

### Module 04: Data Transformation
**File:** `04_data_transformation.ipynb`
**Duration:** 75-90 minutes
**Difficulty:** Intermediate

**Topics:**
- Code node (JavaScript/Python)
- Format conversion (CSV, XML, JSON)
- Date/time operations
- String manipulation
- Regular expressions

**Projects:**
- CSV to JSON converter
- API response cleaner
- Custom Python transformations

**Prerequisites:** Module 03

---

### Module 05: API Integrations
**File:** `05_api_integrations.ipynb`
**Duration:** 75-90 minutes
**Difficulty:** Intermediate

**Topics:**
- REST API fundamentals
- Authentication (API key, OAuth, Bearer)
- HTTP Request advanced usage
- Pagination strategies
- Database operations

**Projects:**
- GitHub automation
- Database CRUD workflows
- Multi-API orchestration

**Prerequisites:** Module 04

---

### Module 06: Webhooks and Triggers
**File:** `06_webhooks_and_triggers.ipynb`
**Duration:** 60-75 minutes
**Difficulty:** Intermediate

**Topics:**
- Webhook concepts
- Setting up webhook triggers
- Testing locally (ngrok)
- Event-driven automation
- Security considerations

**Projects:**
- Form submission handler
- GitHub webhook integration
- Real-time notification system

**Prerequisites:** Module 05

---

### Module 07: Python API Client
**File:** `07_python_api_client.ipynb`
**Duration:** 90-120 minutes
**Difficulty:** Advanced

**Topics:**
- n8n REST API overview
- API authentication
- Programmatic workflow creation
- Triggering from Python
- Monitoring executions
- Custom N8nClient usage

**Projects:**
- Python workflow creator
- Batch execution script
- Execution log analyzer
- Automated deployment tool

**Prerequisites:** Module 06

---

### Module 08: Deployment Strategies
**File:** `08_deployment_strategies.ipynb`
**Duration:** 75-90 minutes
**Difficulty:** Advanced

**Topics:**
- Self-hosting overview
- Docker production setup
- Cloud deployment (AWS, DigitalOcean)
- Environment configuration
- Database setup (PostgreSQL)
- HTTPS/SSL configuration
- Backup strategies
- Scaling considerations

**Hands-On:**
- Cloud platform deployment
- Custom domain setup
- Backup automation
- Monitoring implementation

**Prerequisites:** Module 07

---

### Module 09: Advanced Projects
**File:** `09_advanced_projects.ipynb`
**Duration:** 120+ minutes
**Difficulty:** Advanced

**Capstone Projects:**
1. Complete ETL pipeline
2. AI-powered workflow
3. Social media automation
4. Data processing system

**Prerequisites:** All previous modules

---

### `notebooks/outputs/`
**Purpose:** Store generated files from notebook exercises
**Contents:**
- Workflow exports
- Test data files
- Generated reports
- Screenshots

**Note:** This directory should be in `.gitignore`

---

## Workflows Directory

**Location:** `workflows/`
**Purpose:** Pre-built workflow templates in JSON format

### File Naming Convention
- Two-digit prefix matching module number
- Descriptive name
- `.json` extension

Example: `01_hello_world.json`

---

### Workflow Template Files

#### `01_hello_world.json`
**Module:** 00
**Description:** Simplest possible workflow
**Nodes:** Manual trigger → Set node
**Use:** Learning basic workflow structure

#### `02_weather_api.json`
**Module:** 02
**Description:** Fetch weather data from API
**Nodes:** Schedule trigger → HTTP Request → Set
**Use:** API integration basics

#### `03_email_notification.json`
**Module:** 02
**Description:** Send email based on condition
**Nodes:** Manual trigger → IF → Email
**Use:** Conditional logic and notifications

#### `04_data_transformation.json`
**Module:** 04
**Description:** Transform CSV to JSON
**Nodes:** Manual → CSV parser → Code → Set
**Use:** Data format conversion

#### `05_github_integration.json`
**Module:** 05
**Description:** List repositories and create issues
**Nodes:** Schedule → GitHub nodes
**Use:** OAuth integration

#### `06_webhook_handler.json`
**Module:** 06
**Description:** Process webhook data
**Nodes:** Webhook trigger → Switch → Multiple actions
**Use:** Event-driven workflows

#### `07_etl_pipeline.json`
**Module:** 09
**Description:** Complete ETL workflow
**Nodes:** Multiple sources → Transform → Database → Notify
**Use:** Complex data pipeline

---

### How to Import Workflows

**Method 1: n8n UI**
1. Open n8n at http://localhost:5678
2. Click "Import from File"
3. Select JSON file
4. Click "Import"

**Method 2: Python Client**
```python
from scripts.n8n_client import N8nClient

client = N8nClient()
workflow = client.import_workflow('workflows/01_hello_world.json')
print(f"Imported: {workflow['name']}")
```

**Method 3: Bulk Import Script**
```bash
python scripts/import_workflows.py
```

---

## Scripts Directory

**Location:** `scripts/`
**Purpose:** Python utilities and automation tools

---

### `n8n_client.py`
**Purpose:** Python REST API client for n8n
**Size:** ~600 lines
**Dependencies:** requests, json, typing

**Main Classes:**
- `N8nClient`: Main API client

**Key Methods:**
```python
# Workflow management
list_workflows()
get_workflow(id)
create_workflow(data)
update_workflow(id, data)
delete_workflow(id)
activate_workflow(id)
deactivate_workflow(id)

# Execution
trigger_workflow(webhook, data)
execute_workflow(id, data)
list_executions(workflow_id, limit)
get_execution(id)

# Import/Export
export_workflow(id, file_path)
import_workflow(file_path, activate)

# Utilities
health_check()
get_workflow_by_name(name)
wait_for_execution(id, timeout)
```

**Usage Example:**
```python
from n8n_client import N8nClient

client = N8nClient(api_key="your-key")

# List all workflows
workflows = client.list_workflows()

# Trigger workflow
result = client.trigger_workflow("test", {"data": "value"})

# Export workflow
client.export_workflow("123", "backup.json")
```

---

### `import_workflows.py` (to be created)
**Purpose:** Bulk import workflow templates
**Usage:**
```bash
python scripts/import_workflows.py
```

**Features:**
- Import all JSON files from workflows/
- Skip duplicates
- Option to activate on import
- Progress reporting

---

### `backup_workflows.py` (to be created)
**Purpose:** Backup all workflows to JSON
**Usage:**
```bash
python scripts/backup_workflows.py
```

**Features:**
- Export all workflows
- Timestamped backups
- Option to include executions
- Compressed archives

---

### `monitor_executions.py` (to be created)
**Purpose:** Monitor workflow executions
**Usage:**
```bash
python scripts/monitor_executions.py --workflow-id 123
```

**Features:**
- Real-time execution monitoring
- Failed execution alerts
- Performance metrics
- Log aggregation

---

## Docs Directory

**Location:** `docs/`
**Purpose:** Additional detailed documentation

---

### `DOCKER_SETUP.md`
**Purpose:** Comprehensive Docker installation guide
**Contents:**
- Docker installation (Windows, macOS, Linux)
- Docker Compose setup
- Volume management
- Network configuration
- Container troubleshooting
- Production best practices

---

### `CLOUD_DEPLOYMENT.md`
**Purpose:** Cloud platform deployment guides
**Contents:**
- AWS deployment (EC2, ECS, Lightsail)
- DigitalOcean deployment
- Railway deployment
- Azure deployment
- Custom domain setup
- SSL certificate configuration
- Cost estimation

---

### `API_REFERENCE.md`
**Purpose:** n8n REST API documentation
**Contents:**
- Authentication methods
- Endpoint reference
- Request/response examples
- Error codes
- Rate limiting
- Best practices

---

### `TROUBLESHOOTING.md`
**Purpose:** Common issues and solutions
**Contents:**
- Installation problems
- Connection errors
- Workflow debugging
- Performance issues
- Data problems
- Deployment issues
- FAQ section

---

## Data Directory

**Location:** `data/`
**Purpose:** Working directory for runtime data
**Git Status:** Ignored (in .gitignore)

### Subdirectories

#### `data/exports/`
**Purpose:** Workflow export files
**Contents:**
- Manual workflow backups
- Dated export archives
- Individual workflow JSONs

#### `data/logs/`
**Purpose:** Execution logs and monitoring data
**Contents:**
- Execution logs
- Error logs
- Performance logs
- Audit logs

#### `data/temp/`
**Purpose:** Temporary files during workflow execution
**Contents:**
- Downloaded files
- Processing intermediates
- Test data
- Cache files

**Note:** This directory is automatically created by Docker volume mounts

---

## File Organization Best Practices

### Naming Conventions

**Notebooks:**
- Format: `NN_descriptive_name.ipynb`
- Use lowercase
- Separate words with underscores
- Prefix with module number (00-09)

**Workflows:**
- Format: `NN_workflow_purpose.json`
- Match related notebook module
- Descriptive of function

**Scripts:**
- Format: `action_object.py`
- Use snake_case
- Verb + noun naming

**Documentation:**
- Format: `TOPIC_NAME.md`
- Use UPPERCASE for major docs
- Clear, descriptive names

### Directory Usage Guidelines

**DO:**
- Keep notebooks in `notebooks/`
- Store reusable workflows in `workflows/`
- Put Python utilities in `scripts/`
- Save generated files to `data/`
- Document major features in `docs/`

**DON'T:**
- Commit `.env` files
- Commit `data/` directory contents
- Store credentials in code
- Mix notebooks and workflows
- Put large binary files in git

---

## Maintenance and Updates

### Adding New Modules

1. Create notebook in `notebooks/`
2. Follow numbering convention
3. Create corresponding workflows in `workflows/`
4. Update README.md learning path
5. Update this PROJECT_STRUCTURE.md

### Updating Workflows

1. Export from n8n UI
2. Save to `workflows/` with clear name
3. Document in workflow comments
4. Reference in corresponding notebook

### Adding Documentation

1. Create markdown file in `docs/`
2. Use clear headers and sections
3. Link from README.md
4. Include code examples

---

## Quick Reference

### Essential Files to Read First
1. `README.md` - Project overview
2. `docker-compose.yml` - n8n configuration
3. `00_setup_and_introduction.ipynb` - First module

### Files to Modify Often
- Notebooks (during learning)
- `.env` (configuration)
- Workflows (your custom workflows)

### Files Not to Modify
- `requirements.txt` (unless adding dependencies)
- `docker-compose.yml` (unless changing configuration)
- Workflow templates (create new files instead)

### Files to Backup
- Your custom workflows in `data/exports/`
- Modified notebooks
- Custom scripts

---

## Summary

This project structure is designed to:
- **Separate concerns**: Notebooks, workflows, scripts, docs
- **Progressive learning**: Numbered modules
- **Reusability**: Template workflows
- **Automation**: Python utilities
- **Documentation**: Comprehensive guides

Everything has its place, making it easy to:
- Find what you need
- Add new content
- Maintain the project
- Share with others

For questions about structure or organization, refer to this document or check the README.md.
