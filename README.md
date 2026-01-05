# Master Thesis: Branch-and-Bound for Bilevel Knapsack-Scheduling Optimization
## TU Braunschweig Template

This thesis uses the official TU Braunschweig LaTeX Corporate Design template.

## Structure

```
├── main.tex                    # Main document (customize at top)
├── abstract.tex                # Abstract
├── chapters/                   # Individual chapters
│   ├── 01_introduction.tex
│   ├── 02_problem_formulation.tex
│   ├── 03_methodology.tex
│   ├── 04_implementation.tex
│   ├── 05_experiments.tex
│   └── 06_conclusion.tex
├── figures/                    # Figures and plots
├── code/                       # Code snippets for inclusion
├── data/                       # Experimental results
├── bibliography.bib            # References
├── tubsCD/                     # TU Braunschweig template files (don't edit)
└── logos/                      # University logos

```

## Compiling

### Using VS Code with LaTeX Workshop

1. Open `main.tex`
2. Press `Ctrl+Alt+B` to build
3. View PDF with `Ctrl+Alt+V`

### Using Command Line

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Customization

Edit the user parameters at the top of `main.tex`:
- Your name, email, matriculation number
- Institute name and logo
- Reviewers and supervisors
- Submission date

## Notes

- Template complies with TU Braunschweig requirements
- Includes statutory declaration (Eidesstattliche Erklärung)
- Automatic table of contents, figures, and tables
- Uses biblatex with biber backend
