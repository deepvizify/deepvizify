
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** data-canvas-x-main
- **Date:** 2026-03-07
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001 Run cleaning analysis and apply Mean fill on a numeric column
- **Test Code:** [TC001_Run_cleaning_analysis_and_apply_Mean_fill_on_a_numeric_column.py](./TC001_Run_cleaning_analysis_and_apply_Mean_fill_on_a_numeric_column.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Cleaning tab not found on dashboard page; no interactive element with id starting 'ts-tab-' present.
- Start Analysis button (id='ts-start-analysis') not found on page.
- Dashboard UI remains in loading state — central spinner visible and only notification elements are interactive.
- Unable to verify 'Missing values' text because cleaning workflow controls are not available.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/016812c0-d2e7-47e9-91f6-af7dd50cd352
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002 Apply Mean fill and verify completeness metric updates
- **Test Code:** [TC002_Apply_Mean_fill_and_verify_completeness_metric_updates.py](./TC002_Apply_Mean_fill_and_verify_completeness_metric_updates.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Central loading spinner is present and no interactive elements are available on the dashboard, preventing access to the Cleaning tab or analysis controls.
- Multiple attempts to wait and click the Cleaning tab failed (at least 2 click attempts and several waits), indicating the UI is unresponsive.
- Stale or non-interactable element indices were encountered when attempting to click the Cleaning tab, preventing interaction with required controls.
- Dashboard content required to perform 'Mean fill' (Start Analysis, fix action dropdown, Apply button, and Completeness metric) is not reachable because the SPA did not finish rendering.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/0c274143-f6fc-4c55-ad23-1b28d9611e70
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003 Detect duplicates and remove them
- **Test Code:** [TC003_Detect_duplicates_and_remove_them.py](./TC003_Detect_duplicates_and_remove_them.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard did not render: central loading spinner or login inputs are present and there are 0 interactive elements on the /dashboard page, preventing further interaction.
- Cleaning controls not available: no elements matching the Cleaning tab (ts-tab-...) or Start Analysis (id='ts-start-analysis') were present to click and start analysis.
- Repeated sign-in attempts and waits did not transition the app to a usable dashboard state; the UI remained non-interactive after multiple retries.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/ced23033-6526-401c-a5c3-d7cfeb8eab3a
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005 Prevent Mean fill on a non-numeric column
- **Test Code:** [TC005_Prevent_Mean_fill_on_a_non_numeric_column.py](./TC005_Prevent_Mean_fill_on_a_non_numeric_column.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard not reachable: loading spinner remains visible and blocks interaction, preventing the dashboard UI from rendering fully.
- Cleaning tab not clickable: attempts to click the Cleaning tab failed because the element was not interactable or its index became stale.
- Start Analysis and fix-action dropdown not available: necessary controls (Start Analysis, fix-action dropdown) were not present or interactable, so Mean fill could not be selected.
- Repeated login attempts and waits did not change the app state: multiple sign-in attempts returned a notification but the page stayed in loading or returned to login, preventing progress.
- Required UI elements for completing the test (ts-start-analysis, ts-tab-cleaning, fix-action dropdown) were not present or interactable on the accessible page.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/57042306-25b3-46be-b5ed-57f823be854e
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009 EDA summary table loads from Dashboard
- **Test Code:** [TC009_EDA_summary_table_loads_from_Dashboard.py](./TC009_EDA_summary_table_loads_from_Dashboard.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/310f3e3f-60f8-4139-8746-e83f1e4dfbdc
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010 View numeric column distribution histogram in EDA
- **Test Code:** [TC010_View_numeric_column_distribution_histogram_in_EDA.py](./TC010_View_numeric_column_distribution_histogram_in_EDA.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard did not render after successful sign-in; only a central loading spinner is visible on the /dashboard page.
- EDA tab not found on the page after sign-in and waiting; no navigation elements with the 'ts-tab-' prefix are present.
- Histogram element could not be verified because the EDA area was not reachable.
- Two sign-in attempts were performed but neither produced the expected dashboard UI for further testing.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/e1e98997-72f6-4b5e-ba29-9f97673231fb
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC012 Correlation matrix heatmap view opens and renders
- **Test Code:** [TC012_Correlation_matrix_heatmap_view_opens_and_renders.py](./TC012_Correlation_matrix_heatmap_view_opens_and_renders.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/9efef015-3d0c-49b2-a089-3d7f3a402ea9
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC014 EDA shows 'No data' when dataset is not loaded
- **Test Code:** [TC014_EDA_shows_No_data_when_dataset_is_not_loaded.py](./TC014_EDA_shows_No_data_when_dataset_is_not_loaded.py)
- **Test Error:** Waited for 5 seconds
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/72be5645-dfa0-438d-9f06-c2a478534b49
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC016 Render a bar chart after selecting X and Y columns
- **Test Code:** [TC016_Render_a_bar_chart_after_selecting_X_and_Y_columns.py](./TC016_Render_a_bar_chart_after_selecting_X_and_Y_columns.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/02fd38a2-7006-49ce-97d8-9ceeb2cf761e
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC019 Export chart as PNG after selecting X and Y columns
- **Test Code:** [TC019_Export_chart_as_PNG_after_selecting_X_and_Y_columns.py](./TC019_Export_chart_as_PNG_after_selecting_X_and_Y_columns.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard page did not load after sign-in; the app remains on the login page (http://localhost:5173/login).
- Visualization tab (ts-tab-*) is not present on the page after sign-in, so chart configuration controls are unavailable.
- X/Y column dropdowns and chart-type options could not be located because the dashboard content did not render.
- Export Chart action could not be found or initiated because a configured chart and dashboard UI were not accessible.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/ae914d0a-4024-4cd5-82dc-c7282a229409
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC020 Validation error when Y column is non-numeric for Bar chart
- **Test Code:** [TC020_Validation_error_when_Y_column_is_non_numeric_for_Bar_chart.py](./TC020_Validation_error_when_Y_column_is_non_numeric_for_Bar_chart.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard page could not be reached: after multiple sign-in attempts the application returned to the login page instead of providing the dashboard UI.
- Visualization controls (ts-tab-visualization, X/Y dropdowns, chart type options) were not present on any observed page, preventing the validation scenario from being executed.
- Sign-in was attempted twice and further identical attempts are disallowed by test constraints, preventing additional login attempts to reach the dashboard.
- No UI element on the current page provides a path to the dashboard without re-authenticating, preventing natural navigation as required by the test.
- Verification that selecting a non-numeric Y column with the Bar chart shows the message 'Y must be numeric' could not be completed because the dashboard and chart controls were not reachable.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/3ad75966-7650-46f7-9024-13348c9c557d
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC024 Generate AI insights from Analytics tab and display insights panel
- **Test Code:** [TC024_Generate_AI_insights_from_Analytics_tab_and_display_insights_panel.py](./TC024_Generate_AI_insights_from_Analytics_tab_and_display_insights_panel.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Dashboard main content did not render after successful sign-in; a centered loading spinner persists and blocks interaction.
- Analytics tab elements (ids/testids with prefix 'ts-tab-') were not present or interactable, preventing navigation to the Analytics flow.
- 'AI insights' panel could not be verified because the insights generation flow (Generate Insights) was unreachable due to the loading state.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/c0a0decb-b9bc-4800-80ca-979e5642aea7
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC025 Generate AI insights shows readable insights text content
- **Test Code:** [TC025_Generate_AI_insights_shows_readable_insights_text_content.py](./TC025_Generate_AI_insights_shows_readable_insights_text_content.py)
- **Test Error:** TEST FAILURE

ASSERTIONS:
- Analytics tab or 'Generate Insights' button not present on the dashboard after successful sign-in; required controls are unavailable.
- Dashboard remained on a loading spinner and did not render the interactive analytics UI needed to generate or view insights.
- Repeated authentication attempts and waits did not reveal the analytics UI; the app intermittently returned to the login form or stayed stuck rendering.
- Unable to verify presence of the text 'Insights' or any generated human-readable insights because the UI elements to trigger/ view insights were not reachable.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/c2f6bb6e-1c3f-4912-a22a-be30574af239
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC026 Ask a question in Chart Bot and display AI answer
- **Test Code:** [TC026_Ask_a_question_in_Chart_Bot_and_display_AI_answer.py](./TC026_Ask_a_question_in_Chart_Bot_and_display_AI_answer.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/6a315eab-1f70-4577-a547-13489e67e94d
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC028 AI integration error message appears when insights generation fails
- **Test Code:** [TC028_AI_integration_error_message_appears_when_insights_generation_fails.py](./TC028_AI_integration_error_message_appears_when_insights_generation_fails.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/a15d9338-e962-4a86-ad16-17bea6a984d0/cda804b2-3dd6-4791-96de-1a780492671a
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **26.67** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---