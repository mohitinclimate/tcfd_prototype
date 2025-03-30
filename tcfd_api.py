from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Optional

app = FastAPI(
    title="TCFD Climate Risk API",
    description="Simulated TCFD logic with an HTML front-end for Reliance and JSW Steel.",
    version="0.1.0"
)

# Point to your 'templates' folder
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "TCFD Risk API Prototype is running."}

@app.get("/tcfd-html", response_class=HTMLResponse)
def assess_tcfd_html(
    request: Request,
    company: str = Query(..., description="Company name (e.g. Reliance, JSW Steel)"),
    industry: str = Query(..., description="Industry (e.g. oil and gas, steel)"),
    location: str = Query(..., description="Primary location (e.g. gujarat, mumbai)"),
    climate_goal: Optional[str] = Query("none", description="Climate goal: net zero, compliance, none")
):
    risks = []
    opportunities = []
    recommendations = []
    tcfd_guidance = {}

    # Logic for Reliance (Oil & Gas in Gujarat)
    if (company.lower() == "reliance"
        and industry.lower() == "oil and gas"
        and location.lower() == "gujarat"):
        
        risks.extend([
            "High exposure to transition risks due to carbon-intensive operations.",
            "Vulnerability to heatwaves affecting refinery operations and worker safety.",
            "Water stress in Gujarat could disrupt cooling/refining processes.",
            "Increasing regulatory pressure to reduce emissions."
        ])
        opportunities.extend([
            "Leadership in green hydrogen and renewable energy investments.",
            "Carbon capture and storage (CCS) pilot projects to mitigate emissions.",
            "Financial incentives for clean energy innovation.",
            "Brand advantage in pivoting toward a circular economy and biofuels."
        ])
        recommendations.extend([
            "Accelerate net-zero strategy with clear interim targets.",
            "Implement early-warning systems for climate-related supply chain disruptions.",
            "Conduct scenario analysis for oil demand decline and pricing volatility.",
            "Engage with stakeholders on sustainable energy transition roadmap."
        ])
        tcfd_guidance = {
            "governance": "Ensure climate risk accountability at the board level and assign oversight roles for transition planning.",
            "strategy": "Integrate long-term climate scenarios into business models, especially for peak oil demand and energy diversification.",
            "risk_management": "Monitor regional climate events and carbon policy trends. Build resilience into assets vulnerable to heat or flooding.",
            "metrics_targets": "Track methane emissions, flaring intensity, and low-carbon R&D investments. Align disclosures with SBTi and net-zero frameworks."
        }

    # Logic for JSW Steel (Steel in Mumbai)
    elif (company.lower() == "jsw steel"
          and industry.lower() == "steel"
          and location.lower() == "mumbai"):

        risks.extend([
            "High energy consumption and exposure to rising carbon pricing.",
            "Water stress affecting manufacturing processes.",
            "Urban heat island effects disrupting logistics in Mumbai.",
            "Volatility in raw material supply chains under extreme weather."
        ])
        opportunities.extend([
            "Adoption of low-carbon steel technologies (electric arc furnaces).",
            "Use of recycled materials to reduce emissions.",
            "Access to green financing through climate-aligned bonds.",
            "Export competitiveness through low-carbon product lines."
        ])
        recommendations.extend([
            "Develop a roadmap for low-emission steel production.",
            "Conduct a comprehensive water audit across facilities.",
            "Enhance ESG reporting transparency to meet global buyer expectations.",
            "Collaborate on decarbonization R&D for the steel sector."
        ])
        tcfd_guidance = {
            "governance": "Assign cross-functional climate teams reporting to a board-level ESG committee.",
            "strategy": "Incorporate climate transition risk in capital expenditure planning for plant upgrades.",
            "risk_management": "Stress test operations for raw material price spikes due to climate-related supply disruptions.",
            "metrics_targets": "Define targets for carbon intensity per ton of steel, renewable energy usage, and compliance metrics."
        }
    else:
        # If the user enters a different combination
        return HTMLResponse("<h2>Company-specific data not available. Try Reliance or JSW Steel.</h2>")

    # Build your response context for Jinja2
    context = {
        "request": request,
        "company": company,
        "industry": industry,
        "location": location,
        "climate_goal": climate_goal,
        "risks": risks,
        "opportunities": opportunities,
        "recommendations": recommendations,
        "tcfd_guidance": tcfd_guidance
    }

    return templates.TemplateResponse("result.html", context)

