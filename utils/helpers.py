from typing import Dict, Any

def format_currency(value: float) -> str:
    """Format a numeric value as currency"""
    return f"${value:,.2f}"

def format_percentage(value: float) -> str:
    """Format a numeric value as percentage"""
    return f"{value:.1f}%"

def format_dict(data: Dict[str, Any], indent: int = 2) -> str:
    """Format a dictionary for display"""
    return "\n".join([f"{' ' * indent}{k}: {v}" for k, v in data.items()])