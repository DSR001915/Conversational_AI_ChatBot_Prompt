import plotly.graph_objects as go
import plotly.express as px
import json

# Parse the data
data = {
    "memory_system": {
        "short_term": {
            "title": "Short-term Memory", 
            "components": ["Current session context", "Recent messages (last 5-10)", "Active topics", "Current conversation thread"], 
            "duration": "Single conversation session"
        }, 
        "working_memory": {
            "title": "Working Memory", 
            "components": ["User preferences", "Conversation state", "Current goals/objectives", "Context variables"], 
            "duration": "Extended conversation"
        }, 
        "long_term": {
            "title": "Long-term Memory", 
            "components": ["User profile & preferences", "Conversation history", "Learned interaction patterns", "Relationship building data"], 
            "duration": "Across multiple sessions"
        }, 
        "flow_connections": ["Short-term feeds into Working", "Working updates Long-term", "Long-term informs Working", "Working guides Short-term responses"]
    }
}

# Brand colors
colors = ['#1FB8CD', '#DB4545', '#2E8B57']

# Create figure
fig = go.Figure()

# Define positions for the three memory layers
layer_positions = {
    'Short-term Memory': {'y': 3, 'x': 0},
    'Working Memory': {'y': 2, 'x': 0}, 
    'Long-term Memory': {'y': 1, 'x': 0}
}

# Add main memory layer nodes
layer_names = ['Short-term Memory', 'Working Memory', 'Long-term Memory']
for i, layer in enumerate(layer_names):
    fig.add_trace(go.Scatter(
        x=[layer_positions[layer]['x']], 
        y=[layer_positions[layer]['y']],
        mode='markers+text',
        marker=dict(size=60, color=colors[i], line=dict(width=2, color='white')),
        text=[layer.replace(' Memory', '<br>Memory')],
        textposition='middle center',
        textfont=dict(size=10, color='white'),
        name=layer,
        showlegend=False
    ))

# Add component nodes for each layer
component_data = [
    ('short_term', 'Short-term Memory', 3),
    ('working_memory', 'Working Memory', 2),
    ('long_term', 'Long-term Memory', 1)
]

x_offset = 1.5
for layer_key, layer_name, y_pos in component_data:
    components = data['memory_system'][layer_key]['components']
    layer_color = colors[layer_names.index(layer_name)]
    
    for j, component in enumerate(components):
        # Shorten component names to fit 15 character limit
        short_name = component[:15] if len(component) <= 15 else component[:12] + '...'
        
        fig.add_trace(go.Scatter(
            x=[x_offset + j * 0.8], 
            y=[y_pos],
            mode='markers+text',
            marker=dict(size=25, color=layer_color, opacity=0.7),
            text=[short_name],
            textposition='top center',
            textfont=dict(size=8),
            name=f'{layer_name} Components',
            showlegend=False
        ))
        
        # Add connection line from main layer to component
        fig.add_trace(go.Scatter(
            x=[0, x_offset + j * 0.8],
            y=[y_pos, y_pos],
            mode='lines',
            line=dict(color=layer_color, width=1, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))

# Add flow connections between layers
flow_lines = [
    ([0, 0], [3, 2], colors[0]),  # Short-term to Working
    ([0, 0], [2, 1], colors[1]),  # Working to Long-term  
    ([0, 0], [1, 2], colors[2]),  # Long-term to Working
    ([0, 0], [2, 3], colors[1])   # Working to Short-term
]

for x_coords, y_coords, color in flow_lines:
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='lines',
        line=dict(color=color, width=3, dash='solid'),
        showlegend=False,
        hoverinfo='skip'
    ))

# Update layout
fig.update_layout(
    title='AI Chatbot Memory System',
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, 4.5]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[0.5, 3.5]
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('memory_system_diagram.png', width=1200, height=800)