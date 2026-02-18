# Travel Protection Structure Strategy

**Role:** Staff Product Manager  
**Candidate:** Roman Babunts

## Overview
This repository contains the test assignment solution for the Travel Protection product strategy at DiscoverCars.com.

## Links

*   **Test Assignment Task:** [Discover Cars Test Task.md](Discover%20Cars%20Test%20Task.md)
*   **Presentation (Slides):** [View on GitHub Pages](https://romargera.github.io/DiscoverCarsPresentation/)

## Repository Structure
*   `slides.md`: The main presentation content (Markdown / **The Spec**).
*   `index.html`: Reveal.js entry point (**Code Evaluation**).
*   `create_pptx_clean.py`: Custom pipeline to handle **Drift Detection** (Visual fidelity drift).
*   `Execution_Plan.md`: Detailed breakdown of the execution strategy.
*   `RiskMitigation.md`: Risk analysis and mitigation strategies.

## Engineering Principle: Content as Code
This project was built using a **Spec → Evaluation → Drift Detection** framework:
1.  **Spec:** Strategy defined in `slides.md` as the single source of truth.
2.  **Code Evaluation:** Continuous CI/CD-like rendering via local server to validate UX.
3.  **Drift Detection Example:** 
    *   **Visual Drift:** Automated screenshot pipeline (`create_pptx_clean.py`) to mitigate PDF rendering artifacts.
    *   **Deployment Drift:** Cache-busting implementation to ensure Production (GitHub Pages) matches Development (Localhost).
