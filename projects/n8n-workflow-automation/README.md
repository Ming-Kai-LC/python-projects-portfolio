# n8n Workflow Automation Learning Project

## About This Project

This comprehensive learning project teaches you how to use **n8n**, an open-source workflow automation platform, with a focus on self-hosting, deployment, and integrating with Python. Unlike traditional n8n tutorials, this project uses **Jupyter notebooks** to provide an interactive learning experience and shows you how to programmatically control n8n workflows using Python.

n8n (pronounced "n-eight-n") is a powerful workflow automation tool that lets you connect different apps and services together. It's an open-source alternative to platforms like Zapier, Make (formerly Integromat), or Microsoft Power Automate, with the key advantage that you can **self-host it for free**.

## Key Features

- **10 Progressive Learning Modules**: From installation to advanced deployment
- **Jupyter Notebook-Based**: Interactive, code-along learning experience
- **Python Integration**: Custom Python client for n8n REST API
- **Self-Hosting Focused**: Complete guides for Docker and cloud deployment
- **Data Processing Emphasis**: ETL workflows, API orchestration, data transformation
- **Real-World Projects**: Practical examples you can use immediately
- **Importable Workflow Templates**: Ready-to-use JSON workflows
- **Production-Ready**: Best practices for deployment and scaling

## Who This Project Is For

### Target Audience

- **Python Developers** wanting to learn workflow automation
- **Data Professionals** seeking to automate ETL pipelines
- **DevOps Engineers** looking for self-hosted automation solutions
- **Developers** seeking alternatives to paid automation platforms
- **Teams** wanting full control over their automation infrastructure

### Prerequisites

**Required Knowledge:**
- Basic Python programming
- Understanding of REST APIs
- Command line basics
- Basic JSON knowledge

**Recommended (but not required):**
- Docker basics
- Cloud platform experience (AWS, DigitalOcean, etc.)
- Database fundamentals
- JavaScript basics

**Software Requirements:**
- Python 3.8 or higher
- Docker and Docker Compose (for local n8n installation)
- Jupyter Notebook
- Web browser (for n8n UI)
- Git (for version control)

## What You'll Learn

By completing this learning project, you will:

1. **Understand n8n Fundamentals**
   - Workflow automation concepts
   - n8n architecture and execution model
   - Nodes, triggers, and connections
   - Data flow and transformation

2. **Build Practical Workflows**
   - Create automated workflows in the n8n UI
   - Implement error handling and debugging
   - Work with webhooks and API integrations
   - Build data processing pipelines

3. **Master Python Integration**
   - Control n8n programmatically via REST API
   - Trigger workflows from Python scripts
   - Monitor execution status and retrieve results
   - Build custom automation tools

4. **Deploy to Production**
   - Self-host n8n locally with Docker
   - Deploy to cloud platforms (AWS, DigitalOcean, Railway)
   - Configure HTTPS and security
   - Implement backup and disaster recovery
   - Scale for production use

5. **Advanced Techniques**
   - AI-powered workflows with LangChain
   - Complex data transformations
   - Multi-step automation pipelines
   - Custom node development (basics)

## Installation

### Step 1: Clone This Repository

```bash
cd projects/n8n-workflow-automation
```

### Step 2: Create Python Virtual Environment

```bash
# Navigate to the repository root
cd ../..

# Create virtual environment (if not already created)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r projects/n8n-workflow-automation/requirements.txt
```

### Step 4: Install and Start n8n

**Option A: Using Docker (Recommended)**

```bash
# Navigate to project directory
cd projects/n8n-workflow-automation

# Start n8n using Docker Compose
docker-compose up -d

# Check if n8n is running
docker ps

# View logs
docker logs n8n
```

n8n will be available at: http://localhost:5678

**Default credentials:**
- Username: `admin`
- Password: `changeme123` (⚠️ **Change this immediately!**)

**Option B: Using npm**

```bash
# Install n8n globally
npm install n8n -g

# Start n8n
n8n start
```

**Option C: Using npx (No installation needed)**

```bash
npx n8n
```

### Step 5: Configure Environment Variables (Optional)

Create a `.env` file in the project root:

```bash
# n8n Connection
N8N_BASE_URL=http://localhost:5678
N8N_API_KEY=your-api-key-here

# Or use basic auth
N8N_USERNAME=admin
N8N_PASSWORD=changeme123
```

To generate an API key in n8n:
1. Open n8n at http://localhost:5678
2. Go to Settings → API
3. Click "Create API Key"
4. Copy the key to your `.env` file

### Step 6: Launch Jupyter Notebook

```bash
# From project directory
jupyter notebook notebooks/
```

Your browser will open with the Jupyter notebook interface.

## Project Structure

```
n8n-workflow-automation/
├── README.md                          # This file
├── PROJECT_STRUCTURE.md               # Detailed directory guide
├── docker-compose.yml                 # Docker setup for n8n
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variables template
│
├── notebooks/                         # Jupyter learning modules
│   ├── 00_setup_and_introduction.ipynb
│   ├── 01_n8n_fundamentals.ipynb
│   ├── 02_basic_workflows.ipynb
│   ├── 03_nodes_and_connections.ipynb
│   ├── 04_data_transformation.ipynb
│   ├── 05_api_integrations.ipynb
│   ├── 06_webhooks_and_triggers.ipynb
│   ├── 07_python_api_client.ipynb
│   ├── 08_deployment_strategies.ipynb
│   ├── 09_advanced_projects.ipynb
│   └── outputs/                       # Generated files
│
├── workflows/                         # n8n workflow templates (JSON)
│   ├── 01_hello_world.json
│   ├── 02_weather_api.json
│   ├── 03_email_notification.json
│   ├── 04_data_transformation.json
│   ├── 05_github_integration.json
│   └── ...
│
├── scripts/                           # Python utilities
│   ├── n8n_client.py                  # Python REST API client
│   ├── import_workflows.py            # Bulk workflow import
│   └── backup_workflows.py            # Backup utility
│
├── docs/                              # Additional documentation
│   ├── DOCKER_SETUP.md                # Detailed Docker guide
│   ├── CLOUD_DEPLOYMENT.md            # Cloud deployment guide
│   ├── API_REFERENCE.md               # n8n API reference
│   └── TROUBLESHOOTING.md             # Common issues & solutions
│
└── data/                              # Working directory (gitignored)
    ├── exports/                       # Workflow exports
    ├── logs/                          # Execution logs
    └── temp/                          # Temporary files
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for a detailed explanation of each directory.

## Learning Path

### Module 00: Setup and Introduction (60-75 minutes)
**Notebook:** `00_setup_and_introduction.ipynb`

- What is workflow automation?
- n8n vs other automation platforms
- Installation and setup (Docker, npm, cloud)
- n8n interface tour
- Create your first "Hello World" workflow
- Export and import workflows

**Learning Outcomes:**
- Running n8n instance (local or cloud)
- Understanding of n8n architecture
- First successful workflow execution

---

### Module 01: n8n Fundamentals (45-60 minutes)
**Notebook:** `01_n8n_fundamentals.ipynb`

- Understanding nodes (trigger, action, data nodes)
- Workflow execution model
- Data structure and JSON format
- Node connections and flow control
- Testing and debugging workflows
- Execution history and logs

**Hands-On:**
- Create 3 simple workflows in n8n UI
- Export workflows as JSON
- Analyze workflow JSON structure

---

### Module 02: Basic Workflows (60-75 minutes)
**Notebook:** `02_basic_workflows.ipynb`

- Common workflow patterns
- HTTP Request node
- Working with JSON data
- Basic data filtering
- Error handling fundamentals
- Scheduling with Cron

**Projects:**
1. Fetch weather data from public API
2. Send email notifications
3. Schedule daily automated tasks

---

### Module 03: Nodes and Connections (60-75 minutes)
**Notebook:** `03_nodes_and_connections.ipynb`

- Core nodes: Set, IF, Switch, Merge
- Expressions and variables
- Conditional logic (IF nodes)
- Looping through data
- Data routing (Switch node)
- Merge node strategies

**Projects:**
1. Data validation workflow
2. Multi-path conditional workflow
3. Process array data with loops

---

### Module 04: Data Transformation (75-90 minutes)
**Notebook:** `04_data_transformation.ipynb`

- Data transformation techniques
- Code node (JavaScript/Python)
- Working with CSV, XML, JSON formats
- Date and time manipulation
- String operations and regex
- Function item operations

**Projects:**
1. Transform CSV to JSON
2. Parse and clean API responses
3. Custom Python data processing in n8n

---

### Module 05: API Integrations (75-90 minutes)
**Notebook:** `05_api_integrations.ipynb`

- RESTful API concepts
- Authentication methods (API keys, OAuth, Bearer tokens)
- HTTP Request node advanced usage
- Pagination handling
- Rate limiting strategies
- Database operations (PostgreSQL, MongoDB)

**Projects:**
1. GitHub integration (list repos, create issues)
2. Database CRUD operations
3. Multi-API orchestration workflow

---

### Module 06: Webhooks and Triggers (60-75 minutes)
**Notebook:** `06_webhooks_and_triggers.ipynb`

- Webhook fundamentals
- Creating webhook-triggered workflows
- Testing webhooks locally (ngrok, localhost)
- Event-driven automation
- Polling vs webhooks comparison
- Webhook security

**Projects:**
1. Form submission handler
2. GitHub webhook listener
3. Real-time notification system

---

### Module 07: Python API Client (90-120 minutes)
**Notebook:** `07_python_api_client.ipynb`

- n8n REST API overview
- Authentication with API keys
- Creating workflows programmatically
- Triggering executions from Python
- Monitoring workflow status
- Building automation scripts
- Using the custom N8nClient library

**Projects:**
1. Create workflows from Python
2. Batch trigger workflows from Jupyter
3. Monitor and analyze execution logs
4. Automated workflow deployment script

---

### Module 08: Deployment Strategies (75-90 minutes)
**Notebook:** `08_deployment_strategies.ipynb`

- Self-hosting options comparison
- Docker Compose production setup
- Cloud platform deployment (AWS, DigitalOcean, Railway)
- Environment variables and secrets
- Database configuration (PostgreSQL vs SQLite)
- HTTPS with SSL certificates
- Backup and disaster recovery
- Scaling considerations
- Monitoring and logging

**Hands-On:**
1. Deploy n8n to cloud platform
2. Configure custom domain with HTTPS
3. Set up automated backups
4. Implement monitoring

---

### Module 09: Advanced Projects (120+ minutes)
**Notebook:** `09_advanced_projects.ipynb`

**Capstone Projects:**

1. **Complete ETL Pipeline**
   - Extract data from multiple APIs
   - Transform with Python code
   - Load to database
   - Send notification on completion

2. **AI-Powered Workflow**
   - Webhook trigger with data
   - AI processing (OpenAI/Claude)
   - Multiple conditional actions
   - Results storage

3. **Social Media Automation**
   - Schedule posts across platforms
   - Monitor mentions and keywords
   - Sentiment analysis
   - Automated responses

4. **Data Processing Pipeline**
   - File upload trigger
   - Parse and validate data
   - Transform and enrich
   - Generate reports
   - Email distribution

---

## Quick Start Guide

### 1. Start n8n

```bash
docker-compose up -d
```

### 2. Access n8n UI

Open http://localhost:5678 in your browser

### 3. Import Example Workflow

1. In n8n, go to **Workflows** → **Import from File**
2. Select `workflows/01_hello_world.json`
3. Click **Execute Workflow**

### 4. Use Python Client

```python
# In Jupyter notebook
import sys
sys.path.append('../scripts')
from n8n_client import N8nClient

# Create client
client = N8nClient(
    base_url="http://localhost:5678",
    username="admin",
    password="changeme123"
)

# List workflows
workflows = client.list_workflows()
print(f"Found {len(workflows)} workflows")

# Trigger a workflow
result = client.trigger_workflow("test", {"name": "John"})
print(result)
```

## Tips for Success

### Learning Approach

1. **Follow Sequential Order**: Modules build on each other
2. **Hands-On Practice**: Don't just read—build the workflows
3. **Experiment**: Modify examples to understand how they work
4. **Use Both Interfaces**: Practice in n8n UI and Python
5. **Export Your Work**: Save workflows as JSON for reference

### Best Practices

- **Start Simple**: Master basics before complex workflows
- **Test Incrementally**: Test each node before adding more
- **Handle Errors**: Always include error handling
- **Document Workflows**: Add notes to your workflows
- **Version Control**: Export and commit workflow JSON files
- **Secure Credentials**: Use n8n's credential system, never hardcode

### Common Pitfalls to Avoid

- Don't skip the setup module—proper configuration is crucial
- Don't activate workflows until fully tested
- Don't ignore error handling
- Don't hardcode sensitive data
- Don't forget to backup before major changes

## Troubleshooting

### n8n won't start

```bash
# Check Docker status
docker ps -a

# View logs
docker logs n8n

# Restart container
docker-compose restart
```

### Can't access n8n UI

- Check if port 5678 is already in use
- Verify firewall settings
- Try accessing via 127.0.0.1:5678 instead of localhost

### Python client connection errors

```python
# Test connection
client.health_check()

# Verify credentials in .env file
# Ensure N8N_API_KEY or N8N_USERNAME/PASSWORD are set
```

### Workflow execution fails

1. Check execution history in n8n UI
2. Review error messages in failed nodes
3. Test each node individually
4. Verify credentials are properly configured

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for comprehensive troubleshooting guide.

## Additional Resources

### Official n8n Resources

- [n8n Official Documentation](https://docs.n8n.io/)
- [n8n Community Forum](https://community.n8n.io/)
- [n8n GitHub Repository](https://github.com/n8n-io/n8n)
- [n8n Workflow Templates](https://n8n.io/workflows/)
- [n8n YouTube Channel](https://www.youtube.com/c/n8n-io)

### Python & API Resources

- [Requests Library Documentation](https://requests.readthedocs.io/)
- [n8n REST API Documentation](https://docs.n8n.io/api/)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

### Deployment Resources

- [Docker Documentation](https://docs.docker.com/)
- [n8n Self-Hosting Guide](https://docs.n8n.io/hosting/)
- [DigitalOcean Deployment Guide](https://docs.n8n.io/hosting/installation/docker/)

### Learning Resources

- [Workflow Automation Best Practices](https://n8n.io/blog/workflow-automation-best-practices/)
- [n8n vs Zapier Comparison](https://n8n.io/compare/zapier/)
- [REST API Tutorial](https://www.restapitutorial.com/)

## Project Roadmap

### Current Status: v1.0 - Initial Release

**Completed:**
- ✅ Project structure and setup
- ✅ Docker configuration
- ✅ Python n8n API client
- ✅ 10 learning modules (notebooks)
- ✅ Example workflows
- ✅ Documentation

### Future Enhancements (v1.1+)

- [ ] Advanced AI workflow examples (LangChain integration)
- [ ] Video tutorials for each module
- [ ] Additional workflow templates (20+ workflows)
- [ ] Custom node development guide
- [ ] Advanced monitoring and logging setup
- [ ] Kubernetes deployment guide
- [ ] Performance optimization guide
- [ ] Integration testing framework

## Contributing

This is a personal learning project, but suggestions are welcome! If you find errors or have ideas for improvements:

1. Document the issue or suggestion
2. Create a detailed description
3. Submit via GitHub issues

## License

This project is licensed under the MIT License. See LICENSE file for details.

n8n itself is licensed under the Sustainable Use License and n8n Enterprise License. See [n8n licensing](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) for details.

## Acknowledgments

- **n8n Team** for creating an amazing open-source automation platform
- **Jupyter Project** for the interactive notebook environment
- **Docker** for containerization technology
- **Python Community** for excellent libraries and tools

## Contact

For questions, feedback, or collaboration:

- GitHub: [Your GitHub Profile]
- Email: [Your Email]
- LinkedIn: [Your LinkedIn]

---

**Happy Automating! 🚀**

Start with Module 00 and begin your journey to workflow automation mastery!
