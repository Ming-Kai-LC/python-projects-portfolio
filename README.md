# Python Projects Portfolio

A collection of Python data analysis and machine learning projects for learning and practice. Each project is organized in its own directory with dedicated notebooks, data, and documentation.

## 📁 Folder Structure

```
python-projects-portfolio/
├── projects/                    # All notebook projects
│   ├── personal-finance-tracker/
│   │   ├── personal_finance_tracker.ipynb
│   │   ├── data/               # Project-specific data files
│   │   └── README.md           # Project documentation
│   ├── klse-stock-screener/
│   │   ├── klse_stock_screener.ipynb
│   │   ├── data/               # Cached stock data
│   │   └── README.md           # Project documentation
│   └── [future-projects]/      # Add new projects here
├── shared/                      # Shared utilities and modules (optional)
├── venv/                        # Virtual environment (gitignored)
├── .gitignore
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 📚 Projects

### 1. Personal Finance Tracker
**Location:** `projects/personal-finance-tracker/`

An interactive Jupyter notebook that teaches data analysis fundamentals through personal finance tracking.

**Key Features:**
- Expense tracking by category
- Time-based spending analysis
- Interactive visualizations (pie charts, line graphs, bar charts)
- CSV data persistence
- Automated insights generation

**Skills Covered:**
- pandas DataFrames and data manipulation
- matplotlib and seaborn visualizations
- DateTime operations
- Data aggregation and grouping
- File I/O operations

[View Project Details →](projects/personal-finance-tracker/README.md)

---

### 2. KLSE Stock Screener & Analyzer
**Location:** `projects/klse-stock-screener/`

A comprehensive Malaysian stock market (KLSE/Bursa Malaysia) analysis tool with fundamental analysis, technical indicators, portfolio tracking, and stock screening capabilities.

**Key Features:**
- Fetch real-time Malaysian stock data using yfinance (free & legal!)
- Fundamental analysis (PE ratio, market cap, dividends, EPS)
- Technical indicators (RSI, MACD, Moving Averages, Bollinger Bands)
- Custom stock screener with multiple filters
- Portfolio tracking and performance analysis
- Sector comparison and benchmarking against KLSE index
- Interactive visualizations with plotly

**Skills Covered:**
- API integration (yfinance for Yahoo Finance data)
- Financial data analysis and interpretation
- Technical analysis implementation (pandas-ta)
- Time series analysis for stock prices
- Portfolio management and risk assessment
- Interactive dashboards with plotly
- Data caching and optimization

**Technologies:**
- yfinance (stock data API)
- pandas-ta (technical analysis)
- plotly (interactive visualizations)
- pandas, matplotlib, seaborn

[View Project Details →](projects/klse-stock-screener/README.md)

---

### 3. Malaysian Stock Technical Analysis - Learning Journey
**Location:** `projects/malaysia-stock-technical-analysis/`

A comprehensive, beginner-friendly guide to learning technical analysis using real Malaysian stock data. This project focuses on UUE (Universal Unity Equity) stock as a practical case study to master technical analysis concepts through 6 progressive Jupyter notebooks.

**Key Features:**
- Complete beginner-friendly technical analysis course
- 6 progressive learning notebooks (Introduction → Advanced Dashboard)
- Real-time Malaysian stock data (UUE.KL and others)
- Interactive charts and visualizations
- Hands-on exercises and practice opportunities
- Comprehensive analysis dashboard combining all indicators
- Step-by-step learning with clear explanations

**What You'll Learn:**
- Technical analysis fundamentals and principles
- Reading and interpreting candlestick charts
- Support and resistance level identification
- Moving Averages (SMA and EMA) for trend analysis
- Golden Cross and Death Cross patterns
- RSI (Relative Strength Index) for momentum
- MACD (Moving Average Convergence Divergence)
- Volume analysis and confirmation techniques
- Building a complete technical analysis framework

**Skills Covered:**
- Technical analysis concepts and indicators
- Time series data visualization
- Pattern recognition in price charts
- Multi-indicator analysis and confirmation
- Trading signal generation
- Risk assessment and decision making
- Creating interactive financial dashboards

**Technologies:**
- yfinance (free stock data)
- pandas-ta (technical analysis library)
- plotly (interactive charts)
- pandas, numpy, matplotlib, seaborn

**Perfect For:**
- Complete beginners to technical analysis
- Investors wanting to learn Malaysian stock analysis
- Students building financial analysis skills
- Anyone interested in data-driven investment decisions

[View Project Details →](projects/malaysia-stock-technical-analysis/README.md)

---

## 🚀 Getting Started

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-projects-portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Projects

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a project**
   - Browse to `projects/<project-name>/`
   - Open the `.ipynb` notebook file
   - Run cells sequentially to follow along

### Alternative: JupyterLab

For a more modern IDE-like experience:
```bash
jupyter lab
```

## ➕ Adding New Projects

To add a new notebook project to this portfolio:

1. **Create project directory**
   ```bash
   mkdir projects/your-project-name
   mkdir projects/your-project-name/data
   ```

2. **Create your notebook**
   - Place your `.ipynb` file in the project directory
   - Use the `data/` subfolder for any datasets (they're gitignored)

3. **Add project README**
   ```bash
   # Create projects/your-project-name/README.md
   # Document what your project does, requirements, and usage
   ```

4. **Update main README**
   - Add your project to the "Projects" section above
   - Include a brief description and skills covered

5. **Update requirements.txt** (if needed)
   ```bash
   pip freeze > requirements.txt
   ```

## 📦 Requirements

- **Python:** 3.8 or higher
- **Core Libraries:**
  - pandas >= 2.0.0
  - matplotlib >= 3.7.0
  - seaborn >= 0.12.0
  - jupyter >= 1.0.0
  - notebook >= 7.0.0
- **Additional Libraries:**
  - yfinance >= 0.2.30 (stock market data)
  - pandas-ta >= 0.3.14 (technical analysis)
  - plotly >= 5.14.0 (interactive visualizations)

See `requirements.txt` for complete dependency list.

## 💡 Tips

- **Keep notebooks organized:** Each project should be self-contained in its directory
- **Use data/ folders:** Store generated data files in project-specific `data/` directories
- **Document your work:** Add markdown cells explaining your thought process
- **Version control:** Commit notebooks with outputs cleared for cleaner diffs
- **Shared code:** Put reusable utilities in the `shared/` directory

## 🎯 Project Ideas

Looking for inspiration? Consider these project ideas:

- **Data Analysis:** Stock price analysis, weather patterns, sports statistics
- **Machine Learning:** Classification problems, regression models, clustering
- **Web Scraping:** News aggregation, price tracking, social media analysis
- **Natural Language Processing:** Sentiment analysis, text classification, summarization
- **Computer Vision:** Image classification, object detection, style transfer
- **Time Series:** Sales forecasting, trend analysis, anomaly detection

## 📖 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Jupyter Notebook Basics](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Kaggle Learn](https://www.kaggle.com/learn) - Free courses and datasets

## 📄 License

MIT License - feel free to use and modify for your own learning!

## 🤝 Contributing

This is a personal learning portfolio, but suggestions and improvements are welcome! Feel free to:
- Report issues
- Suggest new project ideas
- Share your own implementations

---

**Happy Learning!** 🎉
