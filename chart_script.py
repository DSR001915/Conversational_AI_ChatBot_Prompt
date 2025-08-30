import plotly.graph_objects as go
import json

# Parse the data
data = {"phases": [{"name": "Context Setting", "components": ["Role Definition", "Personality Design", "Constraints & Rules", "Goal Specification"]}, {"name": "Conversation Structure", "components": ["Intent Recognition", "Dialogue Flow Design", "Response Patterns", "Turn Management"]}, {"name": "Memory Management", "components": ["Short-term Context", "Long-term Memory", "Conversation History", "State Tracking"]}, {"name": "Testing & Refinement", "components": ["Evaluation Metrics", "User Testing", "Iteration Cycles", "Performance Optimization"]}]}

# Define colors for each phase
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F']

# Create figure
fig = go.Figure()

# Position phases with much more spacing
phase_positions = [3, 8, 13, 18]
main_phase_y = 9
component_y_positions = [7, 5.5, 4, 2.5]

# Add main phase boxes with larger size and better text
for i, phase in enumerate(data['phases']):
    phase_x = phase_positions[i]
    
    # Shorten phase names for better fit
    phase_names = ["Context Setup", "Conv Structure", "Memory Mgmt", "Test & Refine"]
    phase_name = phase_names[i]
    
    # Add main phase box - larger and more prominent
    fig.add_trace(go.Scatter(
        x=[phase_x],
        y=[main_phase_y],
        mode='markers+text',
        text=[phase_name],
        textposition='middle center',
        marker=dict(
            size=80,
            color=colors[i],
            symbol='square',
            line=dict(width=4, color='white')
        ),
        hovertext=[data['phases'][i]['name']],
        showlegend=False,
        textfont=dict(size=14, color='white', family='Arial Black')
    ))
    
    # Add component boxes with better spacing and larger text
    for j, component in enumerate(data['phases'][i]['components']):
        comp_y = component_y_positions[j]
        
        # Abbreviate component names for better readability
        comp_abbreviations = {
            "Role Definition": "Role Defn",
            "Personality Design": "Personality",
            "Constraints & Rules": "Constraints",
            "Goal Specification": "Goals",
            "Intent Recognition": "Intent Recog",
            "Dialogue Flow Design": "Dialog Flow",
            "Response Patterns": "Response Pat",
            "Turn Management": "Turn Mgmt",
            "Short-term Context": "Short Context",
            "Long-term Memory": "Long Memory",
            "Conversation History": "Conv History",
            "State Tracking": "State Track",
            "Evaluation Metrics": "Evaluation",
            "User Testing": "User Testing",
            "Iteration Cycles": "Iteration",
            "Performance Optimization": "Performance"
        }
        
        comp_text = comp_abbreviations.get(component, component[:12])
        
        fig.add_trace(go.Scatter(
            x=[phase_x],
            y=[comp_y],
            mode='markers+text',
            text=[comp_text],
            textposition='middle center',
            marker=dict(
                size=55,
                color=colors[i],
                opacity=0.8,
                symbol='square',
                line=dict(width=3, color='white')
            ),
            hovertext=[component],
            showlegend=False,
            textfont=dict(size=11, color='white', family='Arial')
        ))
        
        # Add connecting line from phase to component - thicker
        fig.add_shape(
            type="line",
            x0=phase_x, y0=main_phase_y - 0.8,
            x1=phase_x, y1=comp_y + 0.6,
            line=dict(color=colors[i], width=3, dash="dot")
        )

# Add flow arrows between main phases - much more prominent
for i in range(len(phase_positions) - 1):
    fig.add_annotation(
        x=phase_positions[i] + 1.8,
        y=main_phase_y,
        xref="x",
        yref="y",
        text="",
        showarrow=True,
        arrowhead=3,
        arrowsize=2.5,
        arrowwidth=6,
        arrowcolor="#333333",
        ax=phase_positions[i+1] - 1.8,
        ay=main_phase_y
    )

# Add prominent feedback loop arrow
fig.add_annotation(
    x=phase_positions[-1] + 0.5,
    y=main_phase_y + 2,
    xref="x",
    yref="y",
    text="",
    showarrow=True,
    arrowhead=3,
    arrowsize=2,
    arrowwidth=5,
    arrowcolor="#DB4545",
    ax=phase_positions[0] - 0.5,
    ay=main_phase_y + 2
)

# Add clear feedback loop label
fig.add_annotation(
    x=10.5,
    y=main_phase_y + 2.8,
    text="Iterative Feedback",
    showarrow=False,
    font=dict(size=12, color="#DB4545", family='Arial Black')
)

# Update layout with more space
fig.update_layout(
    title="AI Prompt Framework Process",
    showlegend=False,
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[0, 21]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[1, 13]
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Update traces to prevent clipping
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("ai_prompt_framework_flowchart.png")
print("Enhanced flowchart with improved readability saved successfully!")