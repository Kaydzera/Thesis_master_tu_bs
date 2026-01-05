# AI Agent Instructions for Bilevel Optimization Thesis (TU Braunschweig)

## Project Overview
Master thesis on bilevel optimization using the **official TU Braunschweig LaTeX Corporate Design** template. The research focuses on a branch-and-bound algorithm for knapsack-scheduling problems where a leader maximizes makespan by selecting jobs within budget, and a follower minimizes makespan by optimally scheduling selected jobs.

## Project Structure
```
main.tex              # Main document with TUBS template configuration
abstract.tex          # Abstract (referenced in main.tex)
chapters/*.tex        # 6 modular chapters (intro → conclusion)
code/                 # Python snippets for inclusion (e.g., bound_computation_example.py)
figures/              # Plots and diagrams
data/                 # Experimental results to import as LaTeX tables
bibliography.bib      # BibTeX references (uses biblatex/biber)
tubsCD/              # TU Braunschweig template files (DO NOT EDIT)
logos/               # University and institute logos
```

## LaTeX Build Workflow (CRITICAL)
**IMPORTANT:** This template requires **XeLaTeX**, not pdfLaTeX!

**Build sequence:**
```bash
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex
```

**VS Code:** Configured to use XeLaTeX automatically
- `Ctrl+Alt+B` - Build PDF
- `Ctrl+Alt+V` - View PDF

**Why XeLaTeX?** TUBS template uses `fontspec` package for corporate design fonts, which requires XeLaTeX or LuaLaTeX.

## Template Customization
**Edit these in [main.tex](main.tex) (lines 6-22):**
- `\myName` - Your full name
- `\myEMail` - Contact email
- `\myInstituteName` - Institute/department
- `\myInstituteImg` - Optional logo path (e.g., `logos/FK1/informatik.pdf`)
- `\myPaperTitle` - Thesis title (must match Prüfungsamt records)
- `\myReviewerOnePers` / `\myReviewerOneInst` - First reviewer
- `\myReviewerTwoPers` / `\myReviewerTwoInst` - Second reviewer (optional)
- `\mySupervisorPers` / `\mySupervisorInst` - Supervisor (optional)
- `\myCourseOfStudies` - Degree program
- `\myMatriculationNumer` - Student ID
- `\mySubmissionDate` - Submission date (defaults to `\today`)

## Template Features
**Automatic sections (managed by template):**
- Title page with TUBS corporate design
- Optional acknowledgement (`\myAcknowledgement`)
- Abstract (from [abstract.tex](abstract.tex))
- Optional preface (`\myPreface`)
- Table of contents (auto-generated)
- List of figures and tables (at end)
- Statutory declaration / Eidesstattliche Erklärung (required by university)

**Page numbering:**
- Roman numerals (i, ii, iii...) for front matter
- Arabic (1, 2, 3...) for main chapters
- Roman capitals (I, II, III...) for appendix (if used)

## LaTeX Packages & Conventions
**Key packages already configured:**
- Bibliography: `biblatex` with `biber` backend (NOT bibtex!)
- Algorithms: `algorithm`, `algpseudocode`
- Code listings: `listings` (pre-configured for Python)
- Math: `amsmath`, `amssymb`, `amsthm`
- Theorem environments: `definition`, `theorem`, `lemma`, `example`

**Math notation standards:**
- Leader variables: $x_i$ (job quantities)
- Follower variables: $y_{ijk}$ (job $j$ of type $i$ on machine $k$)
- Makespan: $C_{\max}$ or $C_{\max}^*(x)$ for optimal
- Ceiling knapsack bound: $\sum d_i \lceil x_i / m \rceil$

## Critical Domain Knowledge
### Bilevel Problem Structure
1. **Upper level (Leader):** Maximize makespan subject to budget $\sum p_i x_i \leq B$
2. **Lower level (Follower):** Minimize makespan via optimal scheduling

### Branch-and-Bound Algorithm
**Upper bound formula:**
$$\text{UB} = \sum_{i=1}^{d} d_i \lceil x_i / m \rceil + \max \sum_{i=d+1}^{n} d_i \lceil y_i / m \rceil$$
- First term: committed contribution from decided items
- Second term: ceiling knapsack relaxation over remaining items
- Pruning: If $\text{UB}(x) \leq C_{\max}^{\text{incumbent}}$, discard node

## Common Tasks
**Add references:** 
1. Edit [bibliography.bib](bibliography.bib)
2. Cite with `\cite{key}` in LaTeX
3. Rebuild with biber (NOT bibtex!)

**Include code:**
```latex
\lstinputlisting[caption={Description},label={lst:label}]{code/filename.py}
```

**Add experimental tables:**
Use `booktabs` package (`\toprule`, `\midrule`, `\bottomrule`)

**Change language:**
Set `language=german` in `\documentclass` options in [main.tex](main.tex)

## Important Gotchas
- **XeLaTeX only:** pdflatex will fail with font errors
- **Biber not BibTeX:** Template uses biblatex which requires `biber` command
- **Template files:** Never edit files in `tubsCD/` folder
- **Chapter edits:** Changes to `chapters/*.tex` need main.tex rebuild to see in PDF
- **Class path:** Document class is `tubsCD/tubscd`, not just `tubscd`
- **University compliance:** Check Prüfungsamt requirements - they can change over time

## TODO Tracking (from [README.md](README.md))
- [ ] Fill experimental results in Chapter 5 (tables with runtime, nodes, pruning rates)
- [ ] Add figures (runtime plots, pruning charts) to `figures/`
- [ ] Export Python experiment data to LaTeX tables
- [ ] Expand bibliography with domain-specific references
- [ ] Customize title page with actual reviewer/supervisor information
- [ ] Add institute logo if available
