# Troubleshooting Guide

This guide helps you resolve common issues when working with n8n and this learning project.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Docker Problems](#docker-problems)
- [n8n Connection Issues](#n8n-connection-issues)
- [Workflow Execution Errors](#workflow-execution-errors)
- [Python Client Issues](#python-client-issues)
- [Deployment Issues](#deployment-issues)
- [Performance Issues](#performance-issues)

---

## Installation Issues

### Docker Not Found

**Error:** `docker: command not found`

**Solution:**
1. Install Docker Desktop:
   - Windows: https://www.docker.com/products/docker-desktop
   - macOS: https://www.docker.com/products/docker-desktop
   - Linux: https://docs.docker.com/engine/install/

2. Restart your terminal/computer
3. Verify installation: `docker --version`

### Docker Daemon Not Running

**Error:** `Cannot connect to the Docker daemon`

**Solution:**
- **Windows/macOS**: Start Docker Desktop application
- **Linux**: `sudo systemctl start docker`
- Wait for Docker to fully start (check system tray icon)

### Permission Denied

**Error:** `Permission denied while trying to connect to the Docker daemon`

**Solution (Linux):**
```bash
# Add your user to docker group
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker

# Verify
docker ps
```

---

## Docker Problems

### Port Already in Use

**Error:** `Bind for 0.0.0.0:5678 failed: port is already allocated`

**Solution 1 - Find and stop the conflicting process:**
```bash
# Windows
netstat -ano | findstr :5678
taskkill /PID <process_id> /F

# macOS/Linux
lsof -i :5678
kill -9 <process_id>
```

**Solution 2 - Change the port:**
Edit `docker-compose.yml`:
```yaml
ports:
  - "5679:5678"  # Use port 5679 instead
```

Then access n8n at `http://localhost:5679`

### Container Keeps Restarting

**Error:** Container status shows "Restarting"

**Solution:**
```bash
# Check logs
docker logs n8n

# Common causes:
# 1. Invalid environment variables
# 2. Database connection issues
# 3. Permission problems with volumes

# Fix: Remove and recreate
docker-compose down -v
docker-compose up -d
```

### Out of Disk Space

**Error:** `no space left on device`

**Solution:**
```bash
# Remove unused Docker resources
docker system prune -a

# Remove old containers
docker container prune

# Remove old volumes (⚠️ This deletes data!)
docker volume prune
```

---

## n8n Connection Issues

### Cannot Access http://localhost:5678

**Symptoms:** Browser shows "can't reach this page" or "connection refused"

**Solutions:**

1. **Wait for initialization** (30-60 seconds after starting)

2. **Check if container is running:**
   ```bash
   docker ps | grep n8n
   ```

3. **Try alternative URLs:**
   - `http://127.0.0.1:5678`
   - `http://0.0.0.0:5678`

4. **Check firewall:**
   - Windows: Allow Docker in Windows Firewall
   - macOS: System Preferences → Security → Firewall
   - Linux: `sudo ufw allow 5678`

5. **View logs:**
   ```bash
   docker logs n8n --tail 100
   ```

### Authentication Failed

**Error:** "Invalid credentials" or "Login failed"

**Solutions:**

1. **Check credentials in docker-compose.yml:**
   ```yaml
   environment:
     - N8N_BASIC_AUTH_USER=admin
     - N8N_BASIC_AUTH_PASSWORD=changeme123
   ```

2. **If you created owner account:** Use those credentials instead

3. **Reset (⚠️ Deletes all data):**
   ```bash
   docker-compose down -v
   docker-compose up -d
   ```

### n8n UI Loads But Shows Errors

**Symptoms:** UI appears but workflows don't load, errors in console

**Solutions:**

1. **Clear browser cache:**
   - Chrome: Ctrl+Shift+Delete
   - Firefox: Ctrl+Shift+Delete
   - Safari: Cmd+Option+E

2. **Try incognito/private mode**

3. **Check browser console** (F12) for error messages

4. **Restart n8n:**
   ```bash
   docker-compose restart
   ```

---

## Workflow Execution Errors

### Workflow Execution Fails Immediately

**Common Causes:**

1. **Missing credentials**
   - Solution: Set up credentials in Settings → Credentials

2. **Invalid node configuration**
   - Solution: Check red exclamation marks on nodes
   - Verify all required fields are filled

3. **API rate limiting**
   - Solution: Add delays between requests
   - Check API documentation for limits

### Node Shows "Error: Unauthorized"

**Solutions:**

1. **Check API credentials:**
   - Verify API key/token is correct
   - Check if key has expired
   - Ensure key has required permissions

2. **Check authentication method:**
   - API Key vs Bearer Token
   - Header name (X-API-Key, Authorization, etc.)

3. **Test credentials externally:**
   ```bash
   # Test with curl
   curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com
   ```

### "Cannot read property of undefined"

**Cause:** Accessing data that doesn't exist

**Solutions:**

1. **Check previous node output:**
   - Click on previous node
   - View "Output" tab
   - Verify field names

2. **Use expressions correctly:**
   ```javascript
   // Wrong:
   {{$json.data.user.name}}  // If 'user' is undefined

   // Right:
   {{$json.data?.user?.name}}  // Optional chaining
   ```

3. **Add IF node to check existence:**
   ```javascript
   // Condition:
   {{$json.data !== undefined}}
   ```

### HTTP Request Timeout

**Error:** "Request timed out"

**Solutions:**

1. **Increase timeout in HTTP Request node:**
   - Settings → Timeout (default: 300000ms = 5 min)

2. **Check API endpoint status:**
   ```bash
   curl -I https://api.example.com/endpoint
   ```

3. **Try request with smaller data:**
   - Might be processing too much data
   - Implement pagination

---

## Python Client Issues

### Import Error: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'n8n_client'`

**Solution:**
```python
import sys
sys.path.append('../scripts')  # Adjust path as needed
from n8n_client import N8nClient
```

Or:
```bash
# Add scripts to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/scripts"
```

### Connection Refused from Python

**Error:** `requests.exceptions.ConnectionError`

**Solutions:**

1. **Verify n8n is running:**
   ```bash
   docker ps | grep n8n
   ```

2. **Check URL:**
   ```python
   client = N8nClient(
       base_url="http://localhost:5678",  # Correct
       # NOT: base_url="https://localhost:5678"
   )
   ```

3. **Test connection:**
   ```python
   health = client.health_check()
   print(health)
   ```

### Authentication Failed from Python

**Error:** `401 Unauthorized`

**Solutions:**

1. **Verify credentials:**
   ```python
   client = N8nClient(
       base_url="http://localhost:5678",
       username="admin",
       password="changeme123"  # Match docker-compose.yml
   )
   ```

2. **Use API key instead:**
   ```python
   client = N8nClient(
       base_url="http://localhost:5678",
       api_key="your-api-key"
   )
   ```

3. **Generate API key in n8n:**
   - Settings → API → Create API Key

---

## Deployment Issues

### Cloud Deployment Fails

**Common Issues:**

1. **Insufficient resources:**
   - Minimum: 1GB RAM, 1 CPU
   - Recommended: 2GB RAM, 2 CPU

2. **Port conflicts:**
   - Ensure port 5678 is available
   - Or use reverse proxy (nginx)

3. **Environment variables not set:**
   ```bash
   # Check in container
   docker exec n8n env
   ```

### SSL/HTTPS Not Working

**Solutions:**

1. **Verify DNS:**
   ```bash
   nslookup your-domain.com
   ```

2. **Check Let's Encrypt logs:**
   ```bash
   docker logs letsencrypt
   ```

3. **Verify nginx configuration:**
   ```bash
   docker exec nginx-proxy nginx -t
   ```

### Database Connection Failed

**Error:** "Could not connect to database"

**Solutions:**

1. **Check PostgreSQL is running:**
   ```bash
   docker ps | grep postgres
   ```

2. **Verify database credentials:**
   ```yaml
   environment:
     - DB_POSTGRESDB_PASSWORD=${DB_PASSWORD}
   ```

3. **Test connection:**
   ```bash
   docker exec -it n8n_postgres psql -U n8n -d n8n
   ```

---

## Performance Issues

### Workflows Execute Slowly

**Solutions:**

1. **Optimize API calls:**
   - Batch requests when possible
   - Cache responses
   - Use pagination

2. **Reduce data processing:**
   - Filter early in workflow
   - Process in batches
   - Use database queries instead of loading all data

3. **Increase resources:**
   ```yaml
   # docker-compose.yml
   services:
     n8n:
       deploy:
         resources:
           limits:
             memory: 2G
   ```

### High Memory Usage

**Solutions:**

1. **Check for memory leaks:**
   ```bash
   docker stats n8n
   ```

2. **Restart n8n regularly:**
   ```bash
   # Add to cron
   0 3 * * * docker-compose restart n8n
   ```

3. **Limit execution concurrency:**
   ```yaml
   environment:
     - EXECUTIONS_CONCURRENT=5  # Default: 10
   ```

### Database Growing Too Large

**Solutions:**

1. **Prune old executions:**
   - Settings → Execution Data
   - Set retention period

2. **Manual cleanup:**
   ```sql
   -- In PostgreSQL
   DELETE FROM execution_entity
   WHERE "stoppedAt" < NOW() - INTERVAL '30 days';
   ```

3. **Regular backups and cleanup:**
   ```bash
   # Backup before cleanup
   docker exec n8n_postgres pg_dump -U n8n n8n > backup.sql
   ```

---

## Getting More Help

### Logs and Debugging

**Collect diagnostic information:**

```bash
# n8n logs
docker logs n8n --tail 200 > n8n_logs.txt

# Container status
docker ps -a > docker_status.txt

# System resources
docker stats --no-stream > resources.txt

# n8n version
docker exec n8n n8n --version
```

### Community Support

- [n8n Community Forum](https://community.n8n.io/)
- [GitHub Issues](https://github.com/n8n-io/n8n/issues)
- [Discord Server](https://discord.gg/n8n)

### Reporting Issues

**Include:**
1. n8n version
2. Operating system
3. Docker version
4. Error message (full text)
5. Steps to reproduce
6. Relevant logs

---

## Quick Reference Commands

```bash
# Start n8n
docker-compose up -d

# Stop n8n
docker-compose stop

# Restart n8n
docker-compose restart

# View logs
docker logs n8n --tail 100 -f

# Access n8n shell
docker exec -it n8n sh

# Backup workflows
docker exec n8n n8n export:workflow --all --output=backups/

# Check container health
docker ps
docker stats n8n

# Remove everything (⚠️ DANGER)
docker-compose down -v
```

---

**Still stuck?** Check the [main README](../README.md) or ask in the [community forum](https://community.n8n.io/).
