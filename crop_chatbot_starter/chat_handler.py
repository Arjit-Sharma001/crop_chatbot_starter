from preprocessing import preprocess_text
from chart_generator import generate_chart
from chat_card_builder import build_chat_card
from vertex_ai_model import query_vertexai

def handle_query(user_input):
    keywords = set(preprocess_text(user_input))

    # Keyword groups (flexible synonyms)
    intent_keywords = {
        "yield_over_years": {"yield", "production", "output"},
        "temp_vs_yield": {"temperature", "heat", "climate", "yield"},
        "soil_moisture_over_time": {"soil", "moisture", "wetness", "water"},
    }

    # Plot Types Keyword
    plot_type_keywords = {
    "line": {"line", "line graph", "line chart"},
    "bar": {"bar", "bar graph", "bar chart"},
    "scatter": {"scatter", "scatter plot", "scatter diagram"},
    }

    # Determine plot type (default to line)
    plot_type = "line"
    for ptype, synonyms in plot_type_keywords.items():
        if synonyms.intersection(keywords):
            plot_type = ptype
            break

    # Find all matching chart types
    matched_charts = []
    for chart_type, keyword_set in intent_keywords.items():
        if keyword_set.intersection(keywords):
            matched_charts.append(chart_type)

    # Generate insight text
    prompt = f"Provide an agricultural insight based on this query: {list(keywords)}"
    response_text = query_vertexai(prompt)

    # Generate all matched charts
    chart_url = None
    for chart_type in matched_charts:
        chart_path = generate_chart(chart_type, plot_type)
        if chart_path:
            chart_url = f"http://localhost:5000/{chart_path}"
            break  # Show only one chart for now (or you can loop all)


    # Build cards
    reply = build_chat_card(response_text, chart_url)

    # Optional fallback if nothing matched
    if not chart_url:
        reply["reply"]["text"] += "\n\n💡 Try asking about:\n• Soil moisture\n• Crop yield\n• Temperature vs yield"

    return reply
