from langchain_community.chat_models import ChatOllama  # Alternative import
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Dict, Any

class LLMQueryHandler:
    def __init__(self):
        self.llm = ChatOllama(model="deepseek-r1:14b", temperature=0.7)
        self.output_parser = StrOutputParser()

    def generate_response(self, query: str, context: Dict[str, Any]) -> str:
        """Generate a natural language response based on query and data context"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a data analyst assistant. Your task is to explain the provided data analysis results in clear, natural language. 
             Provide insights and interpretations, not just raw numbers. Format your response for easy reading.
             
             """),
            ("human", "Question: {query}\n\nData Context: {context}")
        ])

        chain = prompt | self.llm | self.output_parser
        return chain.invoke({"query": query, "context": context})