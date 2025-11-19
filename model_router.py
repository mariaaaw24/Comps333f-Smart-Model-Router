class ModelRouter:
    def __init__(self):
        self.technical_terms = ['algorithm', 'deterministic', 'environment',
                                'search', 'optimize', 'complexity', 'dimension']
        self.explanatory_terms = ['explain', 'analyze', 'describe', 'why', 'how'
                                'discuss', 'compare']
        self.simple_terms = ['what', 'when', 'where', 'list', 'define']
    
    def route_question(self, question):
        question_lower = question.lower()
        tech_score = sum(1 for term in self.technical_terms if term in question_lower)
        exp_score = sum(1 for term in self.explanatory_terms if term in question_lower)
        simple_score = sum(1 for term in self.simple_terms if term in question_lower)
        
        if tech_score > exp_score and tech_score > simple_score:
            return "gt-oss:20b"
        elif exp_score > tech_score and exp_score > simple_score:
            return "deepseek-r1:14b"
        else:
            return "llama2-chinese"
    
    def explain_decision(self, question):
        best_model = self.route_question(question)
        return f"Question: '{question}'\nRouting to: {best_model}\nReason:{self._get_reason(question)}"
    
    def _get_reason(self, question):
        question_lower = question.lower()
        if any(term in question_lower for term in self.technical_terms):
            return "Contains technical terms - using gt-oss:20b for precision"
        elif any(term in question_lower for term in self.explanatory_terms):
            return "Requires explanation - using deepseek-r1:14b for clarity"
        else:
            return "Simple factual question - using llama2-chinese for speed"
    
if __name__ == "__main__":
    router = ModelRouter()
    test_questions = [
        "What is the PEAS description of automated taxi drivers?",
        "Explain why Poker is Non-Deterministic?",
        "Analyze the six standard environment type dimensions for Medical Diagnosis"
    ]
    
    print("AI Model Router Test")
    print("="*40)
    for question in test_questions:
        print(router.explain_decision(question))
        print("---")