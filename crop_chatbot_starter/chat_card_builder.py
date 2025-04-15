def build_chat_card(text, chart_url=None):
    # Base reply
    card = {
        "reply": {
            "text": f"🌾 AI Insight:\n{text}"
        }
    }

    # Parse bullets (auto-convert from • or - to card sections)
    bullets = [line.strip("•- ").strip() for line in text.split("\n") if line.strip().startswith(("•", "-"))]

    if bullets:
        card["reply"]["cards"] = [{
            "header": {
                "title": "Summary Points",
                "subtitle": "Extracted from AI Insight"
            },
            "sections": [{
                "widgets": [{"textParagraph": {"text": f"• {b}"}} for b in bullets]
            }]
        }]

    # Add chart if available (stack with card or fallback to image only)
    if chart_url:
        chart_card = {
            "image": {
                "imageUrl": chart_url,
                "altText": "Agriculture chart"
            }
        }

        if "cards" in card["reply"]:
            card["reply"]["cards"].append(chart_card)
        else:
            card["reply"]["cards"] = [chart_card]

    return card
