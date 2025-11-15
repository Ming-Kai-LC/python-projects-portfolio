# Windows Automation & Scripting - Project Summary

## Project Goals

Create a comprehensive, beginner-friendly curriculum for learning Windows automation and scripting through hands-on, interactive Jupyter notebooks.

## Target Audience

Complete beginners with:
- Basic Windows usage experience
- No prior programming or scripting knowledge
- Desire to automate repetitive tasks
- Interest in improving productivity

## Learning Objectives

By the end of this course, students will be able to:
1. Navigate Windows using command-line interfaces
2. Write basic to intermediate PowerShell scripts
3. Automate file and folder operations
4. Schedule tasks to run automatically
5. Extract and process system information
6. Create practical automation solutions for daily tasks

## Curriculum Structure

### Module 0: Introduction to Windows Automation
**Notebook**: `00_introduction.ipynb`
- What is automation and why it matters
- Overview of Windows scripting tools (CMD vs PowerShell)
- Setting up the learning environment
- Running your first command
- Safety and best practices

### Module 1: Command Prompt Basics
**Notebook**: `01_command_prompt_basics.ipynb`
- Navigating the file system (cd, dir)
- File operations (copy, move, del, rename)
- Directory operations (mkdir, rmdir)
- Viewing file contents (type, more)
- Batch files introduction (.bat)
- Practical exercises

### Module 2: Introduction to PowerShell
**Notebook**: `02_powershell_introduction.ipynb`
- What is PowerShell and its advantages
- PowerShell vs Command Prompt
- Basic cmdlets (Get-Command, Get-Help)
- Working with output (Format-Table, Format-List)
- Piping and object-oriented nature
- Creating and running .ps1 scripts
- Execution policies

### Module 3: Variables and Data Types
**Notebook**: `03_variables_and_data_types.ipynb`
- Creating and using variables
- Data types (strings, numbers, arrays, hashtables)
- String manipulation and formatting
- Working with arrays
- Hashtables and key-value pairs
- Type casting and conversion
- Hands-on exercises

### Module 4: Control Flow in PowerShell
**Notebook**: `04_control_flow.ipynb`
- If/Else conditional statements
- Switch statements
- Comparison operators
- Logical operators (AND, OR, NOT)
- For loops
- ForEach loops
- While and Do-While loops
- Break and Continue
- Practice problems

### Module 5: File System Operations
**Notebook**: `05_file_system_operations.ipynb`
- Reading directory contents (Get-ChildItem)
- Creating, copying, moving files and folders
- Deleting and renaming items
- Testing paths and existence
- File properties and attributes
- Recursive operations
- Filtering files by extension, date, size
- Practical project: File organizer script

### Module 6: Text Processing and Data Manipulation
**Notebook**: `06_text_processing.ipynb`
- Reading text files (Get-Content)
- Writing to files (Set-Content, Add-Content)
- Processing CSV files (Import-Csv, Export-Csv)
- Working with JSON data
- String searching and pattern matching
- Regular expressions basics
- Practical project: Log file analyzer

### Module 7: Task Automation Fundamentals
**Notebook**: `07_task_automation.ipynb`
- Environment variables
- Working with the registry (safely)
- Running external programs
- Capturing program output
- Error handling (Try/Catch)
- Creating reusable functions
- Script parameters and arguments
- Practical project: System maintenance script

### Module 8: Scheduled Tasks
**Notebook**: `08_scheduled_tasks.ipynb`
- Introduction to Task Scheduler
- Creating scheduled tasks via PowerShell
- Task triggers (time-based, event-based)
- Task actions and conditions
- Managing existing tasks
- Practical project: Automated backup script
- Setting up daily/weekly automation

### Module 9: System Information and Administration
**Notebook**: `09_system_information.ipynb`
- Getting system information
- Disk usage and monitoring
- Process management
- Service management
- Network information
- User and group management basics
- Generating system reports
- Practical project: System health checker

### Module 10: Final Capstone Project
**Notebook**: `10_final_project.ipynb`
- Project overview and requirements
- Building a comprehensive automation solution
- Suggested projects:
  - Automated file backup system
  - System maintenance suite
  - Log monitoring and alerting
  - File organization and cleanup
  - Report generation system
- Code organization and best practices
- Testing and debugging
- Documentation

## Teaching Methodology

### Interactive Learning
- Each notebook contains:
  - Clear explanations with examples
  - Code cells students can run and modify
  - Practice exercises with solutions
  - Real-world scenarios
  - Troubleshooting tips

### Progressive Difficulty
- Start with simple concepts
- Gradually build complexity
- Review previous concepts
- Cumulative learning approach

### Safety First
- Emphasize testing in safe environments
- Use test folders for practice
- Warn about destructive operations
- Teach proper backup procedures
- Explain administrator privileges

### Hands-On Practice
- Every concept includes exercises
- Mini-projects after each section
- Final capstone project
- Encourage experimentation

## Technical Requirements

### Software
- Windows 10 or Windows 11
- PowerShell 5.1+ (built into Windows)
- Python 3.8+
- Jupyter Notebook
- Text editor (VS Code recommended)

### Python Packages
- jupyter
- notebook
- ipykernel
- powershell-kernel (for PowerShell notebooks)

## Expected Outcomes

Students completing this course will have:
1. Portfolio of 10+ automation scripts
2. Understanding of Windows scripting fundamentals
3. Ability to create custom automation solutions
4. Confidence to explore advanced topics
5. Practical skills for daily productivity

## Future Enhancements

Potential additions:
- Windows Registry deep dive
- Active Directory basics
- Remote administration
- GUI automation with PowerShell
- Integration with Python for advanced automation
- Error logging and monitoring
- Security best practices
- Performance optimization

## Assessment Strategy

- Completion of exercises in each module
- Successfully running all code examples
- Completing the final capstone project
- Creating at least one personal automation script

## Time Estimate

- Total course: 20-30 hours
- Per module: 2-3 hours
- Final project: 4-6 hours
- At recommended pace: 2-3 weeks

## Resources and References

- Microsoft PowerShell Documentation
- Windows Command Reference
- Community forums and Stack Overflow
- Best practices guides
- Video tutorials (links provided in notebooks)

## Version History

- v1.0 (Current): Initial curriculum design
- Future: Will add advanced modules based on feedback

---

**Last Updated**: 2025-11-14
**Status**: Initial Setup
**Maintainer**: Course Developer
