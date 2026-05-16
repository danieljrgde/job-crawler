# Company Classification

Companies are organized following the **Global Industry Classification Standard (GICS®)**, a four-level taxonomy developed by MSCI and S&P Global and widely used in finance and investment research.

## Directory structure

```
companies/
  <sector>/
    <industry-group>/
      <industry>/
        <sub-industry>/
          <company-slug>.yaml
```

All directory names use lowercase kebab-case (e.g., `Diversified Financials` → `diversified-financials`).

## GICS levels

| Level | Count | Example |
|---|---|---|
| Sector | 11 | Financials |
| Industry Group | 25 | Diversified Financials |
| Industry | 74 | Capital Markets |
| Sub-Industry | 163 | Asset Management & Custody Banks |

## How to find a company's GICS classification

1. Look up the company on [MSCI's GICS search](https://www.msci.com/our-solutions/indexes/gics) or check its profile on Bloomberg, Reuters, or Yahoo Finance — all display the GICS classification.
2. Use the four levels as the directory path.
3. Set the same values in the `gics` block inside the YAML file.

## Currently used classifications

| Sector | Industry Group | Industry | Sub-Industry |
|---|---|---|---|
| Financials | Banks | Banks | Diversified Banks |
| Financials | Diversified Financials | Capital Markets | Asset Management & Custody Banks |
| Financials | Diversified Financials | Capital Markets | Investment Banking & Brokerage |
| Financials | Diversified Financials | Consumer Finance | Consumer Finance |
| Financials | Diversified Financials | Diversified Financial Services | Specialized Finance |
| Industrials | Commercial & Professional Services | Professional Services | Research & Consulting Services |
| Information Technology | Software & Services | IT Services | Data Processing & Outsourced Services |
| Information Technology | Software & Services | Software | Application Software |
