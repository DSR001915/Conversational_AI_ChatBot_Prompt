import plotly.graph_objects as go
import json

# Load the framework data
data = {
    "frameworks": [
        {
            "name": "RTF (Role-Task-Format)", 
            "components": ["Role: Define character/position", "Task: Specify what to do", "Format: Set response style"], 
            "use_cases": ["Quick task completion", "Specific role-playing", "Structured outputs"], 
            "example": "Role: Customer service agent\nTask: Help resolve billing issues\nFormat: Professional, empathetic responses"
        },
        {
            "name": "CARE (Context-Action-Result-Example)", 
            "components": ["Context: Background information", "Action: Required behavior", "Result: Expected outcome", "Example: Sample interaction"], 
            "use_cases": ["Complex scenarios", "Training new chatbots", "Detailed guidance needed"], 
            "example": "Context: User frustrated about delayed order\nAction: Acknowledge and provide solution\nResult: Customer satisfaction restored\nExample: 'I understand your frustration...'"
        },
        {
            "name": "RACE (Role-Action-Context-Expectation)", 
            "components": ["Role: Character definition", "Action: Primary function", "Context: Situational background", "Expectation: Desired outcomes"], 
            "use_cases": ["Professional environments", "Goal-oriented conversations", "Clear expectations"], 
            "example": "Role: Financial advisor\nAction: Provide investment guidance\nContext: Market volatility concerns\nExpectation: Informed decision-making"
        },
        {
            "name": "CLEAR (Concise-Logical-Engaging-Actionable-Relevant)", 
            "components": ["Concise: Brief and focused", "Logical: Well-structured", "Engaging: Interactive", "Actionable: Practical steps", "Relevant: Context-appropriate"], 
            "use_cases": ["User-friendly interfaces", "Educational content", "General conversations"], 
            "example": "Concise: Quick problem identification\nLogical: Step-by-step solutions\nEngaging: Ask follow-up questions\nActionable: Provide next steps"
        }
    ]
}

# Prepare table data with condensed text due to 15 character limit
framework_names = []
components = []
use_cases = []
examples = []

for framework in data["frameworks"]:
    # Framework name (abbreviated)
    name = framework["name"].split("(")[0].strip()
    framework_names.append(name)
    
    # Components (heavily abbreviated due to 15 char limit)
    comp_text = "<br>".join([
        "• Role/Char",
        "• Task/Action", 
        "• Format/Result",
        "• Example" if len(framework["components"]) > 3 else ""
    ]).rstrip("<br>• ")
    components.append(comp_text)
    
    # Use cases (abbreviated)
    use_text = "<br>".join([
        "• Quick tasks" if "Quick" in str(framework["use_cases"]) else "• Complex work",
        "• Role-play" if "role" in str(framework["use_cases"]).lower() else "• Training",
        "• Structured" if "Structured" in str(framework["use_cases"]) else "• General use"
    ])
    use_cases.append(use_text)
    
    # Examples (very condensed)
    if "Customer" in framework["example"]:
        ex_text = "Customer svc<br>agent helping<br>with billing"
    elif "Financial" in framework["example"]:
        ex_text = "Financial<br>advisor giving<br>investment tips"  
    elif "frustrated" in framework["example"]:
        ex_text = "Handle angry<br>customer about<br>delayed order"
    else:
        ex_text = "Step-by-step<br>problem<br>solving guide"
    examples.append(ex_text)

# Create table
fig = go.Figure(data=[go.Table(
    header=dict(
        values=['Framework', 'Components', 'Use Cases', 'Example App'],
        fill_color='#1FB8CD',
        font=dict(color='white', size=14),
        align='center',
        height=40
    ),
    cells=dict(
        values=[framework_names, components, use_cases, examples],
        fill_color=[['#f8f9fa', '#ffffff']*2],
        font=dict(color='black', size=12),
        align='left',
        height=80
    )
)])

fig.update_layout(
    title="AI Framework Comparison",
    font=dict(family="Arial"),
    paper_bgcolor='white'
)

# Save the chart
fig.write_image("ai_frameworks_comparison.png", width=1200, height=600)
print("Chart saved as ai_frameworks_comparison.png")