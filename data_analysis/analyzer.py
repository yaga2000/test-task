import pandas as pd
from typing import Dict, Any

class FreelancerDataAnalyzer:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)
        self._preprocess_data()

    def _preprocess_data(self):
        """Clean and preprocess the data"""
        # Convert columns to appropriate types
        numeric_cols = ['Job_Completed', 'Earnings_USD', 'Hourly_Rate',
                        'Job_Success_Rate', 'Client_Rating', 'Job_Duration_Days',
                        'Rehire_Rate', 'Marketing_Spend']
        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

        # Clean text fields
        text_cols = ['Job_Category', 'Platform', 'Experience_Level',
                     'Client_Region', 'Payment_Method', 'Project_Type']
        for col in text_cols:
            if col in self.df.columns:
                self.df[col] = self.df[col].str.strip().str.title()

        # Handle missing values
        self.df['Earnings_USD'] = self.df['Earnings_USD'].fillna(0)
        self.df['Client_Rating'] = self.df['Client_Rating'].fillna(self.df['Client_Rating'].median())
        self.df['Job_Success_Rate'] = self.df['Job_Success_Rate'].fillna(self.df['Job_Success_Rate'].median())

    def get_summary_stats(self) -> Dict[str, Any]:
        """Get basic summary statistics"""
        return {
            'total_freelancers': len(self.df),
            'avg_earnings': self.df['Earnings_USD'].mean(),
            'median_earnings': self.df['Earnings_USD'].median(),
            'top_categories': self.df['Job_Category'].value_counts().head(5).to_dict(),
            'common_regions': self.df['Client_Region'].value_counts().head(5).to_dict()
        }

    def earnings_by_region(self) -> Dict[str, Any]:
        """Analyze earnings distribution by region"""
        return self.df.groupby('Client_Region')['Earnings_USD'].agg(['mean', 'median', 'count']).to_dict()

    def expert_performance_stats(self) -> Dict[str, Any]:
        """Analyze expert freelancer performance"""
        experts = self.df[self.df['Experience_Level'] == 'Expert']
        low_project_experts = experts[experts['Job_Completed'] < 100]

        return {
            'total_experts': len(experts),
            'experts_with_less_than_100_jobs': len(low_project_experts),
            'percentage': (len(low_project_experts) / len(experts)) * 100,
            'avg_earnings_low_project_experts': low_project_experts['Earnings_USD'].mean(),
            'avg_earnings_all_experts': experts['Earnings_USD'].mean()
        }

    def earnings_by_experience_level(self) -> Dict[str, Any]:
        """Analyze earnings by experience level"""
        return self.df.groupby('Experience_Level')['Earnings_USD'].agg(['mean', 'median', 'count']).to_dict()

    def top_performing_platforms(self, n: int = 3) -> Dict[str, Any]:
        """Identify top performing platforms by average earnings"""
        return self.df.groupby('Platform')['Earnings_USD'].mean().nlargest(n).to_dict()

    def analyze_job_success_rate(self) -> Dict[str, Any]:
        """Analyze job success rate statistics"""
        return {
            'avg_success_rate': self.df['Job_Success_Rate'].mean(),
            'success_rate_by_category': self.df.groupby('Job_Category')['Job_Success_Rate'].mean().to_dict(),
            'success_rate_vs_earnings': self.df[['Job_Success_Rate', 'Earnings_USD']].corr().iloc[0, 1]
        }

    def get_data_summary(self) -> str:
        """Generate a text summary of the data"""
        stats = self.get_summary_stats()
        return (
            f"Dataset contains {stats['total_freelancers']} freelancers. "
            f"Average earnings: ${stats['avg_earnings']:,.2f}. "
            f"Top categories: {', '.join(stats['top_categories'].keys())}. "
            f"Most common client regions: {', '.join(stats['common_regions'].keys())}."
        )

    def payment_method_earnings(self) -> Dict[str, Any]:
        """Compare earnings by payment method to find the highest earning one"""
        method_earnings = self.df.groupby('Payment_Method')['Earnings_USD'].mean().sort_values(ascending=False)
        return {
            'highest_earning_method': method_earnings.index[0],
            'highest_earning_amount': method_earnings.iloc[0],
            'all_methods': method_earnings.to_dict()
        }

    def compare_payment_methods(self) -> Dict[str, Any]:
        """Compare earnings by payment method"""
        crypto_earnings = self.df[self.df['Payment_Method'] == 'Crypto']['Earnings_USD'].mean()
        other_earnings = self.df[self.df['Payment_Method'] != 'Crypto']['Earnings_USD'].mean()

        return {
            'crypto_avg_earnings': crypto_earnings,
            'other_avg_earnings': other_earnings,
            'difference': crypto_earnings - other_earnings,
            'percentage_difference': ((crypto_earnings - other_earnings) / other_earnings) * 100
        }

    def experts_with_few_jobs(self) -> Dict[str, Any]:
        """Calculate percentage of experts with fewer than 100 jobs"""
        experts = self.df[self.df['Experience_Level'] == 'Expert']
        count_under_100 = len(experts[experts['Job_Completed'] < 100])
        total_experts = len(experts)

        return {
            'percentage': (count_under_100 / total_experts) * 100,
            'count_under_100': count_under_100,
            'total_experts': total_experts
        }

    def compare_categories_earnings(self, category1: str = 'Web Development', category2: str = 'Graphic Design') -> \
    Dict[str, Any]:
        """Compare earnings between two job categories"""
        comparison = {}

        for category in [category1, category2]:
            cat_data = self.df[self.df['Job_Category'] == category]
            comparison[category] = {
                'avg_earnings': cat_data['Earnings_USD'].mean(),
                'median_earnings': cat_data['Earnings_USD'].median(),
                'count': len(cat_data)
            }

        comparison['difference'] = comparison[category1]['avg_earnings'] - comparison[category2]['avg_earnings']
        return comparison

    def rating_vs_income(self) -> Dict[str, Any]:
        """Analyze how client rating affects freelancer income"""
        # Bin ratings into groups for better analysis
        self.df['Rating_Bin'] = pd.cut(self.df['Client_Rating'],
                                       bins=[0, 3, 4, 4.5, 5],
                                       labels=['0-3', '3-4', '4-4.5', '4.5-5'])

        rating_groups = self.df.groupby('Rating_Bin')['Earnings_USD'].agg(['mean', 'median', 'count'])

        return {
            'rating_earnings': rating_groups.to_dict(),
            'correlation': self.df[['Client_Rating', 'Earnings_USD']].corr().iloc[0, 1]
        }