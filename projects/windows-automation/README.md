# Windows Automation & Scripting for Beginners

A comprehensive, beginner-friendly guide to Windows automation and scripting using interactive Jupyter notebooks.

## Project Overview

This project teaches complete beginners how to automate tasks and improve productivity on Windows using various scripting techniques. Learn to automate repetitive tasks, manage files, schedule operations, and more.

## Target Audience

- Complete beginners with no prior scripting experience
- Windows users looking to automate daily tasks
- Anyone wanting to improve their Windows productivity

## What You'll Learn

- **Command Prompt Basics**: Navigate and perform operations using CMD
- **PowerShell Fundamentals**: Modern Windows scripting and automation
- **File System Automation**: Batch file operations, backups, and organization
- **Task Scheduling**: Automate tasks to run at specific times
- **System Administration**: User management, permissions, and system info
- **Practical Projects**: Real-world automation scenarios

## Prerequisites

- Windows 10 or Windows 11
- Python 3.8+ (for running Jupyter notebooks)
- Administrator access (for some lessons)
- Basic computer literacy

## Setup

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd python-projects-portfolio
   ```

2. **Create virtual environment** (from repository root):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r projects/windows-automation/requirements.txt
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Navigate to**: `projects/windows-automation/notebooks/`

## Project Structure

```
windows-automation/
├── README.md                          # This file
├── PROJECT_SUMMARY.md                 # Curriculum details
├── requirements.txt                   # Python dependencies
└── notebooks/                         # Interactive lessons
    ├── 00_introduction.ipynb
    ├── 01_command_prompt_basics.ipynb
    ├── 02_powershell_introduction.ipynb
    ├── 03_variables_and_data_types.ipynb
    ├── 04_control_flow.ipynb
    ├── 05_file_system_operations.ipynb
    ├── 06_text_processing.ipynb
    ├── 07_task_automation.ipynb
    ├── 08_scheduled_tasks.ipynb
    ├── 09_system_information.ipynb
    └── 10_final_project.ipynb
```

## Learning Path

1. **Getting Started** (Module 0): Introduction to automation concepts
2. **Command Line Basics** (Modules 1): CMD fundamentals
3. **PowerShell Essentials** (Modules 2-4): Core scripting skills
4. **File Operations** (Modules 5-6): Automate file management
5. **Advanced Automation** (Modules 7-9): Task scheduling and system admin
6. **Capstone Project** (Module 10): Build a complete automation solution

## Safety Notes

- Always backup important data before running automation scripts
- Test scripts in a safe environment first
- Be careful with registry operations and system-level commands
- Some operations require administrator privileges

## Tips for Success

- Work through notebooks in order
- Practice with the provided exercises
- Experiment in a test folder
- Save your custom scripts for reuse
- Ask questions when stuck

## Contributing

Feel free to submit issues or pull requests to improve the content.

## License

This project is for educational purposes.

## Additional Resources

- [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [Windows Command Line Reference](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
- [Task Scheduler Documentation](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
