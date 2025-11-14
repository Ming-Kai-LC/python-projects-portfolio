# English Learning Notebooks - Interactive Grammar Course

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, research-backed English grammar learning system built with Jupyter Notebooks. This pilot project covers **A1 (Beginner) level** with 10 interactive modules following proven pedagogical methodologies.

## Overview

This project implements a complete English learning curriculum based on the **Cambridge English Grammar Profile**, **CEFR standards**, and applied linguistics research. It features:

- **Interactive exercises** with immediate feedback
- **Text-to-speech audio** for pronunciation practice
- **Spaced repetition system** for optimal retention
- **Progress tracking** with visual dashboards
- **5-phase learning structure** (Introduction → Controlled Practice → Meaningful Practice → Communicative Practice → Spaced Review)

## Features

### Pedagogical Foundation

Based on research showing:
- **Explicit grammar instruction** yields the highest effect size (d=1.26) among language skills
- **Spaced repetition** improves long-term retention by up to 200%
- **Practice distribution** should favor communicative practice (60-70% at intermediate levels)
- **Focus on Form** approach balances accuracy and fluency

### Technical Features

- **Interactive exercises** using ipywidgets with instant validation
- **Audio generation** using gTTS for pronunciation examples
- **Progress tracking** with JSON-based storage
- **Spaced repetition scheduler** implementing SuperMemo-inspired algorithm
- **Data visualization** using matplotlib and plotly
- **Modular architecture** for easy expansion to 160 modules (A1-C2)

## Project Structure

```
english-learning/
├── notebooks/
│   ├── A1/
│   │   ├── Module_01/          # Verb "To Be"
│   │   │   ├── 01_introduction.ipynb
│   │   │   ├── 02_controlled_practice.ipynb
│   │   │   ├── 03_meaningful_practice.ipynb
│   │   │   ├── 04_communicative_practice.ipynb
│   │   │   └── audio/
│   │   ├── Module_02/          # Personal Pronouns
│   │   ├── Module_03/          # Present Simple - Affirmative
│   │   ├── Module_04/          # Present Simple - Negatives/Questions
│   │   ├── Module_05/          # Articles and Demonstratives
│   │   ├── Module_06/          # Nouns and Plurals
│   │   ├── Module_07/          # Possessives
│   │   ├── Module_08/          # Adjectives
│   │   ├── Module_09/          # There Is/Are
│   │   └── Module_10/          # Prepositions
│   ├── reviews/
│   │   └── A1_Review_Modules_1-5.ipynb
│   └── progress_tracker.ipynb
├── utils/
│   ├── feedback_system.py      # Exercise validation and feedback
│   ├── audio_generator.py      # Text-to-speech functionality
│   └── spaced_repetition.py    # Review scheduling system
├── data/
│   └── progress.json           # Student progress tracking
├── generate_modules.py         # Module generation script
├── requirements.txt
├── English-Path.md            # Complete curriculum documentation
└── README.md
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. **Clone or navigate to the repository:**
   ```bash
   cd projects/english-learning
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Enable Jupyter widgets:**
   ```bash
   jupyter nbextension enable --py widgetsnbextension
   ```

5. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

## Usage

### Getting Started

1. **Open the Progress Tracker:**
   - Navigate to `notebooks/progress_tracker.ipynb`
   - Run all cells to see your learning dashboard
   - This will be empty initially

2. **Start with Module 1:**
   - Go to `notebooks/A1/Module_01/`
   - Open `01_introduction.ipynb`
   - Follow the 4-phase structure

3. **Complete Each Module:**
   - **Phase 1** (01_introduction.ipynb): Learn concepts with examples and audio
   - **Phase 2** (02_controlled_practice.ipynb): Complete exercises with feedback
   - **Phase 3** (03_meaningful_practice.ipynb): Write about your own life
   - **Phase 4** (04_communicative_practice.ipynb): Real communication tasks

4. **Mark Module Complete:**
   - At the end of Phase 4, uncomment and run the completion cell
   - This schedules your first review and updates the progress tracker

5. **Review Regularly:**
   - Check the progress tracker for due reviews
   - Complete review sessions on schedule
   - After Module 5, complete the consolidation review

### Learning Path

**Recommended pace:** 1-2 modules per week

- **Modules 1-5** (Weeks 1-3): Basic grammar foundations
  - Complete the consolidation review after Module 5
- **Modules 6-10** (Weeks 4-6): Expanding vocabulary and structures
  - Regular spaced repetition reviews

**Total time estimate:** 80-100 hours for complete A1 level

### Study Tips

1. **Study regularly:** 30-60 minutes daily > 4 hours once a week
2. **Complete all 4 phases:** Each phase builds on the previous
3. **Do the reviews:** Spaced repetition is crucial for retention
4. **Practice speaking:** Read exercises aloud, use the audio examples
5. **Personalize learning:** The meaningful practice phase is critical
6. **Track progress:** Use the progress tracker to stay motivated

## Module Descriptions

### Module 1: Verb "To Be"
Master am/is/are in positive, negative, and question forms. The foundation for all English grammar.

### Module 2: Personal Pronouns
Subject pronouns (I, you, he, she, it, we, they) and object pronouns (me, you, him, her, it, us, them).

### Module 3: Present Simple - Affirmative
Form positive statements with emphasis on third-person -s/es/ies rules.

### Module 4: Present Simple - Negatives and Questions
Use do/does for negatives and questions, including Wh-questions.

### Module 5: Articles and Demonstratives
Master a/an/the usage and this/that/these/those distinctions.

### Module 6: Nouns and Plurals
Regular and irregular plural forms, countable vs uncountable nouns.

### Module 7: Possessives
Possessive adjectives (my, your, his, her) and possessive 's.

### Module 8: Adjectives
Describing people, places, and things with proper adjective placement.

### Module 9: There Is/Are
Express existence and location with there is/there are constructions.

### Module 10: Prepositions
Place prepositions (in, on, at, under, behind) and time prepositions (in, on, at).

## Technical Details

### Feedback System

The `feedback_system.py` module provides:
- `ExerciseValidator`: Checks answers with various matching strategies
- `InteractiveExercise`: Creates fill-in-blank, multiple choice, and matching exercises
- `create_progress_bar()`: Visual progress indicators
- `display_hint()`: Collapsible hints for difficult exercises

### Audio Generator

The `audio_generator.py` module provides:
- `AudioGenerator`: Text-to-speech with multiple accents (US, UK, AU, IN)
- `create_pronunciation_card()`: Rich vocab cards with audio
- `create_sentence_audio()`: Audio for example sentences
- `create_conversation_audio()`: Dialogue audio with turn-taking

### Spaced Repetition

The `spaced_repetition.py` module implements:
- **Review intervals:** Day 1, 2, 4, 7, 14, 30, 60, 120
- **Adaptive scheduling:** Adjusts based on performance
- **Progress tracking:** JSON-based storage
- **Visual dashboard:** Shows due and upcoming reviews

## Expanding the Project

### Adding New Modules

Use the `generate_modules.py` script as a template:

1. Define module data in the `MODULES` dictionary
2. Run the script to generate all 4 phase notebooks
3. Manually enhance with detailed exercises and content
4. Test thoroughly before releasing

### Scaling to Full Curriculum

The system is designed to scale to **160 modules** (A1-C2):
- **A1**: 20 modules (current pilot covers 10)
- **A2**: 25 modules
- **B1**: 30 modules
- **B2**: 35 modules
- **C1**: 30 modules
- **C2**: 20 modules

See `English-Path.md` for the complete curriculum specification.

## Research Foundation

This project is based on:

- **Cambridge English Grammar Profile** (55 million word corpus analysis)
- **CEFR** (Common European Framework of Reference)
- **Global Scale of English** (Pearson)
- **Applied Linguistics Research** (Rod Ellis, Michael Long, etc.)
- **Cognitive Science** (spaced repetition, retrieval practice)

Key findings implemented:
- Explicit instruction has highest effect size (d=1.26)
- Spaced repetition increases retention by 200%
- Developmental sequences must be respected
- Practice should progress from controlled → communicative
- Feedback should be immediate for accuracy, delayed for fluency

## Contributing

Contributions welcome! Areas for improvement:

- **More exercises:** Each module could have 50+ exercises
- **Better audio:** Professional voice recordings
- **Gamification:** Points, badges, leaderboards
- **Adaptive difficulty:** Adjust based on performance
- **Mobile support:** Responsive design for smartphones
- **Additional modules:** Expand to A2, B1, B2, C1, C2
- **Video content:** Grammar explanations with animations
- **Community features:** Study groups, forums, peer review

## Future Enhancements

- [ ] Web-based interface (Streamlit/Dash)
- [ ] Database backend (SQLite/PostgreSQL)
- [ ] User authentication
- [ ] Cloud deployment
- [ ] Mobile app version
- [ ] Integration with language exchange platforms
- [ ] AI-powered feedback (LLM integration)
- [ ] Speech recognition for pronunciation practice
- [ ] Automated exercise generation
- [ ] Personalized learning paths

## License

MIT License - feel free to use, modify, and distribute.

## Acknowledgments

- **Cambridge University Press** for Grammar Profile research
- **Foreign Service Institute** for language learning timelines
- **Rod Ellis** for Focus on Form methodology
- **Michael Long** for Task-Based Language Teaching
- **Pienemann** for Processability Theory

## Author

Created as a portfolio project demonstrating:
- Educational technology development
- Jupyter notebook expertise
- Python programming
- Data visualization
- UX/UI design for learning
- Research-backed curriculum design

## Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub.

---

**Happy Learning!** 🚀📚

*This pilot project demonstrates a scalable, research-backed approach to language learning. With proper expansion, it could become a complete English learning platform covering all proficiency levels.*
