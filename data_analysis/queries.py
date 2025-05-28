from typing import Dict, Any

PREDEFINED_QUERIES = {
    "payment_method_earnings": {
        "description": "Find which payment method yields the highest earnings",
        "method": "payment_method_earnings"
    },
    "experts_few_jobs": {
        "description": "Percentage of experts with fewer than 100 jobs",
        "method": "experts_with_few_jobs"
    },
    "compare_web_vs_graphic": {
        "description": "Compare earnings between web developers and graphic designers",
        "method": "compare_categories_earnings",
        "args": {"category1": "Web Development", "category2": "Graphic Design"}
    },
    "rating_income": {
        "description": "Analyze how client rating affects income",
        "method": "rating_vs_income"
    },
    "top_platforms": {
        "description": "Show the top 3 platforms by average earnings",
        "method": "top_performing_platforms",
        "args": {"n": 3}
    },
    "payment_method_comparison": {
        "description": "Compare earnings between payment methods",
        "method": "compare_payment_methods"
    },
    "earnings_by_region": {
        "description": "Analyze earnings distribution by client region",
        "method": "earnings_by_region"
    },
    "expert_performance": {
        "description": "Analyze expert freelancer performance metrics",
        "method": "expert_performance_stats"
    },
    "earnings_by_experience": {
        "description": "Analyze earnings by experience level",
        "method": "earnings_by_experience_level"
    },
    "success_rate_analysis": {
        "description": "Analyze job success rate statistics",
        "method": "analyze_job_success_rate"
    }
}

def get_predefined_query(query_name: str) -> Dict[str, Any]:
    """Get a predefined query template"""
    return PREDEFINED_QUERIES.get(query_name, {})