from typing import Dict, Any
from data_analysis.analyzer import FreelancerDataAnalyzer
from llm_integration.llm_handler import LLMQueryHandler
from data_analysis.queries import get_predefined_query, PREDEFINED_QUERIES
import argparse

class FreelancerAnalysisCLI:
    def __init__(self, data_path: str):
        self.analyzer = FreelancerDataAnalyzer(data_path)
        self.llm_handler = LLMQueryHandler()

    def execute_predefined_query(self, query_name: str) -> Dict[str, Any]:
        """Execute a predefined query by name"""
        query = get_predefined_query(query_name)
        if not query:
            return {"error": f"Unknown query: {query_name}"}

        method = getattr(self.analyzer, query["method"])
        return method()

    def list_predefined_queries(self) -> Dict[str, str]:
        """List all available predefined queries"""
        return {name: info["description"] for name, info in PREDEFINED_QUERIES.items()}

    def handle_custom_query(self, query: str) -> str:
        """Handle a custom natural language query"""
        # First try to match with predefined queries
        for q_name, q_info in PREDEFINED_QUERIES.items():
            if q_name.lower() in query.lower() or q_info["description"].lower() in query.lower():
                data = self.execute_predefined_query(q_name)
                return self.llm_handler.generate_response(query, data)

        # If no match, use the general summary
        data = {
            "summary": self.analyzer.get_summary_stats(),
            "message": "No specific analysis found for this query. Here's a general summary."
        }
        return self.llm_handler.generate_response(query, data)

    def run_cli(self):
        """Run the command line interface"""
        parser = argparse.ArgumentParser(description="Freelancer Earnings Analysis Tool")
        subparsers = parser.add_subparsers(dest='command', required=True)

        # List queries command
        list_parser = subparsers.add_parser('list', help='List predefined queries')

        # Execute query command
        query_parser = subparsers.add_parser('query', help='Execute a query')
        query_parser.add_argument('query', help='Query name or natural language question')

        args = parser.parse_args()

        if args.command == 'list':
            queries = self.list_predefined_queries()
            print("\nAvailable predefined queries:")
            for name, desc in queries.items():
                print(f"- {name}: {desc}")
        elif args.command == 'query':
            # First try as a predefined query name
            predefined_result = self.execute_predefined_query(args.query)
            if "error" not in predefined_result:
                response = self.llm_handler.generate_response(args.query, predefined_result)
            else:
                # Treat as natural language query
                response = self.handle_custom_query(args.query)
            print("\n" + response)