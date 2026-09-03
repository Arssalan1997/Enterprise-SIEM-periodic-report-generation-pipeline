# SIEM Periodic Report Generation Pipeline

> **Enterprise-grade automation system** for generating SIEM security reports with sophisticated matrix-based algorithm architecture. Reduces manual report generation from **10+ hours to minutes** while eliminating human error.

## Overview

This is a production-ready **data engineering pipeline** that automates periodic Excel report generation for Security Operations Center (SOC) SIEM environments. The system processes network security data across monthly and quarterly cycles with an elegant, modular orchestration architecture.

**Key Achievement:** Transforms manual, error-prone spreadsheet operations (previously handled by SOC analysts) into a fully automated, formula-regenerating pipeline—demonstrating enterprise-grade problem solving, system design, and operational maturity.

---

## Features

### Core Capabilities

- **Dual-Mode Report Generation**
  - **Monthly Reports:** Aggregates 4-5 weeks of SIEM data from weekly report files
  - **Quarterly Reports:** Consolidates 3 months of monthly data with dynamic cross-sheet calculations

- **Matrix-Based Dynamic Formula System**
  - Adaptive coordinate mapping algorithm handles variable data dimensions
  - Automatically regenerates all SUM formulas when column/row counts change
  - Zero manual formula adjustment required after data insertion

- **Multi-Source Data Consolidation**
  - Aggregates data from heterogeneous input files (weekly/monthly reports)
  - Dynamic rule-name matching across sheets and files
  - Rule-based aggregation scoring system

- **Enterprise-Grade Error Handling**
  - Granular validation with actionable diagnostic feedback
  - Detailed reporting of:
    - Missing aggregation values (with SIEM lookup guidance)
    - Unmapped sheets (with mapping file update instructions)
    - Data transfer failures (with source/destination analysis)
  - Timestamped logging and archival of all report generations

- **Streamlit Web Interface**
  - Minimal, intuitive UI for data input and monitoring
  - Real-time progress tracking across 8 orchestration phases
  - Direct file download and validation feedback

---

## Architecture

### Hierarchical Modular Structure

The system is built on **four layers of abstraction** with 35 modules (4,577 lines of Python):

```
SIEM-Periodic-Report-Generation-Pipeline/
├── introduction.py                          # Entry point
├── main.py                                  # Orchestrator (Front-End ↔ Back-End bridge)
│
├── monthly/                                 # Monthly report generation package
│   ├── monthly_class_handler.py             # Phase orchestrator (inherits base operations)
│   ├── monthly_class.py                     # Core worksheet iterator & formula engine
│   ├── transfer_data_from_weekly_to_monthly_class.py    # Weekly→Monthly data pipeline
│   ├── transfer_data_from_aggregation_list_to_monthly_report_class.py  # Aggregation injection
│   ├── aggregation_list_sheet_class.py      # Aggregation file parser
│   ├── weekly_to_be_transferred_class.py    # Weekly report wrapper
│   └── make_report_info.py                  # Monthly report metadata builder
│
├── quarterly/                               # Quarterly report generation package
│   ├── quarterly_class_handler.py           # Phase orchestrator (extends Monthly handler)
│   ├── quarterly_class.py                   # Quarterly-specific worksheet operations
│   ├── transfer_data_from_monthly_to_quarterly_class.py  # Monthly→Quarterly aggregation
│   ├── monthly_to_be_transferred_class.py   # Monthly report wrapper
│   └── make_report_info.py                  # Quarterly metadata builder
│
├── pages/                                   # Streamlit UI modules (14 pages)
│   ├── 1-determine kind of report.py        # Report type selection
│   ├── 2-determine number of last and current weeks of monthly report.py
│   ├── 3-upload aggregation file.py
│   ├── 4-upload last month report file.py
│   ├── 5-receive date ranges.py             # Persian calendar date input
│   ├── 6-upload weekly report files.py
│   ├── 7-do the report for monthly version.py           # Monthly orchestrator trigger
│   ├── 8-display report info for monthly version.py     # Monthly validation output
│   ├── 9-receive report name of quarterly version.py    # Persian season name input
│   ├── 10-upload last season report file.py
│   ├── 11-receive included month names.py               # Persian month names
│   ├── 12-upload monthly report files.py
│   ├── 13-do the report for quarterly version.py        # Quarterly orchestrator trigger
│   └── 14-display report info for quarterly version.py  # Quarterly validation output
│
├── archive/                                 # Successful report archival (timestamped)
├── files/                                   # Failed report staging (timestamped)
├── logs/                                    # Execution error logs
├── mappings/                                # Sheet-name mapping files
│   ├── monthly_to_weekly_mapping.xlsx       # Resolves naming inconsistencies
│   └── quarterly_to_monthly_mapping.xlsx
│
├── CONSTANTS.py                             # Application configuration
├── handle_errors.py                         # Error handling utilities
├── specify_current_time.py                  # Timestamp management
├── requirements.txt                         # Dependencies
└── SIEMReportsAutomationApplication.bat     # Windows launcher
```

### System Design Sophistication
---
#### Modular Architecture (Separation of Concerns)

```
┌─────────────────────────────────────────┐
│         STREAMLIT FRONTEND (pages/)     │  14 UI modules
│    User inputs, file uploads, download  │  
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│         ORCHESTRATION LAYER             │  main.py + introduction.py
│    Phase-based pipeline coordination    │  
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│  MONTHLY/QUARTERLY HANDLERS             │  Handler classes
│  Template method pattern execution      │  
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│  CORE PROCESSING CLASSES                │  Data transfer classes
│  Weekly→Monthly, Monthly→Quarterly      │  Matrix algorithm
│  Data aggregation & transformation      │  
└─────────────────────────────────────────┘

```

### The Matrix Algorithm (Core Innovation)

The **matrix-based coordinate mapping system** is the architectural cornerstone:

1. **Dynamic Dimensionality:** Handles variable column counts (4 or 5 weeks/months)
2. **Coordinate Persistence:** Maintains a matrix of cell references `[B2→C2, D2→F2, ...]`
3. **Formula Regeneration:** On each data import, recalculates all SUM formula ranges
4. **Linear Algebra Application:** Uses matrix indexing for scalable, adaptive automation

**Result:** Zero manual formula updates across report regenerations—a powerful demonstration of algorithmic thinking applied to real-world spreadsheet automation.

---

### Execution Architecture: Phase-Based Orchestration

The system executes through **6 sequential phases**, coordinated by handler classes:

```python
# main.py orchestration flow
Phase 1: operations_before_iterations_on_worksheets()     (4-18%)
Phase 2: operations_of_iterations_on_worksheets()         (17-40%)
Phase 3: operations_after_iterations_on_worksheets()      (39-59%)
Phase 4: save_file_operation_before_select_data_phase()   (58-81%)
Phase 5: operation_of_select_data()                       (80-93%)
Phase 6: save_final_file_operation_after_select_data_phase() (92-100%)
```

**OOP Design Pattern:** Base handler class (`HandlerOfMainSheetOfMonthlyReport`) defines phase-based template. Quarterly handler (`HandlerOfMainSheetOfQuarterlyReport`) extends via inheritance, demonstrating **multi-layer polymorphism** while maintaining DRY principles.

---

### Data Flow Architecture

#### Monthly Report Pipeline
```
SIEM Weekly Reports (*.xlsx)
    ↓
[Weekly Report Parser] → Extract rule names & counts
    ↓
[Matrix Algorithm] → Determine column mapping (4 or 5 weeks)
    ↓
[Data Consolidator] → Merge weeks 1,3 and 2,4,5 data
    ↓
[Aggregation Injector] → Cross-reference rule names with aggregation file
    ↓
[Formula Regenerator] → Rebuild SUM formulas for new dimensions
    ↓
Monthly Report (Updated *.xlsx)
```

#### Quarterly Report Pipeline
```
Monthly Reports (3 files, *.xlsx)
    ↓
[Monthly Report Parser] → Extract aggregated data
    ↓
[Month Name Mapper] → Apply Persian calendar labels
    ↓
[Data Consolidator] → Merge 3 months into 3 columns
    ↓
[Formula Regenerator] → Create quarterly-level calculations
    ↓
Quarterly Report (Updated *.xlsx)
```

---

## Technologies & Packages

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Manipulation** | `openpyxl` (3.1.5) | Read/write Excel XLSX files programmatically |
| **Excel Interaction** | `xlwings` (0.36.9) | Live Excel manipulation with formula preservation |
| **Data Processing** | `pandas` (3.0.3) | Data frame operations & Streamlit integration |
| **Web Interface** | `streamlit` (1.59.2) | Interactive UI with state management |
| **Error Handling** | `returns` (0.28.0) | Functional error handling (Result types) |
| **Data Validation** | `numpy` (2.4.6) | Numerical operations & validation |
| **Environment** | `python-dateutil` (2.9.0) | Date/time operations (Persian calendar support) |

---

## Scale & Complexity Metrics

| Metric | Value | Significance |
|--------|-------|--------------|
| **Total Lines of Code** | 4,577 | Substantial enterprise application |
| **Number of Modules** | 35 files | Sophisticated modular architecture |
| **Max Single File** | 974 lines | `transfer_data_from_weekly_to_monthly_class.py` |
| **Package Structure** | 3 packages + entry point | Professional separation of concerns |
| **UI Pages** | 14 Streamlit modules | Comprehensive, guided user workflows |
| **Execution Phases** | 6 sequential stages | Detailed orchestration control: initialization → iteration → post-processing → save → data selection → finalization |

---

## Key Competencies Demonstrated

### 1. System Design & Architecture
- **Modular Structure:** Clear separation between monthly/quarterly logic and UI orchestration
- **Scalability:** Report-agnostic core enables adaptation to diverse data scenarios
- **Separation of Concerns:** Data import, transformation, and output are isolated

### 2. OOP Fundamentals
- **Inheritance & Polymorphism:** Quarterly handler extends Monthly handler base class
- **Encapsulation:** Phase-based methods hide complex iteration logic
- **Composition:** Data transfer classes wrap source/destination file handling

### 3. Algorithmic Thinking
- **Matrix-Based Coordination:** Linear algebra applied to dynamic spreadsheet updates
- **Dynamic Dimensionality:** Algorithm adapts to 4 or 5 column configurations
- **Formula Persistence:** Elegant solution to maintaining formula relationships across data reshaping

### 4. Operational Maturity
- **Comprehensive Error Reporting:** Users get actionable feedback for each failure type
- **Timestamped Logging:** All generations tracked for audit/troubleshooting
- **Archival Strategy:** Successful/failed reports organized by execution timestamp
- **Data Privacy:** Configurable anonymization for sensitive SIEM data

---

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/Arssalan1997/SIEM-periodic-report-generation-pipeline.git
cd SIEM-periodic-report-generation-pipeline

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

**Option 1: Windows (Batch File)**
```bash
SIEMReportsAutomationApplication.bat
```

**Option 2: Streamlit CLI**
```bash
streamlit run introduction.py
```

The application will open at `http://localhost:8501`

### Basic Workflow

#### Monthly Report Generation
1. **Start Application** → Click "Start"
2. **Select Report Type** → Choose "Monthly"
3. **Specify Weeks** → Select 4 or 5 weeks (depends on month)
4. **Upload Aggregation File** → Upload `Aggregation List.xlsx`
5. **Upload Previous Month Report** → Upload last month's output
6. **Enter Date Ranges** → Input Persian calendar week boundaries
7. **Upload Weekly Reports** → Select corresponding weekly SIEM exports
8. **Execute** → Click "Start Doing The Report"
9. **Download** → Retrieve generated monthly report

#### Quarterly Report Generation
1. **Select Report Type** → Choose "Quarterly"
2. **Enter Report Name** → Persian season identifier (e.g., "04 تابستان")
3. **Upload Previous Season Report** → Last quarter's output
4. **Enter Month Names** → Persian calendar month labels
5. **Upload Monthly Reports** → Select 3 monthly report files (specify week counts each)
6. **Execute & Download** → Process and retrieve quarterly report

---

## Output & Validation

### Generated Report Structure

**Monthly Report File** (40+ sheets)
- Multiple worksheets with data aggregation tables
- 4 or 5 numerical columns (week counts)
- `Total` & `Total*Aggregation` summary columns
- Dynamic SUM formulas at bottom of each sheet
- Anonymized rule names and values

**Quarterly Report File** (40+ sheets)
- 1st sheet: Overall statistics (calculated from other sheets)
- 3 numerical columns (one per input month)
- `Total` column with aggregated values
- Dynamic formulas for quarterly-level calculations

### Post-Generation Validation Report

After completion, the system displays:
- ✅ **Successfully Updated Sheets:** Count of transformed worksheets
- ⚠️ **Missing Aggregation Values:** Rules not found in aggregation file (requires SIEM lookup)
- ❌ **Failed Data Transfers:** Sheets with mapping/compatibility issues
- 📋 **Mapping Discrepancies:** New sheets needing mapping file updates

**Actionable Feedback:** Each issue includes clear instructions for resolution.

---

## Extensibility & Generalizability

This system is **report-agnostic** and easily adaptable to:
- Different SIEM platforms (by modifying input file structure)
- Bi-weekly or tri-monthly reporting cycles
- Non-security domains (financial reports, operational metrics, etc.)
- Any hierarchical data collection scenario with monthly/quarterly aggregation

**Core Principle:** Algorithm and orchestration remain unchanged; only data sources and sheet names require customization.

---

## Configuration

Edit `CONSTANTS.py` for:
- Directory paths for input/output files
- Archive/failure file staging locations
- Log file locations
- Timestamp formats

Edit mapping files (`mappings/` directory) to:
- Add new sheet name correspondences
- Support additional report formats
- Handle new SIEM data exports

---

## Error Handling & Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Missing aggregation values (0 scores) | New rules in SIEM data | Check SIEM platform for new rule names, add to aggregation file |
| Sheets remained unchanged | Sheet name mismatch | Verify sheet names, update mapping file |
| Data transfer failed | Column/row count mismatch | Check input file structure, ensure consistency |
| Formula errors in output | Matrix calculation error | Review data import phase, check for sparse rows |

### Logging

All execution errors logged to `logs/` directory with:
- Timestamp of execution
- Phase where error occurred
- Detailed error description
- Stack trace for debugging

---

## License

MIT License - See `LICENSE` file for details.

---

## Author

**Arssalan1997** — Data Scientist

This project represents sophisticated **data engineering** focused on system design, modular architecture, and operational thinking. It demonstrates the ability to solve real enterprise problems with clean, maintainable, production-grade code.

---

## Repository Stats

- **Language:** Python (99.8%)
- **Created:** August 2026
- **Size:** 93 KB
- **Lines of Code:** 4,577
- **Modules:** 35 files
- **License:** MIT
