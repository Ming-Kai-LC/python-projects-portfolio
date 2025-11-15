"""
n8n Python Client for Jupyter Notebooks
=========================================

A comprehensive Python client for interacting with the n8n REST API.
This client allows you to manage workflows, executions, and credentials
programmatically from Jupyter notebooks or Python scripts.

Author: Your Name
Date: 2025
License: MIT
"""

import requests
from typing import Dict, List, Optional, Any
import json
from datetime import datetime
import time


class N8nClient:
    """
    Python client for n8n REST API.

    Provides methods to:
    - Manage workflows (list, create, update, delete, activate)
    - Trigger workflow executions
    - Monitor execution status and results
    - Manage credentials
    - Import/export workflows

    Args:
        base_url (str): Base URL of n8n instance (default: http://localhost:5678)
        api_key (Optional[str]): API key for authentication
        username (Optional[str]): Username for basic auth
        password (Optional[str]): Password for basic auth

    Example:
        >>> client = N8nClient(api_key="your-api-key")
        >>> workflows = client.list_workflows()
        >>> print(f"Found {len(workflows)} workflows")
    """

    def __init__(
        self,
        base_url: str = "http://localhost:5678",
        api_key: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None
    ):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

        # Setup authentication
        if api_key:
            self.session.headers.update({
                'X-N8N-API-KEY': api_key,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
        elif username and password:
            self.session.auth = (username, password)
            self.session.headers.update({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })
        else:
            self.session.headers.update({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })

    # ========== Workflow Management ==========

    def list_workflows(self) -> List[Dict[str, Any]]:
        """
        List all workflows in the n8n instance.

        Returns:
            List of workflow dictionaries containing id, name, active status, etc.

        Example:
            >>> workflows = client.list_workflows()
            >>> for wf in workflows:
            ...     print(f"{wf['name']} (Active: {wf['active']})")
        """
        response = self.session.get(f"{self.base_url}/api/v1/workflows")
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])

    def get_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific workflow.

        Args:
            workflow_id: ID of the workflow to retrieve

        Returns:
            Dictionary containing complete workflow details including nodes

        Example:
            >>> workflow = client.get_workflow("123")
            >>> print(workflow['name'])
            >>> print(f"Nodes: {len(workflow['nodes'])}")
        """
        response = self.session.get(f"{self.base_url}/api/v1/workflows/{workflow_id}")
        response.raise_for_status()
        return response.json()

    def create_workflow(self, workflow_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new workflow.

        Args:
            workflow_data: Dictionary containing workflow definition

        Returns:
            Created workflow data including assigned ID

        Example:
            >>> workflow = {
            ...     "name": "My Workflow",
            ...     "nodes": [],
            ...     "connections": {},
            ...     "active": False
            ... }
            >>> created = client.create_workflow(workflow)
            >>> print(f"Created workflow with ID: {created['id']}")
        """
        response = self.session.post(
            f"{self.base_url}/api/v1/workflows",
            json=workflow_data
        )
        response.raise_for_status()
        return response.json()

    def update_workflow(self, workflow_id: str, workflow_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing workflow.

        Args:
            workflow_id: ID of workflow to update
            workflow_data: Updated workflow definition

        Returns:
            Updated workflow data

        Example:
            >>> workflow = client.get_workflow("123")
            >>> workflow['name'] = "Updated Name"
            >>> updated = client.update_workflow("123", workflow)
        """
        response = self.session.patch(
            f"{self.base_url}/api/v1/workflows/{workflow_id}",
            json=workflow_data
        )
        response.raise_for_status()
        return response.json()

    def delete_workflow(self, workflow_id: str) -> bool:
        """
        Delete a workflow.

        Args:
            workflow_id: ID of workflow to delete

        Returns:
            True if successful

        Example:
            >>> client.delete_workflow("123")
            >>> print("Workflow deleted")
        """
        response = self.session.delete(f"{self.base_url}/api/v1/workflows/{workflow_id}")
        response.raise_for_status()
        return True

    def activate_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """
        Activate a workflow to make it run automatically.

        Args:
            workflow_id: ID of workflow to activate

        Returns:
            Updated workflow data

        Example:
            >>> client.activate_workflow("123")
            >>> print("Workflow activated")
        """
        workflow = self.get_workflow(workflow_id)
        workflow['active'] = True
        return self.update_workflow(workflow_id, workflow)

    def deactivate_workflow(self, workflow_id: str) -> Dict[str, Any]:
        """
        Deactivate a workflow to stop automatic execution.

        Args:
            workflow_id: ID of workflow to deactivate

        Returns:
            Updated workflow data

        Example:
            >>> client.deactivate_workflow("123")
            >>> print("Workflow deactivated")
        """
        workflow = self.get_workflow(workflow_id)
        workflow['active'] = False
        return self.update_workflow(workflow_id, workflow)

    # ========== Workflow Execution ==========

    def trigger_workflow(
        self,
        webhook_path: str,
        data: Optional[Dict[str, Any]] = None,
        method: str = "POST"
    ) -> Dict[str, Any]:
        """
        Trigger a workflow via webhook.

        Args:
            webhook_path: Webhook path (e.g., "my-webhook")
            data: Data to send to the workflow
            method: HTTP method (POST, GET, etc.)

        Returns:
            Response from the workflow

        Example:
            >>> result = client.trigger_workflow("test", {"name": "John"})
            >>> print(result)
        """
        url = f"{self.base_url}/webhook/{webhook_path}"

        if method.upper() == "POST":
            response = self.session.post(url, json=data or {})
        elif method.upper() == "GET":
            response = self.session.get(url, params=data or {})
        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()

        # Handle different response types
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            return response.json()
        else:
            return {'response': response.text}

    def execute_workflow(self, workflow_id: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a workflow manually (requires workflow to have a manual trigger).

        Args:
            workflow_id: ID of workflow to execute
            data: Input data for the workflow

        Returns:
            Execution result

        Example:
            >>> result = client.execute_workflow("123", {"input": "value"})
            >>> print(result)
        """
        response = self.session.post(
            f"{self.base_url}/api/v1/workflows/{workflow_id}/execute",
            json={'data': data or {}}
        )
        response.raise_for_status()
        return response.json()

    # ========== Execution History ==========

    def list_executions(
        self,
        workflow_id: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        List workflow executions.

        Args:
            workflow_id: Filter by specific workflow (optional)
            limit: Maximum number of executions to return

        Returns:
            List of execution records

        Example:
            >>> executions = client.list_executions(workflow_id="123", limit=10)
            >>> for ex in executions:
            ...     print(f"Execution {ex['id']}: {ex['finished']}")
        """
        params = {'limit': limit}
        if workflow_id:
            params['workflowId'] = workflow_id

        response = self.session.get(
            f"{self.base_url}/api/v1/executions",
            params=params
        )
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])

    def get_execution(self, execution_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific execution.

        Args:
            execution_id: ID of the execution

        Returns:
            Execution details including data from each node

        Example:
            >>> execution = client.get_execution("456")
            >>> print(f"Status: {execution['finished']}")
            >>> print(f"Start time: {execution['startedAt']}")
        """
        response = self.session.get(f"{self.base_url}/api/v1/executions/{execution_id}")
        response.raise_for_status()
        return response.json()

    def delete_execution(self, execution_id: str) -> bool:
        """
        Delete an execution record.

        Args:
            execution_id: ID of execution to delete

        Returns:
            True if successful

        Example:
            >>> client.delete_execution("456")
        """
        response = self.session.delete(f"{self.base_url}/api/v1/executions/{execution_id}")
        response.raise_for_status()
        return True

    # ========== Import/Export ==========

    def export_workflow(self, workflow_id: str, file_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Export a workflow to JSON.

        Args:
            workflow_id: ID of workflow to export
            file_path: Optional file path to save JSON (if None, returns data)

        Returns:
            Workflow JSON data

        Example:
            >>> # Export to file
            >>> client.export_workflow("123", "my_workflow.json")
            >>>
            >>> # Get as dictionary
            >>> workflow_json = client.export_workflow("123")
        """
        workflow = self.get_workflow(workflow_id)

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(workflow, f, indent=2, ensure_ascii=False)
            print(f"Workflow exported to {file_path}")

        return workflow

    def import_workflow(self, file_path: str, activate: bool = False) -> Dict[str, Any]:
        """
        Import a workflow from JSON file.

        Args:
            file_path: Path to JSON file
            activate: Whether to activate the workflow after import

        Returns:
            Created workflow data

        Example:
            >>> imported = client.import_workflow("my_workflow.json", activate=True)
            >>> print(f"Imported workflow: {imported['name']}")
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)

        # Remove id if present (will be assigned new id)
        workflow_data.pop('id', None)
        workflow_data['active'] = activate

        created = self.create_workflow(workflow_data)
        print(f"Workflow '{created['name']}' imported successfully")
        return created

    # ========== Utility Methods ==========

    def health_check(self) -> Dict[str, Any]:
        """
        Check if n8n instance is healthy.

        Returns:
            Health status information

        Example:
            >>> health = client.health_check()
            >>> print(health)
        """
        try:
            response = self.session.get(f"{self.base_url}/healthz")
            response.raise_for_status()
            return {"status": "healthy", "details": response.json()}
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}

    def get_workflow_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Find a workflow by name.

        Args:
            name: Name of the workflow

        Returns:
            Workflow data or None if not found

        Example:
            >>> workflow = client.get_workflow_by_name("My Workflow")
            >>> if workflow:
            ...     print(f"Found: {workflow['id']}")
        """
        workflows = self.list_workflows()
        for workflow in workflows:
            if workflow['name'] == name:
                return self.get_workflow(workflow['id'])
        return None

    def wait_for_execution(
        self,
        execution_id: str,
        timeout: int = 300,
        poll_interval: int = 2
    ) -> Dict[str, Any]:
        """
        Wait for an execution to complete.

        Args:
            execution_id: ID of execution to monitor
            timeout: Maximum seconds to wait
            poll_interval: Seconds between status checks

        Returns:
            Final execution data

        Example:
            >>> result = client.wait_for_execution("456", timeout=60)
            >>> if result['finished']:
            ...     print("Execution completed successfully")
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            execution = self.get_execution(execution_id)

            if execution.get('finished'):
                return execution

            time.sleep(poll_interval)

        raise TimeoutError(f"Execution {execution_id} did not complete within {timeout} seconds")

    def __repr__(self) -> str:
        """String representation of the client."""
        return f"N8nClient(base_url='{self.base_url}')"


# ========== Helper Functions ==========

def create_client_from_env() -> N8nClient:
    """
    Create an N8nClient using environment variables.

    Expected environment variables:
    - N8N_BASE_URL (default: http://localhost:5678)
    - N8N_API_KEY or
    - N8N_USERNAME and N8N_PASSWORD

    Example:
        >>> from dotenv import load_dotenv
        >>> load_dotenv()
        >>> client = create_client_from_env()
    """
    import os
    from dotenv import load_dotenv

    load_dotenv()

    base_url = os.getenv('N8N_BASE_URL', 'http://localhost:5678')
    api_key = os.getenv('N8N_API_KEY')
    username = os.getenv('N8N_USERNAME')
    password = os.getenv('N8N_PASSWORD')

    return N8nClient(
        base_url=base_url,
        api_key=api_key,
        username=username,
        password=password
    )


def pretty_print_workflow(workflow: Dict[str, Any]) -> None:
    """
    Print workflow information in a readable format.

    Args:
        workflow: Workflow dictionary from API

    Example:
        >>> workflow = client.get_workflow("123")
        >>> pretty_print_workflow(workflow)
    """
    print(f"\n{'='*60}")
    print(f"Workflow: {workflow['name']}")
    print(f"{'='*60}")
    print(f"ID: {workflow.get('id', 'N/A')}")
    print(f"Active: {workflow.get('active', False)}")
    print(f"Created: {workflow.get('createdAt', 'N/A')}")
    print(f"Updated: {workflow.get('updatedAt', 'N/A')}")
    print(f"\nNodes ({len(workflow.get('nodes', []))}):")

    for i, node in enumerate(workflow.get('nodes', []), 1):
        print(f"  {i}. {node['name']} ({node['type']})")

    print(f"\nConnections: {len(workflow.get('connections', {}))}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    # Example usage
    print("n8n Python Client")
    print("="*60)
    print("\nBasic Usage:")
    print("""
    from n8n_client import N8nClient

    # Create client
    client = N8nClient(api_key="your-api-key")

    # List workflows
    workflows = client.list_workflows()
    print(f"Found {len(workflows)} workflows")

    # Trigger workflow
    result = client.trigger_workflow("webhook-path", {"data": "value"})
    print(result)
    """)
