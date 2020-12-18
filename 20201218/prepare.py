import pickle
import time
import glob
import csv


class Company:
    def __init__(self, doc_id, is_label):
        self.doc_id = doc_id
        self.is_label = is_label
        self.document = ""


doc_types = [
    'business_analysis_of_finance',
    'business_management_analysis',
    'business_policy_environment_issue_etc',
    'business_research_and_development',
    'business_risks',
    'company_affiliated_entities',
    'company_business_description',
    'company_employees',
    'company_history',
    'finance_real_estate_for_lease',
    'finance_segment_information',
    'finance_voluntary_accounting_policy_change',
    'information_corporate_governance',
    'information_directors',
    'information_dividend_policy',
    'information_shareholders'
]

companies = []
# ラベルの読み込み
rows = []
with open('./salse_data_format.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
    for row in rows[1:]:
        companies.append(Company(doc_id=row[5], is_label=int(row[4])))

# 文書の読み込み
paths = glob.glob('../2017/docs/*.txt')
for doc_type in doc_types:
    pickle_objects = []
    for path in paths:
        if doc_type in path:
            with open(path, 'r') as f:
                text = f.read().splitlines()
            if len(text) > 0:
                for company in companies:
                    if company.doc_id in path:
                        company.document = ("\n".join(text))
                        pickle_objects.append(company)
    with open('2017_{}.binaryfile'.format(doc_type), 'wb') as web:
        pickle.dump(pickle_objects, web)
